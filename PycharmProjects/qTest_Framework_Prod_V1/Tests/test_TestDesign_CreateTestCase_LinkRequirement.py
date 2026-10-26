import time
import pytest
# from pynput.keyboard import Controller, Key
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.LoginPage_PO import LoginPage_PO
from TestData.LoginPage_TD import LoginPage_TD
from Utilities.BaseClass import BaseClass


class Test_TestDesign_CreateTestCase_LinkRequirement(BaseClass):

    @pytest.fixture(params=LoginPage_TD.testdesign_createtestcase_linkrequirement)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_TestDesign_CreateTestCase_LinkRequirement(self, getUserInput, getTSValue):
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
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "AutomationTesting")))
            time.sleep(5)
            homepage.homepage_po_chooseATProject().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AutomationTesting']")))
            UI_LandingPage_Validation = homepage.homepage_po_ATProject_landingPage_Validation().text
            assert "AutomationTesting" == UI_LandingPage_Validation
            testdesign = homepage.homepage_po_testdesign()
            self.driver.execute_script("arguments[0].click();", testdesign.testdesign_po_Create_NewModule())
            # testdesign.testdesign_po_Create_NewModule().click()
            testdesign.testdesign_po_Update_NewModuleName().send_keys("AT Module")
            self.driver.execute_script("arguments[0].click();", testdesign.testdesign_po_CreateNewTestCase())
            # testdesign.testdesign_po_CreateNewTestCase().click()
            testdesign.testdesign_po_Update_ExistingTestCaseNameField().send_keys("AT TestCase")
            # self.execute_script_Click(testdesign.testdesign_po_Type())
            testdesign.testdesign_po_Type().click()
            # self.execute_script_Click(testdesign.testdesign_po_Choose_AutomationType())
            testdesign.testdesign_po_Choose_AutomationType().click()
            self.driver.execute_script("arguments[0].click();", testdesign.testdesign_po_TDSub_Requirement())
            # testdesign.testdesign_po_TDSub_Requirement().click()
            self.driver.find_element(By.XPATH, "//body").send_keys(Keys.PAGE_DOWN)
            self.driver.execute_script("arguments[0].click();", testdesign.testdesign_po_TDSub_Requirement_AddBtn())
            # testdesign.testdesign_po_TDSub_Requirement_AddBtn().click()
            self.driver.execute_script("arguments[0].click();",
                                       testdesign.testdesign_po_TDSub_AddRequirement_Requirement())
            # testdesign.testdesign_po_TDSub_AddRequirement_Requirement().click()
            testdesign.testdesign_po_TD_Sub_SearchRequirement().send_keys("RQ-799")
            testdesign.testdesign_po_TD_Sub_SearchRequirement().send_keys(Keys.ENTER)
            self.driver.execute_script("arguments[0].click();", testdesign.testdesign_po_TD_Sub_ChooseAllCheckBox())
            # testdesign.testdesign_po_TD_Sub_ChooseAllCheckBox().click()
            self.driver.execute_script("arguments[0].click();", testdesign.testdesign_po_TDSub_Requirement_ADD())
            # testdesign.testdesign_po_TDSub_Requirement_ADD().click()
            LinkRequirement_Verify = testdesign.testdesign_po_TDSub_Requirement_ADD_Verify().text
            assert "Link_Requirement" in LinkRequirement_Verify
            testdesign.testdesign_po_Save().click()
            time.sleep(10)
            self.execute_script_Click(testdesign.testdesign_po_Approve())
            # testdesign.testdesign_po_Approve().click()
            # self.execute_script_Click(testdesign.testdesign_po_Approve_Yes())
            testdesign.testdesign_po_Approve_Yes().click()
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestDesign_CreateTestCase_LinkRequirement', '4962822')
            test_run_id = self.get_TestRun(testSuiteID, 'TestDesign_CreateTestCase_LinkRequirement')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestDesign_CreateTestCase_LinkRequirement', '4962822')
            test_run_id = self.get_TestRun(testSuiteID, 'TestDesign_CreateTestCase_LinkRequirement')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()




