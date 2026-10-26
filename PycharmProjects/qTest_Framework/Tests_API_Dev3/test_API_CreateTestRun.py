import json
import os
import sys
from datetime import datetime

import pytest
import requests
from Utilities.BaseClass_API import BaseClass_API

class Test_API_CreateTestRun:

    @pytest.mark.regression
    @pytest.mark.basic_regression
    # Project AutomationTest1  , module name : AT_API_CreateTestRun

    def test_API_CreateTestRun(self):

        # build_number = self.get_Jenkinsbuildnumber()

        URL = 'https://qtest-dev3.gtie.dell.com/api/v3/projects/403/test-runs'
        HEADERS = {
            "Authorization": "Bearer 29421d63-7c39-437f-83df-c9ac63ab774a",
            "Content-Type": "application/json"
        }

        Date = datetime.now()
        name = "AT_API_CreateTestRun" + str(Date)

        BODY = {
    "parentId": 446473,
    "parentType": "test-suite",
    "automation": "No",
    "testCaseId": 2481582,
    "id": 9853698,
    "name": name,
    "order": 1,
    "pid": "TR-1",
    "properties": [
        {
            "field_id": 80143,
            "field_name": "Run Order",
            "field_value": "1"
        },
        {
            "field_id": 79890,
            "field_name": "Execution Type",
            "field_value": "501",
            "field_value_name": "Functional"
        },
        {
            "field_id": 79891,
            "field_name": "Planned Start Date",
            "field_value": "2024-02-28T00:00:00+00:00"
        },
        {
            "field_id": 79893,
            "field_name": "Planned End Date",
            "field_value": "2024-02-28T00:00:00+00:00"
        },
        {
            "field_id": 79884,
            "field_name": "Assigned To",
            "field_value": "9629",
            "field_value_name": "Dinesh R"
        },
        {
            "field_id": 79899,
            "field_name": "Status",
            "field_value": "601",
            "field_value_name": "Passed"
        },
        {
            "field_id": 79897,
            "field_name": "Priority",
            "field_value": "723",
            "field_value_name": "Medium"
        }
    ],
    "test_case": {
        "links": [],
        "id": 2481582
    },
    "test_case_version_id": 3376317,
    "test_case_version": "1.0",
    "creator_id": 9629
}

        response = requests.post(URL, data=json.dumps(BODY), headers=HEADERS)
        parsed_response = json.loads(response.content)
        assert response.status_code == 201 and "id" in parsed_response

        # buildNumber, env_name = self.get_Jenkinsbuildnumber()
        #
        # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
        #
        # if response.status_code == 201 and "id" in parsed_response:
        #     self.create_TestRun(testSuiteID, 'AT_API_CreateTestRun', '2681807')
        #     test_run_id = self.get_TestRun(testSuiteID, 'AT_API_CreateTestRun')
        #     self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')
        # else:
        #     self.create_TestRun(testSuiteID, 'AT_API_CreateTestRun', '2681807')
        #     test_run_id = self.get_TestRun(testSuiteID, 'AT_API_CreateTestRun')
        #     self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')


