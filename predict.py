import json
import pickle

from flask import Flask
from flask import request
from flask import jsonify


with open('model.bin', 'rb') as f_model: 
    dv, model = pickle.load(f_model)

app = Flask('job_post')

@app.route('/predict', methods=['POST'])
def predict():
    job_post = request.get_json()

    X = dv.transform([job_post])
    y_pred = model.predict(X)
    
    result = {
        'Fraudulent': int(y_pred)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run()
