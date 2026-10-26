import json

import pandas as pd
import requests
from csv import writer
import urllib3

urllib3.disable_warnings()
BASE_URL = "https://qtest.gtie.dell.com"
BASE_URL_Parameter = "https://qtest-appt01.gtie.dell.com:5080"
QTEST_TOKEN = "a5023327-1321-4b8d-a3c2-cefd4e9ecb1e"
Login_API = "/login?redirect=https://qtest.gtie.dell.com/portal/project&requestNonce=MC44Nzg2ODE5OTM4OTkz1245"
Logout_API = '/logout'


def qTest_Parameter():
    url = "https://qtest-appt01.gtie.dell.com:5080/api/v1/parameters/query"

    payload = json.dumps({
        "exactly": False,
        "statistic": True,
        "offset": 1,
        "limit": 5000,
        "sort_by": "created",
        "sort_order": "desc"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    Parameter_Response_info = response.json()
    identifier = Parameter_Response_info["items"]



    for item in identifier:
        identifier = item.get('identifier')
        project_id = item.get('project_ids')

        print(identifier,";", project_id)


def get_Project_Parameter():
    url = "https://qtest-appt01.gtie.dell.com:5080/api/v1/projects"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e'
    }

    response = requests.request("GET", url, headers=headers)
    Parameter_Response_info = response.json()
    for item in Parameter_Response_info:
        project_id = item.get('id')
        project_name = item.get('name')
        print(project_id, ";", project_name)



# qTest_Parameter()
get_Project_Parameter()