import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")

class BaseClass:

    def explicrwait_withlinktext(self, xpath):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))

    def selectdropdown(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def logging(self): #whenever we are creating method inside class, that method should have self
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # __name__  will help us to get file and method name, logger is obj creating to collect log
        fileHandler = logging.FileHandler('logfile.log')  # it used to define the log path
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # defining format time: level like critical :test case name: log message
        fileHandler.setFormatter(formatter)  # assigning formatter to file handler, since only file handler can able to pass to add handler obj
        logger.addHandler(fileHandler)  # add handler only take filehandler obj, #now logger have everything like test case name,which file it has to log and its path, format
        logger.setLevel(logging.DEBUG)  # if we set loglevel as warning from warning to critical only logged
        # Commented below lines , becausewe will use this logging in testcases

        # logger.debug("Print all debug messages")
        # logger.info("Print Information statements")
        # logger.warning("Print warning messages")
        # logger.error("Can print all assertion messages")
        # logger.critical("can print some issue which halt complete framework to stop")
        return logger #returing logger onj