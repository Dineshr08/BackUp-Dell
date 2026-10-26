from selenium.webdriver.common.by import By


class Requirement_PO:

    New_Module = (By.ID,"btnNewModule")
    Update_New_Module_Name = (By.ID,"moduleHeader_editableContentInput")
    New_Requirement = (By.ID, "btnNewReq")
    Status = (By.ID,"statusRequirement_selectNode")
    Priority = (By.ID, "priorityRequirement_selectNode")
    Save = (By.ID, "saveBtnRequirement")
    Saved_Notification = (By.XPATH, "//div[contains(text(),'Changes were saved successfully.')]")
    Update_ExistingRequirementName = (By.XPATH, "//input[@id='dijit_form_TextBox_0']")
    AddBtn = (By.ID,"req-resource-select")
    ChooseModule_LinkTestCase = (By.XPATH,"(//a/span[text()='LinkTestCase'])[2]")
    ChooseModule_LinkTestCase_Expand = (By.ID, "requirement-testcase-tree-expand-0-779695")
    ChooseModule_LinkTestCase_SelectTestCase = (By.XPATH, "//a/span[text()='Link_TestCase']")
    Add_LinkTestCase = (By.ID, "req-resource-select_okButton_label")
    ImportExcel_Icon = (By.ID, "btnImportRequirementExcel")
    # ChooseFile_Hyperlink = (By.ID, "importExcelUploadRequirement_attachmentLink")//input[starts-with(@id,'qas_custom_FileInput_0')]
    ChooseFile_Hyperlink = (By.XPATH, "//input[starts-with(@id,'qas_custom_FileInput_')]")
    ImportFile_Validation = (By.XPATH, "//*[text()='Import.xls']")
    # Import_Next = (By.XPATH, "//span[@id='showImportDialogRequirement_label']")
    Import_Next = (By.XPATH, "//span[@id='showImportDialogRequirement']")
    Import_RequirementName_Source = (By.XPATH, "//ul/li[text()='Requirement Name']")
    Import_Status_Source = (By.XPATH, "//ul/li[text()='Status']")
    Import_RequirementName_Destination = (By.ID, "dijit__Widget_1")
    Import_Status_Destination = (By.ID, "dijit__Widget_2")
    Import_Excel = (By.ID, "mappingImportImportRequirement_label")
    ImportSuccess_PopUp = (By.ID, "successImportMessageRequirement")
    Import_OK = (By.ID, "successImportOKRequirement_label")
    ImportFromJira_Folder = (By.XPATH, "//span[text()='Imported from JIRA']")
    ImportFromJira_Folder_RequirementCount = (By.XPATH, "(//div[@class='info-content']//p[@class='value']//span[@class='number'])[1]")
    Status_Arrow = (By.XPATH, "(//input[contains(@value,'▼')])[1]")
    Status_InProgress = (By.XPATH, "//div[@id='statusRequirement_selectNode_popup1']")
    Existing_AT_CopyModule = (By.XPATH, "//div[@title='MD-25 AT CopyModule']//span[text()='AT CopyModule']")
    Existing_AT_CopyModule_Home_Template = (By.XPATH, "//span[text()='AT_CopyMoodule_Requirement_Template']")
    Existing_AT_CopyModule_Validation = (By.XPATH, "//div[text()='Copied objects have been pushed to database queue successfully']")
    Copy = (By.XPATH, "//span[@title='Copy']")  # //span[@title='Copy']
    Paste = (By.XPATH, "//span[@title='Paste']")
    Export = (By.ID, "tbReqExportExcel")
    Export_Requirement = (By.ID, "btnExportRequirement")
    Export_OK = (By.XPATH, "//div[@class='grid-view-field-operator']//span[starts-with(@id,'dijit_form_Button_')]")
    Reload = (By.ID, "requirementRootHeader_btnReload")
    Export_Req_TraceblityMatrixReport = (By.ID, "exportRequirementMatrix")  # exportRequirementMatrix
    Export_Req_TestCase_Report = (By.ID, "exportRequirementMatrixNew")
    Export_Req_TestExecution_Report = (By.ID, "exportReqAndTEResults")
    Export_Req_TestExecution_Report_NoCellMerge = (By.ID, "exportReqAndTEResultsNoMerge")
    Existing_Requirement = (By.XPATH, "//span[text()='AT_AutomationTesting']")
    RightClick_DataQuery = (By.XPATH, "//span[@title='Data Query'][normalize-space()='Data Query']")
    AllCheckBox = (By.XPATH, "//span[@class='gridxIndirectSelectionCheckBox dijitReset dijitInline dijitCheckBox']")
    DataQuery_ExportXls = (By.ID, "requirement_dataQueryExportBtn_label")
    DataQuery_ExportAll = (By.ID, "requirement_dataQueryExportAllBtn_label")



    def __init__(self, driver):
        self.driver = driver

    def requirement_po_New_Module(self):
        return self.driver.find_element(*Requirement_PO.New_Module)

    def requirement_po_Update_New_Module_Name(self):
        return self.driver.find_element(*Requirement_PO.Update_New_Module_Name)

    def requirement_po_New_Requirement(self):
        return self.driver.find_element(*Requirement_PO.New_Requirement)

    def requirement_po_Status(self):
        return self.driver.find_element(*Requirement_PO.Status)

    def requirement_po_Priority(self):
        return self.driver.find_element(*Requirement_PO.Priority)

    def requirement_po_Save(self):
        return self.driver.find_element(*Requirement_PO.Save)

    def requirement_po_Saved_Notification(self):
        return self.driver.find_element(*Requirement_PO.Saved_Notification)

    def requirement_po_Update_ExistingRequirementName(self):
        return self.driver.find_element(*Requirement_PO.Update_ExistingRequirementName)

    def requirement_po_AddBtn(self):
        return self.driver.find_element(*Requirement_PO.AddBtn)

    def requirement_po_ChooseModule_LinkTestCase(self):
        return self.driver.find_element(*Requirement_PO.ChooseModule_LinkTestCase)

    def requirement_po_ChooseModule_LinkTestCase_Expand(self):
        return self.driver.find_element(*Requirement_PO.ChooseModule_LinkTestCase_Expand)

    def requirement_po_Add_LinkTestCase(self):
        return self.driver.find_element(*Requirement_PO.Add_LinkTestCase)

    def requirement_po_ChooseModule_LinkTestCase_SelectTestCase(self):
        return self.driver.find_element(*Requirement_PO.ChooseModule_LinkTestCase_SelectTestCase)

    def requirement_po_ImportExcel_Icon(self):
        return self.driver.find_element(*Requirement_PO.ImportExcel_Icon)

    def requirement_po_ChooseFile_Hyperlink(self):
        return self.driver.find_element(*Requirement_PO.ChooseFile_Hyperlink)

    def requirement_po_ImportFile_Validation(self):
        return self.driver.find_element(*Requirement_PO.ImportFile_Validation)

    def requirement_po_Import_Next(self):
        return self.driver.find_element(*Requirement_PO.Import_Next)

    def requirement_po_Import_RequirementName_Source(self):
        return self.driver.find_element(*Requirement_PO.Import_RequirementName_Source)

    def requirement_po_Import_Status_Source(self):
        return self.driver.find_element(*Requirement_PO.Import_Status_Source)

    def requirement_po_Import_RequirementName_Destination(self):
        return self.driver.find_element(*Requirement_PO.Import_RequirementName_Destination)

    def requirement_po_Import_Status_Destination(self):
        return self.driver.find_element(*Requirement_PO.Import_Status_Destination)

    def requirement_po_Import_Excel(self):
        return self.driver.find_element(*Requirement_PO.Import_Excel)

    def requirement_po_ImportSuccess_PopUp(self):
        return self.driver.find_element(*Requirement_PO.ImportSuccess_PopUp)

    def requirement_po_Import_OK(self):
        return self.driver.find_element(*Requirement_PO.Import_OK)

    def requirement_po_ImportFromJira_Folder(self):
        return self.driver.find_element(*Requirement_PO.ImportFromJira_Folder)

    def requirement_po_ImportFromJira_Folder_RequirementCount(self):
        return self.driver.find_element(*Requirement_PO.ImportFromJira_Folder_RequirementCount)

    def requirement_po_Status_Arrow(self):
        return self.driver.find_element(*Requirement_PO.Status_Arrow)

    def requirement_po_Status_InProgress(self):
        return self.driver.find_element(*Requirement_PO.Status_InProgress)

    def requirement_po_Existing_AT_CopyModule(self):
        return self.driver.find_element(*Requirement_PO.Existing_AT_CopyModule)

    def requirement_po_Existing_AT_CopyModule_Validation(self):
        return self.driver.find_element(*Requirement_PO.Existing_AT_CopyModule_Validation)

    def requirement_po_Existing_AT_CopyModule_Home_Template(self):
        return self.driver.find_element(*Requirement_PO.Existing_AT_CopyModule_Home_Template)

    def requirement_po_Copy(self):
        return self.driver.find_element(*Requirement_PO.Copy)

    def requirement_po_Paste(self):
        return self.driver.find_element(*Requirement_PO.Paste)

    def requirement_po_Export_OK(self):
        return self.driver.find_element(*Requirement_PO.Export_OK)

    def requirement_po_Export(self):
        return self.driver.find_element(*Requirement_PO.Export)

    def requirement_po_Export_Requirement(self):
        return self.driver.find_element(*Requirement_PO.Export_Requirement)

    def requirement_po_Reload(self):
        return self.driver.find_element(*Requirement_PO.Reload)

    def requirement_po_Export_Req_TestCase_Report(self):
        return self.driver.find_element(*Requirement_PO.Export_Req_TestCase_Report)

    def requirement_po_Export_Req_TestExecution_Report(self):
        return self.driver.find_element(*Requirement_PO.Export_Req_TestExecution_Report)

    def requirement_po_Export_Req_TestExecution_Report_NoCellMerge(self):
        return self.driver.find_element(*Requirement_PO.Export_Req_TestExecution_Report_NoCellMerge)

    def requirement_po_Export_Req_TraceblityMatrixReport(self):
        return self.driver.find_element(*Requirement_PO.Export_Req_TraceblityMatrixReport)

    def requirement_po_Existing_Requirement(self):
        return self.driver.find_element(*Requirement_PO.Existing_Requirement)

    def requirement_po_RightClick_DataQuery(self):
        return self.driver.find_element(*Requirement_PO.RightClick_DataQuery)

    def requirement_po_AllCheckBox(self):
        return self.driver.find_element(*Requirement_PO.AllCheckBox)

    def requirement_po_DataQuery_ExportXls(self):
        return self.driver.find_element(*Requirement_PO.DataQuery_ExportXls)

    def requirement_po_DataQuery_ExportAll(self):
        return self.driver.find_element(*Requirement_PO.DataQuery_ExportAll)



