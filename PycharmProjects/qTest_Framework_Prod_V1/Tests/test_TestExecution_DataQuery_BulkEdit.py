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


class Test_TestExecution_DataQuery_BulkEdit(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_TestExecution_DataQuery_BulkEdit)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_TestExecution_DataQuery_BulkEdit(self, getUserInput, getTSValue):
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
            wait = WebDriverWait(self.driver, 60)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "AutomationTesting1")))
            time.sleep(5)
            homepage.homepage_po_chooseAT1Project().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AutomationTesting1']")))
            UI_LandingPage_Validation = homepage.homepage_po_AT1Project_landingPage_Validation().text
            assert "AutomationTesting1" == UI_LandingPage_Validation
            testexecution = homepage.homepage_po_testexecution()
            time.sleep(5)
            action.move_to_element(testexecution.testexecution_po_Open_Existing_BulkEdit_Folder()).perform()
            testexecution.testexecution_po_Open_Existing_BulkEdit_Folder().click()
            time.sleep(1)
            action.context_click(testexecution.testexecution_po_Open_Existing_BulkEdit_Folder()).perform()
            testexecution.testexecution_po_RightClick_DataQuery().click()
            time.sleep(5)
            wait.until(EC.presence_of_element_located((By.XPATH, "//td[text()='AT Import TestCase Name']")))
            testexecution.testexecution_po_BulkEdit_AllCheckBox().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='✓']")))
            testexecution.testexecution_po_BulkEdit_Edit().click()
            testexecution.testexecution_po_BulkEdit_BulkEdit().click()
            wait.until(EC.presence_of_element_located((By.ID, "indicator_executionTypeBETestRun")))
            testexecution.testexecution_po_BulkEdit_ExecutionType().click()
            testexecution.testexecution_po_BulkEdit_ExecutionType_EnterOption().send_keys("Smoke")
            testexecution.testexecution_po_BulkEdit_ExecutionType_EnterOption().send_keys(Keys.ENTER)
            self.driver.execute_script("arguments[0].click();", testexecution.testexecution_po_BulkEdit_Confirm())
            # testdesign.testdesign_po_BulkEdit_Confirm().click()
            wait1 = WebDriverWait(self.driver, 300)
            wait1.until(EC.element_to_be_clickable((By.ID, "testrun_successbatchedUpdateOK_label")))
            testexecution.testexecution_po_BulkEdit_Ok().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//td[text()='AT Import TestCase Name']")))
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestExecution_DataQuery_BulkEdit', '2681795')
            test_run_id = self.get_TestRun(testSuiteID, 'TestExecution_DataQuery_BulkEdit')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestExecution_DataQuery_BulkEdit', '2681795')
            test_run_id = self.get_TestRun(testSuiteID, 'TestExecution_DataQuery_BulkEdit')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()







