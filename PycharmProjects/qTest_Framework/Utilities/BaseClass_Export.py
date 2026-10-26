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

@pytest.mark.usefixtures("setup_export", "getTSValue")
# @pytest.mark.usefixtures("setup")
class BaseClass_Export:

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

    def drop_files(element, files, offsetX=0, offsetY=0):
        driver = element.parent
        isLocal = not driver._is_remote or '127.0.0.1' in driver.command_executor._url
        paths = []

        # ensure files are present, and upload to the remote server if session is remote
        for file in (files if isinstance(files, list) else [files]):
            if not os.path.isfile(file):
                raise FileNotFoundError(file)
            paths.append(file if isLocal else element._upload(file))

        value = '\n'.join(paths)
        elm_input = driver.execute_script(BaseClass_Export.JS_DROP_FILES, element, offsetX, offsetY)
        elm_input._execute('sendKeysToElement', {'value': [value], 'text': value})

    WebElement.drop_files = drop_files


    def InsightScheduleTime(self):
        Schedule_Date = "//td[normalize-space()='6']"
        Schedule_Time = "//span[normalize-space()='7:25']"
        Schedule_Hour = "[normalize-space()='9']"
        Schedule_Date_Split = Schedule_Date.split("'")
        Schedule_Time_Split = Schedule_Time.split("'")
        Schedule_Hour_Split = Schedule_Hour.split("'")
        Current_time = datetime.now()
        Current_time = Current_time + timedelta(1)
        CurrentDate = Current_time.day
        Schedule_Date_Split[1] = str(CurrentDate)
        AM_PM = datetime.today().strftime("%p")
        # print(AM_PM)
        Current_Hour = Current_time.hour
        if Current_Hour > 12:
            Current_Hour = Current_Hour - 12
        else:
            Current_Hour = Current_Hour
        Current_Minutes = Current_time.minute
        Current_Minutes_Mod = Current_Minutes % 5
        if Current_Minutes_Mod == 0:
            Current_Minutes = Current_Minutes
            if Current_Minutes == 5:
                Current_Minutes = "0" + str(Current_Minutes)
            Current_Hour = Current_Hour
            Schedule_Hour_Split[1] = str(Current_Hour)
            Schedule_Time_Split[1] = "'" + str(Current_Hour) + ":" + str(Current_Minutes) + "'"
            # print(Current_Hour)
            # print(Current_Minutes)
        else:
            Future_Minutes = 5 - Current_Minutes_Mod
            Current_Minutes = Future_Minutes + Current_Minutes
            if Current_Minutes == 5:
                Current_Minutes = "0" + str(Current_Minutes)
            Schedule_Hour_Split[1] = str(Current_Hour)
            Schedule_Time_Split[1] = "'" + str(Current_Hour) + ":" + str(Current_Minutes) + "'"
            # print(Current_Hour)
            # print(Current_Minutes)
            Current_Hour = Current_Hour
            if Current_Minutes == 60:
                Current_Hour = Current_Hour + 1
                Current_Minutes = 00
                Schedule_Hour_Split[1] = str(Current_Hour)
                Schedule_Time_Split[1] = "'" + str(Current_Hour) + ":" + str(Current_Minutes) + "'"
                # print(Current_Hour)
                # print(Current_Minutes)

        Schedule_CurrentTime = ""
        Schedule_CurrentHour = ""
        Schedule_CurrentDate = ""
        for i in range(3):
            Schedule_CurrentTime = Schedule_CurrentTime + Schedule_Time_Split[i]
            Schedule_CurrentHour = Schedule_CurrentHour + Schedule_Hour_Split[i]
            Schedule_CurrentDate = Schedule_CurrentDate + Schedule_Date_Split[i]
        if AM_PM == "AM":
            Schedule_CurrentHour = "//span[@class='hour hour_am']" + Schedule_CurrentHour
        else:
            Schedule_CurrentHour = "//span[@class='hour hour_pm']" + Schedule_CurrentHour
        # print(Schedule_CurrentTime)
        # print(Schedule_CurrentHour)
        # print(Schedule_CurrentDate)

        return Schedule_CurrentTime, Schedule_CurrentHour, Schedule_CurrentDate, AM_PM

    def execute_script_Click(self, object):
        return self.driver.execute_script("arguments[0].click();", object)

    def IntegrationConnectionName(self,connName):
        return self.driver.find_element(By.LINK_TEXT, connName)

    def get_cookies(self):
        all_cookies = self.driver.get_cookies()
        user_context_token = None
        Cookies = None

        # Iterate through the list of cookies
        for cookie in all_cookies:
            if cookie['name'] == 'UserContextToken':
                user_context_token = cookie['value']
                Cookies = 'UserContextToken=' + user_context_token
                break
        # print(user_context_token)
        # print(Cookies)
        return Cookies

    def Logout(self):
        action = ActionChains(self.driver)
        wait = WebDriverWait(self.driver, 20)
        action.move_to_element(self.driver.find_element(By.ID, "topLeftTitle")).perform()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@id='searchProjectInput']").send_keys("AKT-Test")
        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "AKT-Test")))
        self.driver.find_element(By.LINK_TEXT, "AKT-Test").click()
        time.sleep(5)
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[@dojoattachpoint='titleNode']")))
        action.move_to_element(self.driver.find_element(By.CLASS_NAME, "show-user-menu")).perform()
        time.sleep(5)
        wait.until(EC.element_to_be_clickable((By.ID, "log-out-link")))
        time.sleep(5)
        self.driver.find_element(By.ID, "log-out-link").click()

    def TerminateSession(self, Cookies):
        Terminate_response = requests.get(
            url="{}".format('https://qtest-stage.gtie.dell.com/logout'),
            headers={
                'Cookie': Cookies
            },
            verify=False
        )

    def generate_file_name(self, base_name, existing_files):
        counter = 0
        file_name = f"{base_name} - {time.strftime('%Y%m%d')}.zip"
        while True:
            if file_name not in existing_files:
                return file_name
            else:
                counter += 1
                file_name = f"{base_name} - {time.strftime('%Y%m%d')} ({counter}).zip"


    def DirectoryFiles(self, base_file_name):
        # Specify the directory where the file should be downloaded
        download_directory = "C:\\Test"
        # Get a list of existing files in the directory
        existing_files = os.listdir(download_directory)
        # print(existing_files)
        # Generate the expected file name
        file_name = self.generate_file_name(base_file_name, existing_files)
        # Verify if the file is present in the directory
        file_path = os.path.join(download_directory, file_name)
        # print(file_path)
        return file_path

    def Validate_HTMLZipFileContent(self, downloaded_zip_path):
        with zipfile.ZipFile(downloaded_zip_path, 'r') as zip_ref:
            # Get the list of file names inside the zip
            file_names = zip_ref.namelist()

            # Check if there are any files inside the zip
            if file_names:
                # print("The zip file contains data.")
                # print("List of files in the zip:", file_names)

                # Assuming there's only one HTML file in the zip, read its contents
                html_file_name = file_names[0]
                with zip_ref.open(html_file_name) as html_file:
                    html_contents = html_file.read().decode('utf-8')

                    # Check if the HTML file contains data (non-empty)
                    if html_contents.strip():
                        return True
                    else:
                        return False
            else:
                # print("The zip file is empty or does not contain any data.")
                return False

    def Validate_HTMLZipExcelFileContent(self, downloaded_zip_path):
        with zipfile.ZipFile(downloaded_zip_path, 'r') as zip_ref:
            # Get the list of file names inside the zip
            file_names = zip_ref.namelist()

            # Check if there are any files inside the zip
            if file_names:
                # print("The zip file contains data.")
                # print("List of files in the zip:", file_names)

                # Assuming there's only one HTML file in the zip, read its contents

                has_data = False
                excel_file_name = file_names[0]
                zip_ref.extractall('extracted_files')
                excel_file_path = os.path.join('extracted_files', excel_file_name)
                workbook = xlrd.open_workbook(excel_file_path)

                for sheet_name in workbook.sheet_names():
                    sheet = workbook.sheet_by_name(sheet_name)
                    if sheet.nrows > 0 and sheet.ncols > 0:
                        return True
                    else:
                        return False
            else:
                # print("The zip file is empty or does not contain any data.")
                return False

    def generate_file_name_TestDesign_Execution(self, base_name, existing_files):
        counter = 0
        file_name = f"{base_name}-{time.strftime('%Y%m%d')}.zip"
        while True:
            if file_name not in existing_files:
                return file_name
            else:
                counter += 1
                file_name = f"{base_name}-{time.strftime('%Y%m%d')} ({counter}).zip"


    def DirectoryFiles_TestDesign_Execution(self, base_file_name):
        # Specify the directory where the file should be downloaded
        download_directory = "C:\\Test"
        # Get a list of existing files in the directory
        existing_files = os.listdir(download_directory)
        # print(existing_files)
        # Generate the expected file name
        file_name = self.generate_file_name_TestDesign_Execution(base_file_name, existing_files)
        # Verify if the file is present in the directory
        file_path = os.path.join(download_directory, file_name)
        # print(file_path)
        return file_path

    def Validate_Test_Execution_ExportXls(self, downloaded_zip_path):
        # Load the Excel file
        workbook = openpyxl.load_workbook(downloaded_zip_path)

        # Get sheet names
        sheet_names = workbook.sheetnames

        # Check if any sheets have data
        for sheet_name in sheet_names:
            sheet = workbook[sheet_name]
            if sheet.max_row > 0 or sheet.max_column > 0:
                return True
            else:
                return False



    def generate_file_name_Test_Execution_ExportXls(self, base_name, existing_files):
        counter = 0
        file_name = f"{base_name}--{time.strftime('%Y%m%d')}.xlsx"
        while True:
            if file_name not in existing_files:
                return file_name
            else:
                counter += 1
                file_name = f"{base_name}--{time.strftime('%Y%m%d')} ({counter}).xlsx"

    def generate_file_name_Test_Execution_ExportAll(self, base_name, existing_files):
        counter = 0
        file_name = f"{base_name}-{time.strftime('%Y%m%d')}.xlsx"
        while True:
            if file_name not in existing_files:
                return file_name
            else:
                counter += 1
                file_name = f"{base_name}-{time.strftime('%Y%m%d')} ({counter}).xlsx"


    def DirectoryFiles_Test_Execution_ExportXls(self, base_file_name):
        # Specify the directory where the file should be downloaded
        download_directory = "C:\\Test"
        # Get a list of existing files in the directory
        existing_files = os.listdir(download_directory)
        # print(existing_files)
        # Generate the expected file name
        file_name = self.generate_file_name_Test_Execution_ExportXls(base_file_name, existing_files)
        # Verify if the file is present in the directory
        file_path = os.path.join(download_directory, file_name)
        # print(file_path)
        return file_path

    def DirectoryFiles_Test_Execution_ExportAll(self, base_file_name):
        # Specify the directory where the file should be downloaded
        download_directory = "C:\\Test"
        # Get a list of existing files in the directory
        existing_files = os.listdir(download_directory)
        # print(existing_files)
        # Generate the expected file name
        file_name = self.generate_file_name_Test_Execution_ExportAll(base_file_name, existing_files)
        # Verify if the file is present in the directory
        file_path = os.path.join(download_directory, file_name)
        # print(file_path)
        return file_path

    def generate_file_name_TestDesign_Requirement(self, base_name, existing_files, extension):
        counter = 0
        file_name = f"{base_name}"+extension
        # print(file_name)
        while True:
            if file_name not in existing_files:
                # print(file_name)
                return file_name
            else:
                counter += 1
                file_name = f"{base_name} ({counter})"+extension
                # print(file_name)


    def DirectoryFiles_TestDesign_Requirement(self, base_file_name, extension):
        # Specify the directory where the file should be downloaded
        download_directory = "C:\\Test"
        # Get a list of existing files in the directory
        existing_files = os.listdir(download_directory)
        # print(existing_files)
        # Generate the expected file name
        file_name = self.generate_file_name_TestDesign_Requirement(base_file_name, existing_files, extension)
        # Verify if the file is present in the directory
        file_path = os.path.join(download_directory, file_name)
        # print(file_path)
        return file_path

    def get_Jenkinsbuildnumber(self):
        # Get the build number from the environment variable
        build_number = os.environ.get('BUILD_NUMBER')
        env_name = os.environ.get('env_name')

        # Use the build number in your script as needed
        print(f"Build Number: {build_number}")
        print(f"env_name: {env_name}")
        return build_number, env_name

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












