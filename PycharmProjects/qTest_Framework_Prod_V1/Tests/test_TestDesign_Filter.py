import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.TestDesign_PO import TestDesign_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from TestData.LoginPage_TD import LoginPage_TD
from TestData.TestExecution_TD import TestExecution_TD
from Utilities.BaseClass import BaseClass


class Test_TestDesign_Filter(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_TestDesign_Filter)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_TestDesign_Filter(self, getUserInput, getTSValue):
        try:
            log = self.logging()
            loginpage = LoginPage_PO(self.driver)
            loginpage.loginpage_po_username().send_keys(getUserInput["username"])
            loginpage.loginpage_po_password().send_keys(getUserInput["password"])
            homepage = loginpage.loginpage_po_loginBtn()
            cookies = self.get_cookies()
            action = ActionChains(self.driver)
            action.move_to_element(homepage.homepage_po_hoverProjectMenu()).perform()
            homepage.homepage_po_searchProject().send_keys("AutomationTesting")
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "AutomationTesting")))
            time.sleep(5)
            homepage.homepage_po_chooseATProject().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AutomationTesting']")))
            UI_LandingPage_Validation = homepage.homepage_po_ATProject_landingPage_Validation().text
            assert "AutomationTesting" == UI_LandingPage_Validation
            testdesign = homepage.homepage_po_testdesign()
            time.sleep(5)
            testdesign.testdesign_po_Filter().click()
            wait.until(EC.element_to_be_clickable(TestDesign_PO.Set_Filter))
            testdesign.testdesign_po_Set_Filter().click()
            wait.until(EC.element_to_be_clickable(TestDesign_PO.Apply_Filter))
            time.sleep(5)
            # testdesign.testdesign_po_Filter_Type().send_keys("Manual")
            testdesign.testdesign_po_Filter_Type().click()
            testdesign.testdesign_po_Filter_Type().clear()
            testdesign.testdesign_po_Filter_Type().send_keys("Manual")
            testdesign.testdesign_po_Choose_Manual_Type().click()
            testdesign.testdesign_po_Apply_Filter().click()
            # testdesign.testdesign_po_Filter_Type().send_keys(Keys.ENTER)
            wait.until(EC.element_to_be_clickable(TestDesign_PO.Reload))
            testdesign.testdesign_po_Filter().click()
            wait.until(EC.element_to_be_clickable(TestDesign_PO.Set_Filter))
            testdesign.testdesign_po_Clear_Filter().click()
            wait.until(EC.element_to_be_clickable(TestDesign_PO.Clear_Filter_Yes))
            testdesign.testdesign_po_Clear_Filter_Yes().click()
            wait.until(EC.element_to_be_clickable(TestDesign_PO.Reload))
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestDesign_Filter', '2681777')
            test_run_id = self.get_TestRun(testSuiteID, 'TestDesign_Filter')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestDesign_Filter', '2681777')
            test_run_id = self.get_TestRun(testSuiteID, 'TestDesign_Filter')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()









