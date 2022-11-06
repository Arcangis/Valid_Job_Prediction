# Job Post Validator

## Introduction
Project created as the Midterm Project  for the online bootcamp: Machine Learning Zoomcamp ([link](https://github.com/alexeygrigorev/mlbookcamp-code)).

### Problem:

Searching for work is an arduous and repetitive process, often leading to no feedback and a giant waste of time. To turn things more difficult, there are fraudulent job posts mixed in.

The project's objective is to analyze various data from job offers and try to classify which are fraudulents and which are not.

Using insights from: 
- Most frequent used keywords in title;
- Salary Range;
- Offer had requirements?
- Offer had benefits?
- employment_type;
- required_experience;
- required_education;
- Offer had telecommuting (Remote Work)?
- Department;
- Industry;
- Function;   
- Location;
- Company had a profile?
- Company had a logo?
- Job(site) had questions?

<hr>

## Data

Dataset can be found in datasets folder, or by downloading from [here](https://www.kaggle.com/datasets/whenamancodes/real-or-fake-jobs).

This dataset contains 18K job descriptions out of which about 800 are fake. The data consists of both textual information and meta-information about the jobs. The dataset can be used to create classification models which can learn from the job information which ones are fraudulent. (Font: kaggle)

Original data from dataset:

|       Columns       	|                   Description                  	|
|:-------------------:	|:----------------------------------------------:	|
| job_id              	| Unique Job ID                                  	|
| title               	| The title of the job ad entry                  	|
| location            	| Geographical location of the job ad            	|
| department          	| Corporate department (e.g. sales)              	|
| salary_range        	| Indicative salary range (e.g. $50,000-$60,000) 	|
| company_profile     	| A brief company description                    	|
| description         	| The details description of the job ad          	|
| requirements        	| Enlisted requirements for the job opening      	|
| benefits            	| Enlisted offered benefits by the employer      	|
| telecommuting       	| True for telecommuting positions               	|
| hascompanylogo      	| True if company logo is present                	|
| has_questions       	| True if screening questions are present        	|
| employment_type     	| Full-type, Part-time, Contract, etc            	|
| required_experience 	| Executive, Entry level, Intern, etc            	|
| required_education  	| Doctorate, Master’s Degree, Bachelor, etc      	|
| industry            	| Automotive, IT, Health care, Real estate, etc  	|
| function            	| Consulting, Engineering, Research, Sales etc   	|
| fraudulent          	| target - Classification attribute              	|

<hr>

## How to run

It's recommedend to use a virtual environment. For example:

1. Intall virtualenv:
```
pip install virtualenv
```
2. Create a virtualenv(ubuntu):
```
python3 -m venv <env_name>
```
3. Activate the environment(ubuntu):
```
source <env_name>/bin/activate
```
4. Install all modules/dependencies:
```
pip install -r requirements.txt
```
5. Build the application docker:
```
docker build -t <docker_img_name> .
```
6. Run the application docker:
```
docker run -it -p 9696:9696 <docker_img_name>:latest
```

Now the application is running and is ready to receive request for predictions.

BONUS:

1. Run prediction tests
```
python predict_test.py
```
2. For more tests, change the content from job_post with data from [test dataset](datasets/data_for_test.csv).

Example:
```
job_post = {
    'salary_range_min': 0,
    'salary_range_max': 0,
    'title': 'engineer',
    'location': 'gb, , london',
    'department': 'other',
    'employment_type': 'full-time',
    'required_experience': 'entry level',
    'required_education': 'unspecified',
    'industry': 'apparel & fashion',
    'function': 'information technology',
    'company_profile': 1,
    'requirements': 0,
    'benefits': 0,
    'telecommuting': 0,
    'has_company_logo': 1,
    'has_questions': 0,
}
```

<hr>

## Continue ...