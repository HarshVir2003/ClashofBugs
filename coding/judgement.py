import time

import requests
import base64

# url = "https://judge0-ce.p.rapidapi.com/about"

# todo: get api key from os in prod.
# todo: encode incoming code in base64.
#
# url = "https://judge0-ce.p.rapidapi.com/config_info"
#
# headers = {
#     "X-RapidAPI-Key": "8f8c84ecc2msh3a8ec2a9c3a7585p1b6ab3jsne0cdd4526fbd",
#     "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers)
#
# print(response.json())

querystring = {"base64_encoded": "false", "fields": "*"}

# todo: update language ids.
languages = {
    'python': 71,
    'java': 52,
    'c': 50,
    'c++': 54
}


def submission(source_code, language, languages, stdin, stdout):
    url = "http://127.0.0.1:2358/submissions"

    payload = {
        "language_id": languages[language.lower()],
        "source_code": source_code,
        "stdin": stdin,
        "stdout": stdout
    }
    headers = {
        "content-type": "application/json",
        "Content-Type": "application/json",
        # "X-RapidAPI-Key": "8f8c84ecc2msh3a8ec2a9c3a7585p1b6ab3jsne0cdd4526fbd",
        # "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers, params=querystring)

    return response.json()


def get_submission(token):
    url = f"http://127.0.0.1:2358/submissions/{token}"

    headers = {
        # "X-RapidAPI-Key": "8f8c84ecc2msh3a8ec2a9c3a7585p1b6ab3jsne0cdd4526fbd",
        # "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()


def get_status(token):
    url = f"http://127.0.0.1:2358/submissions/{token}"

    header = {
        # "X-RapidAPI-Key": "8f8c84ecc2msh3a8ec2a9c3a7585p1b6ab3jsne0cdd4526fbd",
        # "X-RapidAPI-Host": "judge0-ce.p.rapidapi.com"
    }

    response = requests.get(url, headers=header)

    return response.json()


# token = submission('print(1+1)', language='python', languages=languages)['token']
# print(get_status(token))
# get_submission(submission()['token'])

a = submission("print('jass')", "python", languages, 0, 0)
time.sleep(1)
print(a)
print(get_status(a.get("token")))