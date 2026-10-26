import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.HomePage_PO import HomePage_PO
from PageObjects.Insights_PO import Insights_PO
from PageObjects.IntegrationSetting_PO import IntegrationSetting_PO
from PageObjects.JiraCEC_PO import JiraCEC_PO
from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from TestData.LoginPage_TD import LoginPage_TD
from TestData.TestExecution_TD import TestExecution_TD
from Utilities.BaseClass import BaseClass


class Test_Insights_CreateDashboard(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_Insights_CreateDashboard)
    def getUserInput(self, request):
        return request.param

    # @pytest.fixture(params=TestExecution_TD.test_testexecution_createtestsuiteandcycle_quickrun_TestCase_ID)
    # def getTestCaseID(self, request):
    #     return request.param
    @pytest.mark.regression
    @pytest.mark.UserInterface


    def test_Insights_CreateDashboard(self, getUserInput, getTSValue):
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
            # wait.until(EC.staleness_of(HomePage_PO.chooseAT1Project))
            time.sleep(5)
            homepage.homepage_po_chooseAT1Project().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AutomationTesting1']")))
            UI_LandingPage_Validation = homepage.homepage_po_AT1Project_landingPage_Validation().text
            assert "AutomationTesting1" == UI_LandingPage_Validation
            action.move_to_element(homepage.homepage_po_qTest_Component_Hover()).perform()
            wait.until(EC.presence_of_element_located((HomePage_PO.Insights)))
            insights = homepage.homepage_po_Insights()
            windowsOpened = self.driver.window_handles
            self.driver.switch_to.window(windowsOpened[1])
            wait1 = WebDriverWait(self.driver, 300)
            # wait1.until(EC.new_window_is_opened(self.driver.window_handles))
            wait1.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Insights']")))
            # wait1.until(EC.presence_of_element_located((Insights_PO.Dashboard)))
            insights.insights_po_Dashboard().click()
            insights.insights_po_Create_Dashboard().click()
            wait1.until(EC.presence_of_element_located((By.XPATH, "//span[text()='New Tab']")))
            wait1.until(EC.presence_of_element_located((Insights_PO.Search_ExistingDashboard_Img)))
            insights.insights_po_Search_ExistingDashboard_Img().send_keys("7.1-FPC Test Cases")
            # time.sleep(5)
            # wait2 = WebDriverWait(self.driver, 20)
            # Drag = wait2.until(EC.element_to_be_clickable(Insights_PO.Source_Image))
            # Drop = wait2.until(EC.element_to_be_clickable(Insights_PO.Destination_Place))
            # action.drag_and_drop(Drag, Drop).perform()
            # # action.drag_and_drop(insights.insights_po_Source_Image(),insights.insights_po_Destination_Place()).perform()
            # wait1.until(EC.invisibility_of_element_located(Insights_PO.Schedule_LoadingMsg))
            # wait1.until(EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='7.1-FPC Test Cases']")))
            self.driver.close()
            self.driver.switch_to.window(windowsOpened[0])
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Insights_CreateDashboard', '1091355')
            test_run_id = self.get_TestRun(testSuiteID, 'Insights_CreateDashboard')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Insights_CreateDashboard', '1091355')
            test_run_id = self.get_TestRun(testSuiteID, 'Insights_CreateDashboard')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()






















