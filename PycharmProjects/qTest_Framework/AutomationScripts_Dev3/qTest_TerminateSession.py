import json

import pandas as pd
import requests
from csv import writer

import urllib3

urllib3.disable_warnings()
BASE_URL = "https://qtest-dev3.gtie.dell.com"
QTEST_TOKEN = "29421d63-7c39-437f-83df-c9ac63ab774a"
Login_API = "/login?redirect=https://qtest-dev3.gtie.dell.com/portal/project&requestNonce=MC44Nzg2ODE5OTM4OTkz1245"
Logout_API = '/logout'

def qTest_TerminateSession():
    SessionID = []

    try:
        # Login
        url = "{}{}".format(BASE_URL, Login_API)
        payload = 'j_username=dinesh_r3&j_password=Password%4011&requestNonce=MC44Nzg2ODE5OTM4OTkz1245&service='
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'JSESSIONID=qtest-dev03-app~77753BDA0F21DDD86018175B4FBEE65A; UserContextToken=YTNhMTQ5MjMtNzhhMS00ZTM5LTk4Y2MtMjYyOGMyYzlmMTQy'
        }
        session = requests.Session()
        response = session.post(url, headers=headers, data=payload)
        Cookies = session.cookies.get('UserContextToken')
        print(Cookies)
        Cookies1 = 'UserContextToken=' + Cookies
        print(Cookies1)

        #get all session details

        session_response = requests.get(
            url="{}{}".format(BASE_URL, '/admin/setting/concurrency/sessions?dojo.preventCache=0.21454942796969756'),
            headers={
                'Cookie': Cookies1
            },
            verify=False
        )

        SessionResponse = session_response.json()

        for session in SessionResponse['activeSessionDTOs']:
            if session['email'].startswith('ptuser'):
                SessionID.append(session['sessionId'])

        #TerminateSessions

        for Terminate in SessionID:
            Terminate_response = requests.delete(
            url="{}{}{}{}".format(BASE_URL, '/admin/setting/concurrency/session/', Terminate, '?dojo.preventCache=0.47412399245599013'),
            headers = {
                'Cookie': Cookies1
            },
            verify = False
            )

    finally:
        # Logout
        url2 = "{}{}".format(BASE_URL, Logout_API)
        payload2 = ""
        headers2 = {
            'Cookie': Cookies1
        }

        response2 = requests.request("GET", url2, headers=headers2, data=payload2)

qTest_TerminateSession()
