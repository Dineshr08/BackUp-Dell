import json
import os
from datetime import datetime

import pytest
import requests
from Utilities.BaseClass_API import BaseClass_API
# from Jenkins_TestSuite.Jenkins_TestSuiteCreation_API import *
class Test_API_CreateTestRun(BaseClass_API):

    @pytest.mark.regression

    # Project AutomationTest1  , module name : AT_API_CreateTestRun

    def test_API_CreateTestRun(self, getTSValue):

        # build_number = self.get_Jenkinsbuildnumber()

        URL = 'https://qtest-stage.gtie.dell.com/api/v3/projects/404/test-runs'
        HEADERS = {
            "Authorization": "Bearer fda0002f-500a-47c6-b617-0381dc027b39",
            "Content-Type": "application/json"
        }

        Date = datetime.now()
        name = "AT_API_CreateTestRun" + str(Date)

        BODY = {
    "parentId": 685027,
    "parentType": "test-suite",
    "automation": "No",
    "testCaseId": 4766267,
    "id": 30139319,
    "name": name,
    "order": 1,
    "pid": "TR-63",
    "properties": [
        {
            "field_id": 77583,
            "field_name": "Run Order",
            "field_value": "1"
        },
        {
            "field_id": 77495,
            "field_name": "Execution Type",
            "field_value": "501",
            "field_value_name": "Functional"
        },
        {
            "field_id": 77496,
            "field_name": "Planned Start Date",
            "field_value": "2022-08-20T00:00:00+00:00"
        },
        {
            "field_id": 77498,
            "field_name": "Planned End Date",
            "field_value": "2022-08-20T00:00:00+00:00"
        },
        {
            "field_id": 77489,
            "field_name": "Assigned To",
            "field_value": "10580",
            "field_value_name": "Dinesh R"
        },
        {
            "field_id": 77504,
            "field_name": "Status",
            "field_value": "605",
            "field_value_name": "Unexecuted"
        },
        {
            "field_id": 77502,
            "field_name": "Priority",
            "field_value": "723",
            "field_value_name": "Medium"
        }
    ],
    "test_case": {
        "links": [],
        "id": 4766267
    },
    "test_case_version_id": 6803931,
    "test_case_version": "1.0",
    "creator_id": 10580
}

        response = requests.post(URL, data=json.dumps(BODY), headers=HEADERS)
        parsed_response = json.loads(response.content)
        # assert response.status_code == 201 and "id" in parsed_response
        #
        # buildNumber, env_name = self.get_Jenkinsbuildnumber()
        #
        # testSuiteID = self.getTestSuiteID(buildNumber, env_name)

        testSuiteID = getTSValue

        if response.status_code == 201 and "id" in parsed_response:
            self.create_TestRun(testSuiteID, 'API_CreateTestRun', '2681807')
            test_run_id = self.get_TestRun(testSuiteID, 'API_CreateTestRun')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')
        else:
            self.create_TestRun(testSuiteID, 'API_CreateTestRun', '2681807')
            test_run_id = self.get_TestRun(testSuiteID, 'API_CreateTestRun')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')


