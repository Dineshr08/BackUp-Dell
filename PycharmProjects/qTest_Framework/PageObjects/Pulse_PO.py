from selenium.webdriver.common.by import By


class Pulse_PO:

    ChooseProject_Arrow = (By.XPATH, "//mat-icon[text()='arrow_drop_down']")
    Choose_AKT_Project = (By.XPATH, "//button[text()='AKT-Test']")
    Action_Menu = (By.XPATH,"(//span[@class='mat-button-wrapper']//mat-icon[text()='menu'])[3]")
    Action_ViewLogs = (By.XPATH, "//button[normalize-space()='View Logs']")
    Execution_Refresh = (By.XPATH, "//span[text()='Refresh']")
    Execution_Status = (By.XPATH, "//tbody//*//div[text()='completed']")
    Pulse_Validation = (By.XPATH, "//div[@class='td-data-table-cell-content-wrapper']")
    Execution_ID = (By.XPATH, "(//tr[@class='td-data-table-row ng-star-inserted']//a[@class='text-ellipsis'])[1]")
    Execution_ID_Data = (By.XPATH, "//div[@class='mat-tab-body-content ng-trigger ng-trigger-translateTab']//pre[@class='ng-star-inserted']")
    Execution_ID_Close = (By.XPATH, "(//span[text()='Close'])[2]")
    Execution_Close = (By.XPATH, "(//span[text()='Close'])[1]")
    Choose_AT1_Project = (By.XPATH, "//button[text()='AutomationTesting1']")
    Defect_Unlink = (By.CLASS_NAME, "icon-unlink")


    def __init__(self, driver):
        self.driver = driver

    def pulse_po_ChooseProject_Arrow(self):
        return self.driver.find_element(*Pulse_PO.ChooseProject_Arrow)

    def pulse_po_Choose_AKT_Project(self):
        return self.driver.find_element(*Pulse_PO.Choose_AKT_Project)

    def pulse_po_Action_Menu(self):
        return self.driver.find_element(*Pulse_PO.Action_Menu)

    def pulse_po_Action_ViewLogs(self):
        return self.driver.find_element(*Pulse_PO.Action_ViewLogs)

    def pulse_po_Execution_Refresh(self):
        return self.driver.find_element(*Pulse_PO.Execution_Refresh)

    def pulse_po_Execution_Status(self):
        return self.driver.find_element(*Pulse_PO.Execution_Status)

    def pulse_po_Pulse_Validation(self):
        return self.driver.find_elements(*Pulse_PO.Pulse_Validation)

    def pulse_po_Execution_ID(self):
        return self.driver.find_element(*Pulse_PO.Execution_ID)

    def pulse_po_Execution_ID_Data(self):
        return self.driver.find_element(*Pulse_PO.Execution_ID_Data)

    def pulse_po_Execution_ID_Close(self):
        return self.driver.find_element(*Pulse_PO.Execution_ID_Close)

    def pulse_po_Execution_Close(self):
        return self.driver.find_element(*Pulse_PO.Execution_Close)

    def pulse_po_Choose_AT1_Project(self):
        return self.driver.find_element(*Pulse_PO.Choose_AT1_Project)

    def pulse_po_Defect_Unlink(self):
        return self.driver.find_element(*Pulse_PO.Defect_Unlink)



