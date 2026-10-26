import json

import pandas as pd
import requests
from csv import writer
import urllib3

urllib3.disable_warnings()
BASE_URL = "https://qtest-stage.gtie.dell.com"
QTEST_TOKEN = "cbe60e5b-7969-4505-84a9-d42d3015b0da"
Login_API = "/login?redirect=https://qtest-stage.gtie.dell.com/portal/project&requestNonce=MC44Nzg2ODE5OTM4OTkz1245"
Logout_API = '/logout'


def UserProfile_Project():
    export = []
    try:
        #Login
        url = "{}{}".format(BASE_URL, Login_API)
        payload = 'j_username=dinesh_r3&j_password=Password%408&requestNonce=MC44Nzg2ODE5OTM4OTkz1245&service='
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'JSESSIONID=qtest-stg-app03~3FDD8CF519D907A9805ECE588E8574E4; UserContextToken=ODEwMmIzOWUtZjBlNi00MDFjLTliZWYtMjUxNDJkNzkyMTFj'
        }
        session = requests.Session()
        response = session.post(url, headers=headers, data=payload)
        Cookies = session.cookies.get('UserContextToken')
        Cookies1 = 'UserContextToken=' + Cookies
        print(Cookies1)

        ProjectID = [334, 59]
        UserProfileID = [5, 19]

        for Project_ID in ProjectID:
            for UserProfile_ID in UserProfileID:
                userProfilePermission_response = requests.get(
                    url="{}{}{}{}{}{}".format(BASE_URL, '/p/', Project_ID, '/portal/setting/userprofile/',
                                              UserProfile_ID,
                                              '/permission?dojo.preventCache=0.8362461047795546'),
                    headers={
                        'Cookie': Cookies1
                    },
                    verify=False
                )
                data_userProfilePermission = userProfilePermission_response.content
                export.append([Project_ID, UserProfile_ID, data_userProfilePermission])




    finally:
        # Logout
        url2 = "{}{}".format(BASE_URL, Logout_API)
        payload2 = ""
        headers2 = {
            'Cookie': Cookies1
        }
        response2 = requests.request("GET", url2, headers=headers2, data=payload2)

    df = pd.DataFrame(export, columns=['Project_ID', 'UserProfile_ID', 'ProfilePermission_Data'])
    df.to_excel('qTest_UserProfile_Permission_ProjectSpecific.xlsx', index=False)

UserProfile_Project()