import time
from datetime import datetime

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


class Test_Integration_ConfigureJiraIntegration_AddProjects(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_Integration_ConfigureJiraIntegration_AddProjects)
    def getUserInput(self, request):
        return request.param

    # @pytest.fixture(params=TestExecution_TD.test_testexecution_createtestsuiteandcycle_quickrun_TestCase_ID)
    # def getTestCaseID(self, request):
    #     return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface
    # @pytest.mark.dependency()


    def test_Integration_ConfigureJiraIntegration_AddProjects(self, getUserInput, getTSValue):
    # def test_Integration_ConfigureJiraIntegration_AddProjects(self, getUserInput):
        try:
            log = self.logging()
            loginpage = LoginPage_PO(self.driver)
            loginpage.loginpage_po_username().send_keys(getUserInput["username"])
            loginpage.loginpage_po_password().send_keys(getUserInput["password"])
            homepage = loginpage.loginpage_po_loginBtn()
            cookies = self.get_cookies()
            action = ActionChains(self.driver)
            action.move_to_element(homepage.homepage_po_hoverProjectMenu()).perform()
            homepage.homepage_po_searchProject().send_keys("AutomationTesting2")
            wait = WebDriverWait(self.driver, 120)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "AutomationTesting2")))
            # wait.until(EC.staleness_of(HomePage_PO.chooseAT1Project))
            time.sleep(5)
            homepage.homepage_po_chooseAT2Project().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AutomationTesting2']")))
            UI_LandingPage_Validation = homepage.homepage_po_AT2Project_landingPage_Validation().text
            assert "AutomationTesting2" == UI_LandingPage_Validation
            action.move_to_element(homepage.homepage_po_Global_Setting()).perform()
            wait.until(EC.presence_of_element_located((HomePage_PO.Global_Setting_Field_Setting)))
            integration = homepage.homepage_po_Global_Setting_Integration_Setting()
            integration.integrationsetting_po_AddJiraConnection().click()
            wait.until(EC.element_to_be_clickable(IntegrationSetting_PO.TestJiraConnection))
            Date = datetime.now()
            Name = "AT_ConnectionName" + str(Date)
            integration.integrationsetting_po_ConnectionName().send_keys(Name)
            time.sleep(5)
            # integration.integrationsetting_po_ServerURL().send_keys("https://jira-stage.cec.lab.emc.com")
            integration.integrationsetting_po_ServerURL().send_keys("https://jira-stage.cec.lab.emc.com")
            integration.integrationsetting_po_Connection_UserName().send_keys("svc_npjiratoqtest")
            integration.integrationsetting_po_ConnectionPassword().send_keys("*?w2Xt1+uBY3z~A_69v0mNJH")
            integration.integrationsetting_po_TestJiraConnection().click()
            assert "Connected to server successfully." in integration.integrationsetting_po_ConnectionMsg().get_attribute(
                "innerHTML")
            integration.integrationsetting_po_Save_Configure().click()
            try:
                wait.until(EC.element_to_be_clickable(IntegrationSetting_PO.AddDefectType))
                integration.integrationsetting_po_AddDefectType().click()
            except Exception as e:
                wait.until(EC.element_to_be_clickable(IntegrationSetting_PO.Confirmation_PopUP))
                integration.integrationsetting_po_Confirmation_PopUP().click()
                wait.until(EC.element_to_be_clickable(IntegrationSetting_PO.AddDefectType))
                integration.integrationsetting_po_AddDefectType().click()
            wait.until(EC.element_to_be_clickable(IntegrationSetting_PO.AddDefectType_Ok))
            # integration.integrationsetting_po_AddDefectType_JiraProject().clear()
            # integration.integrationsetting_po_AddDefectType_JiraProject().send_keys("ARTIFACT MANAGEMENT (AMaaS) - Implement")
            # integration.integrationsetting_po_AddDefectType_JiraProject().send_keys(Keys.ENTER)
            # wait.until(EC.element_to_be_clickable(IntegrationSetting_PO.AddDefectType_Ok))
            integration.integrationsetting_po_AddDefectType_Ok().click()
            # assert "ARTIFACT MANAGEMENT (AMaaS) - Implement" in integration.integrationsetting_po_AddDefectType_Validation().get_attribute("innerHTML")
            assert "SES ISG as Code" in integration.integrationsetting_po_AddDefectType_Validation().get_attribute(
                "innerHTML")
            integration.integrationsetting_po_ReleaseRequirement_Activate().click()
            assert "On" in integration.integrationsetting_po_ReleaseRequirement_Activate().get_attribute("innerHTML")
            wait.until(EC.element_to_be_clickable(IntegrationSetting_PO.AddRequirementType))
            integration.integrationsetting_po_AddRequirementType().click()
            wait.until(EC.element_to_be_clickable(IntegrationSetting_PO.AddDefectType_Ok))
            # integration.integrationsetting_po_AddDefectType_JiraProject().clear()
            # integration.integrationsetting_po_AddDefectType_JiraProject().send_keys("ARTIFACT MANAGEMENT (AMaaS) - Implement")
            # integration.integrationsetting_po_AddDefectType_JiraProject().send_keys(Keys.ENTER)
            # wait.until(EC.element_to_be_clickable(IntegrationSetting_PO.AddDefectType_Ok))
            integration.integrationsetting_po_AddDefectType_Ok().click()
            # assert "ARTIFACT MANAGEMENT (AMaaS) - Implement" in integration.integrationsetting_po_AddRequirementType_Validation().get_attribute("innerHTML")
            assert "SES ISG as Code" in integration.integrationsetting_po_AddRequirementType_Validation().get_attribute(
                "innerHTML")
            integration.integrationsetting_po_ReleaseIntegration_Activate().click()
            assert "On" in integration.integrationsetting_po_ReleaseIntegration_Activate().get_attribute("innerHTML")
            wait.until(EC.element_to_be_clickable(IntegrationSetting_PO.AddReleaseType))
            integration.integrationsetting_po_AddReleaseType().click()
            wait.until(EC.element_to_be_clickable(IntegrationSetting_PO.AddReleaseType_Ok))
            integration.integrationsetting_po_AddReleaseType_Ok().click()
            assert "SES ISG as Code" in integration.integrationsetting_po_AddReleaseType_Validation().get_attribute(
                "innerHTML")
            # integration.integrationsetting_po_Save_Activate().click()
            # wait.until(EC.element_to_be_clickable(IntegrationSetting_PO.Refresh))
            # integration.integrationsetting_po_Refresh().click()
            # wait.until(EC.presence_of_element_located(IntegrationSetting_PO.AddJiraConnection))
            # assert Name in self.IntegrationConnectionName(Name).get_attribute("innerHTML")
            integration.integrationsetting_po_Save().click()
            time.sleep(5)
            wait.until(EC.element_to_be_clickable(IntegrationSetting_PO.Close))
            self.driver.execute_script("arguments[0].click();", integration.integrationsetting_po_Close())
            # integration.integrationsetting_po_Close().click()
            wait.until(EC.presence_of_element_located(IntegrationSetting_PO.AddJiraConnection))
            self.driver.find_element(By.XPATH, "//body").send_keys(Keys.END)
            time.sleep(5)
            assert Name in self.IntegrationConnectionName(Name).get_attribute("innerHTML")
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)

            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Integration_ConfigureJiraIntegration_AddProjects', '1080474')
            test_run_id = self.get_TestRun(testSuiteID, 'Integration_ConfigureJiraIntegration_AddProjects')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)

            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Integration_ConfigureJiraIntegration_AddProjects', '1080474')
            test_run_id = self.get_TestRun(testSuiteID, 'Integration_ConfigureJiraIntegration_AddProjects')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()










