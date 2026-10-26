import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.HomePage_PO import HomePage_PO
from PageObjects.LoginPage_PO import LoginPage_PO
from TestData.LoginPage_TD import LoginPage_TD
from Utilities.BaseClass import BaseClass


class Test_TestPlan_SearchTestCase(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_TestPlan_SearchTestCase)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface
    @pytest.mark.Validation
    # @pytest.mark.flaky(reruns=1, reruns_delay=2)


    def test_TestPlan_SearchTestCase(self, getUserInput, getTSValue):

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
            wait.until(EC.element_to_be_clickable((By.ID, "testDesignRootHeader_btnReload")))
            homepage.homepage_po_Global_Search().click()
            homepage.homepage_po_Global_Search_TextBox().clear()
            homepage.homepage_po_Global_Search_TextBox().send_keys("TC-16")
            homepage.homepage_po_Global_Search_TextBox().send_keys(Keys.ENTER)
            wait.until(EC.presence_of_element_located(HomePage_PO.Global_Search_TextBox_Output))
            assert "TC-16 - Link_TestCase" in homepage.homepage_po_Global_Search_TextBox_Output().text
            homepage.homepage_po_Global_Search().click()
            homepage.homepage_po_Global_Search_TextBox().clear()
            homepage.homepage_po_Global_Search_TextBox().send_keys("Link_TestCase")
            homepage.homepage_po_Global_Search_TextBox().send_keys(Keys.ENTER)
            wait.until(EC.presence_of_element_located(HomePage_PO.Global_Search_TextBox_Output))
            assert "TC-16 - Link_TestCase" in homepage.homepage_po_Global_Search_TextBox_Output().text
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestPlan_SearchTestCase', '4955402')
            test_run_id = self.get_TestRun(testSuiteID, 'TestPlan_SearchTestCase')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestPlan_SearchTestCase', '4955402')
            test_run_id = self.get_TestRun(testSuiteID, 'TestPlan_SearchTestCase')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()


















