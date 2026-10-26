import json

import pandas as pd
import requests
from csv import writer

BASE_URL = "https://qtest.gtie.dell.com"
QTEST_TOKEN = "a5023327-1321-4b8d-a3c2-cefd4e9ecb1e"
Login_API = "/login?redirect=https://qtest.gtie.dell.com/portal/project&requestNonce=MC44Nzg2ODE5OTM4OTkz1245"
# PrefixSetting_API = "/p/323/portal/uid/settings"
PrefixSetting_API = "/portal/uid/settings"
Logout_API = '/logout'

def qTest_IntegrationDetails():
    export = []

    try:
        # Login
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

        # prjID = [322, 323, 331, 320, 321, 315, 316, 317, 318, 319, 324, 325, 326, 327, 328, 329, 330, 332, 304, 337, 351, 363]
        prjID = [317, 328, 320, 333, 327, 323, 326, 316, 330, 331, 325, 434, 321, 318, 363, 351, 324, 329, 332, 337, 438, 304, 315, 319, 322]

        # Get Integration Details

        for i in range(len(prjID)):
            ProjectID = '/p/' + str(prjID[i])
            url1 = "{}{}{}".format(BASE_URL, ProjectID, PrefixSetting_API)
            payload1 = ""
            headers1 = {
                'Cookie': Cookies1
            }

            response1 = requests.request("GET", url1, headers=headers1, data=payload1)
            # print(response1.content)
            if response.status_code == 200:
                try:
                    prefix_list = []
                    PrefixSetting_Response = response1.json()
                    for item in PrefixSetting_Response['result']:
                        prefix_list.append(item['prefix'])
                    # List = [prjID[i], prefix_list]
                    export.append([prjID[i], prefix_list])

                except json.decoder.JSONDecodeError as e:
                    print("Error decoding JSON:", e)
            else:
                print("Error fetching user data. Status code:", response.status_code)
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
                      columns=['prjID', 'prefix_list'])
    df.to_excel('qTest_ODMPrefix.xlsx', index=False)







qTest_IntegrationDetails()
