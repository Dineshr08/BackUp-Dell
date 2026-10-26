import json
from datetime import datetime

import pytest
import requests
import sys
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
        "Authorization": "Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e",
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
        "Authorization": "Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e",
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