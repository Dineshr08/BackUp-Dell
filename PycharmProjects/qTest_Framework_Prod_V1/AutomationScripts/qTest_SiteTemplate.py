import json

import pandas as pd
import requests
from csv import writer
import urllib3

urllib3.disable_warnings()
BASE_URL = "https://qtest.gtie.dell.com"
QTEST_TOKEN = "a5023327-1321-4b8d-a3c2-cefd4e9ecb1e"
Login_API = "/login?redirect=https://qtest.gtie.dell.com/portal/project&requestNonce=MC44Nzg2ODE5OTM4OTkz1245"
Logout_API = '/logout'


def SiteTemplate():
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
        Cookies1 = 'UserContextToken=' + Cookies
        print(Cookies1)

        #SiteTemplate
        SiteTemplate_response = requests.get(
            url="{}{}".format(BASE_URL, '/admin/sitetemplate/all-templates'),
            headers={
                'Cookie': Cookies1
            },
            verify=False
        )

        if SiteTemplate_response.status_code == 200:
            try:
                data = SiteTemplate_response.json()

                for item in data:
                    ProjectName = []
                    SiteField = []
                    Template_ID = item.get('templateId')
                    SiteTemplate_Name = item.get('name')

                    if "projects" in item:
                        for project in item['projects']:
                            ProjectName.append(project.get("projectName"))

                    SiteField_response = requests.get(
                        url="{}{}{}{}".format(BASE_URL, '/admin/sitetemplate/', Template_ID, '/all-fields'),
                        headers={
                            'Cookie': Cookies1
                        },
                        verify=False
                    )
                    sitefield_data = SiteField_response.json()
                    if sitefield_data is not None:
                        for field in sitefield_data:
                            if not field["displayName"].startswith("AT_TestCase") and field.get('selected'):
                                SiteField.append(field.get('displayName'))

                    print("SiteTemplate_Name:", SiteTemplate_Name)
                    print("SiteTemplate_Projects:", ProjectName)
                    print("SiteTemplate_AllFields:", SiteField)
                    # List = [SiteTemplate_Name, ProjectName, SiteField]
                    export.append([SiteTemplate_Name, ProjectName, SiteField])

            except json.decoder.JSONDecodeError as e:
                print("Error decoding JSON:", e)
        else:
            print("Error fetching user data. Status code:", SiteTemplate_response.status_code)
            return

    finally:
        # Logout
        url2 = "{}{}".format(BASE_URL, Logout_API)
        payload2 = ""
        headers2 = {
            'Cookie': Cookies1
        }
        response2 = requests.request("GET", url2, headers=headers2, data=payload2)
    df = pd.DataFrame(export,
                      columns=['SiteTemplate_Name', 'ProjectName', 'SiteField'])
    df.to_excel('qTest_SiteTemplate.xlsx', index=False)

SiteTemplate()