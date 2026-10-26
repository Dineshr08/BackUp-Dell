import json
import os
import sys
from datetime import datetime

import pytest
import requests
from Utilities.BaseClass_API import BaseClass_API

# class Test_API_CreateTestCases(BaseClass_API):
class Test_API_CreateTestCases:

    @pytest.mark.regression
    @pytest.mark.basic_regression
    # Project AutomationTest  , module name : AT_API_CreateTestCase

    def test_API_CreateTestCases(self):

        # build_number = self.get_Jenkinsbuildnumber()

        URL = 'https://qtest-dev3.gtie.dell.com/api/v3/projects/402/test-cases'
        HEADERS = {
            "Authorization": "Bearer 29421d63-7c39-437f-83df-c9ac63ab774a",
            "Content-Type": "application/json"
        }
        Date = datetime.now()
        name = "AT_API_CreateTestCase" + str(Date)

        BODY = {
    "name": name,
    "properties": [
        {
            "field_id": 79807,
            "field_name": "Status",
            "field_value": "201",
            "field_value_name": "New"
        },
        {
            "field_id": 79808,
            "field_name": "Type",
            "field_value": "702",
            "field_value_name": "Automation"
        },
        {
            "field_id": 79799,
            "field_name": "Assigned To",
            "field_value": "",
            "field_value_name": ""
        },
        {
            "field_id": 79810,
            "field_name": "Description",
            "field_value": ""
        }

    ],

    "parent_id": 450346
}

        response = requests.post(URL, data=json.dumps(BODY), headers=HEADERS)
        parsed_response = json.loads(response.content)
        assert response.status_code == 200 and "id" in parsed_response

        # buildNumber, env_name = self.get_Jenkinsbuildnumber()
        #
        # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
        #
        # if response.status_code == 200 and "id" in parsed_response:
        #     self.create_TestRun(testSuiteID, 'API_CreateTestCases', '1091204')
        #     test_run_id = self.get_TestRun(testSuiteID, 'API_CreateTestCases')
        #     self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')
        # else:
        #     self.create_TestRun(testSuiteID, 'API_CreateTestCases', '1091204')
        #     test_run_id = self.get_TestRun(testSuiteID, 'API_CreateTestCases')
        #     self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')


