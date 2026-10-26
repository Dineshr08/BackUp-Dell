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

def qTest_LoadProject():

    users = [
        "ptuser1@dell.com",
        "ptuser2@dell.com",
        "ptuser3@dell.com",
        "ptuser4@dell.com",
        "ptuser5@dell.com",
        "ptuser6@dell.com",
        "ptuser7@dell.com",
        "ptuser8@dell.com",
        "ptuser9@dell.com",
        "ptuser10@dell.com",
        "ptuser11@dell.com",
        "ptuser12@dell.com",
        "ptuser13@dell.com",
        "ptuser14@dell.com",
        "ptuser15@dell.com",
        "ptuser16@dell.com",
        "ptuser17@dell.com",
        "ptuser18@dell.com",
        "ptuser19@dell.com",
        "ptuser20@dell.com",
        "ptuser21@dell.com",
        "ptuser22@dell.com",
        "ptuser23@dell.com",
        "ptuser24@dell.com",
        "ptuser25@dell.com",
        "ptuser26@dell.com",
        "ptuser27@dell.com",
        "ptuser28@dell.com",
        "ptuser29@dell.com",
        "ptuser30@dell.com",
        "ptuser31@dell.com",
        "ptuser32@dell.com",
        "ptuser33@dell.com",
        "ptuser34@dell.com",
        "ptuser35@dell.com",
        "ptuser36@dell.com",
        "ptuser37@dell.com",
        "ptuser38@dell.com",
        "ptuser39@dell.com",
        "ptuser40@dell.com",
        "ptuser41@dell.com",
        "ptuser42@dell.com",
        "ptuser43@dell.com",
        "ptuser44@dell.com",
        "ptuser45@dell.com",
        "ptuser46@dell.com",
        "ptuser47@dell.com",
        "ptuser48@dell.com",
        "ptuser49@dell.com",
        "ptuser50@dell.com",
        "ptuser51@dell.com",
        "ptuser52@dell.com",
        "ptuser53@dell.com",
        "ptuser54@dell.com",
        "ptuser55@dell.com",
        "ptuser56@dell.com",
        "ptuser57@dell.com",
        "ptuser58@dell.com",
        "ptuser59@dell.com",
        "ptuser60@dell.com",
        "ptuser61@dell.com",
        "ptuser62@dell.com",
        "ptuser63@dell.com",
        "ptuser64@dell.com",
        "ptuser65@dell.com",
        "ptuser66@dell.com",
        "ptuser67@dell.com",
        "ptuser68@dell.com",
        "ptuser69@dell.com",
        "ptuser70@dell.com"
    ]

    for user in users:

        # Login
        url = "{}{}".format(BASE_URL, Login_API)
        payload = "{}{}{}".format('j_username=', user,
                                '&j_password=Password%401&requestNonce=MC44Nzg2ODE5OTM4OTkz1245&service=')
        # payload = 'j_username=dinesh_r3&j_password=Password%401&requestNonce=MC44Nzg2ODE5OTM4OTkz1245&service='
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

        if Cookies:

            try:
                # Load Project
                LoadProject_response = requests.get(
                    url="{}{}".format(BASE_URL, '/p/45/portal/project'),
                    headers={
                        'Cookie': Cookies1
                    },
                    verify=False
                )

                if LoadProject_response.status_code == 200:
                    print(f"Project Loaded successfully.")
                else:
                    print(f"User {user} update failed with status code {LoadProject_response.status_code}.")

            finally:
                # Logout
                url2 = "{}{}".format(BASE_URL, Logout_API)
                payload2 = ""
                headers2 = {
                    'Cookie': Cookies1
                }
                response2 = requests.request("GET", url2, headers=headers2, data=payload2)


        else:
            print("UserContextToken is empty, skipping user:", user)

qTest_LoadProject()
