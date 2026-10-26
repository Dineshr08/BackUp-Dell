import time

import pyautogui
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.HomePage_PO import HomePage_PO
from PageObjects.JiraCEC_PO import JiraCEC_PO
from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from TestData.LoginPage_TD import LoginPage_TD
from TestData.TestExecution_TD import TestExecution_TD
from Utilities.BaseClass import BaseClass
pyautogui.FAILSAFE = False


class Test_TestExecution_CreateNewDefect(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_TestExecution_CreateNewDefect)
    def getUserInput(self, request):
        return request.param

    # @pytest.fixture(params=TestExecution_TD.test_testexecution_createtestsuiteandcycle_quickrun_TestCase_ID)
    # def getTestCaseID(self, request):
    #     return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_TestExecution_CreateNewDefect(self, getUserInput, getTSValue):
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
            wait = WebDriverWait(self.driver, 30)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "AutomationTesting1")))
            # wait.until(EC.staleness_of(HomePage_PO.chooseAT1Project))
            time.sleep(5)
            homepage.homepage_po_chooseAT1Project().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AutomationTesting1']")))
            UI_LandingPage_Validation = homepage.homepage_po_AT1Project_landingPage_Validation().text
            assert "AutomationTesting1" == UI_LandingPage_Validation
            testexecution = homepage.homepage_po_testexecution()
            time.sleep(10)
            action.move_to_element(testexecution.testexecution_po_Open_Existing_Release_Template()).perform()
            testexecution.testexecution_po_Open_Existing_Release_Template().click()
            for i in range(2):
                testexecution.testexecution_po_New_TestCycle().click()
                if i == 0:
                    testexecution.testexecution_po_New_TestCycle_Name().send_keys("AT TestCycle")
                else:
                    testexecution.testexecution_po_New_TestCycle_Name().send_keys("AT Sub TestCycle")
            testexecution.testexecution_po_New_TestSuite().click()
            testexecution.testexecution_po_New_TestSuite_Name().send_keys("AT Test Suite")
            testCaseID = ["TC-163"]
            for j in range(1):
                if j >= 1:
                    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Test Runs']")))
                # Below statement we have written, because when we click add test run for 3 time got element element click intercepted exception
                self.driver.execute_script("arguments[0].click();", testexecution.testexecution_po_Add_TestRuns())
                # testexecution.testexecution_po_Add_TestRuns().click()
                self.driver.execute_script("arguments[0].click();",
                                           testexecution.testexecution_po_Add_TestRuns_TestCase())
                # testexecution.testexecution_po_Add_TestRuns_TestCase().click()
                testexecution.testexecution_po_Add_TestRuns_Search().clear()
                testexecution.testexecution_po_Add_TestRuns_Search().send_keys(testCaseID[j])
                testexecution.testexecution_po_Add_TestRuns_Search().send_keys(Keys.ENTER)
                testexecution.testexecution_po_Add_TestRuns_AllCheckBox().click()
                wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-default btn-add']")))
                testexecution.testexecution_po_Add_TestRuns_Add().click()
                wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Test Runs']")))
                time.sleep(5)

            wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Test Runs']")))
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='grid-cell-status']")))
            testexecution.testexecution_po_TestSuite_ChooseAllTestCase().click()
            testexecution.testexecution_po_TestSuite_QuickRun().click()
            testexecution.testexecution_po_QuickRun_ChooseAllTestcase().click()
            wait.until(EC.element_to_be_clickable((TestExecution_PO.QuickRun_Apply)))
            testexecution.testexecution_po_QuickRun_Apply().click()
            time.sleep(5)
            testexecution.testexecution_po_QuickRun_OkandRefresh().click()
            time.sleep(5)
            assert testexecution.testexecution_po_TestSuite_QuickRun_TestCase_UpdatedStatus().get_attribute(
                "innerHTML") == "Passed"
            testexecution.testexecution_po_Open_TestRun_ID().click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//span[normalize-space()='Execution History (1)']").click()
            self.driver.find_element(By.TAG_NAME, "html").send_keys(Keys.END)
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='Edit']")))
            action.move_to_element(testexecution.testexecution_po_Bug()).perform()
            time.sleep(5)
            self.driver.execute_script("arguments[0].click();", testexecution.testexecution_po_Bug())
            # testexecution.testexecution_po_Bug().click()
            wait.until(EC.presence_of_element_located((TestExecution_PO.New_Defect)))
            self.driver.execute_script("arguments[0].click();", testexecution.testexecution_po_New_Defect())
            # testexecution.testexecution_po_New_Defect().click()
            wait.until(EC.presence_of_element_located((TestExecution_PO.New_Defect_Add)))
            time.sleep(5)
            # jiracec = self.driver.execute_script("arguments[0].click();", testexecution.testexecution_po_New_Defect_Add())
            jiracec = testexecution.testexecution_po_New_Defect_Add()
            wait.until(EC.new_window_is_opened(self.driver.window_handles))
            # windowsOpened = self.driver.window_handles
            windowsOpened = self.driver.current_window_handle
            # self.driver.switch_to.window(windowsOpened[1])
            wait1 = WebDriverWait(self.driver, 120)
            time.sleep(10)
            for window_handle in self.driver.window_handles:
                if window_handle != windowsOpened:
                    self.driver.switch_to.window(window_handle)
            pyautogui.press('esc')
            self.driver.refresh()
            # wait1.until(EC.presence_of_element_located((By.ID, "issue-create-submit")))
            # assert 'Sign' in self.driver.title
            # self.driver.find_element(By.ID, "username").send_keys("svc_npieoinfra1")
            # self.driver.find_element(By.ID, "Password").send_keys("C_*81hPzN~3bJIQTVyaDrwES")
            # self.driver.find_element(By.ID, "Submit_btn").click()
            # wait1.until(EC.presence_of_element_located((JiraCEC_PO.PageValidation)))
            # assert 'Issue' in self.driver.title
            # # print(self.driver.title)
            # jiracec.jiracec_PO_Summary_Name().send_keys("AT Test")
            # self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
            # self.driver.execute_script("arguments[0].click();", jiracec.jiracec_PO_Create())
            # # jiracec.jiracec_PO_Create().click()
            # wait1.until(EC.element_to_be_clickable((By.ID, "project-name-val")))
            # # self.driver.close()
            # Count_TabOpened = len(windowsOpened)
            # #
            # # while Count_TabOpened > 1:
            # #     windowsOpened = self.driver.window_handles
            # #     Count_TabOpened = len(windowsOpened)
            # #     time.sleep(5)
            #
            # for i in range(10):
            #     if Count_TabOpened > 1:
            #         windowsOpened = self.driver.window_handles
            #         Count_TabOpened = len(windowsOpened)
            #         time.sleep(10)
            #
            # self.driver.switch_to.window(windowsOpened[0])
            # assert testexecution.testexecution_po_New_Defect_Add_Validation().text == 'New'
            # testexecution.testexecution_po_Click_Close_Defect().click()
            try:
                wait1.until(EC.presence_of_element_located((By.ID, "Submit_btn")))
                assert 'Sign' in self.driver.title
                self.driver.find_element(By.ID, "username").send_keys("svc_npieoinfra1")
                self.driver.find_element(By.ID, "Password").send_keys("Dh?9+i78E2MAF*_jKGnoL3pq")
                self.driver.find_element(By.ID, "Submit_btn").click()
                wait1.until(EC.presence_of_element_located((JiraCEC_PO.PageValidation)))
                assert 'Issue' in self.driver.title
                # print(self.driver.title)
                # Recently Commented#
                # wait1.until(EC.element_to_be_clickable((By.ID, "issue-create-submit")))
                # testexecution.testexecution_po_Jira_Click_Project().click()
                # testexecution.testexecution_po_Jira_Click_Project().send_keys("TEST CASE MANAGEMENT (TCMaaS) (TCMAAS)")
                # testexecution.testexecution_po_Jira_Click_Project().send_keys(Keys.ENTER)
                # # testexecution.testexecution_po_Jira_Choose_Project().click()
                # testexecution.testexecution_po_Jira_Click_IssueType().click()
                # # testexecution.testexecution_po_Jira_Click_IssueType()
                # testexecution.testexecution_po_Jira_Click_IssueType().send_keys("Story")
                # testexecution.testexecution_po_Jira_Click_IssueType().send_keys(Keys.ENTER)
                # testexecution.testexecution_po_Jira_Issue_Next().click()
                wait1.until(EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='Create Issue']")))
                jiracec.jiracec_PO_Summary_Name().send_keys("AT Test")
                self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
                self.driver.execute_script("arguments[0].click();", jiracec.jiracec_PO_Create())
                # jiracec.jiracec_PO_Create().click()
                # wait1.until(EC.element_to_be_clickable((By.ID, "project-name-val")))
                # self.driver.close()
                Count_TabOpened = len(windowsOpened)
                #
                # while Count_TabOpened > 1:
                for i in range(10):
                    if Count_TabOpened > 1:
                        windowsOpened = self.driver.window_handles
                        Count_TabOpened = len(windowsOpened)
                        time.sleep(10)
                self.driver.switch_to.window(windowsOpened[0])
                assert testexecution.testexecution_po_New_Defect_Add_Validation().text == 'New'
                testexecution.testexecution_po_Click_Close_Defect().click()
            except Exception as e:
                # wait1.until(EC.presence_of_element_located((By.ID, "Submit_btn")))
                # assert 'Sign' in self.driver.title
                # self.driver.find_element(By.ID, "username").send_keys("svc_npieoinfra1")
                # self.driver.find_element(By.ID, "Password").send_keys("C_*81hPzN~3bJIQTVyaDrwES")
                # self.driver.find_element(By.ID, "Submit_btn").click()
                # Recently Commented#
                # wait1.until(EC.presence_of_element_located((JiraCEC_PO.PageValidation)))
                # assert 'Issue' in self.driver.title
                # # print(self.driver.title)
                # wait1.until(EC.element_to_be_clickable((By.ID, "issue-create-submit")))
                # testexecution.testexecution_po_Jira_Click_Project().click()
                # testexecution.testexecution_po_Jira_Click_Project().send_keys("TEST CASE MANAGEMENT (TCMaaS) (TCMAAS)")
                # testexecution.testexecution_po_Jira_Click_Project().send_keys(Keys.ENTER)
                # # testexecution.testexecution_po_Jira_Choose_Project().click()
                # testexecution.testexecution_po_Jira_Click_IssueType().click()
                # # testexecution.testexecution_po_Jira_Click_IssueType()
                # testexecution.testexecution_po_Jira_Click_IssueType().send_keys("Story")
                # testexecution.testexecution_po_Jira_Click_IssueType().send_keys(Keys.ENTER)
                # testexecution.testexecution_po_Jira_Issue_Next().click()
                wait1.until(EC.presence_of_element_located((By.XPATH, "//h1[normalize-space()='Create Issue']")))
                jiracec.jiracec_PO_Summary_Name().send_keys("AT Test")
                self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
                self.driver.execute_script("arguments[0].click();", jiracec.jiracec_PO_Create())
                # jiracec.jiracec_PO_Create().click()
                # wait1.until(EC.element_to_be_clickable((By.ID, "project-name-val")))
                # self.driver.close()
                Count_TabOpened = len(windowsOpened)
                #
                # while Count_TabOpened > 1:
                for i in range(10):
                    if Count_TabOpened > 1:
                        windowsOpened = self.driver.window_handles
                        Count_TabOpened = len(windowsOpened)
                        time.sleep(10)
                self.driver.switch_to.window(windowsOpened[0])
                assert testexecution.testexecution_po_New_Defect_Add_Validation().text == 'New'
                testexecution.testexecution_po_Click_Close_Defect().click()
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestExecution_CreateNewDefect', '2681797')
            test_run_id = self.get_TestRun(testSuiteID, 'TestExecution_CreateNewDefect')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestExecution_CreateNewDefect', '2681797')
            test_run_id = self.get_TestRun(testSuiteID, 'TestExecution_CreateNewDefect')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()












