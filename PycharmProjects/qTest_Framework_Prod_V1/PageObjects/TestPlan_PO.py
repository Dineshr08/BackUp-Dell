from selenium.webdriver.common.by import By


class TestPlan_PO:

    CreateNewRelease = (By.XPATH,"//span[@title='New Release']")
    ExistingReleaseName = (By.XPATH,"//div/span[@title='Untitled']")
    Update_ExistingReleaseName = (By.XPATH,"//input[@id='dijit_form_TextBox_0']")
    Edit_Description = (By.ID,"tinymce")
    Save = (By.XPATH, "//span[text()='Save']")
    Saved_Notification = (By.CLASS_NAME, "rc-header-message-node")
    ReleaseID = (By.XPATH, "//span[@class='rc-header-id-badge-text']")
    Add = (By.ID, "portal_release_release_popup_label")
    ChooseRequirement = (By.XPATH, "//span[text()='LinkRequirement']")
    Add_Requirement = (By.XPATH, "//span[@id='portal_release_release_popup_okButton_label']")
    Add_Attachment = (By.XPATH, "//input[starts-with(@id,'qas_custom_FileInput_')]")
    Add_Requirement_Validation = (By.XPATH, "//a[text()='Link_Requirement']")
    Add_Attachment_Validation = (By.XPATH, "//span[text()='AT_Import.txt']")
    Copy = (By.XPATH, "//span[@title='Copy']") #//span[@title='Copy']
    Paste = (By.XPATH, "//span[@title='Paste']")#//span[@title='Paste']
    ExistingRelease = (By.XPATH, "//div[@title='RL-3 AT_TestExecution_CreateTestSuiteTestCycle_Template']//span[text()='AT_TestExecution_CreateTestSuiteTestCycle_Template']")
    HomeFolder = (By.XPATH, "//div[@title='AutomationTesting1']//span[text()='AutomationTesting1']")
    CopyRelease_Validation = (By.XPATH, "//div[text()='Copied objects have been pushed to database queue successfully']")
    Build = (By.ID, "projectReleaseNewBuild")
    BuildNote = (By.ID, "tinymce")
    Build_Save = (By.XPATH, "//span[@id='portal_release_build_saveButton_label']")
    Build_Saved_Notification = (By.XPATH, "//div[contains(text(),'Changes were saved successfully.')]")



    def __init__(self, driver):
        self.driver = driver

    def testplan_po_CreateNewRelease(self):
        return self.driver.find_element(*TestPlan_PO.CreateNewRelease)

    def testplan_po_ExistingReleaseName(self):
        return self.driver.find_element(*TestPlan_PO.ExistingReleaseName)

    def testplan_po_Update_ExistingReleaseName(self):
        return self.driver.find_element(*TestPlan_PO.Update_ExistingReleaseName)

    def testplan_po_Edit_Description(self):
        return self.driver.find_element(*TestPlan_PO.Edit_Description)

    def testplan_po_Save(self):
        return self.driver.find_element(*TestPlan_PO.Save)

    def testplan_po_Saved_Notification(self):
        return self.driver.find_element(*TestPlan_PO.Saved_Notification)

    def testplan_po_ReleaseID(self):
        return self.driver.find_element(*TestPlan_PO.ReleaseID)

    def testplan_po_Add(self):
        return self.driver.find_element(*TestPlan_PO.Add)

    def testplan_po_ChooseRequirement(self):
        return self.driver.find_element(*TestPlan_PO.ChooseRequirement)

    def testplan_po_Add_Requirement(self):
        return self.driver.find_element(*TestPlan_PO.Add_Requirement)

    def testplan_po_Add_Attachment(self):
        return self.driver.find_element(*TestPlan_PO.Add_Attachment)

    def testplan_po_Add_Requirement_Validation(self):
        return self.driver.find_element(*TestPlan_PO.Add_Requirement_Validation)

    def testplan_po_Add_Attachment_Validation(self):
        return self.driver.find_element(*TestPlan_PO.Add_Attachment_Validation)

    def testplan_po_Copy(self):
        return self.driver.find_element(*TestPlan_PO.Copy)

    def testplan_po_Paste(self):
        return self.driver.find_element(*TestPlan_PO.Paste)

    def testplan_po_ExistingRelease(self):
        return self.driver.find_element(*TestPlan_PO.ExistingRelease)

    def testplan_po_HomeFolder(self):
        return self.driver.find_element(*TestPlan_PO.HomeFolder)

    def testplan_po_CopyRelease_Validation(self):
        return self.driver.find_element(*TestPlan_PO.CopyRelease_Validation)

    def testplan_po_Build(self):
        return self.driver.find_element(*TestPlan_PO.Build)

    def testplan_po_BuildNote(self):
        return self.driver.find_element(*TestPlan_PO.BuildNote)

    def testplan_po_Build_Save(self):
        return self.driver.find_element(*TestPlan_PO.Build_Save)

    def testplan_po_Build_Saved_Notification(self):
        return self.driver.find_element(*TestPlan_PO.Build_Saved_Notification)



