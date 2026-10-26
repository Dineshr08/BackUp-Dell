from selenium.webdriver.common.by import By


class JiraCEC_PO:



    Summary_Name = (By.ID, "summary")
    Create = (By.ID, "issue-create-submit")
    PageValidation = (By.XPATH, "//h1[normalize-space()='Create Issue']")
    Addon_Expand = (By.CLASS_NAME, "aui-nav-subtree-toggle")
    qTest = (By.XPATH, "//span[text()='qTest']")

    def __init__(self, driver):
        self.driver = driver


    def jiracec_PO_Summary_Name(self):
        return self.driver.find_element(*JiraCEC_PO.Summary_Name)

    def jiracec_PO_Create(self):
        return self.driver.find_element(*JiraCEC_PO.Create)

    def jiracec_PO_PageValidation(self):
        return self.driver.find_element(*JiraCEC_PO.PageValidation)

    def jiracec_PO_Addon_Expand(self):
        return self.driver.find_element(*JiraCEC_PO.Addon_Expand)

    def jiracec_PO_qTest(self):
        return self.driver.find_element(*JiraCEC_PO.qTest)

