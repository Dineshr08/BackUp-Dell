import os
import sys

import requests
import json
import os
import sys
from datetime import datetime
from datetime import datetime, timezone
import pytest
import requests

@pytest.mark.usefixtures("API_setup", "getTSValue")
class BaseClass_API:

    def get_Jenkinsbuildnumber(self):
        # Get the build number from the environment variable
        build_number = os.environ.get('BUILD_NUMBER')
        env_name = os.environ.get('env_name')

        # Use the build number in your script as needed
        print(f"Build Number: {build_number}")
        print(f"env_name: {env_name}")
        return build_number, env_name

    def create_TestRun(self, parentId, name, testCaseID):
        BASE_URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-runs?parentId='
        REM_URL = '&parentType=test-suite'
        URL = "{}{}{}".format(BASE_URL, parentId, REM_URL)
        # URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-runs?parentId=786189&parentType=test-suite'
        HEADERS = {
            "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823",
            "Content-Type": "application/json"
        }

        BODY = {
    "name": name,
    "properties": [
        {
            "field_id": 34202,
            "field_name": "Run Order",
            "field_value": "1"
        },
        {
            "field_id": 33220,
            "field_name": "Execution Type",
            "field_value": "501",
            "field_value_name": "Functional"
        },
        {
            "field_id": 33214,
            "field_name": "Assigned To",
            "field_value": "10580",
            "field_value_name": "Dinesh R"
        },
        {
            "field_id": 33229,
            "field_name": "Status",
            "field_value": "601",
            "field_value_name": "Passed"
        },
        {
            "field_id": 33227,
            "field_name": "Priority",
            "field_value": "723",
            "field_value_name": "Medium"
        },
		{
            "field_id": -199,
            "field_name": "Planned Start Date",
            "field_value": "2023-09-22T00:00:00+00:00"
        },
		{
            "field_id": -198,
            "field_name": "Planned End Date",
            "field_value": "2023-09-22T00:00:00+00:00"
        }
    ],
    "test_case": {
        "links": [],
        "id": testCaseID
    },
    "test_case_version_id": 3644888,
    "test_case_version": "1.0",
    "creator_id": 10580
}
        response = requests.post(URL, data=json.dumps(BODY), headers=HEADERS)
        parsed_response = json.loads(response.content)
        assert response.status_code == 201 and "id" in parsed_response

    def get_TestRun(self, parentId, name):
        BASE_URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-runs?parentId='
        REM_URL = '&parentType=test-suite'
        URL = "{}{}{}".format(BASE_URL, parentId, REM_URL)
        # URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-runs?parentId=786189&parentType=test-suite'
        HEADERS = {
            "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823",
            "Content-Type": "application/json"
        }

        response = requests.get(URL, headers=HEADERS)
        print(response.request.body)
        print(response.request.url)
        print(response.status_code)
        print(response.json())
        parsed_response = json.loads(response.content)
        # assert response.status_code == 200 and "parentId" in parsed_response
        assert response.status_code == 200

        if response.status_code == 200:
            # Connection_info = response.json()

            Connection_info = response.json()["items"]

            target_test_run_name = name

            for test_run in Connection_info:
                if test_run["name"] == target_test_run_name:
                    target_test_run_id = test_run["id"]
                    print(f"The ID of {target_test_run_name} is {target_test_run_id}")
                    return target_test_run_id
            else:
                print(f"{target_test_run_name} not found in the response.")

    def update_TestLog(self, TestRunID, ID, Status, ColourCode):

        BASE_URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-runs/'
        REM_URL = '/test-logs'
        URL = "{}{}{}".format(BASE_URL, TestRunID, REM_URL)
        # URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-runs?parentId=786189&parentType=test-suite'
        HEADERS = {
            "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823",
            "Content-Type": "application/json"
        }

        # Get the current time in UTC
        current_time_utc = datetime.now(timezone.utc)

        # Format the current time as a string in the desired format
        formatted_time = current_time_utc.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

        BODY = {
    "exe_start_date": formatted_time,
    "exe_end_date": formatted_time,
    "status": {
    "id": ID,
    "name": Status,
    "is_default": "false",
    "color": ColourCode,
    "active": "true"
  }
}
        response = requests.post(URL, data=json.dumps(BODY), headers=HEADERS)
        parsed_response = json.loads(response.content)
        assert response.status_code == 201 and "id" in parsed_response

    def getTestSuiteID(self,build_number, env_name):
        # Get the build number from command line arguments
        # build_number = sys.argv[1]
        # env_name = sys.argv[2]

        build_number = build_number
        env_name = env_name

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


