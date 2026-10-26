import time

import pyautogui
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.BaseClass import BaseClass
from PageObjects.HomePage_PO import HomePage_PO
from PageObjects.JiraCEC_PO import JiraCEC_PO
from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from TestData.LoginPage_TD import LoginPage_TD
from TestData.TestExecution_TD import TestExecution_TD
from Utilities.BaseClass import BaseClass
from Utilities.BaseClass_Jira import BaseClass_Jira

pyautogui.FAILSAFE = False

# @pytest.mark.usefixtures("setup_jira")
class Test_JiraIntegration_qTestIntegratedProjects(BaseClass_Jira):

    # @pytest.fixture(params=LoginPage_TD.test_JiraIntegration_qTestIntegratedProjects)
    # def getUserInput(self, request):
    #     return request.param

    # @pytest.fixture(params=TestExecution_TD.test_testexecution_createtestsuiteandcycle_quickrun_TestCase_ID)
    # def getTestCaseID(self, request):
    #     return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface


    def test_JiraIntegration_qTestIntegratedProjects(self, getTSValue):
    # def test_JiraIntegration_qTestIntegratedProjects(self):
        try:

            action = ActionChains(self.driver)
            wait1 = WebDriverWait(self.driver, 20)
            self.driver.get('https://jira-stage.cec.lab.emc.com/projects/TCMAAS/summary')
            time.sleep(10)
            pyautogui.press('esc')
            try:
                wait1.until(EC.presence_of_element_located((By.ID, "Submit_btn")))
                assert 'Sign' in self.driver.title
                self.driver.find_element(By.ID, "username").send_keys("svc_npjiratoqtest")
                self.driver.find_element(By.ID, "Password").send_keys("*?w2Xt1+uBY3z~A_69v0mNJH")
                self.driver.find_element(By.ID, "Submit_btn").click()
                wait1.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Backlog']")))
                assert 'TEST CASE' in self.driver.title
                jiracec = JiraCEC_PO(self.driver)
                self.driver.find_element(By.CLASS_NAME, "aui-sidebar-body").click()
                self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
                jiracec.jiracec_PO_Addon_Expand().click()
                wait1.until(EC.element_to_be_clickable(JiraCEC_PO.qTest))
                jiracec.jiracec_PO_qTest().click()
                wait1.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='qTest']")))
                Frame_element = self.driver.find_element(By.CLASS_NAME, "qtest-panel-content")
                self.driver.switch_to.frame(Frame_element)
                Select_Options = Select(self.driver.find_element(By.ID, "qtest-project"))
                Project = []
                for x in Select_Options.options:
                    Project.append(x.text)
                # print(Project)
                self.driver.switch_to.default_content()
                # assert ['TechOps_Validation', 'AKT-Test', 'AutomationTesting1'] == Project
                assert sorted(
                    ['qConnect - Sample Project', 'AutomationTesting1', 'AKT-Test', 'TechOps_Validation', '2023.5 test project', 'App Infra Test Project']) == sorted(
                    Project)

                testSuiteID = getTSValue
                self.create_TestRun(testSuiteID, 'JiraIntegration_qTestIntegratedProjects', '4887546')
                test_run_id = self.get_TestRun(testSuiteID, 'JiraIntegration_qTestIntegratedProjects')
                self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

            except Exception as e:
                wait1.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Backlog']")))
                assert 'TEST CASE' in self.driver.title
                jiracec = JiraCEC_PO(self.driver)
                self.driver.find_element(By.CLASS_NAME, "aui-sidebar-body").click()
                self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
                jiracec.jiracec_PO_Addon_Expand().click()
                wait1.until(EC.element_to_be_clickable(JiraCEC_PO.qTest))
                jiracec.jiracec_PO_qTest().click()
                wait1.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='qTest']")))
                Frame_element = self.driver.find_element(By.CLASS_NAME, "qtest-panel-content")
                self.driver.switch_to.frame(Frame_element)
                Select_Options = Select(self.driver.find_element(By.ID, "qtest-project"))
                Project = []
                for x in Select_Options.options:
                    Project.append(x.text)
                # print(Project)
                self.driver.switch_to.default_content()
                # assert ['TechOps_Validation', 'AKT-Test', 'AutomationTesting1'] == Project
                assert sorted(
                    ['qConnect - Sample Project', 'AutomationTesting1', 'AKT-Test', 'TechOps_Validation', '2023.5 test project', 'App Infra Test Project']) == sorted(
                    Project)

                testSuiteID = getTSValue
                self.create_TestRun(testSuiteID, 'JiraIntegration_qTestIntegratedProjects', '4887546')
                test_run_id = self.get_TestRun(testSuiteID, 'JiraIntegration_qTestIntegratedProjects')
                self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:
            # pass

            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'JiraIntegration_qTestIntegratedProjects', '4887546')
            test_run_id = self.get_TestRun(testSuiteID, 'JiraIntegration_qTestIntegratedProjects')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')













