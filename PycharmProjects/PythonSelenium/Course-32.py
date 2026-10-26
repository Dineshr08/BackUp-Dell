#How to open a chrome browser, get the tille of the tab and get the current url and how to close the browser

from selenium import webdriver #webdriver is the class in selenium which help us to open the browser
from selenium.webdriver.chrome.service import Service #directly selenium dosenot open the chrome , so we need to download the driver and give path and assign obj.that obj we need to pass in webdriver,chrome.we will create one obj called driver, which we will use to handle all the browser related operations

service_obj = Service('C:\Selenium\chromedriver.exe')
driver = webdriver.Chrome(service=service_obj) # invoke the browser
driver.maximize_window() # maximise the window
driver.get('https://rahulshettyacademy.com/') #launch the url in browser
print(driver.title) #get the tab title
print(driver.current_url) # get the current url that launched in broswer
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/') #launching another url
print(driver.title)
driver.back() # going back to old url
driver.forward() # going to new url again
driver.refresh() #refreshing the page
driver.minimize_window() #minimize the winow
driver.close() # close the browser