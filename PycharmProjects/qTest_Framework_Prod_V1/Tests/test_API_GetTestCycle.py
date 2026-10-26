import json
import os
import sys

import pytest
import requests
from Utilities.BaseClass_API import BaseClass_API

class Test_API_GetTestCycle(BaseClass_API):

    @pytest.mark.regression


    # Project AutomationTest  , module name : AT_API_GetTestCycle

    def test_API_GetTestCycle(self, getTSValue):

        # build_number = self.get_Jenkinsbuildnumber()


        URL = 'https://qtest.gtie.dell.com/api/v3/projects/397/test-cycles/788977'
        HEADERS = {
            "Authorization": "Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e",
            "Content-Type": "application/json"
        }

        response = requests.get(URL, headers=HEADERS)
        parsed_response = json.loads(response.content)
        # assert response.status_code == 200 and "id" in parsed_response

        # buildNumber, env_name = self.get_Jenkinsbuildnumber()
        #
        # testSuiteID = self.getTestSuiteID(buildNumber, env_name)

        testSuiteID = getTSValue

        if response.status_code == 200 and "id" in parsed_response:
            self.create_TestRun(testSuiteID, 'API_GetTestCycle', '1091205')
            test_run_id = self.get_TestRun(testSuiteID, 'API_GetTestCycle')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')
        else:
            self.create_TestRun(testSuiteID, 'API_GetTestCycle', '1091205')
            test_run_id = self.get_TestRun(testSuiteID, 'API_GetTestCycle')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')


