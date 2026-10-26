import time

import pytest
import requests
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.HomePage_PO import HomePage_PO
from PageObjects.IntegrationSetting_PO import IntegrationSetting_PO
from PageObjects.JiraCEC_PO import JiraCEC_PO
from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.Requirement_PO import Requirement_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from TestData.LoginPage_TD import LoginPage_TD
from TestData.TestExecution_TD import TestExecution_TD
from Utilities.BaseClass import BaseClass


class Test_Integration_Release_RetrieveJiraData_Gtie(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_Integration_Release_RetrieveJiraData_Gtie)
    def getUserInput(self, request):
        return request.param

    # @pytest.fixture(params=TestExecution_TD.test_testexecution_createtestsuiteandcycle_quickrun_TestCase_ID)
    # def getTestCaseID(self, request):
    #     return request.param

    # Advance Roadmap training project used with epic

    @pytest.mark.regression
    @pytest.mark.UserInterface
    # @pytest.mark.dependency(depends=["test_Integration_Release_RetrieveJiraData"])

    def test_Integration_Release_RetrieveJiraData_Gtie(self, getUserInput, getTSValue):
        try:
            log = self.logging()
            loginpage = LoginPage_PO(self.driver)
            loginpage.loginpage_po_username().send_keys(getUserInput["username"])
            loginpage.loginpage_po_password().send_keys(getUserInput["password"])
            homepage = loginpage.loginpage_po_loginBtn()
            cookies = self.get_cookies()
            action = ActionChains(self.driver)
            action.move_to_element(homepage.homepage_po_hoverProjectMenu()).perform()
            homepage.homepage_po_searchProject().send_keys("Automation")
            wait = WebDriverWait(self.driver, 120)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "AutomationTesting")))
            time.sleep(5)
            homepage.homepage_po_chooseATProject().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AutomationTesting']")))
            UI_LandingPage_Validation = homepage.homepage_po_ATProject_landingPage_Validation().text
            assert "AutomationTesting" == UI_LandingPage_Validation
            action.move_to_element(homepage.homepage_po_Global_Setting()).perform()
            wait.until(EC.presence_of_element_located((HomePage_PO.Global_Setting_Field_Setting)))
            integration = homepage.homepage_po_Global_Setting_Integration_Setting()
            # action.move_to_element(integration.integrationsetting_po_Connection_Gtie()).perform()
            # time.sleep(5)
            # self.driver.execute_script("arguments[0].click();", integration.integrationsetting_po_Connection_Gtie())
            # integration.integrationsetting_po_Integration_HomePage_Save().click()
            # wait.until(EC.element_to_be_clickable(IntegrationSetting_PO.Integration_HomePage_Save))
            action.move_to_element(integration.integrationsetting_po_Configure()).perform()
            time.sleep(5)
            self.driver.execute_script("arguments[0].click();", integration.integrationsetting_po_Configure())
            # integration.integrationsetting_po_Configure().click()

            try:
                wait.until(EC.element_to_be_clickable(IntegrationSetting_PO.Connection_Refresh))
                integration.integrationsetting_po_Connection_Refresh().click()
                wait.until(EC.element_to_be_clickable(IntegrationSetting_PO.Integration_HomePage_Save))
                action.move_to_element(integration.integrationsetting_po_Configure_Gtie()).perform()
                time.sleep(5)
                self.driver.execute_script("arguments[0].click();", integration.integrationsetting_po_Configure_Gtie())
                wait.until(EC.presence_of_element_located((IntegrationSetting_PO.FetchJIraDefect)))
                self.driver.execute_script("arguments[0].click();",
                                           integration.integrationsetting_po_Release_Retrieve_JiraDefect())
            except Exception as e:
                wait.until(EC.presence_of_element_located((IntegrationSetting_PO.FetchJIraDefect)))
                self.driver.execute_script("arguments[0].click();",
                                           integration.integrationsetting_po_Release_Retrieve_JiraDefect())
            # wait.until(EC.presence_of_element_located((IntegrationSetting_PO.FetchJIraDefect)))
            # self.driver.execute_script("arguments[0].click();", integration.integrationsetting_po_Release_Retrieve_JiraDefect())
            # integration.integrationsetting_po_RetrieveJiraData().click()
            wait1 = WebDriverWait(self.driver, 120)
            wait1.until(EC.visibility_of_element_located((IntegrationSetting_PO.Retrieve_Jira_SuccessMsg)))
            assert "success" in integration.integrationsetting_po_Retrieve_Jira_SuccessMsg().text
            # Retrieved_Total_Count = integration.integrationsetting_po_Retrieve_Jira_Count().text
            wait1.until(EC.element_to_be_clickable(IntegrationSetting_PO.RetrieveJIraData_OK))
            integration.integrationsetting_po_RetrieveJIraData_OK().click()

            # URL = 'https://qtest-stage.gtie.dell.com/api/v3/projects/411/releases'
            # HEADERS = {
            #     "Authorization": "Bearer cbe60e5b-7969-4505-84a9-d42d3015b0da",
            #     "Content-Type": "application/json"
            # }
            #
            # response = requests.get(URL, headers=HEADERS)
            # assert response.status_code == 200
            # data = response.json()
            # ids = []
            # for item in data:
            #     if 'id' in item:
            #         ids.append(item['id'])
            # assert len(ids) > 1
            # Count = len(ids)
            # # Data Setup
            # for i in range(Count):
            #     URL1 = 'https://qtest-stage.gtie.dell.com/api/v3/projects/411/releases/'
            #     if ids[i] == 13093:
            #         continue
            #     else:
            #         Release_ID = ids[i]
            #         response = requests.delete(url="{}{}".format(URL1, Release_ID), headers=HEADERS)
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Integration_Release_RetrieveJiraData_Gtie', '4887541')
            test_run_id = self.get_TestRun(testSuiteID, 'Integration_Release_RetrieveJiraData_Gtie')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Integration_Release_RetrieveJiraData_Gtie', '4887541')
            test_run_id = self.get_TestRun(testSuiteID, 'Integration_Release_RetrieveJiraData_Gtie')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()





        


















