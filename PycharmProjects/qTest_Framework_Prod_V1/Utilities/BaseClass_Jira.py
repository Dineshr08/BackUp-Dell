import fnmatch
import inspect
import logging
import time
import zipfile

import openpyxl
import xlrd
from datetime import datetime, timedelta
from pathlib import Path

import pytest
import requests
from openpyxl.reader.excel import load_workbook
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import os.path
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import json
import os
import sys
from datetime import datetime
from datetime import datetime, timezone
import pytest
import requests

@pytest.mark.usefixtures("setup_jira", "getTSValue")
class BaseClass_Jira:

    def logging(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    JS_DROP_FILES = "var k=arguments,d=k[0],g=k[1],c=k[2],m=d.ownerDocument||document;for(var e=0;;){var f=d.getBoundingClientRect(),b=f.left+(g||(f.width/2)),a=f.top+(c||(f.height/2)),h=m.elementFromPoint(b,a);if(h&&d.contains(h)){break}if(++e>1){var j=new Error('Element not interactable');j.code=15;throw j}d.scrollIntoView({behavior:'instant',block:'center',inline:'center'})}var l=m.createElement('INPUT');l.setAttribute('type','file');l.setAttribute('multiple','');l.setAttribute('style','position:fixed;z-index:2147483647;left:0;top:0;');l.onchange=function(q){l.parentElement.removeChild(l);q.stopPropagation();var r={constructor:DataTransfer,effectAllowed:'all',dropEffect:'none',types:['Files'],files:l.files,setData:function u(){},getData:function o(){},clearData:function s(){},setDragImage:function i(){}};if(window.DataTransferItemList){r.items=Object.setPrototypeOf(Array.prototype.map.call(l.files,function(x){return{constructor:DataTransferItem,kind:'file',type:x.type,getAsFile:function v(){return x},getAsString:function y(A){var z=new FileReader();z.onload=function(B){A(B.target.result)};z.readAsText(x)},webkitGetAsEntry:function w(){return{constructor:FileSystemFileEntry,name:x.name,fullPath:'/'+x.name,isFile:true,isDirectory:false,file:function z(A){A(x)}}}}}),{constructor:DataTransferItemList,add:function t(){},clear:function p(){},remove:function n(){}})}['dragenter','dragover','drop'].forEach(function(v){var w=m.createEvent('DragEvent');w.initMouseEvent(v,true,true,m.defaultView,0,0,0,b,a,false,false,false,false,0,null);Object.setPrototypeOf(w,null);w.dataTransfer=r;Object.setPrototypeOf(w,DragEvent.prototype);h.dispatchEvent(w)})};m.documentElement.appendChild(l);l.getBoundingClientRect();return l"


    def create_TestRun(self, parentId, name, testCaseID):
        BASE_URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-runs?parentId='
        REM_URL = '&parentType=test-suite'
        URL = "{}{}{}".format(BASE_URL, parentId, REM_URL)
        # URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-runs?parentId=786189&parentType=test-suite'
        HEADERS = {
            "Authorization": "Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e",
            "Content-Type": "application/json"
        }

        BODY = {
    "name": name,
    "properties": [
        {
            "field_id": 34202,
            "field_name": "Run Order",
            "field_value": "1"
        },
        {
            "field_id": 33220,
            "field_name": "Execution Type",
            "field_value": "501",
            "field_value_name": "Functional"
        },
        {
            "field_id": 33214,
            "field_name": "Assigned To",
            "field_value": "10580",
            "field_value_name": "Dinesh R"
        },
        {
            "field_id": 33229,
            "field_name": "Status",
            "field_value": "601",
            "field_value_name": "Passed"
        },
        {
            "field_id": 33227,
            "field_name": "Priority",
            "field_value": "723",
            "field_value_name": "Medium"
        },
		{
            "field_id": -199,
            "field_name": "Planned Start Date",
            "field_value": "2023-09-22T00:00:00+00:00"
        },
		{
            "field_id": -198,
            "field_name": "Planned End Date",
            "field_value": "2023-09-22T00:00:00+00:00"
        }
    ],
    "test_case": {
        "links": [],
        "id": testCaseID
    },
    "test_case_version_id": 3644888,
    "test_case_version": "1.0",
    "creator_id": 10580
}
        response = requests.post(URL, data=json.dumps(BODY), headers=HEADERS)
        parsed_response = json.loads(response.content)
        assert response.status_code == 201 and "id" in parsed_response

    def get_TestRun(self, parentId, name):
        BASE_URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-runs?parentId='
        REM_URL = '&parentType=test-suite'
        URL = "{}{}{}".format(BASE_URL, parentId, REM_URL)
        # URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-runs?parentId=786189&parentType=test-suite'
        HEADERS = {
            "Authorization": "Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e",
            "Content-Type": "application/json"
        }

        response = requests.get(URL, headers=HEADERS)
        print(response.request.body)
        print(response.request.url)
        print(response.status_code)
        print(response.json())
        parsed_response = json.loads(response.content)
        # assert response.status_code == 200 and "parentId" in parsed_response
        assert response.status_code == 200

        if response.status_code == 200:
            # Connection_info = response.json()

            Connection_info = response.json()["items"]

            target_test_run_name = name

            for test_run in Connection_info:
                if test_run["name"] == target_test_run_name:
                    target_test_run_id = test_run["id"]
                    print(f"The ID of {target_test_run_name} is {target_test_run_id}")
                    return target_test_run_id
            else:
                print(f"{target_test_run_name} not found in the response.")

    def update_TestLog(self, TestRunID, ID, Status, ColourCode):

        BASE_URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-runs/'
        REM_URL = '/test-logs'
        URL = "{}{}{}".format(BASE_URL, TestRunID, REM_URL)
        # URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-runs?parentId=786189&parentType=test-suite'
        HEADERS = {
            "Authorization": "Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e",
            "Content-Type": "application/json"
        }

        # Get the current time in UTC
        current_time_utc = datetime.now(timezone.utc)

        # Format the current time as a string in the desired format
        formatted_time = current_time_utc.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

        BODY = {
    "exe_start_date": formatted_time,
    "exe_end_date": formatted_time,
    "status": {
    "id": ID,
    "name": Status,
    "is_default": "false",
    "color": ColourCode,
    "active": "true"
  }
}
        response = requests.post(URL, data=json.dumps(BODY), headers=HEADERS)
        parsed_response = json.loads(response.content)
        assert response.status_code == 201 and "id" in parsed_response

    def getTestSuiteID(self,build_number, env_name):
        # Get the build number from command line arguments
        # build_number = sys.argv[1]
        # env_name = sys.argv[2]

        build_number = build_number
        env_name = env_name

        # build_number = 81
        # env_name = 'stage'

        # Your Python script logic here...
        print(f"Build Number: {build_number}")
        print(f"Env Name: {env_name}")
        if env_name == "stage":
            URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-suites?parentId=825119&parentType=test-cycle'
        elif env_name == "prod":
            URL = 'https://qtest.gtie.dell.com/api/v3/projects/167/test-suites?parentId=825122&parentType=test-cycle'

        HEADERS = {
            "Authorization": "Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e",
            "Content-Type": "application/json"
        }

        # Date = datetime.now()
        name = str(env_name) + "_Jenkins_Build_" + str(build_number)

        response = requests.get(URL, headers=HEADERS)
        parsed_response = json.loads(response.content)

        if response.status_code == 200:
            Connection_info = response.json()

            target_test_suite_name = name

            for test_suite in Connection_info:
                if test_suite["name"] == target_test_suite_name:
                    target_test_suite_id = test_suite["id"]
                    print(f"The ID of {target_test_suite_name} is {target_test_suite_id}")
                    return target_test_suite_id
            else:
                print(f"{target_test_suite_name} not found in the response.")












