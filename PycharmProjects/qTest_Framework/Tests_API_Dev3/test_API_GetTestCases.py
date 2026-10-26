import json
import os
import sys

import pytest
import requests

from Utilities.BaseClass_API import BaseClass_API
class Test_API_GetTestCases:

    @pytest.mark.regression
    @pytest.mark.basic_regression
    # Project AutomationTest  , module name : AT_API_GetTestCase

    def test_API_GetTestCases(self):

        # build_number = self.get_Jenkinsbuildnumber()


        URL = 'https://qtest-dev3.gtie.dell.com/api/v3/projects/402/test-cases/2481580'
        HEADERS = {
            "Authorization": "Bearer 29421d63-7c39-437f-83df-c9ac63ab774a",
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
        #     self.create_TestRun(testSuiteID, 'API_GetTestCases', '1091204')
        #     test_run_id = self.get_TestRun(testSuiteID, 'API_GetTestCases')
        #     self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')
        # else:
        #     self.create_TestRun(testSuiteID, 'API_GetTestCases', '1091204')
        #     test_run_id = self.get_TestRun(testSuiteID, 'API_GetTestCases')
        #     self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')


