from selenium.webdriver.common.by import By

from PageObjects.Authentication_PO import Authentication_PO
from PageObjects.Configuration_PO import Configuration_PO
from PageObjects.Security_PO import Security_PO


class Administration_PO:

    FindUser = (By.XPATH, "//input[@placeholder='Email or First, Last name']")
    Action = (By.XPATH, "//td[@id='userListGrid_none_13300_actions']//i[@class='action-icon fa fa-bars action-icon-enabled']")
    Edit_Project_and_Profile = (By.XPATH, "//span[text()='Edit Projects and Profiles']")
    Click_User_Profile = (
    By.XPATH, "//grid-cell-editable-dropdown[@class='grid-cell-editable-dropdown grid-cell-content ng-star-inserted']")
    Current_UserProfile = (By.XPATH, "//div[@class='pointer-cursor mask-text ng-star-inserted']")
    UserProfile_Save = (By.XPATH, "//button[normalize-space()='Save']")
    UserProfile_Developer = (By.XPATH, "//li[text()='Developer']")
    UserProfile_Project_Admin = (By.XPATH, "//li[text()='Project Admin']")
    Groups = (By.ID, "userGroup-control")
    AddGroups = (By.ID, "userGroupsCustomGrid_addGroup")
    Group_GroupName = (By.NAME, "groupName")
    Group_Permission_InightViewer = (By.ID, "ROLE_INSIGHTSVIEWER")
    Group_Permission_InightEditor = (By.ID, "ROLE_INSIGHTSEDITOR")
    Groups_Users = (By.ID, "configureGroupTabView_tab_users")
    Groups_Users_Search  = (By.XPATH, "//input[@placeholder='Find new users by name or email']")
    Groups_Users_SelectAllCheckBox = (By.ID, "selectedUsers_selectThisPage")
    Group_User_Add = (By.XPATH, "//div[@class='col-2 add-remove-button btn-vertical-column']//i[@class='fa fa-caret-right']")
    Group_Save = (By.XPATH, "//button[text()='Save']")
    Group_Creation_Validation = (By.XPATH, "//div[text()='The User Group was created successfully']")
    Find_Group = (By.XPATH, "//input[@placeholder='Find Group']")
    Group_Custom_Group_Action = (By.XPATH, "//i[@class='action-icon fa fa-bars action-icon-enabled']")
    Group_Delete = (By.XPATH, "//span[text()='Delete']")
    Group_Delete_Yes = (By.XPATH, "//button[@class='btn btn-default btn-ok']")
    Group_Deletion_Validation = (By.XPATH, "//div[text()='The User Group was deleted']")
    Projects = (By.XPATH, "//span[text()='Projects']")
    Add_New_Project = (By.XPATH, "//span[text()='Add new project']")
    Project_Project_Name = (By.ID, "projName")
    Project_Template = (By.ID, "siteTemplates")
    Project_Add = (By.ID, "addProjectAction_label")
    Project_OK = (By.ID, "projSuccessfulMsgOK")
    Project_SearchName = (By.XPATH, "//div[@id='project_list_grid_filter_1']//input[@type='text']")
    Project_Delete = (By.XPATH, "//a[@title='Delete']")
    Project_Delete_Yes = (By.ID, "removeProjectConfirmationOK_label")
    SiteField = (By.XPATH, "//span[@class='tab-text'][normalize-space()='Site Fields']")
    SiteField_Manage_SiteField = (By.XPATH, "//button[normalize-space()='Manage Site Fields']")
    SiteField_TestCase = (By.XPATH, "//span[@class='icon qasymphonyTreeIcon qasymphonyTreeIconTestCase']")
    SiteField_Add_CustomField = (By.XPATH, "//button[normalize-space()='Add Custom Field']")
    SiteField_DisplayName = (By.NAME, "displayName")
    SiteField_FieldTypeSelection = (By.NAME, "selectedType")
    SiteField_OK = (By.XPATH, "//button[normalize-space()='OK']")
    SiteField_OK1 = (By.XPATH, "//div[@class='modal-content animated zoomIn']//button[normalize-space()='OK']")
    SiteField_Created_Validation = (By.XPATH, "//div[contains(text(),'Saved successfully')]")
    SiteField_AddValue = (By.LINK_TEXT, "+ Add Value")
    SiteField_AddValue_Input = (By.XPATH, "//input[@class='form-control value-name-inp']")
    SiteField_ComboBox_OK = (By.XPATH, "//div[@class='modal-footer']//button[normalize-space()='OK']")
    Authentication = (By.ID, "authenIntegrationTab-control")
    Configuration = (By.ID, "system-configurations-control")
    Security = (By.ID, "security-control")
    ConfigurationFieldSetting = (By.ID, "configuration-control")
    CloneProject = (By.ID, "cloneProjectBtn_label")
    SourceProject = (By.ID, "sourceProject")
    UserManagmentSetting = (By.ID, "userManagementSettings")
    TestPlanStructure = (By.ID, "testPlanStructure")
    Clone = (By.ID, "addProjectAction_label")
    Clone_Confirmation_Yes = (By.ID, "confirmSaveDialogActionSave_label")
    Clone_Success = (By.ID, "projSuccessfulMsgOK_label")




    def __init__(self, driver):
        self.driver = driver


    def admin_po_FindUser(self):
        return self.driver.find_element(*Administration_PO.FindUser)

    def admin_po_Action(self):
        return self.driver.find_element(*Administration_PO.Action)

    def admin_po_Edit_Project_and_Profile(self):
        return self.driver.find_element(*Administration_PO.Edit_Project_and_Profile)

    def admin_po_Click_User_Profile(self):
        return self.driver.find_element(*Administration_PO.Click_User_Profile)

    def admin_po_Current_UserProfile(self):
        return self.driver.find_element(*Administration_PO.Current_UserProfile)

    def admin_po_UserProfile_Save(self):
        return self.driver.find_element(*Administration_PO.UserProfile_Save)

    def admin_po_UserProfile_Developer(self):
        return self.driver.find_element(*Administration_PO.UserProfile_Developer)

    def admin_po_UserProfile_Project_Admin(self):
        return self.driver.find_element(*Administration_PO.UserProfile_Project_Admin)

    def admin_po_Groups(self):
        return self.driver.find_element(*Administration_PO.Groups)

    def admin_po_AddGroups(self):
        return self.driver.find_element(*Administration_PO.AddGroups)

    def admin_po_Group_GroupName(self):
        return self.driver.find_element(*Administration_PO.Group_GroupName)

    def admin_po_Group_Permission_InightViewer(self):
        return self.driver.find_element(*Administration_PO.Group_Permission_InightViewer)

    def admin_po_Group_Permission_InightEditor(self):
        return self.driver.find_element(*Administration_PO.Group_Permission_InightEditor)

    def admin_po_Groups_Users(self):
        return self.driver.find_element(*Administration_PO.Groups_Users)

    def admin_po_Groups_Users_Search(self):
        return self.driver.find_element(*Administration_PO.Groups_Users_Search)

    def admin_po_Groups_Users_SelectAllCheckBox(self):
        return self.driver.find_element(*Administration_PO.Groups_Users_SelectAllCheckBox)

    def admin_po_Group_User_Add(self):
        return self.driver.find_element(*Administration_PO.Group_User_Add)

    def admin_po_Group_Save(self):
        return self.driver.find_element(*Administration_PO.Group_Save)

    def admin_po_Group_Creation_Validation(self):
        return self.driver.find_element(*Administration_PO.Group_Creation_Validation)

    def admin_po_Find_Group(self):
        return self.driver.find_element(*Administration_PO.Find_Group)

    def admin_po_Group_Custom_Group_Action(self):
        return self.driver.find_element(*Administration_PO.Group_Custom_Group_Action)

    def admin_po_Group_Delete(self):
        return self.driver.find_element(*Administration_PO.Group_Delete)

    def admin_po_Group_Delete_Yes(self):
        return self.driver.find_element(*Administration_PO.Group_Delete_Yes)

    def admin_po_Group_Deletion_Validation(self):
        return self.driver.find_element(*Administration_PO.Group_Deletion_Validation)

    def admin_po_Projects(self):
        return self.driver.find_element(*Administration_PO.Projects)

    def admin_po_Add_New_Project(self):
        return self.driver.find_element(*Administration_PO.Add_New_Project)

    def admin_po_Project_Project_Name(self):
        return self.driver.find_element(*Administration_PO.Project_Project_Name)

    def admin_po_Project_Template(self):
        return self.driver.find_element(*Administration_PO.Project_Template)

    def admin_po_Project_Add(self):
        return self.driver.find_element(*Administration_PO.Project_Add)

    def admin_po_Project_OK(self):
        return self.driver.find_element(*Administration_PO.Project_OK)

    def admin_po_Project_SearchName(self):
        return self.driver.find_element(*Administration_PO.Project_SearchName)

    def admin_po_Project_Delete(self):
        return self.driver.find_element(*Administration_PO.Project_Delete)

    def admin_po_Project_Delete_Yes(self):
        return self.driver.find_element(*Administration_PO.Project_Delete_Yes)

    def admin_po_SiteField(self):
        return self.driver.find_element(*Administration_PO.SiteField)

    def admin_po_SiteField_Manage_SiteField(self):
        return self.driver.find_element(*Administration_PO.SiteField_Manage_SiteField)

    def admin_po_SiteField_TestCase(self):
        return self.driver.find_element(*Administration_PO.SiteField_TestCase)

    def admin_po_SiteField_Add_CustomField(self):
        return self.driver.find_element(*Administration_PO.SiteField_Add_CustomField)

    def admin_po_SiteField_DisplayName(self):
        return self.driver.find_element(*Administration_PO.SiteField_DisplayName)

    def admin_po_SiteField_FieldTypeSelection(self):
        return self.driver.find_element(*Administration_PO.SiteField_FieldTypeSelection)

    def admin_po_SiteField_OK(self):
        return self.driver.find_element(*Administration_PO.SiteField_OK)

    def admin_po_SiteField_OK1(self):
        return self.driver.find_element(*Administration_PO.SiteField_OK1)

    def admin_po_SiteField_Created_Validation(self):
        return self.driver.find_element(*Administration_PO.SiteField_Created_Validation)

    def admin_po_SiteField_AddValue(self):
        return self.driver.find_element(*Administration_PO.SiteField_AddValue)

    def admin_po_SiteField_AddValue_Input(self):
        return self.driver.find_element(*Administration_PO.SiteField_AddValue_Input)

    def admin_po_SiteField_ComboBox_OK(self):
        return self.driver.find_element(*Administration_PO.SiteField_ComboBox_OK)

    def admin_po_Authentication(self):
        self.driver.find_element(*Administration_PO.Authentication).click()
        authentication = Authentication_PO(self.driver)
        return authentication

    def admin_po_Configuration(self):
        self.driver.find_element(*Administration_PO.Configuration).click()
        configuration = Configuration_PO(self.driver)
        return configuration

    def admin_po_Security(self):
        self.driver.find_element(*Administration_PO.Security).click()
        security = Security_PO(self.driver)
        return security

    def admin_po_ConfigurationFieldSetting(self):
        return self.driver.find_element(*Administration_PO.ConfigurationFieldSetting)

    def admin_po_CloneProject(self):
        return self.driver.find_element(*Administration_PO.CloneProject)

    def admin_po_SourceProject(self):
        return self.driver.find_element(*Administration_PO.SourceProject)

    def admin_po_UserManagmentSetting(self):
        return self.driver.find_element(*Administration_PO.UserManagmentSetting)

    def admin_po_TestPlanStructure(self):
        return self.driver.find_element(*Administration_PO.TestPlanStructure)

    def admin_po_Clone(self):
        return self.driver.find_element(*Administration_PO.Clone)

    def admin_po_Clone_Confirmation_Yes(self):
        return self.driver.find_element(*Administration_PO.Clone_Confirmation_Yes)

    def admin_po_Clone_Success(self):
        return self.driver.find_element(*Administration_PO.Clone_Success)











