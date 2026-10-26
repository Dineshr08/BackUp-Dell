import json

import pandas as pd
import requests
from csv import writer
import urllib3
import urllib3
urllib3.disable_warnings()
BASE_URL = "https://qtest-dev3.gtie.dell.com"
QTEST_TOKEN = "29421d63-7c39-437f-83df-c9ac63ab774a"
Login_API = "/login?redirect=https://qtest-dev3.gtie.dell.com/portal/project&requestNonce=MC44Nzg2ODE5OTM4OTkz1245"
Integration_API = "/portal/defect/integration/setting/connection/list/9?dojo.preventCache=0.1208288477138908"
Logout_API = '/logout'
Project_API = "/api/v3/projects?assigned=false"

def qTest_ActivateIntegrationDetails_Dev():
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

            # prjID = [45]

            for Project_ID in prjID:
                Connection_Response = requests.get(
                    url="{}{}{}{}".format(BASE_URL, '/p/',Project_ID, '/portal/defect/integration/setting/connection/list/9?dojo.preventCache=0.28221418647330476'),
                    headers={
                        'Cookie': Cookies1
                    },
                    verify=False
                )
                if Connection_Response.status_code == 200:
                    Connection_info = Connection_Response.json()
                    items_data = Connection_info.get('items', [])
                    if items_data:
                        id_count = 0
                        for item in Connection_info['items']:
                            if 'id' in item:
                                id_count += 1
                        if id_count == 1:
                            for data in Connection_info['items']:
                                extracted_item = {
                                    "id": data.get("id"),
                                    "name": data.get("name"),
                                    "serverURL": data.get("serverURL"),
                                    "username": data.get("username"),
                                    "systemId": data.get("systemId")
                                }
                                # print("Connection Inputs:", extracted_item)

                                if "cec" in extracted_item['serverURL']:
                                    password = '*?w2Xt1+uBY3z~A_69v0mNJH'
                                    serverURL = 'https://jira-dev6.cec.lab.emc.com'
                                elif "gtie" in extracted_item['serverURL']:
                                    password = 'Ytnf3kjr3*64vdb3d'
                                    serverURL = 'https://jira1-dev7.gtie.dell.com'

                                id = extracted_item['id']
                                systemId = extracted_item['systemId']
                                name = extracted_item['name']
                                serverURL = serverURL
                                username = extracted_item['username']

                                # Test Jira Connection
                                url = "{}{}{}{}".format(BASE_URL, '/p/', Project_ID,
                                                    '/portal/defect/integration/setting/connection/test')

                                payload_data = {
                                        'id': id,
                                        'systemId': systemId,
                                        'name': name,
                                        'serverURL': serverURL,
                                        'webURL': serverURL,
                                        'username': username,
                                        'password': password,
                                        'isIssueMigrationConnection': False
                                    }

                                payload = {
                                    "data": json.dumps(payload_data),  # Convert the dynamic values to a JSON string
                                    "dojo.preventCache": "0.08894175726338172"
                                }

                                headers = {
                                    "X-CSRF-Token": "ea1acbd6-f378-4ddb-8699-ebd22e161e0eQASMTY5MzgyNjQ3OTc2OA==",
                                    'Cookie': Cookies1
                                }

                                TestJiraConnection_Response = requests.request("POST", url, headers=headers, data=payload)

                                if TestJiraConnection_Response.status_code == 200:
                                    TestJiraConnection_info = TestJiraConnection_Response.json()
                                    # print(TestJiraConnection_info)
                                    if TestJiraConnection_info.get("status"):
                                        #Save Connection
                                        url = "{}{}{}{}".format(BASE_URL, '/p/', Project_ID,
                                                                '/portal/defect/integration/setting/connection/update')

                                        SaveJiraConnection_Response = requests.request("POST", url, headers=headers,
                                                                                       data=payload)
                                        if SaveJiraConnection_Response.status_code == 200:
                                            SaveJiraConnection_info = SaveJiraConnection_Response.json()
                                            # print(SaveJiraConnection_info)
                                            if SaveJiraConnection_info.get("status"):
                                                #Save and Activate Connection
                                                url = "{}{}{}{}".format(BASE_URL, '/p/', Project_ID,
                                                                        '/portal/defect/integration/setting/update')
                                                payload_data = {
                                                    'usingInternalSystem': False,
                                                    'activeConnectionId': id,
                                                    'deletingConnectionIds': [],
                                                    'externalSystemId': 9
                                                }

                                                payload = {
                                                    "data": json.dumps(payload_data),
                                                    # Convert the dynamic values to a JSON string
                                                    "dojo.preventCache": "0.08894175726338172"
                                                }

                                                SaveActivateJiraConnection_Response = requests.request("POST", url,
                                                                                               headers=headers,
                                                                                               data=payload)
                                                if SaveActivateJiraConnection_Response.status_code == 200:
                                                    SaveActivateJiraConnection_info = SaveActivateJiraConnection_Response.json()
                                                    print(
                                                        "Save and Activate Jira Connection is successful for Project ID:",
                                                        Project_ID,
                                                        "with Status Code:", TestJiraConnection_Response.status_code)
                                                else:
                                                    print(
                                                        "Save and Activate Jira Connection is not successful for Project ID:",
                                                        Project_ID,
                                                        "with Status Code:", TestJiraConnection_Response.status_code)

                                            else:
                                                print("Save and Activate Jira Connection is not successful for Project ID:",
                                                      Project_ID,
                                                      "with Status Code:", TestJiraConnection_Response.status_code)
                                        else:
                                            print("Save Jira Connection is not successful for Project ID:", Project_ID,
                                                  "with Status Code:", TestJiraConnection_Response.status_code)


                                    else:
                                        print("Test Jira Connection is not successful for Project ID:", Project_ID, "with Status Code:", TestJiraConnection_Response.status_code)
                                else:
                                    print("Test Jira Connection is not successful for Project ID:", Project_ID, "with Status Code:", TestJiraConnection_Response.status_code)




                        else:
                            print("Project with Multiple Integration Connection", Project_ID)
                    else:
                        print("Project without Integration Connection", Project_ID)
                else:
                    print("Access Denied for the Project ",Project_ID, "with Status code", Connection_Response.status_code)


    finally:
        # Logout
        url2 = "{}{}".format(BASE_URL, Logout_API)
        payload2 = ""
        headers2 = {
            'Cookie': Cookies1
        }

        response2 = requests.request("GET", url2, headers=headers2, data=payload2)


qTest_ActivateIntegrationDetails_Dev()
