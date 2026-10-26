from selenium.webdriver.common.by import By

from PageObjects.JiraCEC_PO import JiraCEC_PO


class TestExecution_PO:

    Get_AllReleaseID = (By.XPATH, "//*[@class='object-type-8']")
    Open_Existing_Release_Template = (By.XPATH, "//div[@id='test-execution-tree-6-531905-children']//div[@title='RL-3 AT_TestExecution_CreateTestSuiteTestCycle_Template']")
    New_TestCycle = (By.ID, "testExecution_NewTestCycle_Id")
    New_TestSuite = (By.ID, "testExecution_NewTestSuite_Id")
    Add_TestRuns = (By.ID, "testExecution_NewTestRun_Id")
    Add_TestRuns_TestCase = (By.ID, "addTestRunTabView_tab_testCases")
    Add_TestRuns_Search = (By.ID, "searchbox_contentInput")
    # Add_TestRuns_AllCheckBox = (By.XPATH, "//my-checkbox[@class='ng-star-inserted']")
    Add_TestRuns_AllCheckBox = (By.XPATH, "//th[@class='header-cell data-table-column-undefined ng-star-inserted']//i[@class='fa fa-square-o']")
    Add_TestRuns_Add = (By.XPATH, "//button[@class='btn btn-default btn-add']")
    Add_TestRuns_Close = (By.XPATH, "//button[@class='btn-close']")
    TestSuite_ChooseAllTestCase = (By.ID, "testRunGrid_selectThisPage")
    TestSuite_QuickRun = (By.ID, "testRunGrid_btnQuickRun")
    QuickRun_ChooseAllTestcase = (By.XPATH, "//span[@role='checkbox']")
    QuickRun_Status = (By.ID, "testSuiteQuickRunStatus_selectNode")
    QuickRun_Apply = (By.ID, "btnTestSuiteQuickRunApply_label")
    QuickRun_OkandRefresh = (By.ID, "testSuiteQuickRunSubmitAndRefresh_label")
    TestSuite_QuickRun_TestCase_UpdatedStatus = (By.XPATH, "//span[@class='grid-cell-status']")
    New_TestCycle_Name = (By.ID, "testCycleHeader_editableContentInput")
    New_TestSuite_Name = (By.ID, "testSuiteHeader_editableContentInput")
    Run_dropdown = (By.XPATH, "//button[@title='Select your default Test Execution Tool']")
    TestPad_Only = (By.XPATH, "//a[@title='TestPad only']")
    TestPad_Only_AllCheckBox = (By.ID, "testStepsGrid_selectThisPage")
    TestPad_Only_SetStatus_Select = (By.XPATH, "//span[@type='button']")
    TestPad_Only_SetStatus_Passed = (By.LINK_TEXT, "Passed")
    TestPad_Only_MarkSelectedSteps = (By.ID, "testpad_markStatus_btn")
    TestPad_Only_Save = (By.XPATH, "//button[@class='btn btn-default btn-short save']")
    OpenExisting_CopyTestCycle = (By.XPATH, "//div[@title='CL-6 AT_TestExecution_Copy_TestCycle']//span[text()='AT_TestExecution_Copy_TestCycle']")
    Copy = (By.XPATH, "//span[@title='Copy']")
    Paste = (By.XPATH, "//span[@title='Paste']")
    OpenExisting_CopyTestSuite = (By.XPATH, "//div[@title='TS-9 AT_TestExecution_Copy_TestSuite']//span[text()='AT_TestExecution_Copy_TestSuite']")
    Verify_CopiedCount = (By.XPATH, "//div[@class='tree-row removable']")
    Copy_Loading_PopUP = (By.XPATH, "//div[@class='font-weight-normal pb-1']")
    Open_Existing_Release_Template_collapse = (By.XPATH, "//*[@id='test-execution-tree-expand-8-16193']")
    DataQuery = (By.ID, "btnTestCaseExecutionQueryButtonId")
    DataQuery_Clear = (By.ID, "testrun_dataQueryClearBtn_label")
    DataQuery_QueryName = (By.ID, "testrun_dataQueryName")
    DataQuery_Criteria = (By.ID, "testrun_dataQueryGrid_cell_0_1")
    DataQuery_Operator = (By.ID, "testrun_dataQueryGrid_cell_0_2")
    DataQuery_Value = (By.ID, "testrun_dataQueryGrid_cell_0_3")
    DataQuery_Value_Passed = (By.ID, "testrun_25-ValueEditor_popup2")
    DataQuery_AddNewClause = (By.ID, "testrun_dataQueryAddClauseBtn_label")
    DataQuery_Close = (By.ID, "testrun_dataQueryCloseBtn_label")
    DataQuery_OutputCount = (By.XPATH, "//span[@class='grid-count-message']")
    DataQuery_RunQuery = (By.ID, "testrun_dataQueryRunBtn_label")
    DataQuery_Criteria_Arrow = (By.XPATH, "//input[@class='dijitReset dijitInputField dijitArrowButtonInner']")
    DataQuery_Operator_Arrow = (By.XPATH, "//div[@class='dijitReset dijitArrowButtonChar']")
    DataQuery_Criteria_Status = (By.XPATH, "//div[@id='testrun_dataQueryGrid_selectCriteria_popup']//div[text()='Status']")
    DataQuery_Operator_EqualTo = (By.ID, "dijit_MenuItem_11")
    Open_Existing_BulkEdit_Folder = (By.XPATH, "//span[text()='AT_BulkEdit_TestRun']")
    RightClick_DataQuery = (By.XPATH, "//span[@title='Data Query'][normalize-space()='Data Query']")
    BulkEdit_AllCheckBox = (By.XPATH, "//span[@class='gridxIndirectSelectionCheckBox dijitReset dijitInline dijitCheckBox']")
    BulkEdit_Edit = (By.XPATH, "//span[text()='Edit']")
    BulkEdit_BulkEdit = (By.XPATH, "//td[text()='Batch Edit']")
    BulkEdit_ExecutionType = (By.ID, "indicator_executionTypeBETestRun")
    BulkEdit_ExecutionType_EnterOption = (By.ID, "executionTypeBETestRun_selectNode")
    BulkEdit_Confirm = (By.ID, "testrun_batchEditSubmitBtn_label")
    BulkEdit_Ok = (By.ID, "testrun_successbatchedUpdateOK_label")
    Open_TestRun_ID = (By.CLASS_NAME, "grid-cell-pid")
    Bug = (By.XPATH, "//span[@class='bug-add ng-star-inserted']")
    Enter_Defect_ID = (By.ID, "defectModal_linkSearch_defectId_inp")
    Defect_Link = (By.ID, "defectModal_linkSearch_link_btn")
    Linked_Defect_Msg = (By.XPATH, "//div[@class='noti-message success-message ng-star-inserted']")
    New_Defect = (By.ID, "defectModal_new")
    New_Defect_Add = (By.XPATH, "//div[@class='modal-dialog modal-dialog-centered ui-draggable']//button[normalize-space()='Add']")
    Click_Close_Defect = (By.XPATH, "//span[@aria-hidden='true'][normalize-space()='×']")
    New_Defect_Add_Validation = (By.XPATH, "//td[@class='status'][text()='New']")
    TestCaseSharing_TestCase_ChooseProject = (By.XPATH, "//span[@class='selection']//span[@class='select2-selection__rendered'][@title='AutomationTesting']")
    TestCaseSharing_TestCase_Search = (By.XPATH, "//input[@class='select2-search__field']")
    TestCaseSharing_SelectSharingFolder = (By.XPATH, "//span[normalize-space()='AT_TestCaseSharing']")
    TestCaseSharing_TestCase_ChooseAllCheckBox = (By.ID, "addTestRunTestCaseModalGrid_selectThisPage")
    TestCaseSharingValidation = (By.ID, "testRunHeader_btnQuickRun")
    TestCaseSharing_Unshared_Validation = (By.XPATH, "//div[contains(text(),'You are not able to execute this Test Run since the associated Test Case is no longer shared to your project.')]")
    TestCycle_Suite_Copy_Validation = (By.XPATH, "//div[@class='header'][normalize-space()='Copied objects have been pushed to database queue successfully']")
    Statistics = (By.ID, "testSuiteTabView_tab_statistics")
    Jira_Click_Project = (By.ID, "project-field")
    Jira_Choose_Project = (By.XPATH, "//a[normalize-space()='TEST CASE MANAGEMENT (TCMaaS) (TCMAAS)']")
    Jira_Click_IssueType = (By.ID, "issuetype-field")
    Jira_Issue_Next = (By.ID, "issue-create-submit")
    Filter = (By.ID, "btnFilterTestExecution")
    Set_Filter = (By.ID, "setting-test-execution-filter")
    Clear_Filter = (By.ID, "clearning-test-execution-filter")
    Clear_Filter_Yes = (By.ID, "confirmDialogActionYes_label")
    Apply_Filter = (By.ID, "submitted-test-execution-filter-setting_label")
    # Filter_Type = (By.ID, "typeTestCaseFilter")
    Reload = (By.ID, "rootHeader_btnReload")
    Export = (By.ID, "btnExportExecution")
    Export_TestDesign = (By.ID, "tbTestExecutionExportExcel")
    Export_OK = (By.XPATH, "//div[@class='grid-view-field-operator']//span[starts-with(@id,'dijit_form_Button_')]")
    Existing_TestRun_TestSuiteFolder = (By.XPATH, "//div[@title='TS-63 AT_Copy_TestRun_TestSuit']//span[text()='AT_Copy_TestRun_TestSuit']")
    Existing_TestRun_TestSuiteFolder_Expand = (By.ID, "test-execution-tree-expand-2-734644")
    Existing_TestRun = (By.XPATH, "//div[@title='TR-239 AT_Copy_TestRun_TestRun']//span[text()='AT_Copy_TestRun_TestRun']")
    Existing_AT_TestRun_Validation = (By.XPATH, "//div[text()='Copied objects have been pushed to database queue successfully']")
    Export_Xls = (By.ID, "testrun_dataQueryExportBtn_label")
    Export_All = (By.ID, "testrun_dataQueryExportAllBtn_label")
    Export_TestExecution_Defect = (By.ID, "btnExportExeAndDefExcel")
    Export_TestExecution_Defect_NoCellMerging = (By.ID, "btnExportExeAndDefExcelNoMerge")
    Active_Bug = (By.XPATH, "//span[@class='bug-active ng-star-inserted']")
    TestRun_Reload = (By.ID, "testRunHeader_btnReload")



    def __init__(self, driver):
        self.driver = driver

    def testexecution_po_Get_AllReleaseID(self):
        return self.driver.find_elements(*TestExecution_PO.Get_AllReleaseID)

    def testexecution_po_Open_Existing_Release_Template(self):
        return self.driver.find_element(*TestExecution_PO.Open_Existing_Release_Template)

    def testexecution_po_New_TestCycle(self):
        return self.driver.find_element(*TestExecution_PO.New_TestCycle)

    def testexecution_po_New_TestSuite(self):
        return self.driver.find_element(*TestExecution_PO.New_TestSuite)

    def testexecution_po_Add_TestRuns(self):
        return self.driver.find_element(*TestExecution_PO.Add_TestRuns)

    def testexecution_po_Add_TestRuns_TestCase(self):
        return self.driver.find_element(*TestExecution_PO.Add_TestRuns_TestCase)

    def testexecution_po_Add_TestRuns_Search(self):
        return self.driver.find_element(*TestExecution_PO.Add_TestRuns_Search)

    def testexecution_po_Add_TestRuns_AllCheckBox(self):
        return self.driver.find_element(*TestExecution_PO.Add_TestRuns_AllCheckBox)

    def testexecution_po_Add_TestRuns_Add(self):
        return self.driver.find_element(*TestExecution_PO.Add_TestRuns_Add)

    def testexecution_po_Add_TestRuns_Close(self):
        return self.driver.find_element(*TestExecution_PO.Add_TestRuns_Close)

    def testexecution_po_TestSuite_ChooseAllTestCase(self):
        return self.driver.find_element(*TestExecution_PO.TestSuite_ChooseAllTestCase)

    def testexecution_po_TestSuite_QuickRun(self):
        return self.driver.find_element(*TestExecution_PO.TestSuite_QuickRun)

    def testexecution_po_QuickRun_ChooseAllTestcase(self):
        return self.driver.find_element(*TestExecution_PO.QuickRun_ChooseAllTestcase)

    def testexecution_po_QuickRun_Status(self):
        return self.driver.find_element(*TestExecution_PO.QuickRun_Status)

    def testexecution_po_QuickRun_Apply(self):
        return self.driver.find_element(*TestExecution_PO.QuickRun_Apply)

    def testexecution_po_QuickRun_OkandRefresh(self):
        return self.driver.find_element(*TestExecution_PO.QuickRun_OkandRefresh)

    def testexecution_po_TestSuite_QuickRun_TestCase_UpdatedStatus(self):
        return self.driver.find_element(*TestExecution_PO.TestSuite_QuickRun_TestCase_UpdatedStatus)

    def testexecution_po_New_TestCycle_Name(self):
        return self.driver.find_element(*TestExecution_PO.New_TestCycle_Name)

    def testexecution_po_New_TestSuite_Name(self):
        return self.driver.find_element(*TestExecution_PO.New_TestSuite_Name)

    def testexecution_po_Run_dropdown(self):
        return self.driver.find_element(*TestExecution_PO.Run_dropdown)

    def testexecution_po_TestPad_Only(self):
        return self.driver.find_element(*TestExecution_PO.TestPad_Only)

    def testexecution_po_TestPad_Only_AllCheckBox(self):
        return self.driver.find_element(*TestExecution_PO.TestPad_Only_AllCheckBox)

    def testexecution_po_TestPad_Only_SetStatus_Select(self):
        return self.driver.find_element(*TestExecution_PO.TestPad_Only_SetStatus_Select)

    def testexecution_po_TestPad_Only_SetStatus_Passed(self):
        return self.driver.find_element(*TestExecution_PO.TestPad_Only_SetStatus_Passed)

    def testexecution_po_TestPad_Only_MarkSelectedSteps(self):
        return self.driver.find_element(*TestExecution_PO.TestPad_Only_MarkSelectedSteps)

    def testexecution_po_TestPad_Only_Save(self):
        return self.driver.find_element(*TestExecution_PO.TestPad_Only_Save)

    def testexecution_po_OpenExisting_CopyTestCycle(self):
        return self.driver.find_element(*TestExecution_PO.OpenExisting_CopyTestCycle)

    def testexecution_po_Copy(self):
        return self.driver.find_element(*TestExecution_PO.Copy)

    def testexecution_po_Paste(self):
        return self.driver.find_element(*TestExecution_PO.Paste)

    def testexecution_po_OpenExisting_CopyTestSuite(self):
        return self.driver.find_element(*TestExecution_PO.OpenExisting_CopyTestSuite)

    def testexecution_po_Verify_CopiedCount(self):
        return self.driver.find_elements(*TestExecution_PO.Verify_CopiedCount)

    def testexecution_po_Copy_Loading_PopUP(self):
        return self.driver.find_element(*TestExecution_PO.Copy_Loading_PopUP)

    def testexecution_po_Open_Existing_Release_Template_collapse(self):
        return self.driver.find_element(*TestExecution_PO.Open_Existing_Release_Template_collapse)

    def testexecution_po_DataQuery(self):
        return self.driver.find_element(*TestExecution_PO.DataQuery)

    def testexecution_po_DataQuery_Clear(self):
        return self.driver.find_element(*TestExecution_PO.DataQuery_Clear)

    def testexecution_po_DataQuery_QueryName(self):
        return self.driver.find_element(*TestExecution_PO.DataQuery_QueryName)

    def testexecution_po_DataQuery_Criteria(self):
        return self.driver.find_element(*TestExecution_PO.DataQuery_Criteria)

    def testexecution_po_DataQuery_Operator(self):
        return self.driver.find_element(*TestExecution_PO.DataQuery_Operator)

    def testexecution_po_DataQuery_Value(self):
        return self.driver.find_element(*TestExecution_PO.DataQuery_Value)

    def testexecution_po_DataQuery_Value_Passed(self):
        return self.driver.find_element(*TestExecution_PO.DataQuery_Value_Passed)

    def testexecution_po_DataQuery_AddNewClause(self):
        return self.driver.find_element(*TestExecution_PO.DataQuery_AddNewClause)

    def testexecution_po_DataQuery_Close(self):
        return self.driver.find_element(*TestExecution_PO.DataQuery_Close)

    def testexecution_po_DataQuery_OutputCount(self):
        return self.driver.find_element(*TestExecution_PO.DataQuery_OutputCount)

    def testexecution_po_DataQuery_RunQuery(self):
        return self.driver.find_element(*TestExecution_PO.DataQuery_RunQuery)

    def testexecution_po_DataQuery_Criteria_Arrow(self):
        return self.driver.find_element(*TestExecution_PO.DataQuery_Criteria_Arrow)

    def testexecution_po_DataQuery_Operator_Arrow(self):
        return self.driver.find_element(*TestExecution_PO.DataQuery_Operator_Arrow)

    def testexecution_po_DataQuery_Criteria_Status(self):
        return self.driver.find_element(*TestExecution_PO.DataQuery_Criteria_Status)

    def testexecution_po_DataQuery_Operator_EqualTo(self):
        return self.driver.find_element(*TestExecution_PO.DataQuery_Operator_EqualTo)

    def testexecution_po_Open_Existing_BulkEdit_Folder(self):
        return self.driver.find_element(*TestExecution_PO.Open_Existing_BulkEdit_Folder)

    def testexecution_po_RightClick_DataQuery(self):
        return self.driver.find_element(*TestExecution_PO.RightClick_DataQuery)

    def testexecution_po_BulkEdit_AllCheckBox(self):
        return self.driver.find_element(*TestExecution_PO.BulkEdit_AllCheckBox)

    def testexecution_po_BulkEdit_Edit(self):
        return self.driver.find_element(*TestExecution_PO.BulkEdit_Edit)

    def testexecution_po_BulkEdit_BulkEdit(self):
        return self.driver.find_element(*TestExecution_PO.BulkEdit_BulkEdit)

    def testexecution_po_BulkEdit_ExecutionType(self):
        return self.driver.find_element(*TestExecution_PO.BulkEdit_ExecutionType)

    def testexecution_po_BulkEdit_ExecutionType_EnterOption(self):
        return self.driver.find_element(*TestExecution_PO.BulkEdit_ExecutionType_EnterOption)

    def testexecution_po_BulkEdit_Confirm(self):
        return self.driver.find_element(*TestExecution_PO.BulkEdit_Confirm)

    def testexecution_po_BulkEdit_Ok(self):
        return self.driver.find_element(*TestExecution_PO.BulkEdit_Ok)

    def testexecution_po_Open_TestRun_ID(self):
        return self.driver.find_element(*TestExecution_PO.Open_TestRun_ID)

    def testexecution_po_Bug(self):
        return self.driver.find_element(*TestExecution_PO.Bug)

    def testexecution_po_Enter_Defect_ID(self):
        return self.driver.find_element(*TestExecution_PO.Enter_Defect_ID)

    def testexecution_po_Defect_Link(self):
        return self.driver.find_element(*TestExecution_PO.Defect_Link)

    def testexecution_po_Linked_Defect_Msg(self):
        return self.driver.find_element(*TestExecution_PO.Linked_Defect_Msg)

    def testexecution_po_New_Defect(self):
        return self.driver.find_element(*TestExecution_PO.New_Defect)

    def testexecution_po_New_Defect_Add(self):
        # return self.driver.find_element(*TestExecution_PO.New_Defect_Add)
        self.driver.find_element(*TestExecution_PO.New_Defect_Add).click()
        jiracec = JiraCEC_PO(self.driver)
        return jiracec

    def testexecution_po_Click_Close_Defect(self):
        return self.driver.find_element(*TestExecution_PO.Click_Close_Defect)

    def testexecution_po_New_Defect_Add_Validation(self):
        return self.driver.find_element(*TestExecution_PO.New_Defect_Add_Validation)

    def testexecution_po_TestCaseSharing_TestCase_ChooseProject(self):
        return self.driver.find_element(*TestExecution_PO.TestCaseSharing_TestCase_ChooseProject)

    def testexecution_po_TestCaseSharing_TestCase_Search(self):
        return self.driver.find_element(*TestExecution_PO.TestCaseSharing_TestCase_Search)

    def testexecution_po_TestCaseSharing_SelectSharingFolder(self):
        return self.driver.find_element(*TestExecution_PO.TestCaseSharing_SelectSharingFolder)

    def testexecution_po_TestCaseSharing_TestCase_ChooseAllCheckBox(self):
        return self.driver.find_element(*TestExecution_PO.TestCaseSharing_TestCase_ChooseAllCheckBox)

    def testexecution_po_TestCaseSharingValidation(self):
        return self.driver.find_element(*TestExecution_PO.TestCaseSharingValidation)

    def testexecution_po_TestCaseSharing_Unshared_Validation(self):
        return self.driver.find_element(*TestExecution_PO.TestCaseSharing_Unshared_Validation)

    def testexecution_po_TestCycle_Suite_Copy_Validation(self):
        return self.driver.find_element(*TestExecution_PO.TestCycle_Suite_Copy_Validation)

    def testexecution_po_Statistics(self):
        return self.driver.find_element(*TestExecution_PO.Statistics)

    def testexecution_po_Jira_Click_Project(self):
        return self.driver.find_element(*TestExecution_PO.Jira_Click_Project)

    def testexecution_po_Jira_Choose_Project(self):
        return self.driver.find_element(*TestExecution_PO.Jira_Choose_Project)

    def testexecution_po_Jira_Click_IssueType(self):
        return self.driver.find_element(*TestExecution_PO.Jira_Click_IssueType)

    def testexecution_po_Jira_Issue_Next(self):
        return self.driver.find_element(*TestExecution_PO.Jira_Issue_Next)

    def testexecution_po_Filter(self):
        return self.driver.find_element(*TestExecution_PO.Filter)

    def testexecution_po_Set_Filter(self):
        return self.driver.find_element(*TestExecution_PO.Set_Filter)

    def testexecution_po_Clear_Filter(self):
        return self.driver.find_element(*TestExecution_PO.Clear_Filter)

    def testexecution_po_Clear_Filter_Yes(self):
        return self.driver.find_element(*TestExecution_PO.Clear_Filter_Yes)

    def testexecution_po_Apply_Filter(self):
        return self.driver.find_element(*TestExecution_PO.Apply_Filter)

    def testexecution_po_Reload(self):
        return self.driver.find_element(*TestExecution_PO.Reload)

    def testexecution_po_Export(self):
        return self.driver.find_element(*TestExecution_PO.Export)

    def testexecution_po_Export_TestDesign(self):
        return self.driver.find_element(*TestExecution_PO.Export_TestDesign)

    def testexecution_po_Export_OK(self):
        return self.driver.find_element(*TestExecution_PO.Export_OK)

    def testexecution_po_Existing_TestRun_TestSuiteFolder(self):
        return self.driver.find_element(*TestExecution_PO.Existing_TestRun_TestSuiteFolder)

    def testexecution_po_Existing_TestRun_TestSuiteFolder_Expand(self):
        return self.driver.find_element(*TestExecution_PO.Existing_TestRun_TestSuiteFolder_Expand)

    def testexecution_po_Existing_TestRun(self):
        return self.driver.find_element(*TestExecution_PO.Existing_TestRun)

    def testexecution_po_Existing_AT_TestRun_Validation(self):
        return self.driver.find_element(*TestExecution_PO.Existing_AT_TestRun_Validation)

    def testexecution_po_Export_Xls(self):
        return self.driver.find_element(*TestExecution_PO.Export_Xls)

    def testexecution_po_Export_All(self):
        return self.driver.find_element(*TestExecution_PO.Export_All)

    def testexecution_po_Export_TestExecution_Defect(self):
        return self.driver.find_element(*TestExecution_PO.Export_TestExecution_Defect)

    def testexecution_po_Export_TestExecution_Defect_NoCellMerging(self):
        return self.driver.find_element(*TestExecution_PO.Export_TestExecution_Defect_NoCellMerging)

    def testexecution_po_Active_Bug(self):
        return self.driver.find_element(*TestExecution_PO.Active_Bug)

    def testexecution_po_TestRun_Reload(self):
        return self.driver.find_element(*TestExecution_PO.TestRun_Reload)









