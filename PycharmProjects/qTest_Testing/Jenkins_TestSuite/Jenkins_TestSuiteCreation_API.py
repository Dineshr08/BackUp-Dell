import json
from datetime import datetime

import pytest
import requests
import sys

import json

import pandas as pd
import requests
from csv import writer
import urllib3
import urllib3
urllib3.disable_warnings()
BASE_URL = "https://qtest.gtie.dell.com"
QTEST_TOKEN = "45a89380-8d45-4143-826c-e0dbda0a1823"
Login_API = "/login?redirect=https://qtest.gtie.dell.com/portal/project&requestNonce=MC44Nzg2ODE5OTM4OTkz1245"
Integration_API = "/portal/defect/integration/setting/connection/list/9?dojo.preventCache=0.1208288477138908"
Logout_API = '/logout'
def Jenkins_TestSuite_Creation_API():
    # Get the build number from command line arguments
    build_number = sys.argv[1]
    env_name = sys.argv[2]

    # Your Python script logic here...
    print(f"Build Number: {build_number}")
    print(f"Env Name: {env_name}")
    if env_name == "stage":
        URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-suites?parentId=825352&parentType=test-cycle'
    elif env_name == "prod":
        URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-suites?parentId=825353&parentType=test-cycle'

    HEADERS = {
        "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823",
        "Content-Type": "application/json"
    }

    # Date = datetime.now()
    name = str(env_name) + "_Jenkins_Build_" + str(build_number)

    BODY = {
    "name": name,
    "properties": [
        {
            "field_id": -202,
            "field_name": "Target Release/Build",
            "field_value": "-19046",
            "field_value_name": "Jenkins Automation Testing"
        },
        {
            "field_id": -186,
            "field_name": "Assigned To",
            "field_value": "[10580]",
            "field_value_name": "[Dinesh R]"
        },
        {
            "field_id": -191,
            "field_name": "Execution Type",
            "field_value": "501",
            "field_value_name": "Functional"
        },
        {
            "field_id": -189,
            "field_name": "Description",
            "field_value": ""
        }
    ]
}

    response = requests.post(URL, data=json.dumps(BODY), headers=HEADERS)
    parsed_response = json.loads(response.content)
    assert response.status_code == 200 and "id" in parsed_response

def getTestSuiteID():
    # Get the build number from command line arguments
    build_number = sys.argv[1]
    env_name = sys.argv[2]

    # build_number = 81
    # env_name = 'stage'

    # Your Python script logic here...
    print(f"Build Number: {build_number}")
    print(f"Env Name: {env_name}")
    if env_name == "stage":
        URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-suites?parentId=825352&parentType=test-cycle'
    elif env_name == "prod":
        URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-suites?parentId=825353&parentType=test-cycle'

    HEADERS = {
        "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823",
        "Content-Type": "application/json"
    }

    # Date = datetime.now()
    name = str(env_name) + "_Jenkins_Build_" + str(build_number)

    response = requests.get(URL, headers=HEADERS)
    parsed_response = json.loads(response.content)

    if response.status_code == 200:
        Connection_info = response.json()

        target_test_suite_name = name

        for test_suite in Connection_info:
            if test_suite["name"] == target_test_suite_name:
                target_test_suite_id = test_suite["id"]
                print(f"The ID of {target_test_suite_name} is {target_test_suite_id}")
                return target_test_suite_id
        else:
            print(f"{target_test_suite_name} not found in the response.")





Jenkins_TestSuite_Creation_API()
getTestSuiteID()