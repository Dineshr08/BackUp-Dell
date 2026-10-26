from selenium.webdriver.common.by import By


class FieldSetting_PO:

    Global_Setting_Field_Setting_TestRun = (By.XPATH, "//span[text()='Test Run']")
    Global_Setting_Field_Setting_AddCustomField = (By.XPATH, "//span[text()='Add Custom Field']")
    Global_Setting_Field_Setting_AddCustomField_DisplayName = (By.NAME, "displayName")
    Global_Setting_Field_Setting_AddCustomField_OK = (By.ID, "addCustomFieldForm_btnSubmit_label")
    Global_Setting_Field_Setting_AddCustomField_OK1 = (By.XPATH, "//div[@id='customfield_edit_field_dialog']//span[@id='customfieldSave_label']")
    Global_Setting_Field_Setting_AddCustomField_FieldType = (By.ID, "addCustomFieldForm_fieldType")
    Global_Setting_Field_Setting_AddCustomField_AddValue = (By.ID, "customfield_btn_add_combofield_label")
    Global_Setting_Field_Setting_AddCustomField__ComboBox_OK1 = (By.XPATH, "//div[@class='dijitDialogPaneActionBar']//span[@id='customfieldSave_label']")

    def __init__(self, driver):
        self.driver = driver

    def fieldsetting_po_Global_Setting_Field_Setting_TestRun(self):
        return self.driver.find_element(*FieldSetting_PO.Global_Setting_Field_Setting_TestRun)

    def fieldsetting_po_Global_Setting_Field_Setting_AddCustomField(self):
        return self.driver.find_element(*FieldSetting_PO.Global_Setting_Field_Setting_AddCustomField)

    def fieldsetting_po_Global_Setting_Field_Setting_AddCustomField_DisplayName(self):
        return self.driver.find_element(*FieldSetting_PO.Global_Setting_Field_Setting_AddCustomField_DisplayName)

    def fieldsetting_po_Global_Setting_Field_Setting_AddCustomField_OK(self):
        return self.driver.find_element(*FieldSetting_PO.Global_Setting_Field_Setting_AddCustomField_OK)

    def fieldsetting_po_Global_Setting_Field_Setting_AddCustomField_OK1(self):
        return self.driver.find_element(*FieldSetting_PO.Global_Setting_Field_Setting_AddCustomField_OK1)

    def fieldsetting_po_Global_Setting_Field_Setting_AddCustomField_FieldType(self):
        return self.driver.find_element(*FieldSetting_PO.Global_Setting_Field_Setting_AddCustomField_FieldType)

    def fieldsetting_po_Global_Setting_Field_Setting_AddCustomField_AddValue(self):
        return self.driver.find_element(*FieldSetting_PO.Global_Setting_Field_Setting_AddCustomField_AddValue)

    def fieldsetting_po_Global_Setting_Field_Setting_AddCustomField__ComboBox_OK1(self):
        return self.driver.find_element(*FieldSetting_PO.Global_Setting_Field_Setting_AddCustomField__ComboBox_OK1)

