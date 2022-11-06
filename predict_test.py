import json
import requests


url = 'http://localhost:9696/predict'

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


response = requests.post(url, json=job_post).json()
print(response)