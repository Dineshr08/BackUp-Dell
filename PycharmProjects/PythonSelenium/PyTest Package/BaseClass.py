import inspect
#here creating class and returing the obj logger in return statement.
#when other class inherit this class, can call the method, when it call, it will return the object logger, so using that logger, it can perform all logger.debug etc function
#then earlier we used logger = logging.getLogger(__name__) st for printing the file name, but now we added loggerName = inspect.stack()[1][3] this and passing loggerName in the place of __name__
#above will helpful to get the testcase name , where this method is called test_logging(), instead od this file name
import logging
#if we are wiruting any thing like normal file instead of test_filename , we can directly give class name and method name instead of testclassname and test_methodname
class LoggerBaseClass():
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
