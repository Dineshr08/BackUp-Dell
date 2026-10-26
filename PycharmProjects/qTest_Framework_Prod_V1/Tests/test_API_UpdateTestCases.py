import json
import os
import sys
from datetime import datetime

import pytest
import requests
from Utilities.BaseClass_API import BaseClass_API

class Test_API_UpdateTestCases(BaseClass_API):

    @pytest.mark.regression

    # Project AutomationTest1  , module name : AT_API_UpdateTestCase

    def test_API_UpdateTestCases(self, getTSValue):

        # build_number = self.get_Jenkinsbuildnumber()

        URL = 'https://qtest.gtie.dell.com/api/v3/projects/404/test-cases/4766272'
        HEADERS = {
            "Authorization": "Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e",
            "Content-Type": "application/json"
        }

        Date = datetime.now()
        name = "AT Update TestCase Name"+str(Date)
        BODY = {
    "name": name,
    "properties": [
        {
            "field_id": 75798,
            "field_name": "Status",
            "field_value": "201",
            "field_value_name": "New"
        },
        {
            "field_id": 75799,
            "field_name": "Type",
            "field_value": "702",
            "field_value_name": "Automation"
        },
        {
            "field_id": 75790,
            "field_name": "Assigned To",
            "field_value": "",
            "field_value_name": ""
        },
        {
            "field_id": 75801,
            "field_name": "Description",
            "field_value": ""
        }

    ],

    "parent_id": 779689
}

        response = requests.put(URL, data=json.dumps(BODY), headers=HEADERS)
        parsed_response = json.loads(response.content)
        # assert response.status_code == 200 and "id" in parsed_response

        # buildNumber, env_name = self.get_Jenkinsbuildnumber()
        #
        # testSuiteID = self.getTestSuiteID(buildNumber, env_name)

        testSuiteID = getTSValue

        if response.status_code == 200 and "id" in parsed_response:
            self.create_TestRun(testSuiteID, 'API_UpdateTestCases', '1091204')
            test_run_id = self.get_TestRun(testSuiteID, 'API_UpdateTestCases')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')
        else:
            self.create_TestRun(testSuiteID, 'API_UpdateTestCases', '1091204')
            test_run_id = self.get_TestRun(testSuiteID, 'API_UpdateTestCases')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')


