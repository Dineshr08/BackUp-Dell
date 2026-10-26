import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Administration_PO import Administration_PO
from PageObjects.HomePage_PO import HomePage_PO
from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.TestDesign_PO import TestDesign_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from TestData.LoginPage_TD import LoginPage_TD
from TestData.TestExecution_TD import TestExecution_TD
from Utilities.BaseClass import BaseClass


class Test_Administration_SiteField_TestCase_ComboBox(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_Administration_SiteField_TestCase_ComboBox)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface
    def test_Administration_SiteField_TestCase_ComboBox(self, getUserInput, getTSValue):
        try:
            log = self.logging()
            loginpage = LoginPage_PO(self.driver)
            loginpage.loginpage_po_username().send_keys(getUserInput["username"])
            loginpage.loginpage_po_password().send_keys(getUserInput["password"])
            homepage = loginpage.loginpage_po_loginBtn()
            cookies = self.get_cookies()
            action = ActionChains(self.driver)
            action.move_to_element(homepage.homepage_po_User_Menu()).perform()
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.presence_of_element_located((HomePage_PO.Admin)))
            admin = homepage.homepage_po_Admin()
            wait.until(EC.presence_of_element_located(
                (By.XPATH, "//label[@class='pt-1 pl-3 col-form-label filter-title no-padding-right text-nowrap']")))
            admin.admin_po_SiteField().click()
            wait.until(EC.presence_of_element_located((Administration_PO.SiteField_Manage_SiteField)))
            admin.admin_po_SiteField_Manage_SiteField().click()
            wait.until(EC.presence_of_element_located((Administration_PO.SiteField_TestCase)))
            admin.admin_po_SiteField_TestCase().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//th[normalize-space()='Display Name']")))
            admin.admin_po_SiteField_Add_CustomField().click()
            admin.admin_po_SiteField_DisplayName().clear()
            admin.admin_po_SiteField_DisplayName().send_keys("AT_TestCase_CustomField_ComboBox")
            dropdown = Select(admin.admin_po_SiteField_FieldTypeSelection())
            dropdown.select_by_visible_text("Combo box")
            admin.admin_po_SiteField_OK().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Display Name']")))
            admin.admin_po_SiteField_AddValue().click()
            # admin.admin_po_SiteField_AddValue_Input().clear()
            admin.admin_po_SiteField_AddValue_Input().send_keys("1")
            self.driver.execute_script("arguments[0].click();", admin.admin_po_SiteField_ComboBox_OK())
            # admin.admin_po_SiteField_OK1().click()
            assert "success" in admin.admin_po_SiteField_Created_Validation().get_attribute("innerHTML")
            action.move_to_element(homepage.homepage_po_qTest_Component_Hover()).perform()
            wait.until(EC.presence_of_element_located((HomePage_PO.qTest_Manager)))
            homepage.homepage_po_qTest_Manager().click()
            wait.until(EC.presence_of_element_located((By.ID, "topLeftTitle")))
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Administration_SiteField_TestCase_ComboBox', '1091086')
            test_run_id = self.get_TestRun(testSuiteID, 'Administration_SiteField_TestCase_ComboBox')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Administration_SiteField_TestCase_ComboBox', '1091086')
            test_run_id = self.get_TestRun(testSuiteID, 'Administration_SiteField_TestCase_ComboBox')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()














