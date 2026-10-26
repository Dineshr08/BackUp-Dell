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

def qTest_GetCustomFields():
    export = []

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

            # Fetching Connection Details

            # prjID = [45, 1]

            for Project_ID in prjID:
                objType_ID = [8, 13, 5, 1, 2, 3, 17]
                for ObjectType_ID in objType_ID:
                    sum = 0
                    ObjType_Response = requests.get(
                        url="{}{}{}{}{}{}".format(BASE_URL, '/p/', Project_ID,
                                                '/portal/customfield/artifact/customfield/', ObjectType_ID, '?dojo.preventCache=0.08800687640906757'),
                        headers={
                            'Cookie': Cookies1
                        },
                        verify=False
                    )
                    if ObjType_Response.status_code == 200:
                        ObjType_info = ObjType_Response.json()
                        for item in ObjType_info:
                            if item.get("fieldSystemName") == "DefaultField":
                                sum = sum+1
                        print("Project,Object Type:", Project_ID, ObjectType_ID, sum)


    finally:
        # Logout
        url2 = "{}{}".format(BASE_URL, Logout_API)
        payload2 = ""
        headers2 = {
            'Cookie': Cookies1
        }

        response2 = requests.request("GET", url2, headers=headers2, data=payload2)


qTest_GetCustomFields()
