from selenium.webdriver.common.by import By

from PageObjects.Administration_PO import Administration_PO
from PageObjects.Arrow_PO import Arrow_PO
from PageObjects.Explore_Session_PO import Explore_Session_PO
from PageObjects.FieldSetting_PO import FieldSetting_PO
from PageObjects.Insights_PO import Insights_PO
from PageObjects.IntegrationSetting_PO import IntegrationSetting_PO
from PageObjects.Launch_PO import Launch_PO
from PageObjects.Pulse_PO import Pulse_PO
from PageObjects.Requirement_PO import Requirement_PO
from PageObjects.TestDesign_PO import TestDesign_PO
from PageObjects.TestExecution_PO import TestExecution_PO
from PageObjects.TestPlan_PO import TestPlan_PO


class HomePage_PO:

    hoverProjectMenu = (By.ID, "topLeftTitle")
    searchProject = (By.XPATH, "//input[@id='searchProjectInput']")
    chooseATProject = (By.LINK_TEXT,"AutomationTesting")
    chooseAKTTestProject = (By.LINK_TEXT, "AKT-Test")
    AKTTestProject_landingPage_Validation = (By.XPATH, "//span[@title='AKT-Test']")
    ATProject_landingPage_Validation = (By.XPATH,"//span[@title='AutomationTesting']")
    chooseAT1Project = (By.LINK_TEXT, "AutomationTesting1")
    AT1Project_landingPage_Validation = (By.XPATH, "//span[@title='AutomationTesting1']")
    testplan = (By.XPATH,"//span[text()='Test Plan']")
    testexecution = (By.XPATH, "//span[text()='Test Execution']")
    requirement = (By.XPATH, "//span[text()='Requirements']")
    testdesign = (By.XPATH, "//span[text()='Test Design']")
    Admin = (By.ID, "userAvatarMenuAdminSetting")
    User_Menu = (By.CLASS_NAME, "show-user-menu")
    qTest_Component_Hover = (By.XPATH, "//div[@class='ninebox-icon dropbtn']")
    qTest_Manager = (By.XPATH, "(//div[text()='Manager'])[2]")
    Global_Setting = (By.ID, "gb_setting")
    Global_Setting_Field_Setting = (By.XPATH, "//td[text()='Field Settings']")
    Insights = (By.XPATH, "//div[text()='Insights']")
    Global_Setting_Integration_Setting = (By.XPATH, "//td[text()='Integration Settings']")
    Explore_Session = (By.XPATH, "//div[@class='svg-icon icon-explorer <br />+ sessions']")
    Launch = (By.XPATH, "//div[text()='Launch']")
    Pulse = (By.XPATH, "//div[text()='Pulse']")
    Global_Search = (By.ID, "globalSearchButton")
    Global_Search_TextBox = (By.ID, "globalSearchTextbox")
    Global_Search_TextBox_Output = (By.XPATH, "//div[@class='searchedItemName']")
    Arrow = (By.ID, "resources-button")
    chooseAT2Project = (By.LINK_TEXT, "AutomationTesting2")
    AT2Project_landingPage_Validation = (By.XPATH, "//span[@title='AutomationTesting2']")


    def __init__(self, driver):
        self.driver = driver

    def homepage_po_hoverProjectMenu(self):
        return self.driver.find_element(*HomePage_PO.hoverProjectMenu)

    def homepage_po_searchProject(self):
        return self.driver.find_element(*HomePage_PO.searchProject)

    def homepage_po_chooseATProject(self):
        return self.driver.find_element(*HomePage_PO.chooseATProject)

    def homepage_po_ATProject_landingPage_Validation(self):
        return self.driver.find_element(*HomePage_PO.ATProject_landingPage_Validation)

    def homepage_po_chooseAT1Project(self):
        return self.driver.find_element(*HomePage_PO.chooseAT1Project)

    def homepage_po_AT1Project_landingPage_Validation(self):
        return self.driver.find_element(*HomePage_PO.AT1Project_landingPage_Validation)

    def homepage_po_chooseAT2Project(self):
        return self.driver.find_element(*HomePage_PO.chooseAT2Project)

    def homepage_po_AT2Project_landingPage_Validation(self):
        return self.driver.find_element(*HomePage_PO.AT2Project_landingPage_Validation)


    def homepage_po_testplan(self):
        self.driver.find_element(*HomePage_PO.testplan).click()
        testplan = TestPlan_PO(self.driver)
        return testplan

    def homepage_po_testexecution(self):
        self.driver.find_element(*HomePage_PO.testexecution).click()
        testexecution = TestExecution_PO(self.driver)
        return testexecution

    def homepage_po_requirement(self):
        self.driver.find_element(*HomePage_PO.requirement).click()
        requirement = Requirement_PO(self.driver)
        return requirement

    def homepage_po_testdesign(self):
        self.driver.find_element(*HomePage_PO.testdesign).click()
        testdesign = TestDesign_PO(self.driver)
        return testdesign

    def homepage_po_Admin(self):
        self.driver.find_element(*HomePage_PO.Admin).click()
        admin = Administration_PO(self.driver)
        return admin


    def homepage_po_User_Menu(self):
        return self.driver.find_element(*HomePage_PO.User_Menu)

    def homepage_po_qTest_Component_Hover(self):
        return self.driver.find_element(*HomePage_PO.qTest_Component_Hover)

    def homepage_po_qTest_Manager(self):
        return self.driver.find_element(*HomePage_PO.qTest_Manager)

    def homepage_po_Global_Setting(self):
        return self.driver.find_element(*HomePage_PO.Global_Setting)

    def homepage_po_Global_Setting_Field_Setting(self):
        self.driver.find_element(*HomePage_PO.Global_Setting_Field_Setting).click()
        field = FieldSetting_PO(self.driver)
        return field

    def homepage_po_Insights(self):
        self.driver.find_element(*HomePage_PO.Insights).click()
        insights = Insights_PO(self.driver)
        return insights

    def homepage_po_Global_Setting_Integration_Setting(self):
        self.driver.find_element(*HomePage_PO.Global_Setting_Integration_Setting).click()
        integration = IntegrationSetting_PO(self.driver)
        return integration

    def homepage_po_Explore_Session(self):
        self.driver.find_element(*HomePage_PO.Explore_Session).click()
        explore_session = Explore_Session_PO(self.driver)
        return explore_session

    def homepage_po_Launch(self):
        self.driver.find_element(*HomePage_PO.Launch).click()
        launch = Launch_PO(self.driver)
        return launch

    def homepage_po_Pulse(self):
        self.driver.find_element(*HomePage_PO.Pulse).click()
        pulse = Pulse_PO(self.driver)
        return pulse

    def homepage_po_chooseAKTTestProject(self):
        return self.driver.find_element(*HomePage_PO.chooseAKTTestProject)

    def homepage_po_AKTTestProject_landingPage_Validation(self):
        return self.driver.find_element(*HomePage_PO.AKTTestProject_landingPage_Validation)

    def homepage_po_Global_Search(self):
        return self.driver.find_element(*HomePage_PO.Global_Search)

    def homepage_po_Global_Search_TextBox(self):
        return self.driver.find_element(*HomePage_PO.Global_Search_TextBox)

    def homepage_po_Global_Search_TextBox_Output(self):
        return self.driver.find_element(*HomePage_PO.Global_Search_TextBox_Output)

    def homepage_po_Arrow(self):
        self.driver.find_element(*HomePage_PO.Arrow).click()
        arrow = Arrow_PO(self.driver)
        return arrow
