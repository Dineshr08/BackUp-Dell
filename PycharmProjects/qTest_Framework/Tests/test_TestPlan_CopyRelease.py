import time

import pytest
import requests
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.HomePage_PO import HomePage_PO
from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.TestPlan_PO import TestPlan_PO
from TestData.LoginPage_TD import LoginPage_TD
from Utilities.BaseClass import BaseClass


class Test_TestPlan_CopyRelease(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_TestPlan_CopyRelease)
    def getUserInput(self, request):
        return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_TestPlan_CopyRelease(self, getUserInput, getTSValue):
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
            time.sleep(5)
            homepage.homepage_po_chooseAT1Project().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AutomationTesting1']")))
            UI_LandingPage_Validation = homepage.homepage_po_AT1Project_landingPage_Validation().text
            assert "AutomationTesting1" == UI_LandingPage_Validation
            testplan = homepage.homepage_po_testplan()
            time.sleep(5)
            action.move_to_element(testplan.testplan_po_ExistingRelease()).perform()
            testplan.testplan_po_ExistingRelease().click()
            time.sleep(5)
            action.context_click(testplan.testplan_po_ExistingRelease()).perform()
            wait.until(EC.element_to_be_clickable(TestPlan_PO.Copy))
            testplan.testplan_po_Copy().click()
            action.move_to_element(testplan.testplan_po_HomeFolder()).perform()
            # testplan.testplan_po_HomeFolder().click()
            action.context_click(testplan.testplan_po_HomeFolder()).perform()
            # time.sleep(5)
            testplan.testplan_po_Paste().click()
            assert "success" in testplan.testplan_po_CopyRelease_Validation().get_attribute("innerHTML")
            wait.until(EC.element_to_be_clickable(HomePage_PO.requirement))
            time.sleep(10)

            # Data setup to delete test release
            URL = 'https://qtest-stage.gtie.dell.com/api/v3/projects/404/releases'
            HEADERS = {
                "Authorization": "Bearer fda0002f-500a-47c6-b617-0381dc027b39",
                "Content-Type": "application/json"
            }

            response = requests.get(URL, headers=HEADERS)
            assert response.status_code == 200
            data = response.json()
            ids = []
            for item in data:
                if 'id' in item:
                    ids.append(item['id'])
            assert len(ids) > 1
            Count = len(ids)
            # Data Setup
            for i in range(Count):
                URL1 = 'https://qtest-stage.gtie.dell.com/api/v3/projects/404/releases/'
                if ids[i] == 16193:
                    continue
                else:
                    Release_ID = ids[i]
                    response = requests.delete(url="{}{}".format(URL1, Release_ID), headers=HEADERS)
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestPlan_CopyRelease', '2681780')
            test_run_id = self.get_TestRun(testSuiteID, 'TestPlan_CopyRelease')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'TestPlan_CopyRelease', '2681780')
            test_run_id = self.get_TestRun(testSuiteID, 'TestPlan_CopyRelease')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()










