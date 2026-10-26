import json

import pandas as pd
import requests
from csv import writer
import urllib3
import urllib3
urllib3.disable_warnings()
BASE_URL = "https://qtest.gtie.dell.com"
QTEST_TOKEN = "a5023327-1321-4b8d-a3c2-cefd4e9ecb1e"
Login_API = "/login?redirect=https://qtest.gtie.dell.com/portal/project&requestNonce=MC44Nzg2ODE5OTM4OTkz1245"
Integration_API = "/portal/defect/integration/setting/connection/list/9?dojo.preventCache=0.1208288477138908"
Logout_API = '/logout'
Project_API = "/api/v3/projects?assigned=false"

def qTest_Configuration():

    try:
        # Login
        session = requests.Session()
        response = session.post(
            url="{}{}".format(BASE_URL, Login_API),
            data='j_username=dinesh_r3&j_password=Password%4011&requestNonce=MC44Nzg2ODE5OTM4OTkz1245&service=',
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'JSESSIONID=qtest-stg-app03~3FDD8CF519D907A9805ECE588E8574E4; UserContextToken=ODEwMmIzOWUtZjBlNi00MDFjLTliZWYtMjUxNDJkNzkyMTFj'
            },

            verify=False
        )
        Cookies = session.cookies.get('UserContextToken')
        Cookies1 = 'UserContextToken=' + Cookies
        print(Cookies1)

        # Get list of project

        ProjectList_Response = requests.get(
            url="{}{}".format(BASE_URL, Project_API),
            headers={
                "Authorization": "Bearer {}".format(QTEST_TOKEN)
            },
            verify=False
        )
        if ProjectList_Response.status_code == 200:
            project_info = ProjectList_Response.json()
            prjID = []
            for item in project_info:
                prjID.append(item['id'])
            print("Project ID List:", prjID)
            print("Total Projects:", len(prjID))

            for Project_ID in prjID:
                Connection_Response = requests.get(
                    url="{}{}{}{}".format(BASE_URL, '/p/',Project_ID, '/portal/customfield/artifact/customfield/3?dojo.preventCache=0.8843984265046947'),
                    headers={
                        'Cookie': Cookies1
                    },
                    verify=False
                )
                if Connection_Response.status_code == 200:
                    Connection_info = Connection_Response.json()
                    configuration_found = False
                    for item in Connection_info:
                        if item.get("displayName") == "Configuration":
                            configuration_found = True
                            isActive = item.get("isActive")
                            print("Configuration with Project:", Project_ID, "is active:", isActive)
                            # print("isActive value:", isActive)
                            break
                    if not configuration_found:
                        print("displayName is not available for Project:", Project_ID)




        else:
            print("Unable to fetch all project details", ProjectList_Response.status_code)


    finally:
        # Logout
        url2 = "{}{}".format(BASE_URL, Logout_API)
        payload2 = ""
        headers2 = {
            'Cookie': Cookies1
        }

        response2 = requests.request("GET", url2, headers=headers2, data=payload2)

qTest_Configuration()

