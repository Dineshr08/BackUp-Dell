import json
import os
import sys
from datetime import datetime

import pytest
import requests
from Utilities.BaseClass_API import BaseClass_API

class Test_API_UpdateTestCycle(BaseClass_API):

    @pytest.mark.regression


    # Project AutomationTest1  , module name : AT_API_UpdateTestCycle

    def test_API_UpdateTestCycle(self, getTSValue):

        # build_number = self.get_Jenkinsbuildnumber()

        URL = 'https://qtest.gtie.dell.com/api/v3/projects/404/test-cycles/787617'
        HEADERS = {
            "Authorization": "Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e",
            "Content-Type": "application/json"
        }

        Date = datetime.now()
        name = "AT Update TestCycle Description"+str(Date)
        BODY = {
    "description": name
}

        response = requests.put(URL, data=json.dumps(BODY), headers=HEADERS)
        parsed_response = json.loads(response.content)
        # assert response.status_code == 200 and "id" in parsed_response

        # buildNumber, env_name = self.get_Jenkinsbuildnumber()
        #
        # testSuiteID = self.getTestSuiteID(buildNumber, env_name)

        testSuiteID = getTSValue

        if response.status_code == 200 and "id" in parsed_response:
            self.create_TestRun(testSuiteID, 'API_UpdateTestCycle', '1091205')
            test_run_id = self.get_TestRun(testSuiteID, 'API_UpdateTestCycle')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')
        else:
            self.create_TestRun(testSuiteID, 'API_UpdateTestCycle', '1091205')
            test_run_id = self.get_TestRun(testSuiteID, 'API_UpdateTestCycle')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')


