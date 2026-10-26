import json
import os
import sys
from datetime import datetime

import pytest
import requests
from Utilities.BaseClass_API import BaseClass_API

# class Test_API_CreateTestSuite(BaseClass_API):
class Test_API_CreateTestSuite:

    @pytest.mark.regression
    # Project AutomationTest  , module name : AT_API_CreateTestSuite2023-09-28 16:48:28.073751

    def test_API_CreateTestSuite(self):

        # build_number = self.get_Jenkinsbuildnumber()

        URL = 'https://qtest-dev3.gtie.dell.com/api/v3/projects/402/test-suites'
        HEADERS = {
            "Authorization": "Bearer 29421d63-7c39-437f-83df-c9ac63ab774a",
            "Content-Type": "application/json"
        }

        Date = datetime.now()
        name = "AT_API_CreateTestSuite" + str(Date)


        BODY = {
    "name": name,
    "properties": [
        {
            "field_id": -199,
            "field_name": "Planned Start Date",
            "field_value": "2024-02-28T00:00:00+00:00"
        },
        {
            "field_id": -198,
            "field_name": "Planned End Date",
            "field_value": "2024-02-28T00:00:00+00:00"
        },
        {
            "field_id": -186,
            "field_name": "Assigned To",
            "field_value": "[9629]",
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

        # buildNumber, env_name = self.get_Jenkinsbuildnumber()
        #
        # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
        #
        # if response.status_code == 200 and "id" in parsed_response:
        #     self.create_TestRun(testSuiteID, 'API_CreateTestSuite', '1091205')
        #     test_run_id = self.get_TestRun(testSuiteID, 'API_CreateTestSuite')
        #     self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')
        # else:
        #     self.create_TestRun(testSuiteID, 'API_CreateTestSuite', '1091205')
        #     test_run_id = self.get_TestRun(testSuiteID, 'API_CreateTestSuite')
        #     self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')


