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


class Test_TestExecution_Export(BaseClass_Export):

    @pytest.fixture(params=LoginPage_TD.test_TestExecution_Export)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_TestExecution_Export(self, getUserInput, getTSValue):
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
            testexecution = homepage.homepage_po_testexecution()
            time.sleep(5)
            testexecution.testexecution_po_Export().click()
            wait.until(EC.element_to_be_clickable(TestExecution_PO.Export_TestDesign))
            testexecution.testexecution_po_Export_TestDesign().click()
            wait.until(EC.element_to_be_clickable(TestExecution_PO.Export_OK))
            base_file_name = "AutomationTesting1-Test Run"
            file_path = self.DirectoryFiles_TestDesign_Execution(base_file_name)
            testexecution.testexecution_po_Export_OK().click()
            wait.until(EC.element_to_be_clickable(TestExecution_PO.Reload))
            time.sleep(50)  # Adjust the time based on your expected download time
            assert os.path.exists(file_path), f'File not found at {file_path}'
            assert self.Validate_HTMLZipExcelFileContent(file_path) is True
            assert os.path.getsize(file_path) > 0
            # Delete the file
            os.remove(file_path)
            time.sleep(15)
            assert not os.path.exists(file_path), f'File still exists at {file_path}'

            # TestCase2
            testexecution.testexecution_po_Reload().click()
            testexecution.testexecution_po_Export().click()
            base_file_name = "AutomationTesting1-Test Execution and Defects"
            file_path = self.DirectoryFiles_TestDesign_Execution(base_file_name)
            wait.until(EC.element_to_be_clickable(TestExecution_PO.Export_TestDesign))
            testexecution.testexecution_po_Export_TestExecution_Defect().click()
            wait.until(EC.element_to_be_clickable(TestExecution_PO.Reload))
            time.sleep(10)  # Adjust the time based on your expected download time
            assert os.path.exists(file_path), f'File not found at {file_path}'
            assert self.Validate_HTMLZipExcelFileContent(file_path) is True
            assert os.path.getsize(file_path) > 0
            # Delete the file
            os.remove(file_path)
            time.sleep(15)
            assert not os.path.exists(file_path), f'File still exists at {file_path}'

            # TestCase3
            testexecution.testexecution_po_Reload().click()
            testexecution.testexecution_po_Export().click()
            base_file_name = "AutomationTesting1-Test Execution and Defects"
            file_path = self.DirectoryFiles_TestDesign_Execution(base_file_name)
            wait.until(EC.element_to_be_clickable(TestExecution_PO.Export_TestDesign))
            testexecution.testexecution_po_Export_TestExecution_Defect_NoCellMerging().click()
            wait.until(EC.element_to_be_clickable(TestExecution_PO.Reload))
            time.sleep(10)  # Adjust the time based on your expected download time
            assert os.path.exists(file_path), f'File not found at {file_path}'
            assert self.Validate_HTMLZipExcelFileContent(file_path) is True
            assert os.path.getsize(file_path) > 0
            # Delete the file
            os.remove(file_path)
            time.sleep(15)
            assert not os.path.exists(file_path), f'File still exists at {file_path}'

            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestExecution_Export', '4962838')
            test_run_id = self.get_TestRun(testSuiteID, 'TestExecution_Export')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestExecution_Export', '4962838')
            test_run_id = self.get_TestRun(testSuiteID, 'TestExecution_Export')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()










