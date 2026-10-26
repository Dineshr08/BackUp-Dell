import json
import os
import sys
from datetime import datetime

import pytest
import requests

# from Tests.conftest import getTSValue
from Utilities.BaseClass import BaseClass
from Utilities.BaseClass_API import BaseClass_API

# @pytest.mark.usefixtures("testsuitedata")
class Test_API_CreateRequirements(BaseClass_API):

    @pytest.mark.regression

    #Project AutomationTest  , module name : AT_API_CreateRequirement

    def test_API_CreateRequirements(self, getTSValue):


        # build_number = self.get_Jenkinsbuildnumber()

        URL = 'https://qtest.gtie.dell.com/api/v3/projects/397/requirements'
        HEADERS = {
            "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823",
            "Content-Type": "application/json"
        }
        Date = datetime.now()
        name = "AT API Requirement" + str(Date)

        BODY = {
    "name": name,
    "properties": [
        {
            "field_id": 75781,
            "field_name": "Status",
            "field_value": "911",
            "field_value_name": "New"
        },
        {
            "field_id": 75782,
            "field_name": "Priority",
            "field_value": "903",
            "field_value_name": "Nice to Have"
        },
        {
            "field_id": 75783,
            "field_name": "Type",
            "field_value": "801",
            "field_value_name": "Functional"
        }
    ],
    "parent_id": 779855
}

        response = requests.post(URL, data=json.dumps(BODY), headers=HEADERS)
        parsed_response = json.loads(response.content)
        # assert response.status_code == 200 and "id" in parsed_response
        testSuiteID=getTSValue
        print("the testsuiteid is:",testSuiteID)

        # # testSuiteID = os.environ.get('TestSuiteID')
        # testSuiteID = request.config.getoption("--test_suiteID")
        #
        # # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
        if response.status_code == 200 and "id" in parsed_response:
            self.create_TestRun(testSuiteID, 'API_CreateRequirements', '1091204')
            test_run_id = self.get_TestRun(testSuiteID, 'API_CreateRequirements')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')
            assert response.status_code == 200 and "id" in parsed_response
        else:
            self.create_TestRun(testSuiteID, 'API_CreateRequirements', '1091204')
            test_run_id = self.get_TestRun(testSuiteID, 'API_CreateRequirements')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')
            assert response.status_code == 200 and "id" in parsed_response


