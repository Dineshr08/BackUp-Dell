import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.TestDesign_PO import TestDesign_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from TestData.LoginPage_TD import LoginPage_TD
from TestData.TestExecution_TD import TestExecution_TD
from Utilities.BaseClass import BaseClass


class Test_TestCaseSharing_Unsharing(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_TestCaseSharing_Unsharing)
    def getUserInput(self, request):
        return request.param

    # @pytest.fixture(params=TestExecution_TD.test_testexecution_createtestsuiteandcycle_quickrun_TestCase_ID)
    # def getTestCaseID(self, request):
    #     return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_TestCaseSharing_Unsharing(self, getUserInput, getTSValue):
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
            time.sleep(5)
            homepage.homepage_po_chooseAT1Project().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AutomationTesting1']")))
            UI_LandingPage_Validation = homepage.homepage_po_AT1Project_landingPage_Validation().text
            assert "AutomationTesting1" == UI_LandingPage_Validation
            testdesign = homepage.homepage_po_testdesign()
            time.sleep(10)
            action.move_to_element(testdesign.testdesign_po_Existing_TestCaseSharingFolder()).perform()
            testdesign.testdesign_po_Existing_TestCaseSharingFolder().click()
            testdesign.testdesign_po_TestCaseSharing_Properties().click()
            agreed = testdesign.testdesign_po_Choose_Shared_Yes()
            time.sleep(2)
            if agreed.get_attribute("checked") == "true":
                testdesign.testdesign_po_TestCaseSharing_Reload().click()
                time.sleep(2)

            else:
                testdesign.testdesign_po_Choose_Shared_Yes().click()
                testdesign.testdesign_po_TestCaseSharing_Save().click()
                wait.until(EC.element_to_be_clickable(TestDesign_PO.TestCaseSharing_Save_Confirmation))
                testdesign.testdesign_po_TestCaseSharing_Save_Confirmation().click()

            action.move_to_element(homepage.homepage_po_hoverProjectMenu()).perform()
            homepage.homepage_po_searchProject().send_keys("AutomationTesting")
            wait = WebDriverWait(self.driver, 30)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "AutomationTesting")))
            time.sleep(5)
            homepage.homepage_po_chooseATProject().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AutomationTesting']")))
            testexecution = homepage.homepage_po_testexecution()
            # testexecution.testexecution_po_New_TestCycle().click()
            time.sleep(5)
            NewTestCycle = testexecution.testexecution_po_New_TestCycle()
            time.sleep(5)
            NewTestCycle.click()
            testexecution.testexecution_po_New_TestCycle_Name().send_keys("AT TestCycle")
            testexecution.testexecution_po_New_TestSuite().click()
            testexecution.testexecution_po_New_TestSuite_Name().send_keys("AT Test Suite")
            self.driver.execute_script("arguments[0].click();", testexecution.testexecution_po_Add_TestRuns())
            self.driver.execute_script("arguments[0].click();", testexecution.testexecution_po_Add_TestRuns_TestCase())
            # testexecution.testexecution_po_Add_TestRuns_TestCase().click()
            time.sleep(2)
            # action.move_to_element(testexecution.testexecution_po_TestCaseSharing_TestCase_ChooseProject()).click().perform()
            testexecution.testexecution_po_TestCaseSharing_TestCase_ChooseProject().click()
            testexecution.testexecution_po_TestCaseSharing_TestCase_Search().send_keys("AutomationTesting1")
            testexecution.testexecution_po_TestCaseSharing_TestCase_Search().send_keys(Keys.ENTER)
            testexecution.testexecution_po_TestCaseSharing_SelectSharingFolder().click()
            testexecution.testexecution_po_TestCaseSharing_TestCase_ChooseAllCheckBox().click()
            testexecution.testexecution_po_Add_TestRuns_Add().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='grid-cell-status']")))
            testexecution.testexecution_po_Open_TestRun_ID().click()
            wait.until(EC.element_to_be_clickable(TestExecution_PO.TestCaseSharingValidation))
            CurrentURL = self.driver.current_url
            # print(CurrentURL)
            action.move_to_element(homepage.homepage_po_hoverProjectMenu()).perform()
            homepage.homepage_po_searchProject().send_keys("AutomationTesting1")
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "AutomationTesting1")))
            time.sleep(5)
            homepage.homepage_po_chooseAT1Project().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AutomationTesting1']")))
            UI_LandingPage_Validation = homepage.homepage_po_AT1Project_landingPage_Validation().text
            assert "AutomationTesting1" == UI_LandingPage_Validation
            time.sleep(5)
            testdesign = homepage.homepage_po_testdesign()
            action.move_to_element(testdesign.testdesign_po_Existing_TestCaseSharingFolder()).perform()
            testdesign.testdesign_po_Existing_TestCaseSharingFolder().click()
            testdesign.testdesign_po_TestCaseSharing_Properties().click()
            testdesign.testdesign_po_Choose_Shared_Yes().click()
            testdesign.testdesign_po_TestCaseSharing_Save().click()
            wait.until(EC.element_to_be_clickable(TestDesign_PO.TestCaseSharing_Save_Confirmation))
            testdesign.testdesign_po_TestCaseSharing_Save_Confirmation().click()
            time.sleep(5)
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
            self.driver.get(CurrentURL)
            # time.sleep(5)
            wait.until(EC.visibility_of_element_located(
                (By.ID, "testrun_properties_PlannedEndTestRunSystemField_PlannedEndDate")))
            assert "You are not able to execute this Test Run since the associated Test Case is no longer shared to your project" in testexecution.testexecution_po_TestCaseSharing_Unshared_Validation().get_attribute(
                "innerHTML")
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 'w')
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestCaseSharing_Unsharing', '2681863')
            test_run_id = self.get_TestRun(testSuiteID, 'TestCaseSharing_Unsharing')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestCaseSharing_Unsharing', '2681863')
            test_run_id = self.get_TestRun(testSuiteID, 'TestCaseSharing_Unsharing')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()
