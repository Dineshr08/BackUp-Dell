import json
import os
import sys

import pytest
import requests
from Utilities.BaseClass_API import BaseClass_API

class Test_API_GetTestRun(BaseClass_API):

    @pytest.mark.regression
    # @pytest.mark.basic_regression

    # Project AutomationTest  , module name : AT_API_GetTestCycle, AT_API_GetTestSuite, AT_API_CreateTestCase

    def test_API_GetTestRun(self):

        # build_number = self.get_Jenkinsbuildnumber()


        URL = 'https://qtest.gtie.dell.com/api/v3/projects/397/test-runs/31112237'
        HEADERS = {
            "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823",
            "Content-Type": "application/json"
        }

        response = requests.get(URL, headers=HEADERS)
        parsed_response = json.loads(response.content)
        assert response.status_code == 200 and "id" in parsed_response

        # buildNumber, env_name = self.get_Jenkinsbuildnumber()
        #
        # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
        #
        # if response.status_code == 200 and "id" in parsed_response:
        #     self.create_TestRun(testSuiteID, 'API_GetTestRun', '2681807')
        #     test_run_id = self.get_TestRun(testSuiteID, 'API_GetTestRun')
        #     self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')
        # else:
        #     self.create_TestRun(testSuiteID, 'API_GetTestRun', '2681807')
        #     test_run_id = self.get_TestRun(testSuiteID, 'API_GetTestRun')
        #     self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')




