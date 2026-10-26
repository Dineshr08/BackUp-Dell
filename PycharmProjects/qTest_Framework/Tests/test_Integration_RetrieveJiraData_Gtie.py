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


class Test_Integration_RetrieveJiraData_Gtie(BaseClass):
    @pytest.fixture(params=LoginPage_TD.test_Integration_RetrieveJiraData_Gtie)
    def getUserInput(self, request):
        return request.param

    # @pytest.fixture(params=TestExecution_TD.test_testexecution_createtestsuiteandcycle_quickrun_TestCase_ID)
    # def getTestCaseID(self, request):
    #     return request.param

    # Advance Roadmap training project used with epic

    @pytest.mark.regression
    @pytest.mark.UserInterface

    # @pytest.mark.dependency(depends=["test_Integration_RetrieveJiraData"])

    def test_Integration_RetrieveJiraData_Gtie(self, getUserInput, getTSValue):
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
                action.move_to_element(integration.integrationsetting_po_RetrieveJiraData_Project1()).perform()
                self.driver.execute_script("arguments[0].click();", integration.integrationsetting_po_RetrieveJiraData_Project1())
            except Exception as e:
                wait.until(EC.presence_of_element_located((IntegrationSetting_PO.FetchJIraDefect)))
                action.move_to_element(integration.integrationsetting_po_RetrieveJiraData_Project1()).perform()
                self.driver.execute_script("arguments[0].click();",integration.integrationsetting_po_RetrieveJiraData_Project1())

            # wait.until(EC.presence_of_element_located((IntegrationSetting_PO.FetchJIraDefect)))
            # action.move_to_element(integration.integrationsetting_po_RetrieveJiraData_Project1()).click().perform()
            # self.driver.execute_script("arguments[0].click();", integration.integrationsetting_po_RetrieveJiraData())
            # integration.integrationsetting_po_RetrieveJiraData().click()
            wait1 = WebDriverWait(self.driver, 200)
            wait1.until(EC.visibility_of_element_located((IntegrationSetting_PO.Retrieve_Jira_SuccessMsg)))
            assert "success" in integration.integrationsetting_po_Retrieve_Jira_SuccessMsg().text
            Retrieved_Total_Count = integration.integrationsetting_po_Retrieve_Jira_Count().text
            integration.integrationsetting_po_RetrieveJIraData_OK().click()

            # Commented Below, because validating using api below

            # requirement = homepage.homepage_po_requirement()
            # # self.driver.refresh()
            # wait.until(EC.presence_of_element_located((Requirement_PO.ImportFromJira_Folder)))
            # action.move_to_element(requirement.requirement_po_ImportFromJira_Folder()).perform()
            # requirement.requirement_po_ImportFromJira_Folder().click()
            # wait.until(EC.presence_of_element_located((Requirement_PO.ImportFromJira_Folder_RequirementCount)))
            # Requirement_Count = requirement.requirement_po_ImportFromJira_Folder_RequirementCount().get_attribute("innerHTML")
            # assert int(Requirement_Count) >= int(Retrieved_Total_Count)

            # Retrieve Jira Requirement using Filter
            wait.until(EC.presence_of_element_located((IntegrationSetting_PO.FetchJIraDefect)))
            action.move_to_element(integration.integrationsetting_po_RetrieveJiraData_Project2()).perform()
            self.driver.execute_script("arguments[0].click();",integration.integrationsetting_po_RetrieveJiraData_Project2())
            wait1 = WebDriverWait(self.driver, 200)
            wait1.until(EC.visibility_of_element_located((IntegrationSetting_PO.Retrieve_Jira_SuccessMsg)))
            assert "success" in integration.integrationsetting_po_Retrieve_Jira_SuccessMsg().text
            Retrieved_Total_Count1 = integration.integrationsetting_po_Retrieve_Jira_Count().text
            integration.integrationsetting_po_RetrieveJIraData_OK().click()

            # integration.integrationsetting_po_RetrieveJiraData_Project2().click()
            # wait.until(EC.element_to_be_clickable(HomePage_PO.requirement))
            # requirement = homepage.homepage_po_requirement()
            # wait.until(EC.element_to_be_clickable((Requirement_PO.ImportFromJira_Folder)))
            # action.move_to_element(requirement.requirement_po_ImportFromJira_Folder()).perform()
            # requirement.requirement_po_ImportFromJira_Folder().click()
            # wait.until(EC.presence_of_element_located((Requirement_PO.ImportFromJira_Folder_RequirementCount)))
            # Requirement_Count = requirement.requirement_po_ImportFromJira_Folder_RequirementCount().get_attribute("innerHTML")
            # response1 = requests.get(URL, headers=HEADERS)
            # assert response1.status_code == 200
            # data1 = response1.json()
            # ids1 = []
            # for item1 in data1:
            #     if 'id' in item1:
            #         ids1.append(item1['id'])
            # assert len(ids1) == int(Requirement_Count)
            # Count = len(ids1)
            # if requirement.requirement_po_ImportFromJira_Folder().text == 'Imported from JIRA':
            #     url = self.driver.current_url
            #     print(url)
            #     url.split('=')
            #     ModuleID = url[-1]
            #     print(ModuleID)
            #     URL2 = 'https://qtest-stage.gtie.dell.com/api/v3/projects/411/modules/'
            #     response2 = requests.delete(url="{}{}{}".format(URL2, ModuleID, '?force=true'), headers=HEADERS)
            #     assert response2.status_code == 200
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Integration_RetrieveJiraData_Gtie', '1081007')
            test_run_id = self.get_TestRun(testSuiteID, 'Integration_RetrieveJiraData_Gtie')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Integration_RetrieveJiraData_Gtie', '1081007')
            test_run_id = self.get_TestRun(testSuiteID, 'Integration_RetrieveJiraData_Gtie')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()
