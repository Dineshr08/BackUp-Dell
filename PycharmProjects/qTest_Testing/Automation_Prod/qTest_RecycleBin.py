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

def qTest_RecycleBin():

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

        # Get RecycleBin details

        start = 0
        end = 5437
        interval = 20





        for i in range(start, end, interval):
            end_range = i+19
            print(i)
            print(end_range)

            # test case included https://qtest.gtie.dell.com/p/138/portal/tree/recycleActions/9,1/?range=items%3D0-19

            # url1 = "{}{}".format(BASE_URL, '/p/138/portal/tree/recycleActions/9/?range=items%3D5420-5439')
            url1 = "{}{}{}{}{}".format(BASE_URL, '/p/138/portal/tree/recycleActions/9/?range=items%3D',i,'-',end_range)
            payload1 = ""
            headers1 = {
                'Cookie': Cookies1
            }

            response1 = requests.request("GET", url1, headers=headers1, data=payload1)
            print(response1.text)

            with open('Recyclebin.txt', 'a') as file:
                # Write data to the file
                file.write(response1.text)



    finally:
        # Logout
        url2 = "{}{}".format(BASE_URL, Logout_API)
        payload2 = ""
        headers2 = {
            'Cookie': Cookies1
        }

        response2 = requests.request("GET", url2, headers=headers2, data=payload2)

qTest_RecycleBin()

