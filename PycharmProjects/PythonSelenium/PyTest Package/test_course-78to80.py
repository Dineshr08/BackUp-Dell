#here we are going to see how we are going to log data into file
#Logging - its used the log all msg in log file
#Logging hierarchy - debug, info,warning,error, critical
#if we set loglevel as warning from warning to critical only logged
#whatever code we written in pytest, it should be as method
import logging


#below code are some static code, better to use same as provided

def test_logging():
    logger = logging.getLogger(__name__) #__name__  will help us to get file and method name, logger is obj creating to collect log
    fileHandler = logging.FileHandler('logfile.log') # it used to define the log path
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s") # defining format time: level like critical :test case name: log message
    fileHandler.setFormatter(formatter) #assigning formatter to file handler, since only file handler can able to pass to add handler obj
    logger.addHandler(fileHandler) #add handler only take filehandler obj, #now logger have everything like test case name,which file it has to log and its path, format
    logger.setLevel(logging.DEBUG)#if we set loglevel as warning from warning to critical only logged
    logger.debug("Print all debug messages")
    logger.info("Print Information statements")
    logger.warning("Print warning messages")
    logger.error("Can print all assertion messages")
    logger.critical("can print some issue which halt complete framework to stop")

