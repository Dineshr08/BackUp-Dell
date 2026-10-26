import json
import os
import sys
from datetime import datetime

import pytest
import requests
from Utilities.BaseClass_API import BaseClass_API

class Test_API_UpdateTestCases:

    @pytest.mark.regression
    @pytest.mark.basic_regression
    # Project AutomationTest1  , module name : AT_API_UpdateTestCase

    def test_API_UpdateTestCases(self):

        # build_number = self.get_Jenkinsbuildnumber()

        URL = 'https://qtest-dev3.gtie.dell.com/api/v3/projects/403/test-cases/2481582'
        HEADERS = {
            "Authorization": "Bearer 29421d63-7c39-437f-83df-c9ac63ab774a",
            "Content-Type": "application/json"
        }

        Date = datetime.now()
        name = "AT Update TestCase Name"+str(Date)
        BODY = {
    "name": name,
    "properties": [
        {
            "field_id": 79876,
            "field_name": "Status",
            "field_value": "201",
            "field_value_name": "New"
        },
        {
            "field_id": 79877,
            "field_name": "Type",
            "field_value": "701",
            "field_value_name": "Manual"
        },
        {
            "field_id": 79868,
            "field_name": "Assigned To",
            "field_value": "",
            "field_value_name": ""
        },
        {
            "field_id": 79879,
            "field_name": "Description",
            "field_value": "<p>AT_API_UpdateTestCase</p>"
        }

    ],

    "parent_id": 450349
}

        response = requests.put(URL, data=json.dumps(BODY), headers=HEADERS)
        parsed_response = json.loads(response.content)
        assert response.status_code == 200 and "id" in parsed_response

        # buildNumber, env_name = self.get_Jenkinsbuildnumber()
        #
        # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
        #
        # if response.status_code == 200 and "id" in parsed_response:
        #     self.create_TestRun(testSuiteID, 'API_UpdateTestCases', '1091204')
        #     test_run_id = self.get_TestRun(testSuiteID, 'API_UpdateTestCases')
        #     self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')
        # else:
        #     self.create_TestRun(testSuiteID, 'API_UpdateTestCases', '1091204')
        #     test_run_id = self.get_TestRun(testSuiteID, 'API_UpdateTestCases')
        #     self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')


