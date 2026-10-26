import json
import os
import sys
from datetime import datetime

import pytest
import requests
from Utilities.BaseClass_API import BaseClass_API

# class Test_API_CreateRequirements(BaseClass_API):
class Test_API_CreateRequirements():

    @pytest.mark.regression

    #Project AutomationTest  , module name : AT_API_CreateRequirement

    def test_API_CreateRequirements(self):


        # build_number = self.get_Jenkinsbuildnumber()

        URL = 'https://qtest-dev3.gtie.dell.com/api/v3/projects/402/requirements'
        HEADERS = {
            "Authorization": "Bearer 29421d63-7c39-437f-83df-c9ac63ab774a",
            "Content-Type": "application/json"
        }
        Date = datetime.now()
        name = "AT API Requirement" + str(Date)

        BODY = {
    "name": name,
    "properties": [
        {
            "field_id": 79790,
            "field_name": "Status",
            "field_value": "911",
            "field_value_name": "New"
        },
        {
            "field_id": 79791,
            "field_name": "Priority",
            "field_value": "903",
            "field_value_name": "Nice to Have"
        },
        {
            "field_id": 79792,
            "field_name": "Type",
            "field_value": "801",
            "field_value_name": "Functional"
        }
    ],
    "parent_id": 450344
}

        response = requests.post(URL, data=json.dumps(BODY), headers=HEADERS)
        parsed_response = json.loads(response.content)
        assert response.status_code == 200 and "id" in parsed_response

        # buildNumber, env_name = self.get_Jenkinsbuildnumber()
        #
        # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
        # if response.status_code == 200 and "id" in parsed_response:
        #     self.create_TestRun(testSuiteID, 'API_CreateRequirements', '1091204')
        #     test_run_id = self.get_TestRun(testSuiteID, 'API_CreateRequirements')
        #     self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')
        # else:
        #     self.create_TestRun(testSuiteID, 'API_CreateRequirements', '1091204')
        #     test_run_id = self.get_TestRun(testSuiteID, 'API_CreateRequirements')
        #     self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')


