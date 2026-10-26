#Here we are going to see how we are going to see the log data in html report, using logging code
#first we are going to create seperate class for logging , so for all testcase, we can just use that by inheriting.
#Class name: LoggerBaseClass and file name: BaseClass
#Then we will inherit that logger base class and try to print the log in html report
import pytest

from BaseClass import LoggerBaseClass


@pytest.mark.usefixtures("getdata")
class TestExample2(LoggerBaseClass):
    def test_logging1(self, getdata):
        log = self.logging()
        log.info(getdata[1])

#another example

@pytest.mark.usefixtures("getdata")
class TestExample1(LoggerBaseClass):
    def test_edit(self, getdata):
        log = self.logging()
        log.info(getdata)
        log.info(getdata[1])


