from selenium.webdriver.common.by import By


class Configuration_PO:

    hostname = (By.ID, "hostname")
    SMTPPort = (By.ID, "smtpport")
    Email = (By.ID, "emailAddress")
    Username = (By.ID, "username")
    SecurityProtocol = (By.NAME, "securityProtocol")
    Session_Explorer = (By.ID, "eXplorerApiUrl")
    Parameter = (By.ID, "parametersURLOnpremise")
    Pulse = (By.ID, "pulseURLOnpremise")
    Launch = (By.ID, "launchURLOnpremise")
    Insights = (By.ID, "configureInsightsURL")
    AttachmentSize = (By.ID, "adminSettingAttachmentVolume")

    def __init__(self, driver):
        self.driver = driver

    def configuration_po_hostname(self):
        return self.driver.find_element(*Configuration_PO.hostname)

    def configuration_po_SMTPPort(self):
        return self.driver.find_element(*Configuration_PO.SMTPPort)

    def configuration_po_Email(self):
        return self.driver.find_element(*Configuration_PO.Email)

    def configuration_po_Username(self):
        return self.driver.find_element(*Configuration_PO.Username)

    def configuration_po_SecurityProtocol(self):
        return self.driver.find_element(*Configuration_PO.SecurityProtocol)

    def configuration_po_Session_Explorer(self):
        return self.driver.find_element(*Configuration_PO.Session_Explorer)

    def configuration_po_Parameter(self):
        return self.driver.find_element(*Configuration_PO.Parameter)

    def configuration_po_Pulse(self):
        return self.driver.find_element(*Configuration_PO.Pulse)

    def configuration_po_Launch(self):
        return self.driver.find_element(*Configuration_PO.Launch)

    def configuration_po_Insights(self):
        return self.driver.find_element(*Configuration_PO.Insights)

    def configuration_po_AttachmentSize(self):
        return self.driver.find_element(*Configuration_PO.AttachmentSize)


