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


class Test_Administration_Authentication(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_Administration_Authentication)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_Administration_Authentication(self, getUserInput, getTSValue):

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
            authentication = admin.admin_po_Authentication()
            wait.until(EC.element_to_be_clickable((By.ID, "btnSaveLdapConfig_label")))
            # authentication.authentication_po_AppAuth().click()
            action.move_to_element(authentication.authentication_po_AppAuth()).click().perform()
            time.sleep(5)
            assert "appauth.dell.com:636" in authentication.authentication_po_AppAuth_Url().get_attribute("value")
            assert "DC=dell,DC=com" in authentication.authentication_po_AppAuth_Base().get_attribute("value")
            assert authentication.authentication_po_AppAuth_SSL().is_selected()
            assert authentication.authentication_po_AppAuth_IsActive().is_selected()
            assert "sAMAccountName" in authentication.authentication_po_AppAuth_Username().get_attribute("value")
            assert "givenName" in authentication.authentication_po_AppAuth_Fname().get_attribute("value")
            assert "sn" in authentication.authentication_po_AppAuth_Lname().get_attribute("value")
            assert "mail" in authentication.authentication_po_AppAuth_Email().get_attribute("value")
            assert "SUCCESSFUL" in authentication.authentication_po_AppAuth_SyncStatus().get_attribute("innerHTML")
            authentication.authentication_po_Gtie().click()
            action.move_to_element(authentication.authentication_po_Gtie()).click().perform()
            time.sleep(5)
            assert "ad1-cec.gtie.dell.com:636" in authentication.authentication_po_AppAuth_Url().get_attribute("value")
            assert "OU=Dell,DC=gtie,DC=dell,DC=com" in authentication.authentication_po_AppAuth_Base().get_attribute(
                "value")
            assert authentication.authentication_po_AppAuth_SSL().is_selected()
            assert authentication.authentication_po_AppAuth_IsActive().is_selected()
            assert "sAMAccountName" in authentication.authentication_po_AppAuth_Username().get_attribute("value")
            assert "givenName" in authentication.authentication_po_AppAuth_Fname().get_attribute("value")
            assert "sn" in authentication.authentication_po_AppAuth_Lname().get_attribute("value")
            assert "mail" in authentication.authentication_po_AppAuth_Email().get_attribute("value")
            assert "SUCCESSFUL" in authentication.authentication_po_AppAuth_SyncStatus().get_attribute("innerHTML")
            action.move_to_element(homepage.homepage_po_qTest_Component_Hover()).perform()
            wait.until(EC.presence_of_element_located((HomePage_PO.qTest_Manager)))
            homepage.homepage_po_qTest_Manager().click()
            wait.until(EC.presence_of_element_located((By.ID, "topLeftTitle")))
            self.Logout()

            #New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Administration_Authentication', '4962908')
            test_run_id = self.get_TestRun(testSuiteID, 'Administration_Authentication')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Administration_Authentication', '4962908')
            test_run_id = self.get_TestRun(testSuiteID, 'Administration_Authentication')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()


















