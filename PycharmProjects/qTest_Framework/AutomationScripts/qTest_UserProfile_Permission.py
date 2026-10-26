import json

import pandas as pd
import requests
from csv import writer
import urllib3

urllib3.disable_warnings()
BASE_URL = "https://qtest-stage.gtie.dell.com"
QTEST_TOKEN = "fda0002f-500a-47c6-b617-0381dc027b39"
Login_API = "/login?redirect=https://qtest-stage.gtie.dell.com/portal/project&requestNonce=MC44Nzg2ODE5OTM4OTkz1245"
Logout_API = '/logout'


def UserProfile():
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

        #User Profile
        userProfile_response = requests.get(
            url="{}{}".format(BASE_URL, '/api/v3/user-profiles'),
            headers={
                "Authorization": "Bearer {}".format(QTEST_TOKEN)
            },
            verify=False
        )

        UserProfile_ID = []
        UserProfile_Name = []


        if userProfile_response.status_code == 200:
            try:
                data = userProfile_response.json()
                Total_UserProfile = data.get('total_user_profiles')
                print("Total_UserProfile:", Total_UserProfile)

                for profile in data['user_profiles']:
                    UserProfile_ID.append(profile['id'])
                    UserProfile_Name.append(profile['name'])

                print('UserProfile ID', UserProfile_ID)
                print('UserProfile Name', UserProfile_Name)

            except json.decoder.JSONDecodeError as e:
                print("Error decoding JSON:", e)
        else:
            print("Error fetching user data. Status code:", userProfile_response.status_code)
            return

        #Get UserProfile Permission
        for i in range(len(UserProfile_ID)):
            ProjectID = UserProfile_ID[i]
            userProfilePermission_response = requests.get(
                url="{}{}{}{}".format(BASE_URL, '/admin/profile/userprofile/', ProjectID, '/permission?dojo.preventCache=0.7950262623367894'),
                headers={
                    'Cookie': Cookies1
                },
                verify=False
            )
            data_userProfilePermission = userProfilePermission_response.content
            # List = [ProjectID, UserProfile_Name[i],data_userProfilePermission]
            export.append([ProjectID, UserProfile_Name[i],data_userProfilePermission])



    finally:
        # Logout
        url2 = "{}{}".format(BASE_URL, Logout_API)
        payload2 = ""
        headers2 = {
            'Cookie': Cookies1
        }
        response2 = requests.request("GET", url2, headers=headers2, data=payload2)

    df = pd.DataFrame(export,
                      columns=['ProjectID', 'UserProfile_Name','data_userProfilePermission'])
    df.to_excel('qTest_UserProfile_Permission.xlsx', index=False)

UserProfile()