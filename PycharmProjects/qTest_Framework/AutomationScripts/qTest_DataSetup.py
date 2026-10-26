import json

import requests
import urllib3

urllib3.disable_warnings()
BASE_URL = "https://qtest-stage.gtie.dell.com"
QTEST_TOKEN = "fda0002f-500a-47c6-b617-0381dc027b39"

def getTestCase():

    response = requests.get(
        url="{}{}".format(BASE_URL, '/api/v3/projects/349/test-cases'),
        headers={
            "Authorization": "Bearer {}".format(QTEST_TOKEN)
        },
        verify=False
    )

    if response.status_code == 200:
        try:
            data = response.json()
            for item in data:
                print(item['parent_id'])
            # TestCaseID = data.get('id')
            # print("TestCaseID:", TestCaseID)
        except json.decoder.JSONDecodeError as e:
            print("Error decoding JSON:", e)
    else:
        print("Error fetching user data. Status code:", response.status_code)
        return

def getTestRun():

    response = requests.get(
        url="{}{}".format(BASE_URL, '/api/v3/projects/370/test-runs'),
        headers={
            "Authorization": "Bearer {}".format(QTEST_TOKEN)
        },
        verify=False
    )

    if response.status_code == 200:
        try:
            data = response.json()
            for item in data['items']:
                print(item['id'])
            # TestCaseID = data.get('id')
            # print("TestCaseID:", TestCaseID)
        except json.decoder.JSONDecodeError as e:
            print("Error decoding JSON:", e)
    else:
        print("Error fetching user data. Status code:", response.status_code)
        return


getTestRun()

