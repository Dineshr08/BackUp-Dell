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
from PageObjects.Launch_PO import Launch_PO
from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.Pulse_PO import Pulse_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from TestData.LoginPage_TD import LoginPage_TD
from TestData.TestExecution_TD import TestExecution_TD
from Utilities.BaseClass import BaseClass


class Test_Pulse(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_Pulse)
    def getUserInput(self, request):
        return request.param

    # @pytest.fixture(params=TestExecution_TD.test_testexecution_createtestsuiteandcycle_quickrun_TestCase_ID)
    # def getTestCaseID(self, request):
    #     return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface



    def test_Pulse(self, getUserInput, getTSValue):
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
            testdesign = homepage.homepage_po_testdesign()
            action.move_to_element(testdesign.testdesign_po_Open_Existing_PulseTesting_Folder()).perform()
            self.driver.execute_script("arguments[0].click();", testdesign.testdesign_po_Open_Existing_PulseTesting_Folder())
            # testdesign.testdesign_po_Open_Existing_PulseTesting_Folder().click()
            time.sleep(5)
            self.driver.execute_script("arguments[0].click();", testdesign.testdesign_po_CreateNewTestCase())
            # testdesign.testdesign_po_CreateNewTestCase().click()
            testdesign.testdesign_po_Update_ExistingTestCaseNameField().send_keys("AT TestCase")
            # testdesign.testdesign_po_Status_Arrow().click()
            # testdesign.testdesign_po_Status_Search().send_keys("New")
            # testdesign.testdesign_po_Status_Search().send_keys(Keys.ENTER)
            testdesign.testdesign_po_Save().click()
            time.sleep(10)
            CurrentURL = self.driver.current_url
            wait1 = WebDriverWait(self.driver, 300)
            action.move_to_element(homepage.homepage_po_qTest_Component_Hover()).perform()
            wait.until(EC.presence_of_element_located((HomePage_PO.Pulse)))
            time.sleep(10)
            pulse = homepage.homepage_po_Pulse()
            windowsOpened = self.driver.window_handles
            self.driver.switch_to.window(windowsOpened[1])
            wait1.until(EC.presence_of_element_located((By.XPATH, "//a[text()='My Rules']")))
            pulse.pulse_po_ChooseProject_Arrow().click()
            self.driver.execute_script("arguments[0].click();", pulse.pulse_po_Choose_AKT_Project())
            # pulse.pulse_po_Choose_AKT_Project().click()
            self.driver.find_element(By.XPATH, "/html/body").send_keys(Keys.PAGE_DOWN)
            pulse.pulse_po_Action_Menu().click()
            wait.until(EC.element_to_be_clickable((Pulse_PO.Action_ViewLogs)))
            pulse.pulse_po_Action_ViewLogs().click()
            wait.until(EC.element_to_be_clickable((Pulse_PO.Execution_Refresh)))
            TestCaseID = CurrentURL.split("=")
            test = TestCaseID[3]
            test1 = test.split("&")
            ExtractedID = test1[0]
            pulse.pulse_po_Execution_ID().click()
            time.sleep(2)
            Body = pulse.pulse_po_Execution_ID_Data().text
            pulse.pulse_po_Execution_ID_Close().click()
            Body1 = Body.split(":")
            Str1 = Body1[4]
            Str2 = Str1.split(",")
            ExtractedID1 = Str2[0]
            for i in range(1, 10):
                if int(ExtractedID) != int(ExtractedID1):
                    time.sleep(20)
                    pulse.pulse_po_Execution_Refresh().click()
                    pulse.pulse_po_Execution_ID().click()
                    time.sleep(2)
                    Body = pulse.pulse_po_Execution_ID_Data().text
                    pulse.pulse_po_Execution_ID_Close().click()
                    Body1 = Body.split(":")
                    Str1 = Body1[4]
                    Str2 = Str1.split(",")
                    ExtractedID1 = Str2[0]
                else:
                    break

            pulse.pulse_po_Execution_Refresh().click()
            assert "completed" == pulse.pulse_po_Execution_Status().text
            pulse.pulse_po_Execution_Close().click()
            self.driver.close()
            self.driver.switch_to.window(windowsOpened[0])
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Pulse', '2683579')
            test_run_id = self.get_TestRun(testSuiteID, 'Pulse')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Pulse', '2683579')
            test_run_id = self.get_TestRun(testSuiteID, 'Pulse')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()





























