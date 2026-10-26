import json

import pandas as pd
import requests
from csv import writer
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()
BASE_URL = "https://qtest-stage.gtie.dell.com"
# BASE_URL = "https://qtest.gtie.dell.com"
QTEST_TOKEN = "fda0002f-500a-47c6-b617-0381dc027b39"
Login_API = "/login?redirect=https://qtest-stage.gtie.dell.com/portal/project&requestNonce=MC44Nzg2ODE5OTM4OTkz1245"
Logout_API = '/logout'


def TestCaseSharing():
    export = []
    try:
        #Login
        url = "{}{}".format(BASE_URL, Login_API)
        payload = 'j_username=dinesh_r3&j_password=Password%4011&requestNonce=MC44Nzg2ODE5OTM4OTkz1245&service='
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'JSESSIONID=qtest-stg-app03~3FDD8CF519D907A9805ECE588E8574E4; UserContextToken=ODEwMmIzOWUtZjBlNi00MDFjLTliZWYtMjUxNDJkNzkyMTFj'
        }
        session = requests.Session()
        response = session.post(url, headers=headers, data=payload)
        Cookies = session.cookies.get('UserContextToken')
        print(Cookies)
        Cookies1 = 'UserContextToken=' + Cookies
        print(Cookies1)

        #TestCase Sharing Activation Status

        TestcaseSharingSettings_response = requests.get(
            url="{}{}".format(BASE_URL, '/p/334/portal/project/settings?dojo.preventCache=0.15068918171912093'),
            headers={
                'Cookie': Cookies1
            },
            verify=False
        )

        if TestcaseSharingSettings_response.status_code == 200:
            data = json.loads(TestcaseSharingSettings_response.text)
            sharing_info = data.get("sharing")
            print(sharing_info)
        else:
            print("Error fetching user data. Status code:", TestcaseSharingSettings_response.status_code)
            return

        #TestCase Sharing Project List

        TestcaseSharingProjectList_response = requests.get(
            url="{}{}".format(BASE_URL, '/p/334/portal/testcasesharing/page-setting'),
            headers={
                'Cookie': Cookies1
            },
            verify=False
        )

        # Parse the HTML content
        soup = BeautifulSoup(TestcaseSharingProjectList_response.text, 'html.parser')

        # Find the input element with id 'testCaseSharingSettingProjectsData'
        input_element = soup.find('input', {'id': 'testCaseSharingSettingProjectsData'})

        # Extract the 'value' attribute of the input element
        value = input_element['value']

        # Now, 'value' contains the data you want
        data = json.loads(value)

        ProjectShared = []

        for item in data:
            if item["shared"]:
                ProjectShared.append(item['name'])

        print(ProjectShared)
        # List = [sharing_info, ProjectShared]
        export.append([sharing_info, ProjectShared])


    finally:
        # Logout
        url2 = "{}{}".format(BASE_URL, Logout_API)
        payload2 = ""
        headers2 = {
            'Cookie': Cookies1
        }
        response2 = requests.request("GET", url2, headers=headers2, data=payload2)
    df = pd.DataFrame(export, columns=['sharing_info', 'ProjectShared'])
    df.to_excel('qTest_TestCaseSharing.xlsx', index=False)

TestCaseSharing()