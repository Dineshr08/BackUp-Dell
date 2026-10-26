import json
import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.HomePage_PO import HomePage_PO
from PageObjects.LoginPage_PO import LoginPage_PO
from PageObjects.Pulse_PO import Pulse_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from TestData.LoginPage_TD import LoginPage_TD
from TestData.TestExecution_TD import TestExecution_TD
from Utilities.BaseClass import BaseClass


class Test_Pulse_Link_Unlink_Defect(BaseClass):

    @pytest.fixture(params=LoginPage_TD.test_Pulse_Link_Unlink_Defect)
    def getUserInput(self, request):
        return request.param

    # @pytest.fixture(params=TestExecution_TD.test_testexecution_createtestsuiteandcycle_quickrun_TestCase_ID)
    # def getTestCaseID(self, request):
    #     return request.param

    @pytest.mark.regression
    @pytest.mark.UserInterface

    def test_Pulse_Link_Unlink_Defect(self, getUserInput, getTSValue):
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
            # wait.until(EC.staleness_of(HomePage_PO.chooseAT1Project))
            time.sleep(5)
            homepage.homepage_po_chooseAT1Project().click()
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='AutomationTesting1']")))
            UI_LandingPage_Validation = homepage.homepage_po_AT1Project_landingPage_Validation().text
            assert "AutomationTesting1" == UI_LandingPage_Validation
            testexecution = homepage.homepage_po_testexecution()
            time.sleep(10)
            action.move_to_element(testexecution.testexecution_po_Open_Existing_Release_Template()).perform()
            testexecution.testexecution_po_Open_Existing_Release_Template().click()
            for i in range(2):
                testexecution.testexecution_po_New_TestCycle().click()
                if i == 0:
                    testexecution.testexecution_po_New_TestCycle_Name().send_keys("AT TestCycle")
                else:
                    testexecution.testexecution_po_New_TestCycle_Name().send_keys("AT Sub TestCycle")
            testexecution.testexecution_po_New_TestSuite().click()
            testexecution.testexecution_po_New_TestSuite_Name().send_keys("AT Test Suite")
            testCaseID = ["TC-163"]
            for j in range(1):
                if j >= 1:
                    wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Test Runs']")))
                # Below statement we have written, because when we click add test run for 3 time got element element click intercepted exception
                self.driver.execute_script("arguments[0].click();", testexecution.testexecution_po_Add_TestRuns())
                # testexecution.testexecution_po_Add_TestRuns().click()
                self.driver.execute_script("arguments[0].click();",
                                           testexecution.testexecution_po_Add_TestRuns_TestCase())
                # testexecution.testexecution_po_Add_TestRuns_TestCase().click()
                testexecution.testexecution_po_Add_TestRuns_Search().clear()
                testexecution.testexecution_po_Add_TestRuns_Search().send_keys(testCaseID[j])
                testexecution.testexecution_po_Add_TestRuns_Search().send_keys(Keys.ENTER)
                testexecution.testexecution_po_Add_TestRuns_AllCheckBox().click()
                wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-default btn-add']")))
                testexecution.testexecution_po_Add_TestRuns_Add().click()
                wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Test Runs']")))
                time.sleep(5)

            wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Test Runs']")))
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='grid-cell-status']")))
            testexecution.testexecution_po_TestSuite_ChooseAllTestCase().click()
            testexecution.testexecution_po_TestSuite_QuickRun().click()
            testexecution.testexecution_po_QuickRun_ChooseAllTestcase().click()
            wait.until(EC.element_to_be_clickable((TestExecution_PO.QuickRun_Apply)))
            testexecution.testexecution_po_QuickRun_Apply().click()
            time.sleep(5)
            testexecution.testexecution_po_QuickRun_OkandRefresh().click()
            time.sleep(5)
            assert testexecution.testexecution_po_TestSuite_QuickRun_TestCase_UpdatedStatus().get_attribute(
                "innerHTML") == "Passed"
            testexecution.testexecution_po_Open_TestRun_ID().click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//span[normalize-space()='Execution History (1)']").click()
            self.driver.find_element(By.TAG_NAME, "html").send_keys(Keys.END)
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='Edit']")))
            action.move_to_element(testexecution.testexecution_po_Bug()).perform()
            time.sleep(5)
            self.driver.execute_script("arguments[0].click();", testexecution.testexecution_po_Bug())
            # testexecution.testexecution_po_Bug().click()
            wait.until(EC.presence_of_element_located((TestExecution_PO.New_Defect)))
            testexecution.testexecution_po_Enter_Defect_ID().send_keys("TCMAAS-15685")
            testexecution.testexecution_po_Defect_Link().click()
            assert "Link Defect is completed" in testexecution.testexecution_po_Linked_Defect_Msg().text
            testexecution.testexecution_po_Click_Close_Defect().click()
            CurrentURL = self.driver.current_url
            print(CurrentURL)
            wait1 = WebDriverWait(self.driver, 300)
            action.move_to_element(homepage.homepage_po_qTest_Component_Hover()).perform()
            wait.until(EC.presence_of_element_located((HomePage_PO.Pulse)))
            time.sleep(10)
            pulse = homepage.homepage_po_Pulse()
            windowsOpened = self.driver.window_handles
            self.driver.switch_to.window(windowsOpened[1])
            wait1.until(EC.presence_of_element_located((By.XPATH, "//a[text()='My Rules']")))
            pulse.pulse_po_ChooseProject_Arrow().click()
            self.driver.execute_script("arguments[0].click();", pulse.pulse_po_Choose_AT1_Project())
            # pulse.pulse_po_Choose_AKT_Project().click()
            self.driver.find_element(By.XPATH, "/html/body").send_keys(Keys.PAGE_DOWN)
            pulse.pulse_po_Action_Menu().click()
            wait.until(EC.element_to_be_clickable((Pulse_PO.Action_ViewLogs)))
            pulse.pulse_po_Action_ViewLogs().click()
            wait.until(EC.element_to_be_clickable((Pulse_PO.Execution_Refresh)))
            TestCaseID = CurrentURL.split("=")
            test = TestCaseID[3]
            test1 = test.split("&")
            ExtractedID = test1[0]
            print(ExtractedID)
            pulse.pulse_po_Execution_ID().click()
            time.sleep(2)
            Body = pulse.pulse_po_Execution_ID_Data().text
            pulse.pulse_po_Execution_ID_Close().click()
            data = json.loads(Body)
            print(data)
            event_type = data['event_type']
            testrun_id = data['defect']['testrun_id']
            print(event_type)
            print(testrun_id)
            for i in range(1, 10):
                if (int(ExtractedID) != int(testrun_id)) and (event_type != "defect_linked"):
                    print('loop')
                    time.sleep(20)
                    pulse.pulse_po_Execution_Refresh().click()
                    pulse.pulse_po_Execution_ID().click()
                    time.sleep(2)
                    Body = pulse.pulse_po_Execution_ID_Data().text
                    pulse.pulse_po_Execution_ID_Close().click()
                    data = json.loads(Body)
                    print(data)
                    event_type = data['event_type']
                    testrun_id = data['defect']['testrun_id']
                    print(event_type)
                    print(testrun_id)
                else:
                    break

            pulse.pulse_po_Execution_Refresh().click()
            assert "completed" == pulse.pulse_po_Execution_Status().text
            pulse.pulse_po_Execution_Close().click()
            self.driver.close()
            self.driver.switch_to.window(windowsOpened[0])
            #Unlink defect
            time.sleep(5)
            testexecution.testexecution_po_TestRun_Reload().click()
            self.driver.find_element(By.XPATH, "//span[normalize-space()='Execution History (1)']").click()
            self.driver.find_element(By.TAG_NAME, "html").send_keys(Keys.END)
            wait.until(EC.presence_of_element_located((By.XPATH, "//span[@title='Edit']")))
            action.move_to_element(testexecution.testexecution_po_Active_Bug()).perform()
            time.sleep(5)
            self.driver.execute_script("arguments[0].click();", testexecution.testexecution_po_Active_Bug())
            # testexecution.testexecution_po_Bug().click()
            wait.until(EC.presence_of_element_located((TestExecution_PO.New_Defect)))
            wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "TCMAAS-15685")))
            action.move_to_element(pulse.pulse_po_Defect_Unlink()).perform()
            self.driver.execute_script("arguments[0].click();", pulse.pulse_po_Defect_Unlink())
            wait.until(EC.invisibility_of_element((By.LINK_TEXT, "TCMAAS-15685")))
            testexecution.testexecution_po_Click_Close_Defect().click()
            time.sleep(5)
            CurrentURL = self.driver.current_url
            action.move_to_element(homepage.homepage_po_qTest_Component_Hover()).perform()
            wait.until(EC.presence_of_element_located((HomePage_PO.Pulse)))
            time.sleep(10)
            pulse = homepage.homepage_po_Pulse()
            windowsOpened = self.driver.window_handles
            self.driver.switch_to.window(windowsOpened[1])
            wait1.until(EC.presence_of_element_located((By.XPATH, "//a[text()='My Rules']")))
            pulse.pulse_po_ChooseProject_Arrow().click()
            self.driver.execute_script("arguments[0].click();", pulse.pulse_po_Choose_AT1_Project())
            # pulse.pulse_po_Choose_AKT_Project().click()
            self.driver.find_element(By.XPATH, "/html/body").send_keys(Keys.PAGE_DOWN)
            pulse.pulse_po_Action_Menu().click()
            wait.until(EC.element_to_be_clickable((Pulse_PO.Action_ViewLogs)))
            pulse.pulse_po_Action_ViewLogs().click()
            wait.until(EC.element_to_be_clickable((Pulse_PO.Execution_Refresh)))
            pulse.pulse_po_Execution_ID().click()
            time.sleep(2)
            Body = pulse.pulse_po_Execution_ID_Data().text
            pulse.pulse_po_Execution_ID_Close().click()
            data = json.loads(Body)
            print(data)
            event_type = data['event_type']
            testrun_id = data['defect']['testrun_id']
            print(event_type)
            print(testrun_id)
            for j in range(1, 10):
                print('for')
                if (int(ExtractedID) != int(testrun_id)) and (event_type != "defect_unlinked"):
                    print('loop')
                    time.sleep(20)
                    pulse.pulse_po_Execution_Refresh().click()
                    pulse.pulse_po_Execution_ID().click()
                    time.sleep(2)
                    Body = pulse.pulse_po_Execution_ID_Data().text
                    pulse.pulse_po_Execution_ID_Close().click()
                    data = json.loads(Body)
                    print(data)
                    event_type = data['event_type']
                    testrun_id = data['defect']['testrun_id']
                    print(event_type)
                    print(testrun_id)
                else:
                    break

            pulse.pulse_po_Execution_Refresh().click()
            assert "completed" == pulse.pulse_po_Execution_Status().text
            pulse.pulse_po_Execution_Close().click()
            self.driver.close()
            self.driver.switch_to.window(windowsOpened[0])
            self.Logout()

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Pulse_Link_Unlink_Defect', '5255151')
            test_run_id = self.get_TestRun(testSuiteID, 'Pulse_Link_Unlink_Defect')
            self.update_TestLog(test_run_id, '601', 'Passed', '#0cdda8')

        except Exception as e:

            # New Automatic update test results code
            # buildNumber, env_name = self.get_Jenkinsbuildnumber()
            # testSuiteID = self.getTestSuiteID(buildNumber, env_name)
            testSuiteID = getTSValue
            self.create_TestRun(testSuiteID, 'Pulse_Link_Unlink_Defect', '5255151')
            test_run_id = self.get_TestRun(testSuiteID, 'Pulse_Link_Unlink_Defect')
            self.update_TestLog(test_run_id, '602', 'Failed', '#ff4259')

            # cookies = self.get_cookies()
            self.TerminateSession(cookies)
            pytest.fail()




