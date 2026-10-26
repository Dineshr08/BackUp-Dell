#Static dropdown selection
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
#Working on static dropdown
#for static dropdown, mostly there will be select tag will be there, we can use select call and perform that
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
#static dropdown handle in 3 ways
#1 select by index, if 4 value 1st value start with 0
dropdown.select_by_index(1)
# select by  visible text
dropdown.select_by_visible_text("Male")
# select by value, we will find the attribute value , we can use this
#dropdown.select_by_value()

time.sleep(25)