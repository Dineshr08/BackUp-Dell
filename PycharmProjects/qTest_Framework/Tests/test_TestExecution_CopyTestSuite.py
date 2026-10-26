import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from TestData.LoginPage_TD import LoginPage_TD
from TestData.TestExecution_TD import TestExecution_TD
from Utilities.BaseClass import BaseClass


class Test_TestExecution_CopyTestSuite(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_testexecution_copytestsuite)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface


    def test_TestExecution_CopyTestSuite(self, getUserInput, getTSValue):
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
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "AutomationTesting1")))
            time.sleep(5)
            homepage.homepage_po_chooseAT1Project().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AutomationTesting1']")))
            UI_LandingPage_Validation = homepage.homepage_po_AT1Project_landingPage_Validation().text
            assert "AutomationTesting1" == UI_LandingPage_Validation
            testexecution = homepage.homepage_po_testexecution()
            time.sleep(10)
            action.move_to_element(testexecution.testexecution_po_Open_Existing_Release_Template()).perform()
            testexecution.testexecution_po_Open_Existing_Release_Template().click()
            testexecution.testexecution_po_Open_Existing_Release_Template_collapse().click()
            testexecution.testexecution_po_Open_Existing_Release_Template_collapse().click()
            time.sleep(5)
            BeforeCopy_Count = testexecution.testexecution_po_Verify_CopiedCount()
            action.move_to_element(testexecution.testexecution_po_OpenExisting_CopyTestSuite()).perform()
            testexecution.testexecution_po_OpenExisting_CopyTestSuite().click()
            action.context_click(testexecution.testexecution_po_OpenExisting_CopyTestSuite()).perform()
            testexecution.testexecution_po_Copy().click()
            action.move_to_element(testexecution.testexecution_po_Open_Existing_Release_Template()).perform()
            testexecution.testexecution_po_Open_Existing_Release_Template().click()
            action.context_click(testexecution.testexecution_po_Open_Existing_Release_Template()).perform()
            testexecution.testexecution_po_Paste().click()
            assert "success" in testexecution.testexecution_po_TestCycle_Suite_Copy_Validation().get_attribute(
                "innerHTML")
            wait1 = WebDriverWait(self.driver, 30)
            wait1.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='font-weight-normal pb-1']")))
            # AfterCopy_Count = testexecution.testexecution_po_Verify_CopiedCount()
            # assert len(AfterCopy_Count) > len(BeforeCopy_Count)
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestExecution_CopyTestSuite', '2681780')
            test_run_id = self.get_TestRun(testSuiteID, 'TestExecution_CopyTestSuite')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestExecution_CopyTestSuite', '2681780')
            test_run_id = self.get_TestRun(testSuiteID, 'TestExecution_CopyTestSuite')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()





