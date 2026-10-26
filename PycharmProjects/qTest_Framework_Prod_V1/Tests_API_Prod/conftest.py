import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



def pytest_addoption(parser):
    parser.addoption(
        "--env_name", action="store", default="prod"
    )



@pytest.fixture(scope="class")
def API_setup(request):
    global auth_token, url
    env_name = request.config.getoption("env_name")
    if env_name == "stage":
        url = "https://qtest-stage.gtie.dell.com"
        auth_token = "Bearer cbe60e5b-7969-4505-84a9-d42d3015b0da"
    elif env_name == "prod":
        url = "https://qtest.gtie.dell.com"
        auth_token = "Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e"
    request.cls.env_name = env_name
    request.cls.url = url
    request.cls.auth_token = auth_token




