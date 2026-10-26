import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Administration_PO import Administration_PO
from PageObjects.FieldSetting_PO import FieldSetting_PO
from PageObjects.HomePage_PO import HomePage_PO
from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.TestDesign_PO import TestDesign_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from TestData.LoginPage_TD import LoginPage_TD
from TestData.TestExecution_TD import TestExecution_TD
from Utilities.BaseClass import BaseClass


class Test_ProjectFieldSetting_TestRun_TextBox(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_ProjectFieldSetting_TestRun_TextBox)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_ProjectFieldSetting_TestRun_TextBox(self, getUserInput, getTSValue):
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
            action.move_to_element(homepage.homepage_po_Global_Setting()).perform()
            wait.until(EC.presence_of_element_located((HomePage_PO.Global_Setting_Field_Setting)))
            field = homepage.homepage_po_Global_Setting_Field_Setting()
            wait.until(EC.presence_of_element_located((FieldSetting_PO.Global_Setting_Field_Setting_AddCustomField)))
            field.fieldsetting_po_Global_Setting_Field_Setting_TestRun().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//th[normalize-space()='Display Name']")))
            field.fieldsetting_po_Global_Setting_Field_Setting_AddCustomField().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Display name')]")))
            field.fieldsetting_po_Global_Setting_Field_Setting_AddCustomField_DisplayName().clear()
            field.fieldsetting_po_Global_Setting_Field_Setting_AddCustomField_DisplayName().send_keys(
                "AT_TestCase_CustomField_TextBox")
            field.fieldsetting_po_Global_Setting_Field_Setting_AddCustomField_OK().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Display name']")))
            self.driver.execute_script("arguments[0].click();",
                                       field.fieldsetting_po_Global_Setting_Field_Setting_AddCustomField_OK1())
            # field.fieldsetting_po_Global_Setting_Field_Setting_AddCustomField_OK1().click()
            wait.until(EC.presence_of_element_located((By.LINK_TEXT, "AT_TestCase_CustomField_TextBox")))
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'ProjectFieldSetting_TestRun_TextBox', '1091086')
            test_run_id = self.get_TestRun(testSuiteID, 'ProjectFieldSetting_TestRun_TextBox')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'ProjectFieldSetting_TestRun_TextBox', '1091086')
            test_run_id = self.get_TestRun(testSuiteID, 'ProjectFieldSetting_TestRun_TextBox')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()















