# Dynamic dropdown selection and get attribute value

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(5)
#find elements will get all value in below css selector and store in list
# here using below css locatore, we are doing parent child extraction and getting multiple values and from that only india we are selecting
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
# countries will store webelements, so we store that countries webelement in country , so we can perform webelements operations lik clikc ,text etc
#print(countries)
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
#get attribute("value"): if we want to get ui text of that place we can use .text, but here the value we have given is dynamic and to fetch that we cant use .text,we need to use get_attribute("value"), which will store in backend of our dynamically given value , so fromm there we can get it
country1 = driver.find_element(By.ID,"autosuggest").get_attribute("value")
print(country1)
assert country1 in "India"
assert country1 == "India"
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"

time.sleep(10)