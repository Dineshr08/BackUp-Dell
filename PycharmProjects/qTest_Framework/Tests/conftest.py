
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json
import requests
import urllib3
urllib3.disable_warnings()
BASE_URL = "https://qtest.gtie.dell.com"


def pytest_addoption(parser):
    parser.addoption(
        "--env_name", action="store", default="stage"
    )
    parser.addoption(
        "--TC_Name", action="store", default="test"
    )

@pytest.fixture(scope="class")
def setup(request):
    download_dir = "C:\\Test"
    chromeoption = webdriver.ChromeOptions()
    chromeoption.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    chromeoption.add_argument("--disable-application-cache")
    chromeoption.add_argument("--disk-cache-size=0")
    chromeoption.add_argument("--headless=new")
    chromeoption.add_argument("--incognito")
    chromeoption.add_argument("--window-size=1920,1080")
    chromeoption.add_argument('--ignore-certificate-errors')
    chromeoption.add_argument('--disable-extensions')
    chromeoption.add_argument('--disable-popup-blocking')
    chromeoption.add_argument('--disable-plugins-discovery')
    service_obj = Service("C:\Selenium\chromedriver.exe")
    global driver
    env_name = request.config.getoption("env_name")
    driver = webdriver.Chrome(service=service_obj,options=chromeoption)
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()

    if env_name == "stage":
        driver.get("https://qtest-stage.gtie.dell.com/")
    elif env_name == "dev02":
        driver.get("https://qtest-dev02.cec.lab.emc.com/")
    elif env_name == "dev03":
        driver.get("https://qtest-dev3.gtie.dell.com/")
    elif env_name == "prod":
        driver.get("https://qtest.gtie.dell.com/")
    request.cls.driver = driver
    yield
    # action = ActionChains(driver)
    # wait = WebDriverWait(driver, 20)
    # action.move_to_element(driver.find_element(By.ID, "topLeftTitle")).perform()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//input[@id='searchProjectInput']").send_keys("AKT-Test")
    # time.sleep(5)
    # wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "AKT-Test")))
    # driver.find_element(By.LINK_TEXT, "AKT-Test").click()
    # time.sleep(5)
    # wait.until(EC.presence_of_element_located((By.XPATH, "//span[@dojoattachpoint='titleNode']")))
    # action.move_to_element(driver.find_element(By.CLASS_NAME, "show-user-menu")).perform()
    # time.sleep(5)
    # wait.until(EC.element_to_be_clickable((By.ID, "log-out-link")))
    # time.sleep(5)
    # driver.find_element(By.ID, "log-out-link").click()
    # driver.close()
    driver.quit()

@pytest.fixture(scope="class")
def API_setup(request):
    global auth_token, url
    env_name = request.config.getoption("env_name")
    if env_name == "stage":
        url = "https://qtest-stage.gtie.dell.com"
        auth_token = "Bearer cbe60e5b-7969-4505-84a9-d42d3015b0da"
    elif env_name == "prod":
        url = "https://qtest.gtie.dell.com"
        auth_token = "Bearer fda0002f-500a-47c6-b617-0381dc027b39"
    request.cls.env_name = env_name
    request.cls.url = url
    request.cls.auth_token = auth_token

# @pytest.fixture
# def testsuitedata(request):
#     testsuiteID = request.config.getoption('--testsuiteID')
#     print("The testsuiteID value:", testsuiteID)
#     return testsuiteID

@pytest.fixture(scope="session")
def getTSValue(request):

    TC_Name = request.config.getoption("TC_Name")
    env_name = request.config.getoption("env_name")
    # TC_Name = sys.argv[1]
    # env_name = sys.argv[2]
    # TC_Name = 'test'
    # env_name = 'stage'

    if env_name == 'stage':
        Env_Value = 'Stage'
    elif env_name == 'prod':
        Env_Value = 'Prod'

    # Get all TestCycle details from root

    get_List_TC_Response = requests.get(
        url="{}{}".format(BASE_URL, '/api/v3/projects/167/test-cycles?parentType=root'),
        headers={
            "Authorization": "Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e"
        },
        verify=False
    )
    if get_List_TC_Response.status_code == 200:
        get_List_TC_info = get_List_TC_Response.json()
        get_List_TC_info_dict = {}

        for item in get_List_TC_info:
            name = item["name"]
            objId = item["id"]
            get_List_TC_info_dict[name] = objId
        # print(get_List_TC_info_dict)

        # Get details of Test cycle which we created from Jenkins

        Created_TC_Value = get_List_TC_info_dict[TC_Name]

        get_Created_TC_Response = requests.get(
            url="{}{}{}{}".format(BASE_URL,
                                  '/api/v3/projects/167/test-cycles?parentId=', Created_TC_Value,
                                  '&parentType=test-cycle&expand=descendants&page=1&pageSize=100'),
            headers={
                "Authorization": "Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e"
            },
            verify=False
        )

        if get_Created_TC_Response.status_code == 200:
            get_Created_TC_info = get_Created_TC_Response.json()
            get_Created_TC_info_dict = {}

            for item in get_Created_TC_info:
                name = item["name"]
                objId = item["id"]
                get_Created_TC_info_dict[name] = objId
            # print(get_Created_TC_info_dict)

            # Get TestSuite detils

            Created_TC_Value = get_Created_TC_info_dict[Env_Value]
            # print("Stage_TC_Value", Stage_TC_Value)

            get_TS_Response = requests.get(
                url="{}{}{}{}".format(BASE_URL,
                                      '/api/v3/projects/167/test-suites?parentId=', Created_TC_Value,
                                      '&parentType=test-cycle&expand=descendants&page=1&pageSize=100'),
                headers={
                    "Authorization": "Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e"
                },
                verify=False
            )

            TS_parsed_response = json.loads(get_TS_Response.content)

            if get_TS_Response.status_code == 200:
                TS_Value = TS_parsed_response[0]["id"]
                print(TS_Value)
                request.config.cache.set("script_output", TS_Value)
                return TS_Value


            else:
                print("Unable to fetch TestSuite details", get_TS_Response.status_code)
        else:
            print("Unable to fetch Created TestCycle details", get_Created_TC_Response.status_code)

    else:
        print("Unable to fetch TestCycle from root level", get_List_TC_Response.status_code)

@pytest.fixture(scope="class")
def setup_export(request):
    download_dir = "C:\\Test"
    chromeoption = webdriver.ChromeOptions()
    chromeoption.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    chromeoption.add_argument("--disable-application-cache")
    chromeoption.add_argument("--disk-cache-size=0")
    chromeoption.add_argument("--headless=new")
    # chromeoption.add_argument("--incognito")
    chromeoption.add_argument("--window-size=1920,1080")
    chromeoption.add_argument('--ignore-certificate-errors')
    chromeoption.add_argument('--disable-extensions')
    chromeoption.add_argument('--disable-popup-blocking')
    chromeoption.add_argument('--disable-plugins-discovery')
    service_obj = Service("C:\Selenium\chromedriver.exe")
    global driver
    env_name = request.config.getoption("env_name")
    driver = webdriver.Chrome(service=service_obj,options=chromeoption)
    # driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()

    if env_name == "stage":
        driver.get("https://qtest-stage.gtie.dell.com/")
    elif env_name == "dev02":
        driver.get("https://qtest-dev02.cec.lab.emc.com/")
    elif env_name == "dev03":
        driver.get("https://qtest-dev3.gtie.dell.com/")
    elif env_name == "prod":
        driver.get("https://qtest.gtie.dell.com/")
    request.cls.driver = driver
    yield
    # action = ActionChains(driver)
    # wait = WebDriverWait(driver, 20)
    # action.move_to_element(driver.find_element(By.ID, "topLeftTitle")).perform()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//input[@id='searchProjectInput']").send_keys("AKT-Test")
    # time.sleep(5)
    # wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "AKT-Test")))
    # driver.find_element(By.LINK_TEXT, "AKT-Test").click()
    # time.sleep(5)
    # wait.until(EC.presence_of_element_located((By.XPATH, "//span[@dojoattachpoint='titleNode']")))
    # action.move_to_element(driver.find_element(By.CLASS_NAME, "show-user-menu")).perform()
    # time.sleep(5)
    # wait.until(EC.element_to_be_clickable((By.ID, "log-out-link")))
    # time.sleep(5)
    # driver.find_element(By.ID, "log-out-link").click()
    # driver.close()
    driver.quit()

@pytest.fixture(scope="class")
def setup_jira(request):
    chromeoption = webdriver.ChromeOptions()
    chromeoption.add_argument("--disable-application-cache")
    chromeoption.add_argument("headless")
    chromeoption.add_argument("incognito")
    service_obj = Service("C:\Selenium\chromedriver.exe")
    global driver
    env_name = request.config.getoption("env_name")
    driver = webdriver.Chrome(service=service_obj,options=chromeoption)
    driver.delete_all_cookies()
    driver.set_window_size(1920, 578)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if 'UserInterface' in item.keywords:
        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                # Check if the test class has a driver attribute before attempting screenshot
                if hasattr(item, 'cls') and hasattr(item.cls, 'driver'):
                    _capture_screenshot(item.cls.driver, file_name)
                    if file_name:
                        # html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                        #        'onclick="window.open(this.src)" align="right"/></div>' % file_name
                        file_name_html = file_name.encode('utf-8', 'xmlcharrefreplace').decode('utf-8')
                        html = f'<div><img src="{file_name_html}" alt="screenshot" style="width:304px;height:228px;" ' \
                               f'onclick="window.open(this.src)" align="right"/></div>'
                        extra.append(pytest_html.extras.html(html))
            report.extra = extra




def _capture_screenshot(driver, name):
    driver.get_screenshot_as_file(name)















