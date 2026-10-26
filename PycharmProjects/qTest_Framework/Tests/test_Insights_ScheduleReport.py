import time
from datetime import datetime
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


class Test_Insights_ScheduleReport(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_Insights_ScheduleReport)
    def getUserInput(self, request):
        return request.param

    # @pytest.fixture(params=TestExecution_TD.test_testexecution_createtestsuiteandcycle_quickrun_TestCase_ID)
    # def getTestCaseID(self, request):
    #     return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface


    def test_Insights_ScheduleReport(self, getUserInput, getTSValue):
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
            insights.insights_po_Saved_Reports().click()
            insights.insights_po_Saved_Report_Manage().click()
            wait1.until(EC.presence_of_element_located((By.XPATH, "//h1[@class='title-manage-report']")))
            insights.insights_po_Choose_AT_Report().click()
            insights.insights_po_Schedule().click()
            wait1.until(EC.presence_of_element_located((By.XPATH, "//span[@id='saveScheduleBtn']")))
            insights.insights_po_Schedule_StartTime().click()
            Schedule_CurrentTime, Schedule_CurrentHour, Schedule_CurrentDate, AM_PM = self.InsightScheduleTime()
            # print(Schedule_CurrentTime)
            # print(Schedule_CurrentHour)
            # print(Schedule_CurrentDate)
            # print(AM_PM)
            log.info(Schedule_CurrentDate)
            log.info(Schedule_CurrentHour)
            log.info(Schedule_CurrentTime)
            self.driver.find_element(By.XPATH, Schedule_CurrentDate).click()
            time.sleep(5)
            # insights.insights_po_Schedule_ActiveDay().click()
            # self.driver.find_element(By.XPATH, Schedule_CurrentHour).click()
            self.driver.find_element(By.XPATH, "(//span[@class='hour hour_pm'])[5]").click()
            time.sleep(5)
            # self.driver.find_element(By.XPATH, Schedule_CurrentTime).click()
            # self.driver.find_element(By.XPATH, Schedule_CurrentTime).click()
            self.driver.find_element(By.XPATH, "(//span[@class='minute'])[5]").click()
            time.sleep(5)

            # insights.insights_po_Schedule_Time().click()
            insights.insights_po_Schedule_Save().click()
            # wait1.until(EC.invisibility_of_element_located(Insights_PO.Schedule_LoadingMsg))
            wait1.until(EC.presence_of_element_located((By.XPATH, "//div[@class='toast-message']")))
            assert "success" in insights.insights_po_Schedule_SuccessMsg().text
            self.driver.close()
            self.driver.switch_to.window(windowsOpened[0])
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Insights_ScheduleReport', '1091356')
            test_run_id = self.get_TestRun(testSuiteID, 'Insights_ScheduleReport')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Insights_ScheduleReport', '1091356')
            test_run_id = self.get_TestRun(testSuiteID, 'Insights_ScheduleReport')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()























