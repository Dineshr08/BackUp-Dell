#Some functional validation, adding up the value added in cart and compoared with total amt

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
actualresult = []
ExpectedResult = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
service_obj = Service("C:\Selenium\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(5) # it will wait max of 5 sec for each findelements to load, if its load within 1 sec it move to next step.its global.
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CLASS_NAME,"search-keyword").send_keys("ber") #searching with ber
time.sleep(10)
#selecting all the product displying based on ber search
resultProducts = driver.find_elements(By.XPATH,"//div[@class='products']/div") #getting all appering product, which include add to cart + - all button
print(len(resultProducts))
count = len(resultProducts)
assert count > 0
for result in resultProducts:
    actualresult.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click() #result will have all child page webelements, from that we only choose add to cart
assert actualresult == ExpectedResult
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click() #locating the x path based on text
driver.find_element(By.CLASS_NAME,"promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()
#Explicit wait, it applicable only for this action
wait = WebDriverWait(driver, 10) #we are explicitely waiting 10 sec
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))#we are waiting till 10 sec until that msg appears.
coupen = driver.find_element(By.XPATH,"//span[@class='promoInfo']").text
assert coupen == "Code applied ..!"
AmtAfterDiscount = driver.find_element(By.CLASS_NAME,"discountAmt").text
sum = 0
amounts = driver.find_elements(By.XPATH,"//tr/td[5]/p")
for amount in amounts:
    sum = sum + int(amount.text)
totalamt = driver.find_element(By.CLASS_NAME,"totAmt").text
assert float(AmtAfterDiscount) < int(totalamt)
assert sum == int(totalamt)
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
time.sleep(10)