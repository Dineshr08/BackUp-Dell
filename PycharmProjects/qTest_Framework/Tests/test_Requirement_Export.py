import os
import time
from datetime import datetime

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.Requirement_PO import Requirement_PO
from PageObjects.TestDesign_PO import TestDesign_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from TestData.LoginPage_TD import LoginPage_TD
from TestData.TestExecution_TD import TestExecution_TD
from Utilities.BaseClass import BaseClass
from Utilities.BaseClass_Export import BaseClass_Export


class Test_Requirement_Export(BaseClass_Export):

    @pytest.fixture(params=LoginPage_TD.test_Requirement_Export)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface


    def test_Requirement_Export(self, getUserInput, getTSValue):
        try:
            log = self.logging()
            loginpage = LoginPage_PO(self.driver)
            loginpage.loginpage_po_username().send_keys(getUserInput["username"])
            loginpage.loginpage_po_password().send_keys(getUserInput["password"])
            homepage = loginpage.loginpage_po_loginBtn()
            cookies = self.get_cookies()
            action = ActionChains(self.driver)
            action.move_to_element(homepage.homepage_po_hoverProjectMenu()).perform()
            homepage.homepage_po_searchProject().send_keys("AutomationTesting1")
            wait = WebDriverWait(self.driver, 30)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "AutomationTesting1")))
            time.sleep(5)
            homepage.homepage_po_chooseAT1Project().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AutomationTesting1']")))
            UI_LandingPage_Validation = homepage.homepage_po_AT1Project_landingPage_Validation().text
            assert "AutomationTesting1" == UI_LandingPage_Validation
            requirement = homepage.homepage_po_requirement()
            time.sleep(5)
            requirement.requirement_po_Export().click()
            wait.until(EC.element_to_be_clickable(Requirement_PO.Export_Requirement))
            requirement.requirement_po_Export_Requirement().click()
            wait.until(EC.element_to_be_clickable(Requirement_PO.Export_OK))
            base_file_name = "AutomationTesting1 - Requirement"
            file_path = self.DirectoryFiles(base_file_name)
            # print(file_path)
            requirement.requirement_po_Export_OK().click()
            wait.until(EC.element_to_be_clickable(Requirement_PO.Reload))
            time.sleep(120)  # Adjust the time based on your expected download time
            assert os.path.exists(file_path), f'File not found at {file_path}'
            assert self.Validate_HTMLZipFileContent(file_path) is True
            assert os.path.getsize(file_path) > 0
            # Delete the file
            os.remove(file_path)
            assert not os.path.exists(file_path), f'File still exists at {file_path}'

            #TestCase2
            requirement.requirement_po_Reload().click()
            time.sleep(5)
            requirement.requirement_po_Export().click()
            wait.until(EC.element_to_be_clickable(Requirement_PO.Export_Requirement))
            base_file_name = "AutomationTesting1 - Requirement Traceability Matrix"
            extension = '.xlsx'
            attempts = 0
            max_attempts = 2
            while attempts < max_attempts:
                try:
                    requirement.requirement_po_Export_Req_TraceblityMatrixReport().click()
                    time.sleep(10)  # Adjust the time based on your expected download time
                    # print(file_path)
                    file_path = self.DirectoryFiles_TestDesign_Requirement(base_file_name, extension)
                    wait.until(EC.element_to_be_clickable(Requirement_PO.Reload))
                    assert os.path.exists(file_path), f'File not found at {file_path}'
                    # assert self.Validate_HTMLZipFileContent(file_path) is True
                    assert os.path.getsize(file_path) > 0
                    # Delete the file
                    os.remove(file_path)
                    assert not os.path.exists(file_path), f'File still exists at {file_path}'
                except:
                    attempts += 1
                    time.sleep(5)


            # time.sleep(20)  # Adjust the time based on your expected download time
            # print(file_path)
            # file_path = self.DirectoryFiles_TestDesign_Requirement(base_file_name, extension)
            # wait.until(EC.element_to_be_clickable(Requirement_PO.Reload))
            # assert os.path.exists(file_path), f'File not found at {file_path}'
            # # assert self.Validate_HTMLZipFileContent(file_path) is True
            # assert os.path.getsize(file_path) > 0
            # # Delete the file
            # os.remove(file_path)
            # assert not os.path.exists(file_path), f'File still exists at {file_path}'

            # TestCase3
            requirement.requirement_po_Reload().click()
            requirement.requirement_po_Export().click()
            wait.until(EC.element_to_be_clickable(Requirement_PO.Export_Requirement))
            base_file_name = "AutomationTesting1 - Requirements and Test Cases report"
            extension = '.xlsx'
            file_path = self.DirectoryFiles_TestDesign_Requirement(base_file_name, extension)
            requirement.requirement_po_Export_Req_TestCase_Report().click()
            # print(file_path)
            wait.until(EC.element_to_be_clickable(Requirement_PO.Reload))
            time.sleep(10)  # Adjust the time based on your expected download time
            assert os.path.exists(file_path), f'File not found at {file_path}'
            # assert self.Validate_HTMLZipFileContent(file_path) is True
            assert os.path.getsize(file_path) > 0
            # Delete the file
            os.remove(file_path)
            assert not os.path.exists(file_path), f'File still exists at {file_path}'

            # TestCase4
            requirement.requirement_po_Reload().click()
            requirement.requirement_po_Export().click()
            wait.until(EC.element_to_be_clickable(Requirement_PO.Export_Requirement))
            base_file_name = "AutomationTesting1 - Requirement and Test Execution Results"
            extension = '.xls'
            file_path = self.DirectoryFiles_TestDesign_Requirement(base_file_name, extension)
            requirement.requirement_po_Export_Req_TestExecution_Report().click()
            # print(file_path)
            wait.until(EC.element_to_be_clickable(Requirement_PO.Reload))
            time.sleep(10)  # Adjust the time based on your expected download time
            assert os.path.exists(file_path), f'File not found at {file_path}'
            # assert self.Validate_HTMLZipFileContent(file_path) is True
            assert os.path.getsize(file_path) > 0
            # Delete the file
            os.remove(file_path)
            assert not os.path.exists(file_path), f'File still exists at {file_path}'

            # TestCase5
            requirement.requirement_po_Reload().click()
            requirement.requirement_po_Export().click()
            wait.until(EC.element_to_be_clickable(Requirement_PO.Export_Requirement))
            base_file_name = "AutomationTesting1 - Requirement and Test Execution Results"
            extension = '.xls'
            file_path = self.DirectoryFiles_TestDesign_Requirement(base_file_name, extension)
            requirement.requirement_po_Export_Req_TestExecution_Report_NoCellMerge().click()
            # print(file_path)
            wait.until(EC.element_to_be_clickable(Requirement_PO.Reload))
            time.sleep(10)  # Adjust the time based on your expected download time
            assert os.path.exists(file_path), f'File not found at {file_path}'
            # assert self.Validate_HTMLZipFileContent(file_path) is True
            assert os.path.getsize(file_path) > 0
            # Delete the file
            os.remove(file_path)
            assert not os.path.exists(file_path), f'File still exists at {file_path}'


            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Requirement_Export', '4962838')
            test_run_id = self.get_TestRun(testSuiteID, 'Requirement_Export')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Requirement_Export', '4962838')
            test_run_id = self.get_TestRun(testSuiteID, 'Requirement_Export')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()










