from selenium.webdriver.common.by import By


class Insights_PO:

    # Dashboard = (By.XPATH, "//a[text()='Dashboards ']")
    # Create_Dashboard = (By.XPATH, "//span[text()='Create Dashboard']")
    # Source_Image = (By.XPATH, "(//img[@src='rdDownload/rdThumb-71383cbc230746b580818da89841c67b.png'])[2]")
    # Destination_Place = (By.ID, "rdDashboardPanels")
    # Search_ExistingDashboard_Img = (By.XPATH, "(//table[@class='rdDashboardPanel']//input[@id='dgPanelSearch'])[2]")
    # Saved_Reports = (By.XPATH, "//a[text()='Saved Reports ']")
    # Saved_Report_Manage = (By.XPATH, "(//span[text()='Manage'])[2]")
    # Choose_AT_Report = (By.ID, "icon-caret_Row1")
    # Schedule = (By.XPATH, "//span[text()='  Schedule']")
    # Send_ReportNow = (By.XPATH, "//span[normalize-space()='Send Report Now']")
    # Run_Report = (By.XPATH, "//span[normalize-space()='Run Report']")
    # Run_Report_Validation = (By.XPATH, "//h1[@id='txtReportTitle']")
    # Schedule_StartTime = (By.ID, "scheduleStartTime")
    # Schedule_ActiveDay = (By.XPATH, "//td[@class='day active']")
    # Schedule_ActiveHour_PM = (By.XPATH, "//span[@class='hour active hour_pm']")
    # Schedule_ActiveHour_AM = (By.XPATH, "//span[@class='hour active hour_am']")
    # Schedule_Time = (By.XPATH, "//span[@class='minute']")
    # # Schedule_Time = (By.XPATH, "//span[@class='minute active']")
    # Schedule_Save = (By.ID, "saveScheduleBtn")
    # Schedule_LoadingMsg = (By.XPATH, "//span[@class='rdThemeWaitCaption']")
    # Schedule_SuccessMsg = (By.XPATH, "//div[@class='toast-message']")
    # SendReportNow_SuccessMsg = (By.XPATH, "//div[@class='toast-message']")
    # ExploreData = (By.XPATH, "//a[normalize-space()='Explore Data']")
    # ExploreData_TestCases = (By.XPATH, "//span[normalize-space()='Test Cases']")
    # ExploreData_TestRun = (By.XPATH, "//li[@id='listTestRuns']//span[contains(text(),'Test Runs')]")
    # ExploreData_CrossTab = (By.ID, "lblHeadingCrosstab")
    # ExploreData_TestCase_Runs_Validation = (By.ID, "lblHeadingTable")
    # Dashboard_Manage = (By.XPATH, "//span[text()='Manage']")
    # OpenATDashboard = (By.XPATH, "//span[@class='txtReportTitle ThemeTextNormal'][text()='AT Dashboard']")
    # OpenATDashboard_Validation = (By.XPATH, "//h1[text()='AT Dashboard']")

    Dashboard = (By.XPATH, "//a[text()='Dashboards ']")
    Create_Dashboard = (By.XPATH, "//span[text()='Create Dashboard']")
    Source_Image = (By.XPATH, "(//img[@src='rdDownload/rdThumb-71383cbc230746b580818da89841c67b.png'])[2]")
    Destination_Place = (By.ID, "rdDashboardPanels")
    Search_ExistingDashboard_Img = (By.XPATH, "(//table[@class='rdDashboardPanel']//input[@id='dgPanelSearch'])[2]")
    Saved_Reports = (By.XPATH, "//a[text()='Saved Reports ']")
    Saved_Report_Manage = (By.XPATH, "(//span[text()='Manage'])[2]")
    Choose_AT_Report = (By.XPATH, "//div[@id='PersonalReports']//i[@id='icon-caret_Row1']")
    Schedule = (By.XPATH, "//div[@id='PersonalReports']//span[text()='  Schedule']")
    Send_ReportNow = (By.XPATH, "//div[@id='PersonalReports']//span[normalize-space()='Send Report Now']")
    Run_Report = (By.XPATH, "//div[@id='PersonalReports']//span[normalize-space()='Run Report']")
    Run_Report_Validation = (By.XPATH, "//h1[@id='txtReportTitle']")
    Schedule_StartTime = (By.ID, "scheduleStartTime")
    Schedule_ActiveDay = (By.XPATH, "//td[@class='day active']")
    Schedule_ActiveHour_PM = (By.XPATH, "//span[@class='hour active hour_pm']")
    Schedule_ActiveHour_AM = (By.XPATH, "//span[@class='hour active hour_am']")
    Schedule_Time = (By.XPATH, "//span[@class='minute']")
    # Schedule_Time = (By.XPATH, "//span[@class='minute active']")
    Schedule_Save = (By.ID, "saveScheduleBtn")
    Schedule_LoadingMsg = (By.XPATH, "//span[@class='rdThemeWaitCaption']")
    Schedule_SuccessMsg = (By.XPATH, "//div[@class='toast-message']")
    SendReportNow_SuccessMsg = (By.XPATH, "//div[@class='toast-message']")
    ExploreData = (By.XPATH, "//a[normalize-space()='Explore Data']")
    ExploreData_TestCases = (By.XPATH, "//span[normalize-space()='Test Cases']")
    ExploreData_TestRun = (By.XPATH, "//li[@id='listTestRuns']//span[contains(text(),'Test Runs')]")
    ExploreData_CrossTab = (By.ID, "lblHeadingCrosstab")
    ExploreData_TestCase_Runs_Validation = (By.ID, "lblHeadingTable")
    Dashboard_Manage = (By.XPATH, "//span[text()='Manage']")
    OpenATDashboard = (By.XPATH, "//span[@id='divSharedOuter']//*[text()='AT Dashboard']")
    OpenATDashboard_Validation = (By.XPATH, "//h1[text()='AT Dashboard']")




    def __init__(self, driver):
        self.driver = driver

    def insights_po_Dashboard(self):
        return self.driver.find_element(*Insights_PO.Dashboard)

    def insights_po_Create_Dashboard(self):
        return self.driver.find_element(*Insights_PO.Create_Dashboard)

    def insights_po_Source_Image(self):
        return self.driver.find_element(*Insights_PO.Source_Image)

    def insights_po_Destination_Place(self):
        return self.driver.find_element(*Insights_PO.Destination_Place)

    def insights_po_Search_ExistingDashboard_Img(self):
        return self.driver.find_element(*Insights_PO.Search_ExistingDashboard_Img)

    def insights_po_Saved_Reports(self):
        return self.driver.find_element(*Insights_PO.Saved_Reports)

    def insights_po_Saved_Report_Manage(self):
        return self.driver.find_element(*Insights_PO.Saved_Report_Manage)

    def insights_po_Choose_AT_Report(self):
        return self.driver.find_element(*Insights_PO.Choose_AT_Report)

    def insights_po_Schedule(self):
        return self.driver.find_element(*Insights_PO.Schedule)

    def insights_po_Send_ReportNow(self):
        return self.driver.find_element(*Insights_PO.Send_ReportNow)

    def insights_po_Run_Report(self):
        return self.driver.find_element(*Insights_PO.Run_Report)

    def insights_po_Run_Report_Validation(self):
        return self.driver.find_element(*Insights_PO.Run_Report_Validation)

    def insights_po_Schedule_StartTime(self):
        return self.driver.find_element(*Insights_PO.Schedule_StartTime)

    def insights_po_Schedule_ActiveDay(self):
        return self.driver.find_element(*Insights_PO.Schedule_ActiveDay)

    def insights_po_Schedule_ActiveHour_PM(self):
        return self.driver.find_element(*Insights_PO.Schedule_ActiveHour_PM)

    def insights_po_Schedule_ActiveHour_AM(self):
        return self.driver.find_element(*Insights_PO.Schedule_ActiveHour_AM)

    def insights_po_Schedule_Time(self):
        return self.driver.find_element(*Insights_PO.Schedule_Time)

    def insights_po_Schedule_Save(self):
        return self.driver.find_element(*Insights_PO.Schedule_Save)

    def insights_po_Schedule_LoadingMsg(self):
        return self.driver.find_element(*Insights_PO.Schedule_LoadingMsg)

    def insights_po_Schedule_SuccessMsg(self):
        return self.driver.find_element(*Insights_PO.Schedule_SuccessMsg)

    def insights_po_SendReportNow_SuccessMsg(self):
        return self.driver.find_element(*Insights_PO.SendReportNow_SuccessMsg)

    def insights_po_ExploreData(self):
        return self.driver.find_element(*Insights_PO.ExploreData)

    def insights_po_ExploreData_TestCases(self):
        return self.driver.find_element(*Insights_PO.ExploreData_TestCases)

    def insights_po_ExploreData_TestRun(self):
        return self.driver.find_element(*Insights_PO.ExploreData_TestRun)

    def insights_po_ExploreData_CrossTab(self):
        return self.driver.find_element(*Insights_PO.ExploreData_CrossTab)

    def insights_po_ExploreData_TestCase_Runs_Validation(self):
        return self.driver.find_element(*Insights_PO.ExploreData_TestCase_Runs_Validation)

    def insights_po_Dashboard_Manage(self):
        return self.driver.find_element(*Insights_PO.Dashboard_Manage)

    def insights_po_OpenATDashboard(self):
        return self.driver.find_element(*Insights_PO.OpenATDashboard)

    def insights_po_OpenATDashboard_Validation(self):
        return self.driver.find_element(*Insights_PO.OpenATDashboard_Validation)






