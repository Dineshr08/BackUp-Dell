#Choosing radio button using get attribute by value method
#out of 3 button , we are getting the one button which we like using get attribute option
#get attribute will help us to get the attribute value of tag.from below we can get value of value, name, class , type etc
#<input value="radio1" name="radioButton" class="radioButton" type="radio">

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
radioBtns = driver.find_elements(By.XPATH,"//input[@name='radioButton']") # which get all options ie 3 radio button
print(len(radioBtns)) #radioBtns will hold all 3 webelement
for radioBtn in radioBtns: #iterate all 3 web element
    if radioBtn.get_attribute("value") == "radio3": #getting webelement value and comparing, if match
        radioBtn.click() # if match then click
        assert radioBtn.is_selected() # validation is radio btn is selected or not
        break

# to check whether in UI the text id displaying or not we can use is displayed method
assert driver.find_element(By.ID,"displayed-text").is_displayed() #it oprovide true or false and we use the output and validating with assert. if true assert will pass
time.sleep(10)
#we are hiding now and check its not displayed
Display =  driver.find_element(By.ID,"hide-textbox").click() # not used to check the false statement
assert not Display.is_displayed()
time.sleep(10)