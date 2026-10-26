import os
import time

import pytest
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


class Test_Requirement_DataQuery_Export(BaseClass_Export):

    @pytest.fixture(params=LoginPage_TD.test_Requirement_DataQuery_Export)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_Requirement_DataQuery_Export(self, getUserInput, getTSValue):
        try:
            log = self.logging()
            loginpage = LoginPage_PO(self.driver)
            loginpage.loginpage_po_username().send_keys(getUserInput["username"])
            loginpage.loginpage_po_password().send_keys(getUserInput["password"])
            homepage = loginpage.loginpage_po_loginBtn()
            cookies = self.get_cookies()
            action = ActionChains(self.driver)
            action.move_to_element(homepage.homepage_po_hoverProjectMenu()).perform()
            homepage.homepage_po_searchProject().send_keys("AKT-Test")
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "AKT-Test")))
            # wait.until(EC.staleness_of(HomePage_PO.chooseAT1Project))
            time.sleep(5)
            homepage.homepage_po_chooseAKTTestProject().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AKT-Test']")))
            UI_LandingPage_Validation = homepage.homepage_po_AKTTestProject_landingPage_Validation().text
            assert "AKT-Test" == UI_LandingPage_Validation
            requirement = homepage.homepage_po_requirement()
            time.sleep(5)
            action.move_to_element(requirement.requirement_po_Existing_Requirement()).perform()
            requirement.requirement_po_Existing_Requirement().click()
            time.sleep(1)
            action.context_click(requirement.requirement_po_Existing_Requirement()).perform()
            wait.until(EC.element_to_be_clickable(Requirement_PO.RightClick_DataQuery))
            requirement.requirement_po_RightClick_DataQuery().click()
            time.sleep(5)
            wait.until(EC.presence_of_element_located((By.XPATH, "//td[text()='AT_AutomationTesting']")))
            requirement.requirement_po_AllCheckBox().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='✓']")))
            base_file_name = "AKT-Test"
            file_path = self.DirectoryFiles_Test_Execution_ExportXls(base_file_name)
            requirement.requirement_po_DataQuery_ExportXls().click()
            time.sleep(50)
            assert os.path.exists(file_path), f'File not found at {file_path}'
            assert self.Validate_Test_Execution_ExportXls(file_path) is True
            assert os.path.getsize(file_path) > 0
            # Delete the file
            os.remove(file_path)
            assert not os.path.exists(file_path), f'File still exists at {file_path}'
            base_file_name = "AKT-Test"
            file_path = self.DirectoryFiles_Test_Execution_ExportAll(base_file_name)
            requirement.requirement_po_DataQuery_ExportAll().click()
            time.sleep(50)
            assert os.path.exists(file_path), f'File not found at {file_path}'
            assert self.Validate_Test_Execution_ExportXls(file_path) is True
            assert os.path.getsize(file_path) > 0
            # Delete the file
            os.remove(file_path)
            assert not os.path.exists(file_path), f'File still exists at {file_path}'

            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Requirement_DataQuery_Export', '4962838')
            test_run_id = self.get_TestRun(testSuiteID, 'Requirement_DataQuery_Export')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Requirement_DataQuery_Export', '4962838')
            test_run_id = self.get_TestRun(testSuiteID, 'Requirement_DataQuery_Export')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()







