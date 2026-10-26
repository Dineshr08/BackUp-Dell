import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.HomePage_PO import HomePage_PO
from PageObjects.IntegrationSetting_PO import IntegrationSetting_PO
from PageObjects.JiraCEC_PO import JiraCEC_PO
from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from TestData.LoginPage_TD import LoginPage_TD
from TestData.TestExecution_TD import TestExecution_TD
from Utilities.BaseClass import BaseClass


class Test_Integration_FetchJiraDefect(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_Integration_FetchJiraDefect)
    def getUserInput(self, request):
        return request.param

    # @pytest.fixture(params=TestExecution_TD.test_testexecution_createtestsuiteandcycle_quickrun_TestCase_ID)
    # def getTestCaseID(self, request):
    #     return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_Integration_FetchJiraDefect(self, getUserInput, getTSValue):
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
            wait = WebDriverWait(self.driver, 120)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "AutomationTesting1")))
            # wait.until(EC.staleness_of(HomePage_PO.chooseAT1Project))
            time.sleep(5)
            homepage.homepage_po_chooseAT1Project().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AutomationTesting1']")))
            UI_LandingPage_Validation = homepage.homepage_po_AT1Project_landingPage_Validation().text
            assert "AutomationTesting1" == UI_LandingPage_Validation
            action.move_to_element(homepage.homepage_po_Global_Setting()).perform()
            wait.until(EC.presence_of_element_located((HomePage_PO.Global_Setting_Field_Setting)))
            integration = homepage.homepage_po_Global_Setting_Integration_Setting()
            action.move_to_element(integration.integrationsetting_po_Configure()).perform()
            time.sleep(5)
            self.driver.execute_script("arguments[0].click();", integration.integrationsetting_po_Configure())
            # integration.integrationsetting_po_Configure().click()
            wait.until(EC.presence_of_element_located((IntegrationSetting_PO.FetchJIraDefect)))
            integration.integrationsetting_po_FetchJIraDefect().click()
            wait.until(EC.presence_of_element_located((IntegrationSetting_PO.FetchJIraDefect_OK)))
            integration.integrationsetting_po_FetchJIraDefect_OK().click()
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Integration_FetchJiraDefect', '1080983')
            test_run_id = self.get_TestRun(testSuiteID, 'Integration_FetchJiraDefect')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Integration_FetchJiraDefect', '1080983')
            test_run_id = self.get_TestRun(testSuiteID, 'Integration_FetchJiraDefect')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()
















