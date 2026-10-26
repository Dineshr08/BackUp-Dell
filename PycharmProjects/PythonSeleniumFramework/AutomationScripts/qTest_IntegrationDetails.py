import pandas as pd
import requests
from csv import writer

BASE_URL = "https://qtest-stage.gtie.dell.com"
QTEST_TOKEN = "cbe60e5b-7969-4505-84a9-d42d3015b0da"
Login_API = "/login?redirect=https://qtest-stage.gtie.dell.com/portal/project&requestNonce=MC44Nzg2ODE5OTM4OTkz1245"
# Integration_API = "/p/45/portal/defect/integration/setting/connection/list/9?dojo.preventCache=0.1208288477138908"
Integration_API = "/portal/defect/integration/setting/connection/list/9?dojo.preventCache=0.1208288477138908"
Logout_API = '/logout'
Project_API = "/api/v3/projects?assigned=false"
def qTest_IntegrationDetails():
    export = []

    try:
        # Login
        url = "{}{}".format(BASE_URL, Login_API)
        payload = 'j_username=dinesh_r3&j_password=Password%408&requestNonce=MC44Nzg2ODE5OTM4OTkz1245&service='
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

        # Get list of project

        url3 = "{}{}".format(BASE_URL, Project_API)
        headers3 = {
            "Authorization": "Bearer {}".format(QTEST_TOKEN)
        }
        response3 = requests.request("GET", url3, headers=headers3)
        project_info = response3.json()
        prjID = []
        for item in project_info:
            prjID.append(item['id'])

        print(prjID)
        print(len(prjID))

        # Get Integration Details

        for i in range(len(prjID)):
            ProjectID = '/p/' + str(prjID[i])
            url1 = "{}{}{}".format(BASE_URL, ProjectID, Integration_API)
            payload1 = ""
            headers1 = {
                'Cookie': Cookies1
            }
            # print(url1)

            response1 = requests.request("GET", url1, headers=headers1, data=payload1)

            if response1.status_code == 200:
                try:
                    Integration_Response = response1.json()

                    # if response1.status_code == 200 and len(Integration_Response["items"]) != 0 and not
                    # Integration_Response["items"][0]["name"].startswith("AT_ConnectionName"):
                    if len(Integration_Response.get("items", [])) > 0 and not Integration_Response["items"][0][
                        "name"].startswith("AT_ConnectionName"):
                        Configured_Name = Integration_Response["items"][0]["name"]
                        Configured_ServerURL = Integration_Response["items"][0]["serverURL"]
                        Configured_Username = Integration_Response["items"][0]["username"]
                        Configured_Status = Integration_Response["items"][0]["active"]
                        Configured_project = Integration_Response["items"][0]["projectName"]
                        print(Configured_Name, "|", Configured_ServerURL, "|", Configured_Username, "|",
                              Configured_Status, "|",
                              Configured_project)
                        export.append([Configured_Name, Configured_ServerURL, Configured_Username, Configured_Status,
                                       Configured_project])
                except ValueError as e:
                    print(f"Error parsing JSON response: {e}")

    finally:
        # Logout
        url2 = "{}{}".format(BASE_URL, Logout_API)
        payload2 = ""
        headers2 = {
            'Cookie': Cookies1
        }

        response2 = requests.request("GET", url2, headers=headers2, data=payload2)
    df = pd.DataFrame(export, columns=['Configured_Name', 'Configured_ServerURL', 'Configured_Username', 'Configured_Status',
                        'Configured_project'])
    df.to_excel('qTest_IntegrationDetails.xlsx', index=False)


qTest_IntegrationDetails()
