import time

import pytest
import requests
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.Requirement_PO import Requirement_PO
from PageObjects.TestPlan_PO import TestPlan_PO
from TestData.LoginPage_TD import LoginPage_TD
from Utilities.BaseClass import BaseClass


class Test_TestDesign_CopyTestCase(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_TestDesign_CopyTestCase)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface


    def test_TestDesign_CopyTestCase(self, getUserInput, getTSValue):
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
            action.move_to_element(testdesign.testdesign_po_Existing_AT_CopyModuleFolder()).perform()
            testdesign.testdesign_po_Existing_AT_CopyModuleFolder().click()
            testdesign.testdesign_po_AT_CopyModule_Expand().click()
            time.sleep(5)
            action.move_to_element(testdesign.testdesign_po_AT_Copy_TestCase()).perform()
            testdesign.testdesign_po_AT_Copy_TestCase().click()
            action.context_click(testdesign.testdesign_po_AT_Copy_TestCase()).perform()
            wait.until(EC.element_to_be_clickable(Requirement_PO.Copy))
            testdesign.testdesign_po_Copy().click()
            action.move_to_element(testdesign.testdesign_po_AT_CopyModule_HomeTemplate()).perform()
            testdesign.testdesign_po_AT_CopyModule_HomeTemplate().click()
            action.context_click(testdesign.testdesign_po_AT_CopyModule_HomeTemplate()).perform()
            time.sleep(5)
            testdesign.testdesign_po_Paste().click()
            assert "success" in testdesign.testdesign_po_CopyTestCase_Validation().get_attribute("innerHTML")
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestDesign_CopyTestCase', '2681777')
            test_run_id = self.get_TestRun(testSuiteID, 'TestDesign_CopyTestCase')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestDesign_CopyTestCase', '2681777')
            test_run_id = self.get_TestRun(testSuiteID, 'TestDesign_CopyTestCase')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()












