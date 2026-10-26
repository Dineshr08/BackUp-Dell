import json
import os
from datetime import datetime

import pytest
import requests
from Utilities.BaseClass_API import BaseClass_API
# from Jenkins_TestSuite.Jenkins_TestSuiteCreation_API import *
class Test_API_UpdateTestRun(BaseClass_API):

    @pytest.mark.regression
    # @pytest.mark.basic_regression
    # Project AutomationTest1  , module name : AT_API_UpdateTestRun

    def test_API_UpdateTestRun(self):

        build_number = self.get_Jenkinsbuildnumber()

        URL = 'https://qtest-stage.gtie.dell.com/api/v3/projects/404/test-runs/30139320'
        HEADERS = {
            "Authorization": "Bearer fda0002f-500a-47c6-b617-0381dc027b39",
            "Content-Type": "application/json"
        }

        Date = datetime.now()
        name = "AT Update TestRun Name"+str(Date)
        BODY = {

    "name": name,
    "properties": [
        {
            "field_id": 76023,
            "field_name": "Run Order",
            "field_value": "1"
        },
        {
            "field_id": 75812,
            "field_name": "Execution Type",
            "field_value": "38470",
            "field_value_name": "Acceptance"
        },
        {
            "field_id": 75813,
            "field_name": "Planned Start Date",
            "field_value": "2022-07-16T00:00:00+00:00"
        },
        {
            "field_id": 75821,
            "field_name": "Status",
            "field_value": "601",
            "field_value_name": "Passed"
        },
        {
            "field_id": 75815,
            "field_name": "Planned End Date",
            "field_value": "2022-07-16T00:00:00+00:00"
        },
        {
            "field_id": 75806,
            "field_name": "Assigned To",
            "field_value": "10580",
            "field_value_name": "Dinesh R"
        },
        {
            "field_id": 75848,
            "field_name": "Build",
            "field_value": ""
        },
        {
            "field_id": 75819,
            "field_name": "Priority",
            "field_value": "723",
            "field_value_name": "Medium"
        }
    ]
}

        response = requests.put(URL, data=json.dumps(BODY), headers=HEADERS)
        parsed_response = json.loads(response.content)
        assert response.status_code == 200 and "id" in parsed_response

        buildNumber, env_name = self.get_Jenkinsbuildnumber()

        testSuiteID = self.getTestSuiteID(buildNumber, env_name)


        if response.status_code == 200 and "id" in parsed_response:
            self.create_TestRun(testSuiteID, 'API_UpdateTestRun', '2681807')
            test_run_id = self.get_TestRun(testSuiteID, 'API_UpdateTestRun')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')
        else:
            self.create_TestRun(testSuiteID, 'API_UpdateTestRun', '2681807')
            test_run_id = self.get_TestRun(testSuiteID, 'API_UpdateTestRun')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')


