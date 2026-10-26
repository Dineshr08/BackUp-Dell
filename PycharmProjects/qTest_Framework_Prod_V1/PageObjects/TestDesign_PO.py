from selenium.webdriver.common.by import By


class TestDesign_PO:

    Create_NewModule = (By.XPATH, "//span[@title='New Module']")
    Existing_ModuleName = (By.ID, "moduleHeader_editableContent")
    Update_NewModuleName = (By.XPATH, "//input[@id='moduleHeader_editableContentInput']")
    CreateNewTestCase = (By.ID, "tbtestdesignNewTestCase")
    ExistingTestCaseNameField = (By.XPATH, "//div/span[@title='Untitled']")
    Update_ExistingTestCaseNameField = (By.ID, "testCaseHeader_editableContentInput")
    Type = (By.XPATH,"//span[@title='Manual']")
    Attachment = (By.XPATH, "(//a[@id='testCaseTabView_tab_attachments'])")
    Upload = (By.XPATH, "//*[@class='browse-zone text-center']")
    # Upload = (By.XPATH, "//div[contains(text(),'Upload Files')]")
    Save = (By.ID, "testDesign_btnSaveAll")
    Approve = (By.ID, "testDesign_btnApprove")
    Choose_AutomationType = (By.XPATH, "//li[text()='Automation']")
    Validating_AttachmentTxt = (By.XPATH, "//span[@title='AT_Import.txt']")
    Approve_Yes = (By.XPATH, "//button[normalize-space()='Yes']")
    TDSub_Requirement = (By.XPATH, "(//a[@id='testCaseTabView_tab_requirements'])")
    TDSub_Requirement_AddBtn  = (By.XPATH, "//button[contains(text(),'Add')]")
    TDSub_AddRequirement_Requirement = (By.XPATH, "//a[@id='addRequirementTabView_tab_requirements']")
    TDSub_ChooseRequirement = (By.XPATH, "//a/span[text()='Link_Requirement']")
    TDSub_Requirement_ADD = (By.XPATH, "//div/button[@class='btn btn-default']")
    TDSub_Requirement_ADD_Verify = (By.XPATH, "(//a[@class='ng-star-inserted'])[2]")
    TD_Sub_SearchRequirement = (By.ID, "searchbox_contentInput")
    TD_Sub_ChooseAllCheckBox = (By.XPATH, "//th[@class='header-cell data-table-column-undefined ng-star-inserted']//i[@class='fa fa-square-o']")
    ImportExcel_Icon = (By.ID, "btnImportExcel")
    # ChooseFile_Hyperlink = (By.ID, "importTestcaseExcelUpload_attachmentLink")
    ChooseFile_Hyperlink = (By.XPATH, "//input[starts-with(@id,'qas_custom_FileInput_')]")
    ImportFile_Validation = (By.XPATH, "//*[text()='Import_TestCase.xls']")
    Import_Next = (By.XPATH, "//span[@id='inputImportTestCaseNext_label']")
    # Import_RequirementName_Source = (By.XPATH, "//ul/li[text()='Requirement Name']")
    # Import_Status_Source = (By.XPATH, "//ul/li[text()='Status']")
    # Import_RequirementName_Destination = (By.ID, "dijit__Widget_1")
    # Import_Status_Destination = (By.ID, "dijit__Widget_2")
    Import_Excel = (By.ID, "mappingImportTestCaseImport_label")
    ImportSuccess_PopUp = (By.ID, "successImportMessage")
    Import_OK = (By.ID, "successImportTestCaseOK_label")
    DataQuery = (By.ID, "btnTestCaseDataQueryButtonId")
    DataQuery_Clear = (By.ID, "testdesign_dataQueryClearBtn_label")
    DataQuery_QueryName = (By.ID, "testdesign_dataQueryName")
    DataQuery_Group = (By.ID, "testdesign_dataQueryGrid_cell_0_0")
    DataQuery_Criteria = (By.ID, "testdesign_dataQueryGrid_cell_0_1")
    DataQuery_Operator = (By.ID, "testdesign_dataQueryGrid_cell_0_2")
    DataQuery_Value = (By.ID, "testdesign_dataQueryGrid_cell_0_3")
    DataQuery_Value_New = (By.ID, "testdesign_2-77481ValueEditor")
    DataQuery_AddNewClause = (By.ID, "testdesign_dataQueryAddClauseBtn_label")
    DataQuery_Close = (By.ID, "testdesign_dataQueryCloseBtn_label")
    DataQuery_OutputCount = (By.XPATH, "//span[@class='grid-count-message']")
    DataQuery_RunQuery = (By.ID, "testdesign_dataQueryRunBtn_label")
    DataQuery_Criteria_Arrow = (By.XPATH, "//input[@class='dijitReset dijitInputField dijitArrowButtonInner']")
    DataQuery_Operator_Arrow = (By.XPATH, "//div[@class='dijitReset dijitArrowButtonInner']")
    DataQuery_Criteria_Status = (By.XPATH, "//div[@id='testdesign_dataQueryGrid_selectCriteria_popup']//div[text()='Status']")
    DataQuery_Criteria_Type = (By.XPATH, "//div[@id='testdesign_dataQueryGrid_selectCriteria_popup']//div[text()='Type']")
    DataQuery_Group_And = (By.XPATH, "//td[text()='and']")
    DataQuery_Operator_AllItemDropDown = (By.ID, "2--91OperatorData")
    DataQuery_Operator_EqualTo = (By.ID, "dijit_MenuItem_1_text")
    Open_Existing_BulkEdit_Folder = (By.XPATH, "//span[text()='AT_BulkEdit_TestCase']")
    RightClick_DataQuery = (By.XPATH, "//span[@title='Data Query'][normalize-space()='Data Query']")
    BulkEdit_AllCheckBox = (By.XPATH, "//span[@class='gridxIndirectSelectionCheckBox dijitReset dijitInline dijitCheckBox']")
    BulkEdit_Edit = (By.XPATH, "//span[text()='Edit']")
    BulkEdit_BulkEdit = (By.XPATH, "//td[text()='Batch Edit']")
    BulkEdit_Status = (By.ID, "indicator_statusIdBETestCase")
    BulkEdit_Status_EnterOption = (By.ID, "statusIdBETestCase")
    BulkEdit_Confirm = (By.ID, "testdesign_batchEditSubmitBtn_label")
    BulkEdit_Ok = (By.ID, "testdesign_successbatchedUpdateOK_label")
    Existing_TestCaseSharingFolder = (By.XPATH, "//span[text()='AT_TestCaseSharing']")
    TestCaseSharing_Properties = (By.XPATH, "//span[normalize-space()='Properties']")
    Choose_Shared_Yes = (By.XPATH, "//div[@class='checkbox d-flex']//input[@type='checkbox']")
    TestCaseSharing_Save = (By.ID, "properties_btnSaveAll")
    TestCaseSharing_Save_Confirmation = (By.XPATH, "//button[normalize-space()='Yes']")
    TestCaseSharing_Reload = (By.ID, "moduleHeader_btnReload")
    TestCaseSharing_IsShared = (By.ID,"testdesign_project_module_properties_SharedModuleField_Shared")
    Status_Arrow = (By.XPATH, "(//span[@class='select2-selection__arrow'])[1]")
    Status_Search = (By.XPATH, "//input[@role='searchbox']")
    Open_Existing_PulseTesting_Folder = (By.XPATH, "//span[text()='AT Pulse Testing']")
    Filter = (By.ID, "btnFilterTestcase")
    Set_Filter = (By.ID, "optionSetTestCaseFilter")
    Clear_Filter = (By.ID, "optionClearTestCasetFilter")
    Clear_Filter_Yes = (By.ID, "confirmDialogActionYes_label")
    Apply_Filter = (By.ID, "buttonFilterTestCase_label")
    Filter_Type = (By.ID, "typeTestCaseFilter")
    Reload = (By.ID, "testDesignRootHeader_btnReload")
    Choose_Manual_Type = (By.XPATH, "//div[@id='typeTestCaseFilter_popup0']")
    Export = (By.ID, "tbTestDesginExportReport")
    Export_TestDesign = (By.ID, "tbTestDesginExportExcel")
    Export_OK = (By.XPATH, "//div[@class='grid-view-field-operator']//span[starts-with(@id,'dijit_form_Button_')]")
    AT_CopyModule_Expand = (By.ID, "test-design-tree-expand-0-817934")
    AT_Copy_TestCase = (By.XPATH, "//div[@title='TC-162 AT_Copy_TestCase']//span[text()='AT_Copy_TestCase']")
    AT_CopyModule_HomeTemplate = (By.XPATH, "//div[@title='MD-28 AT_CopyTestCaseModule_Template']//span[text()='AT_CopyTestCaseModule_Template']")
    CopyTestCase_Validation = (By.XPATH, "//div[text()='Copied objects have been pushed to database queue successfully']")
    Copy = (By.XPATH, "//span[@title='Copy']")  # //span[@title='Copy']
    Paste = (By.XPATH, "//li[@id='contextMenuGrid-common.paste']")  #//span[@title='Paste']
    Existing_AT_CopyModuleFolder = (By.XPATH, "//div[@title='MD-27 AT_CopyTestCaseModule']//span[text()='AT_CopyTestCaseModule']")
    CopyTestCase_Validation = (By.XPATH, "//div[text()='Copied objects have been pushed to database queue successfully']")
    TestCaseTraceblity_Matrix_Report = (By.ID, "btnExportTraceMatrix")
    TestCaseandRequirement_Report = (By.ID, "btnExportTraceMatrixNew")
    Existing_LinkTestCase = (By.XPATH, "//span[text()='LinkTestCase']")
    DataQuery_Export_Xls = (By.ID, "testdesign_dataQueryExportBtn_label")
    DataQuery_Export_All = (By.ID, "testdesign_dataQueryExportAllBtn_label")

    def __init__(self, driver):
        self.driver = driver

    def testdesign_po_Create_NewModule(self):
        return self.driver.find_element(*TestDesign_PO.Create_NewModule)

    def testdesign_po_Existing_ModuleName(self):
        return self.driver.find_element(*TestDesign_PO.Existing_ModuleName)

    def testdesign_po_Update_NewModuleName(self):
        return self.driver.find_element(*TestDesign_PO.Update_NewModuleName)

    def testdesign_po_CreateNewTestCase(self):
        return self.driver.find_element(*TestDesign_PO.CreateNewTestCase)

    def testdesign_po_ExistingTestCaseNameField(self):
        return self.driver.find_element(*TestDesign_PO.ExistingTestCaseNameField)

    def testdesign_po_Update_ExistingTestCaseNameField(self):
        return self.driver.find_element(*TestDesign_PO.Update_ExistingTestCaseNameField)

    def testdesign_po_Type(self):
        return self.driver.find_element(*TestDesign_PO.Type)

    def testdesign_po_Attachment(self):
        return self.driver.find_element(*TestDesign_PO.Attachment)

    def testdesign_po_Upload(self):
        return self.driver.find_element(*TestDesign_PO.Upload)

    def testdesign_po_Save(self):
        return self.driver.find_element(*TestDesign_PO.Save)

    def testdesign_po_Approve(self):
        return self.driver.find_element(*TestDesign_PO.Approve)

    def testdesign_po_Choose_AutomationType(self):
        return self.driver.find_element(*TestDesign_PO.Choose_AutomationType)

    def testdesign_po_Validating_AttachmentTxt(self):
        return self.driver.find_element(*TestDesign_PO.Validating_AttachmentTxt)

    def testdesign_po_TDSub_Requirement(self):
        return self.driver.find_element(*TestDesign_PO.TDSub_Requirement)

    def testdesign_po_TDSub_Requirement_AddBtn(self):
        return self.driver.find_element(*TestDesign_PO.TDSub_Requirement_AddBtn)

    def testdesign_po_TDSub_AddRequirement_Requirement(self):
        return self.driver.find_element(*TestDesign_PO.TDSub_AddRequirement_Requirement)

    def testdesign_po_TDSub_ChooseRequirement(self):
        return self.driver.find_element(*TestDesign_PO.TDSub_ChooseRequirement)

    def testdesign_po_TDSub_Requirement_ADD(self):
        return self.driver.find_element(*TestDesign_PO.TDSub_Requirement_ADD)

    def testdesign_po_TDSub_Requirement_ADD_Verify(self):
        return self.driver.find_element(*TestDesign_PO.TDSub_Requirement_ADD_Verify)

    def testdesign_po_TD_Sub_SearchRequirement(self):
        return self.driver.find_element(*TestDesign_PO.TD_Sub_SearchRequirement)

    def testdesign_po_TD_Sub_ChooseAllCheckBox(self):
        return self.driver.find_element(*TestDesign_PO.TD_Sub_ChooseAllCheckBox)

    def testdesign_po_Approve_Yes(self):
        return self.driver.find_element(*TestDesign_PO.Approve_Yes)

    def testdesign_po_ImportExcel_Icon(self):
        return self.driver.find_element(*TestDesign_PO.ImportExcel_Icon)

    def testdesign_po_ChooseFile_Hyperlink(self):
        return self.driver.find_element(*TestDesign_PO.ChooseFile_Hyperlink)

    def testdesign_po_ImportFile_Validation(self):
        return self.driver.find_element(*TestDesign_PO.ImportFile_Validation)

    def testdesign_po_Import_Next(self):
        return self.driver.find_element(*TestDesign_PO.Import_Next)

    def testdesign_po_Import_Excel(self):
        return self.driver.find_element(*TestDesign_PO.Import_Excel)

    def testdesign_po_ImportSuccess_PopUp(self):
        return self.driver.find_element(*TestDesign_PO.ImportSuccess_PopUp)

    def testdesign_po_DataQuery_AddNewClause(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_AddNewClause)

    def testdesign_po_DataQuery(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery)

    def testdesign_po_DataQuery_Clear(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_Clear)

    def testdesign_po_DataQuery_QueryName(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_QueryName)

    def testdesign_po_DataQuery_Group(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_Group)

    def testdesign_po_DataQuery_Criteria(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_Criteria)

    def testdesign_po_DataQuery_Operator(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_Operator)

    def testdesign_po_DataQuery_Value(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_Value)

    def testdesign_po_DataQuery_Close(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_Close)

    def testdesign_po_DataQuery_OutputCount(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_OutputCount)

    def testdesign_po_DataQuery_RunQuery(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_RunQuery)

    def testdesign_po_DataQuery_Criteria_Status(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_Criteria_Status)

    def testdesign_po_DataQuery_Criteria_Type(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_Criteria_Type)

    def testdesign_po_DataQuery_Group_And(self):
        return self.driver.find_element(*TestDesign_PO.Import_OK)

    def testdesign_po_Import_OK(self):
        return self.driver.find_element(*TestDesign_PO.Import_OK)

    def testdesign_po_DataQuery_Criteria_Arrow(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_Criteria_Arrow)

    def testdesign_po_DataQuery_Operator_Arrow(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_Operator_Arrow)

    def testdesign_po_DataQuery_Operator_AllItemDropDown(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_Operator_AllItemDropDown)

    def testdesign_po_DataQuery_Operator_EqualTo(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_Operator_EqualTo)

    def testdesign_po_DataQuery_Value_New(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_Value_New)

    def testdesign_po_Open_Existing_BulkEdit_Folder(self):
        return self.driver.find_element(*TestDesign_PO.Open_Existing_BulkEdit_Folder)

    def testdesign_po_RightClick_DataQuery(self):
        return self.driver.find_element(*TestDesign_PO.RightClick_DataQuery)

    def testdesign_po_BulkEdit_AllCheckBox(self):
        return self.driver.find_element(*TestDesign_PO.BulkEdit_AllCheckBox)

    def testdesign_po_BulkEdit_Edit(self):
        return self.driver.find_element(*TestDesign_PO.BulkEdit_Edit)

    def testdesign_po_BulkEdit_BulkEdit(self):
        return self.driver.find_element(*TestDesign_PO.BulkEdit_BulkEdit)

    def testdesign_po_BulkEdit_Status(self):
        return self.driver.find_element(*TestDesign_PO.BulkEdit_Status)

    def testdesign_po_BulkEdit_Status_EnterOption(self):
        return self.driver.find_element(*TestDesign_PO.BulkEdit_Status_EnterOption)

    def testdesign_po_BulkEdit_Confirm(self):
        return self.driver.find_element(*TestDesign_PO.BulkEdit_Confirm)

    def testdesign_po_BulkEdit_Ok(self):
        return self.driver.find_element(*TestDesign_PO.BulkEdit_Ok)

    def testdesign_po_Existing_TestCaseSharingFolder(self):
        return self.driver.find_element(*TestDesign_PO.Existing_TestCaseSharingFolder)

    def testdesign_po_TestCaseSharing_Properties(self):
        return self.driver.find_element(*TestDesign_PO.TestCaseSharing_Properties)

    def testdesign_po_Choose_Shared_Yes(self):
        return self.driver.find_element(*TestDesign_PO.Choose_Shared_Yes)

    def testdesign_po_TestCaseSharing_Save(self):
        return self.driver.find_element(*TestDesign_PO.TestCaseSharing_Save)

    def testdesign_po_TestCaseSharing_Save_Confirmation(self):
        return self.driver.find_element(*TestDesign_PO.TestCaseSharing_Save_Confirmation)

    def testdesign_po_TestCaseSharing_Reload(self):
        return self.driver.find_element(*TestDesign_PO.TestCaseSharing_Reload)

    def testdesign_po_TestCaseSharing_IsShared(self):
        return self.driver.find_element(*TestDesign_PO.TestCaseSharing_IsShared)

    def testdesign_po_Status_Arrow(self):
        return self.driver.find_element(*TestDesign_PO.Status_Arrow)

    def testdesign_po_Status_Search(self):
        return self.driver.find_element(*TestDesign_PO.Status_Search)

    def testdesign_po_Open_Existing_PulseTesting_Folder(self):
        return self.driver.find_element(*TestDesign_PO.Open_Existing_PulseTesting_Folder)

    def testdesign_po_Filter(self):
        return self.driver.find_element(*TestDesign_PO.Filter)

    def testdesign_po_Set_Filter(self):
        return self.driver.find_element(*TestDesign_PO.Set_Filter)

    def testdesign_po_Clear_Filter(self):
        return self.driver.find_element(*TestDesign_PO.Clear_Filter)

    def testdesign_po_Apply_Filter(self):
        return self.driver.find_element(*TestDesign_PO.Apply_Filter)

    def testdesign_po_Filter_Type(self):
        return self.driver.find_element(*TestDesign_PO.Filter_Type)

    def testdesign_po_Reload(self):
        return self.driver.find_element(*TestDesign_PO.Reload)

    def testdesign_po_Clear_Filter_Yes(self):
        return self.driver.find_element(*TestDesign_PO.Clear_Filter_Yes)

    def testdesign_po_Choose_Manual_Type(self):
        return self.driver.find_element(*TestDesign_PO.Choose_Manual_Type)

    def testdesign_po_Export(self):
        return self.driver.find_element(*TestDesign_PO.Export)

    def testdesign_po_Export_TestDesign(self):
        return self.driver.find_element(*TestDesign_PO.Export_TestDesign)

    def testdesign_po_Export_OK(self):
        return self.driver.find_element(*TestDesign_PO.Export_OK)

    def testdesign_po_AT_CopyModule_Expand(self):
        return self.driver.find_element(*TestDesign_PO.AT_CopyModule_Expand)

    def testdesign_po_AT_Copy_TestCase(self):
        return self.driver.find_element(*TestDesign_PO.AT_Copy_TestCase)

    def testdesign_po_AT_CopyModule_HomeTemplate(self):
        return self.driver.find_element(*TestDesign_PO.AT_CopyModule_HomeTemplate)

    def testdesign_po_CopyTestCase_Validation(self):
        return self.driver.find_element(*TestDesign_PO.CopyTestCase_Validation)

    def testdesign_po_CopyTestCase_Validation(self):
        return self.driver.find_element(*TestDesign_PO.CopyTestCase_Validation)

    def testdesign_po_Copy(self):
        return self.driver.find_element(*TestDesign_PO.Copy)

    def testdesign_po_Paste(self):
        return self.driver.find_element(*TestDesign_PO.Paste)

    def testdesign_po_Existing_AT_CopyModuleFolder(self):
        return self.driver.find_element(*TestDesign_PO.Existing_AT_CopyModuleFolder)

    def testdesign_po_CopyTestCase_Validation(self):
        return self.driver.find_element(*TestDesign_PO.CopyTestCase_Validation)

    def testdesign_po_TestCaseTraceblity_Matrix_Report(self):
        return self.driver.find_element(*TestDesign_PO.TestCaseTraceblity_Matrix_Report)

    def testdesign_po_TestCaseandRequirement_Report(self):
        return self.driver.find_element(*TestDesign_PO.TestCaseandRequirement_Report)

    def testdesign_po_Existing_LinkTestCase(self):
        return self.driver.find_element(*TestDesign_PO.Existing_LinkTestCase)

    def testdesign_po_DataQuery_Export_Xls(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_Export_Xls)

    def testdesign_po_DataQuery_Export_All(self):
        return self.driver.find_element(*TestDesign_PO.DataQuery_Export_All)









