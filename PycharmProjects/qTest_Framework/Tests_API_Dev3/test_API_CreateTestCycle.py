import json
import os
import sys
from datetime import datetime

import pytest
import requests
from Utilities.BaseClass_API import BaseClass_API

# class Test_API_CreateTestCycle(BaseClass_API):
class Test_API_CreateTestCycle:

    @pytest.mark.regression
    @pytest.mark.basic_regression
    # Project AutomationTest  , module name : AT_API_CreateTestCycle2023-09-28 16:31:20.325583

    def test_API_CreateTestCycle(self):

        # build_number = self.get_Jenkinsbuildnumber()

        URL = 'https://qtest-dev3.gtie.dell.com/api/v3/projects/402/test-cycles'
        HEADERS = {
            "Authorization": "Bearer 29421d63-7c39-437f-83df-c9ac63ab774a",
            "Content-Type": "application/json"
        }
        Date = datetime.now()
        name = "AT_API_CreateTestCycle" + str(Date)
        BODY = {
    "name": name,
    "description": "<p>AT_API_CreateTestCycle</p>"

}

        response = requests.post(URL, data=json.dumps(BODY), headers=HEADERS)
        parsed_response = json.loads(response.content)
        assert response.status_code == 200 and "id" in parsed_response

        # buildNumber, env_name = self.get_Jenkinsbuildnumber()
        #
        # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
        #
        # if response.status_code == 200 and "id" in parsed_response:
        #     self.create_TestRun(testSuiteID, 'API_CreateTestCycle', '1091205')
        #     test_run_id = self.get_TestRun(testSuiteID, 'API_CreateTestCycle')
        #     self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')
        # else:
        #     self.create_TestRun(testSuiteID, 'API_CreateTestCycle', '1091205')
        #     test_run_id = self.get_TestRun(testSuiteID, 'API_CreateTestCycle')
        #     self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')


