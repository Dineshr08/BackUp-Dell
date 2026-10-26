#Selenium framework standards
# While creating project, always create package called tests, inside that keep all the testcase files
#always create class and inside that create method and keep selenium test case.beacuse if we have class we can use oops concepts like inheritance
#inside method we will have our selenium code, method name is testcase name

import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestOne:
    def test_e2e(self):#here we will keep our end 2 end test case
        body = {"name": "morpheus", "job": "leader"}
        # body1 = json.loads(body)
        print(body)
        url = "https://reqres.in/api/users"
        response = requests.post(url, body)
        print(response)
        assert response.status_code == 200
