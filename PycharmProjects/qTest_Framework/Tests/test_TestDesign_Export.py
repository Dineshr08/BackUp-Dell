import os
import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.TestDesign_PO import TestDesign_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from TestData.LoginPage_TD import LoginPage_TD
from TestData.TestExecution_TD import TestExecution_TD
from Utilities.BaseClass import BaseClass
from Utilities.BaseClass_Export import BaseClass_Export


class Test_TestDesign_Export(BaseClass_Export):

    @pytest.fixture(params=LoginPage_TD.test_TestDesign_Export)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface


    def test_TestDesign_Export(self, getUserInput, getTSValue):
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
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "AutomationTesting1")))
            time.sleep(5)
            homepage.homepage_po_chooseAT1Project().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AutomationTesting1']")))
            UI_LandingPage_Validation = homepage.homepage_po_AT1Project_landingPage_Validation().text
            assert "AutomationTesting1" == UI_LandingPage_Validation
            testdesign = homepage.homepage_po_testdesign()
            time.sleep(5)
            testdesign.testdesign_po_Export().click()
            wait.until(EC.element_to_be_clickable(TestDesign_PO.Export_TestDesign))
            testdesign.testdesign_po_Export_TestDesign().click()
            # wait.until(EC.element_to_be_clickable(TestDesign_PO.Export_OK))
            wait.until(EC.element_to_be_clickable(TestDesign_PO.Export_OK))
            base_file_name = "AutomationTesting1-Test Case"
            file_path = self.DirectoryFiles_TestDesign_Execution(base_file_name)
            testdesign.testdesign_po_Export_OK().click()
            wait.until(EC.element_to_be_clickable(TestDesign_PO.Reload))
            time.sleep(50)  # Adjust the time based on your expected download time
            assert os.path.exists(file_path), f'File not found at {file_path}'
            assert self.Validate_HTMLZipExcelFileContent(file_path) is True
            assert os.path.getsize(file_path) > 0
            # Delete the file
            os.remove(file_path)
            assert not os.path.exists(file_path), f'File still exists at {file_path}'

            #TestCas 2
            testdesign.testdesign_po_Reload().click()
            testdesign.testdesign_po_Export().click()
            base_file_name = "AutomationTesting1 - Test Case Traceability Matrix"
            extension = '.xlsx'
            wait.until(EC.element_to_be_clickable(TestDesign_PO.Export_TestDesign))
            testdesign.testdesign_po_TestCaseTraceblity_Matrix_Report().click()
            # wait.until(EC.element_to_be_clickable(TestDesign_PO.Export_OK))
            file_path = self.DirectoryFiles_TestDesign_Requirement(base_file_name, extension)
            wait.until(EC.element_to_be_clickable(TestDesign_PO.Reload))
            time.sleep(20)  # Adjust the time based on your expected download time
            assert os.path.exists(file_path), f'File not found at {file_path}'
            # assert self.Validate_HTMLZipExcelFileContent(file_path) is True
            assert os.path.getsize(file_path) > 0
            # Delete the file
            os.remove(file_path)
            assert not os.path.exists(file_path), f'File still exists at {file_path}'

            # TestCas 3
            testdesign.testdesign_po_Reload().click()
            testdesign.testdesign_po_Export().click()
            base_file_name = "AutomationTesting1 - Test Cases and Requirements report"
            extension = '.xlsx'
            wait.until(EC.element_to_be_clickable(TestDesign_PO.Export_TestDesign))
            testdesign.testdesign_po_TestCaseandRequirement_Report().click()
            # wait.until(EC.element_to_be_clickable(TestDesign_PO.Export_OK))
            file_path = self.DirectoryFiles_TestDesign_Requirement(base_file_name, extension)
            wait.until(EC.element_to_be_clickable(TestDesign_PO.Reload))
            time.sleep(20)  # Adjust the time based on your expected download time
            assert os.path.exists(file_path), f'File not found at {file_path}'
            # assert self.Validate_HTMLZipExcelFileContent(file_path) is True
            assert os.path.getsize(file_path) > 0
            # Delete the file
            os.remove(file_path)
            assert not os.path.exists(file_path), f'File still exists at {file_path}'

            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestDesign_Export', '4962838')
            test_run_id = self.get_TestRun(testSuiteID, 'TestDesign_Export')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestDesign_Export', '4962838')
            test_run_id = self.get_TestRun(testSuiteID, 'TestDesign_Export')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()










