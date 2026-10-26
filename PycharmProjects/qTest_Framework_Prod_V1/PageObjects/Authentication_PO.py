from selenium.webdriver.common.by import By


class Authentication_PO:

    AppAuth = (By.XPATH, "//span[@role='treeitem'][normalize-space()='APPAUTH']")
    AppAuth_Url = (By.ID, "ldapConfigUrl")
    AppAuth_Base = (By.ID, "ldapConfigBase")
    AppAuth_UserDN = (By.ID, "ldapConfigUserDn")
    AppAuth_SSL = (By.ID, "ldap_isLDAPS")
    AppAuth_IsActive = (By.ID, "ldap_isActiveDirectory")
    AppAuth_Username = (By.ID, "ldapConfigMappedUname")
    AppAuth_Fname = (By.ID, "ldapConfigMappedFname")
    AppAuth_Lname = (By.ID, "ldapConfigMappedLname")
    AppAuth_Email = (By.ID, "ldapConfigMappedEmail")
    AppAuth_SyncStatus = (By.ID, "syncStatus")
    Gtie = (By.XPATH, "//span[@role='treeitem'][normalize-space()='GTIE']")
    #For Gtie also same ID,s only
    # Gtie_Url = (By.ID, "ldapConfigUrl")
    # Gtie_Base = (By.ID, "ldapConfigBase")
    # Gtie_UserDN = (By.ID, "ldapConfigUserDn")
    # Gtie_SSL = (By.ID, "ldap_isLDAPS")
    # Gtie_IsActive = (By.ID, "ldap_isActiveDirectory")
    # Gtie_Username = (By.ID, "ldapConfigMappedUname")
    # Gtie_Fname = (By.ID, "ldapConfigMappedFname")
    # Gtie_Lname = (By.ID, "ldapConfigMappedLname")
    # Gtie_Email = (By.ID, "ldapConfigMappedEmail")
    # Gtie_SyncStatus = (By.ID, "syncStatus")


    def __init__(self, driver):
        self.driver = driver

    def authentication_po_AppAuth(self):
        return self.driver.find_element(*Authentication_PO.AppAuth)

    def authentication_po_AppAuth_Url(self):
        return self.driver.find_element(*Authentication_PO.AppAuth_Url)

    def authentication_po_AppAuth_Base(self):
        return self.driver.find_element(*Authentication_PO.AppAuth_Base)

    def authentication_po_AppAuth_UserDN(self):
        return self.driver.find_element(*Authentication_PO.AppAuth_UserDN)

    def authentication_po_AppAuth_SSL(self):
        return self.driver.find_element(*Authentication_PO.AppAuth_SSL)

    def authentication_po_AppAuth_IsActive(self):
        return self.driver.find_element(*Authentication_PO.AppAuth_IsActive)

    def authentication_po_AppAuth_Username(self):
        return self.driver.find_element(*Authentication_PO.AppAuth_Username)

    def authentication_po_AppAuth_Fname(self):
        return self.driver.find_element(*Authentication_PO.AppAuth_Fname)

    def authentication_po_AppAuth_Lname(self):
        return self.driver.find_element(*Authentication_PO.AppAuth_Lname)

    def authentication_po_AppAuth_Email(self):
        return self.driver.find_element(*Authentication_PO.AppAuth_Email)

    def authentication_po_AppAuth_SyncStatus(self):
        return self.driver.find_element(*Authentication_PO.AppAuth_SyncStatus)

    def authentication_po_Gtie(self):
        return self.driver.find_element(*Authentication_PO.Gtie)





