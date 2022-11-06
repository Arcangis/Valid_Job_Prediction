import pandas as pd
import numpy as np

import pickle
import unidecode

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import tree

# read data
job_df = pd.read_csv('datasets/fake_job_postings.csv').drop(['job_id'],axis=1)
job_df.head()

# data treatment
job_df.drop(['description'], axis=1, inplace=True)

job_df.company_profile = (job_df.company_profile.isna()).astype(int)
job_df.requirements = (job_df.requirements.isna()).astype(int)
job_df.benefits = (job_df.benefits.isna()).astype(int)

job_df['salary_range'].replace('(.*[a-zA-Z]+.*)',np.NaN,regex=True, inplace=True)
job_df[['salary_range_min', 'salary_range_max']] = job_df['salary_range'].str.split('-', 1, expand=True)
job_df.drop(['salary_range'], axis=1, inplace=True)
job_df[['salary_range_min', 'salary_range_max']] = job_df[['salary_range_min', 'salary_range_max']].fillna(0)

job_df = job_df.replace(np.NaN,'other')

categorical = ['title','location','department', 'employment_type', 'required_experience', 'required_education', 'industry', 'function']
numerical = ['salary_range_min', 'salary_range_max']
binary = ['company_profile', 'requirements', 'benefits', 'telecommuting', 'has_company_logo', 'has_questions', 'fraudulent']

for column in categorical:
    job_df[column] = job_df[column].apply(lambda x: unidecode.unidecode(x).lower())

vectorizer = CountVectorizer(stop_words='english')

def get_repeated_words(df, column, percent):
    
    df_vector = vectorizer.fit_transform(df[column])
    bag_df = pd.DataFrame(df_vector.toarray(),columns=vectorizer.get_feature_names())
    
    col = []
    appear = []
    for column in bag_df.columns:
        col.append(column)
        appear.append(bag_df[column].sum())
    
    temp_df = pd.DataFrame({'col_name':col,'qtd':appear})
    
    df_order = temp_df.sort_values(by='qtd', ascending=False)
    
    return df_order[0:round((1-percent)*len(df_order))]

title_df = get_repeated_words(job_df,'title',0.95)

def replace_word(string, df):
    index = 100000
    for s in string.split(' '):
        ind = df[df.col_name == s].index.to_list()
        if not len(ind):
            continue
        elif index > ind[0]:
            index = ind[0]
    if index == 100000:
        return 'other'
    return df.loc[index].col_name

job_df.title = job_df.title.apply(lambda x: replace_word(x, title_df))

# separate train, val, test data
df_train_full, df_test = train_test_split(job_df, test_size=0.2, random_state=42)
df_train, df_val = train_test_split(df_train_full, test_size=0.25, random_state=42)

df_train.reset_index(drop=True, inplace=True)
df_val.reset_index(drop=True, inplace=True)
df_test.reset_index(drop=True, inplace=True)

y_train = df_train.fraudulent
y_val = df_val.fraudulent
y_test = df_test.fraudulent

del df_train['fraudulent']
del df_val['fraudulent']
del df_test['fraudulent']

# Train model
def train_one_hot_encondig(df_train, columns):
    train_dict = df_train[columns].to_dict(orient='records')
    dv = DictVectorizer(sparse=False)
    dv.fit(train_dict)
    X_train = dv.transform(train_dict)
    return X_train, dv

X_train, dv = train_one_hot_encondig(df_train,numerical+categorical+binary[0:-1])

# Decision Tree
model = tree.DecisionTreeClassifier(max_depth=None, min_samples_split=2)
model.fit(X_train, y_train)

# Save model
with open('model.bin', 'wb') as f_out:
   pickle.dump((dv, model), f_out)
f_out.close()