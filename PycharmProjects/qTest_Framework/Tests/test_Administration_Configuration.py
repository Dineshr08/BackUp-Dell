import time
from datetime import datetime

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.Administration_PO import Administration_PO
from PageObjects.Authentication_PO import Authentication_PO
from PageObjects.HomePage_PO import HomePage_PO
from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.TestDesign_PO import TestDesign_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from TestData.LoginPage_TD import LoginPage_TD
from TestData.TestExecution_TD import TestExecution_TD
from Utilities.BaseClass import BaseClass


class Test_Administration_Configuration(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_Administration_Configuration)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_Administration_Configuration(self, getUserInput, getTSValue):
        try:
            log = self.logging()
            loginpage = LoginPage_PO(self.driver)
            loginpage.loginpage_po_username().send_keys(getUserInput["username"])
            loginpage.loginpage_po_password().send_keys(getUserInput["password"])
            homepage = loginpage.loginpage_po_loginBtn()
            cookies = self.get_cookies()
            action = ActionChains(self.driver)
            action.move_to_element(homepage.homepage_po_User_Menu()).perform()
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((HomePage_PO.Admin)))
            admin = homepage.homepage_po_Admin()
            wait.until(EC.presence_of_element_located(
                (By.XPATH, "//label[@class='pt-1 pl-3 col-form-label filter-title no-padding-right text-nowrap']")))
            configuration = admin.admin_po_Configuration()
            wait.until(EC.element_to_be_clickable((By.ID, "submitEmailConfiguration_label")))
            assert "smtp-cec.gtie.dell.com" in configuration.configuration_po_hostname().get_attribute("value")
            assert "25" in configuration.configuration_po_SMTPPort().get_attribute("value")
            assert "none" in configuration.configuration_po_SecurityProtocol().get_attribute("value")
            assert "qTest-stage@dell.com" in configuration.configuration_po_Email().get_attribute("value")
            assert "ServiceQmetry" in configuration.configuration_po_Username().get_attribute("value")
            assert "https://qtest-stg-appt1.gtie.dell.com:9443" in configuration.configuration_po_Session_Explorer().get_attribute(
                "value")
            assert "https://qtest-stg-appt1.gtie.dell.com:5080" in configuration.configuration_po_Parameter().get_attribute(
                "value")
            assert "https://qtest-stg-appt1.gtie.dell.com:4080" in configuration.configuration_po_Pulse().get_attribute(
                "value")
            assert "https://qtest-stg-appt1.gtie.dell.com:3080" in configuration.configuration_po_Launch().get_attribute(
                "value")
            assert "https://qtest-stg-ins01.gtie.dell.com" in configuration.configuration_po_Insights().get_attribute(
                "value")
            assert "999" in configuration.configuration_po_AttachmentSize().get_attribute("value")
            action.move_to_element(homepage.homepage_po_qTest_Component_Hover()).perform()
            wait.until(EC.presence_of_element_located((HomePage_PO.qTest_Manager)))
            homepage.homepage_po_qTest_Manager().click()
            wait.until(EC.presence_of_element_located((By.ID, "topLeftTitle")))
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Administration_Configuration', '4962908')
            test_run_id = self.get_TestRun(testSuiteID, 'Administration_Configuration')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Administration_Configuration', '4962908')
            test_run_id = self.get_TestRun(testSuiteID, 'Administration_Configuration')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()














