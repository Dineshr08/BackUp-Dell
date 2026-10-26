import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.HomePage_PO import HomePage_PO
from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from TestData.LoginPage_TD import LoginPage_TD
from TestData.TestExecution_TD import TestExecution_TD
from Utilities.BaseClass import BaseClass


class Test_TestExecution_LinkDefect_TestRun(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_TestExecution_LinkDefect_TestRun)
    def getUserInput(self, request):
        return request.param

    # @pytest.fixture(params=TestExecution_TD.test_testexecution_createtestsuiteandcycle_quickrun_TestCase_ID)
    # def getTestCaseID(self, request):
    #     return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_TestExecution_LinkDefect_TestRun(self, getUserInput, getTSValue):
    # def test_TestExecution_LinkDefect_TestRun(self, getUserInput):
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
            testexecution.testexecution_po_Enter_Defect_ID().send_keys("TCMAAS-15685")
            testexecution.testexecution_po_Defect_Link().click()
            assert "Link Defect is completed" in testexecution.testexecution_po_Linked_Defect_Msg().text
            testexecution.testexecution_po_Click_Close_Defect().click()
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestExecution_LinkDefect_TestRun', '2681806')
            test_run_id = self.get_TestRun(testSuiteID, 'TestExecution_LinkDefect_TestRun')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestExecution_LinkDefect_TestRun', '2681806')
            test_run_id = self.get_TestRun(testSuiteID, 'TestExecution_LinkDefect_TestRun')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()




