import json

import pandas as pd
import requests
from csv import writer
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()
BASE_URL = "https://qtest.gtie.dell.com"
QTEST_TOKEN = "a5023327-1321-4b8d-a3c2-cefd4e9ecb1e"
Login_API = "/login?redirect=https://qtest.gtie.dell.com/portal/project&requestNonce=MC44Nzg2ODE5OTM4OTkz1245"
Logout_API = '/logout'


def API_TokenValidation():
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


        API_Token = requests.get(
            url="{}{}".format(BASE_URL, '/p/45/portal/resource/main'),
            headers={
                'Cookie': Cookies1
            },
            verify=False
        )

        # Parse the HTML content
        soup = BeautifulSoup(API_Token.text, 'html.parser')

        # Find the elements containing the Bearer tokens
        bearer_token_elements = soup.find_all('span', {'class': 'highlight-text'})

        # Exclude the value associated with the specified span id
        excluded_token_id = 'legacy-user-access-token'
        bearer_tokens = [element.text for element in bearer_token_elements if element.get('id') != excluded_token_id]

        # Create a DataFrame to store the Bearer tokens
        data = {'Bearer Token': bearer_tokens}
        df = pd.DataFrame(data)

        # Write to Excel
        excel_file = 'qTest_BearerToken.xlsx'
        df.to_excel(excel_file, index=False)

        print('Bearer tokens extracted (excluding the specified token) and saved to', excel_file)


    finally:
        # Logout
        url2 = "{}{}".format(BASE_URL, Logout_API)
        payload2 = ""
        headers2 = {
            'Cookie': Cookies1
        }
        response2 = requests.request("GET", url2, headers=headers2, data=payload2)
    # df = pd.DataFrame(export, columns=['sharing_info', 'ProjectShared'])
    # df.to_excel('qTest_TestCaseSharing.xlsx', index=False)

API_TokenValidation()