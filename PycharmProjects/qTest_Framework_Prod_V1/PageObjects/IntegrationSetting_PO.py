from selenium.webdriver.common.by import By


class IntegrationSetting_PO:

    def __init__(self, driver):
        self.driver = driver

    Configure = (By.XPATH, "(//*[@title = 'Configure'])[1]")
    Configure_Gtie = (By.XPATH, "(//*[@title = 'Configure'])[2]")
    FetchJIraDefect = (By.ID, "fetchDefectBtn_label")
    FetchJIraDefect_OK = (By.ID, "successPopulateFieldOK_label")
    RetrieveJiraData = (By.ID, "PopulateAllIssueTypes_label")
    Retrieve_Jira_Count = (By.XPATH, "//b[@id='populatedDefectTypeTotal']")
    RetrieveJIraData_OK = (By.ID, "successPopulateFieldOK_label")
    Retrieve_Jira_RunningCount = (By.XPATH, "//b[@id='populatedDefectTypeCount']")
    Retrieve_Jira_SuccessMsg = (By.XPATH, "//div[@id='populateFieldSuccessfulMessage']")
    AddJiraConnection = (By.ID, "portalIntegrationSettingAddConnection_label")
    ConnectionName = (By.ID, "connectionInforName")
    ServerURL = (By.ID, "connectionInforServerURL")
    Connection_UserName = (By.ID, "connectionInforUsername")
    ConnectionPassword = (By.ID, "connectionInforPassword")
    TestJiraConnection = (By.ID, "addConnectionTest_label")
    Save_Configure = (By.ID, "addConnectionSave")
    ConnectionMsg = (By.ID, "connectionMessageSuccess")
    AddDefectType = (By.ID, "connectionConfigureAddType_label")
    AddDefectType_JiraProject = (By.ID, "connectionConfigureDefectProject")
    AddDefectType_Ok = (By.ID, "connectionConfigureAddTypeDialogOK_label")
    AddDefectType_Validation = (By.ID, "connectionConfiguredMappedType_cell_0_0")
    ReleaseRequirement_Activate = (By.ID, "requirementIntegrationSwitch_label")
    AddRequirementType = (By.ID, "connectionConfigureAddTypeRequirement_label")
    AddRequirementType_Validation = (By.ID, "connectionConfiguredMappedTypeRequirement_cell_0_0")
    ReleaseIntegration_Activate = (By.ID, "releaseIntegrationSwitch_label")
    AddReleaseType = (By.ID, "connectionConfigureAddTypeRelease_label")
    AddReleaseType_JiraProject = (By.ID, "connectionConfigureReleaseProject")
    AddReleaseType_Ok = (By.ID, "connectionConfigureAddReleaseDialogOK_label")
    AddReleaseType_Validation = (By.ID, "connectionConfiguredMappedTypeRelease_cell_0_0")
    Save_Activate = (By.ID, "connectionConfigureSaveClose_label")
    Refresh = (By.XPATH, "//span[text()='Refresh']")
    Confirmation_PopUP = (By.ID, "duplicatedJiraURLDialogOK_label")
    Release_Retrieve_JiraDefect = (By.ID, "populateAllReleaseType_label")
    RetrieveJiraData_Project1 = (By.XPATH, "//td[@id='connectionConfiguredMappedTypeRequirement_cell_0_3']//span[@title='Get the latest data to qTest requirements from this integrated Jira issue type only']")
    RetrieveJiraData_Project2 = (By.XPATH, "//td[@id='connectionConfiguredMappedTypeRequirement_cell_1_3']//span[@title='Get the latest data to qTest requirements from this integrated Jira issue type only']")
    JiraIssueFields = (By.XPATH, "//div[@class='connectionConfigureDialogContent']//div[@role='presentation']//div//td[1]")
    RetrieveJiraData_Project2_Configure = (By.XPATH, "//td[@id='connectionConfiguredMappedTypeRequirement_cell_1_3']//span[@class='dijitReset dijitInline dijitIcon qasymphonyGridToolbarIcon qasymphonyGridToolbarIconControl']")
    RefreshFieldSetting = (By.ID, "connectionConfigureAddMapping")
    JiraIssueFields_Cancel = (By.ID, "connectionConfigureMappingDialogCancel_label")
    Connection_CEC = (By.XPATH, "(//input[@name='connectionGrid'])[1]")
    Connection_Gtie = (By.XPATH, "(//input[@name='connectionGrid'])[2]")
    Integration_HomePage_Save = (By.ID, "portalIntegrationSettingSave_label")
    Connection_Refresh = (By.XPATH, "//span[text()='Refresh']")
    Save = (By.XPATH, "//span[@id='connectionConfigureSave_label']")
    Close = By.XPATH, "//span[@id='connectionConfigureClose_label']"





    def integrationsetting_po_Configure(self):
        return self.driver.find_element(*IntegrationSetting_PO.Configure)


    def integrationsetting_po_Configure_Gtie(self):
        return self.driver.find_element(*IntegrationSetting_PO.Configure_Gtie)

    def integrationsetting_po_FetchJIraDefect(self):
        return self.driver.find_element(*IntegrationSetting_PO.FetchJIraDefect)

    def integrationsetting_po_FetchJIraDefect_OK(self):
        return self.driver.find_element(*IntegrationSetting_PO.FetchJIraDefect_OK)

    def integrationsetting_po_Retrieve_Jira_Count(self):
        return self.driver.find_element(*IntegrationSetting_PO.Retrieve_Jira_Count)

    def integrationsetting_po_RetrieveJIraData_OK(self):
        return self.driver.find_element(*IntegrationSetting_PO.RetrieveJIraData_OK)

    def integrationsetting_po_Retrieve_Jira_RunningCount(self):
        return self.driver.find_element(*IntegrationSetting_PO.Retrieve_Jira_RunningCount)

    def integrationsetting_po_RetrieveJiraData(self):
        return self.driver.find_element(*IntegrationSetting_PO.RetrieveJiraData)

    def integrationsetting_po_Retrieve_Jira_SuccessMsg(self):
        return self.driver.find_element(*IntegrationSetting_PO.Retrieve_Jira_SuccessMsg)

    def integrationsetting_po_AddJiraConnection(self):
        return self.driver.find_element(*IntegrationSetting_PO.AddJiraConnection)

    def integrationsetting_po_ConnectionName(self):
        return self.driver.find_element(*IntegrationSetting_PO.ConnectionName)

    def integrationsetting_po_ServerURL(self):
        return self.driver.find_element(*IntegrationSetting_PO.ServerURL)

    def integrationsetting_po_Connection_UserName(self):
        return self.driver.find_element(*IntegrationSetting_PO.Connection_UserName)

    def integrationsetting_po_ConnectionPassword(self):
        return self.driver.find_element(*IntegrationSetting_PO.ConnectionPassword)

    def integrationsetting_po_TestJiraConnection(self):
        return self.driver.find_element(*IntegrationSetting_PO.TestJiraConnection)

    def integrationsetting_po_Save_Configure(self):
        return self.driver.find_element(*IntegrationSetting_PO.Save_Configure)

    def integrationsetting_po_ConnectionMsg(self):
        return self.driver.find_element(*IntegrationSetting_PO.ConnectionMsg)

    def integrationsetting_po_AddDefectType(self):
        return self.driver.find_element(*IntegrationSetting_PO.AddDefectType)

    def integrationsetting_po_AddDefectType_JiraProject(self):
        return self.driver.find_element(*IntegrationSetting_PO.AddDefectType_JiraProject)

    def integrationsetting_po_AddDefectType_Ok(self):
        return self.driver.find_element(*IntegrationSetting_PO.AddDefectType_Ok)

    def integrationsetting_po_AddDefectType_Validation(self):
        return self.driver.find_element(*IntegrationSetting_PO.AddDefectType_Validation)

    def integrationsetting_po_ReleaseRequirement_Activate(self):
        return self.driver.find_element(*IntegrationSetting_PO.ReleaseRequirement_Activate)

    def integrationsetting_po_AddRequirementType(self):
        return self.driver.find_element(*IntegrationSetting_PO.AddRequirementType)

    def integrationsetting_po_AddRequirementType_Validation(self):
        return self.driver.find_element(*IntegrationSetting_PO.AddRequirementType_Validation)

    def integrationsetting_po_ReleaseIntegration_Activate(self):
        return self.driver.find_element(*IntegrationSetting_PO.ReleaseIntegration_Activate)

    def integrationsetting_po_AddReleaseType(self):
        return self.driver.find_element(*IntegrationSetting_PO.AddReleaseType)

    def integrationsetting_po_AddReleaseType_JiraProject(self):
        return self.driver.find_element(*IntegrationSetting_PO.AddReleaseType_JiraProject)

    def integrationsetting_po_AddReleaseType_Ok(self):
        return self.driver.find_element(*IntegrationSetting_PO.AddReleaseType_Ok)

    def integrationsetting_po_AddReleaseType_Validation(self):
        return self.driver.find_element(*IntegrationSetting_PO.AddReleaseType_Validation)

    def integrationsetting_po_Save_Activate(self):
        return self.driver.find_element(*IntegrationSetting_PO.Save_Activate)

    def integrationsetting_po_Refresh(self):
        return self.driver.find_element(*IntegrationSetting_PO.Refresh)

    def integrationsetting_po_Confirmation_PopUP(self):
        return self.driver.find_element(*IntegrationSetting_PO.Confirmation_PopUP)

    def integrationsetting_po_Release_Retrieve_JiraDefect(self):
        return self.driver.find_element(*IntegrationSetting_PO.Release_Retrieve_JiraDefect)

    def integrationsetting_po_RetrieveJiraData_Project1(self):
        return self.driver.find_element(*IntegrationSetting_PO.RetrieveJiraData_Project1)

    def integrationsetting_po_RetrieveJiraData_Project2(self):
        return self.driver.find_element(*IntegrationSetting_PO.RetrieveJiraData_Project2)

    def integrationsetting_po_JiraIssueFields(self):
        return self.driver.find_elements(*IntegrationSetting_PO.JiraIssueFields)

    def integrationsetting_po_RetrieveJiraData_Project2_Configure(self):
        return self.driver.find_element(*IntegrationSetting_PO.RetrieveJiraData_Project2_Configure)

    def integrationsetting_po_RefreshFieldSetting(self):
        return self.driver.find_element(*IntegrationSetting_PO.RefreshFieldSetting)

    def integrationsetting_po_JiraIssueFields_Cancel(self):
        return self.driver.find_element(*IntegrationSetting_PO.JiraIssueFields_Cancel)

    def integrationsetting_po_Connection_CEC(self):
        return self.driver.find_element(*IntegrationSetting_PO.Connection_CEC)

    def integrationsetting_po_Connection_Gtie(self):
        return self.driver.find_element(*IntegrationSetting_PO.Connection_Gtie)

    def integrationsetting_po_Integration_HomePage_Save(self):
        return self.driver.find_element(*IntegrationSetting_PO.Integration_HomePage_Save)

    def integrationsetting_po_Connection_Refresh(self):
        return self.driver.find_element(*IntegrationSetting_PO.Connection_Refresh)

    def integrationsetting_po_Save(self):
        return self.driver.find_element(*IntegrationSetting_PO.Save)

    def integrationsetting_po_Close(self):
        return self.driver.find_element(*IntegrationSetting_PO.Close)





