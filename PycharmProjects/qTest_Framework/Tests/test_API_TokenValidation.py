import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Arrow_PO import Arrow_PO
from PageObjects.HomePage_PO import HomePage_PO
from PageObjects.LoginPage_PO import LoginPage_PO
from TestData.LoginPage_TD import LoginPage_TD
from Utilities.BaseClass import BaseClass


class Test_API_TokenValidation(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_API_TokenValidation)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface


    def test_API_TokenValidation(self, getUserInput, getTSValue):
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
            arrow = homepage.homepage_po_Arrow()
            wait.until(EC.element_to_be_clickable(Arrow_PO.CI_ToolIntegartion))
            arrow.arrow_po_CI_ToolIntegartion().click()
            wait.until(EC.visibility_of_element_located(Arrow_PO.Jenkin_RefreshToken))
            assert "f3b7578b-9c0a-4652-8942-881aa4a7c84b" == arrow.arrow_po_Jenkin_RefreshToken().text
            self.driver.find_element(By.XPATH, "//body").send_keys(Keys.END)
            wait.until(EC.element_to_be_clickable(Arrow_PO.API_SDK))
            self.driver.execute_script("arguments[0].click();", arrow.arrow_po_API_SDK())
            time.sleep(5)
            # arrow.arrow_po_API_SDK().click()
            self.driver.find_element(By.XPATH, "//body").send_keys(Keys.END)
            time.sleep(5)
            assert "Bearer 87716aa1-702c-4ea6-8308-e6f05f332b57" in arrow.arrow_po_API_BearerToken().text
            # assert "bmVwaGVsZXxwdHVzZXI0M0BkZWxsLmNvbToxNzI0NDE4NjgwNDUyOmU5MmFjNmVmZDc3MzQ1YzRlNmY5YTNiMmRlMDljMTlm" in arrow.arrow_po_API_Token().text
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'API_TokenValidation', '4962908')
            test_run_id = self.get_TestRun(testSuiteID, 'API_TokenValidation')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'API_TokenValidation', '4962908')
            test_run_id = self.get_TestRun(testSuiteID, 'API_TokenValidation')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()










