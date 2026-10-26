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

def main():
    export = []

    UD = UserDetails()
    GC = Group_Count()
    UP = UserProfile_Count()

    export.extend(UD)
    export.append(GC)
    export.append(UP)

    df = pd.DataFrame([export],
                      columns=['AppAuth_Count', 'Gtie_Count', 'Internal_Count', 'All_Count', 'InActive_Count', 'Group_Count', 'UserProfile_Count'])
    # df = pd.DataFrame(export)
    df.to_excel('qTest_UserDetails.xlsx', index=False)


def UserDetails():
    UI_UserDetails = []
    AppAuth_Count = 0
    Gtie_Count = 0
    Internal_Count = 0
    All_Count = 0
    InActive_Count = 0
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

        #AppPAth Users
        url = "{}{}".format(BASE_URL, '/admin/user/list-users.json/?range=items=0-199')
        headers = {
            "X-CSRF-Token": "ea1acbd6-f378-4ddb-8699-ebd22e161e0eQASMTY5MzgyNjQ3OTc2OA==",
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            'Cookie': Cookies1
        }
        payload = json.dumps({"authTypeId":[1]})
        AppAuth_response = requests.post(url, headers=headers, data=payload)

        if AppAuth_response.status_code == 200:
            try:
                data = AppAuth_response.json()
                AppAuth = data.get('content-range')
                AppAuth_Count = AppAuth.split('/')[-1]
                print("AppAuth Count", AppAuth_Count)
            except json.decoder.JSONDecodeError as e:
                print("Error decoding JSON:", e)
        else:
            print("Error fetching user data. Status code:", AppAuth_response.status_code)
            return

        #Gtie Users
        url_gtie = "{}{}".format(BASE_URL, '/admin/user/list-users.json/?range=items=0-199')
        headers_gtie = {
            "X-CSRF-Token": "ea1acbd6-f378-4ddb-8699-ebd22e161e0eQASMTY5MzgyNjQ3OTc2OA==",
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            'Cookie': Cookies1
        }
        payload_gtie = json.dumps({"authTypeId":[3]})
        Gtie_response = requests.post(url_gtie, headers=headers_gtie, data=payload_gtie)

        if Gtie_response.status_code == 200:
            try:
                data_gtie = Gtie_response.json()
                Gtie = data_gtie.get('content-range')
                Gtie_Count = Gtie.split('/')[-1]
                print("Gtie Count", Gtie_Count)
            except json.decoder.JSONDecodeError as e:
                print("Error decoding JSON:", e)
        else:
            print("Error fetching user data. Status code:", AppAuth_response.status_code)
            return

        #Internal Users
        url_Internal = "{}{}".format(BASE_URL, '/admin/user/list-users.json/?range=items=0-199')
        headers_Internal = {
            "X-CSRF-Token": "ea1acbd6-f378-4ddb-8699-ebd22e161e0eQASMTY5MzgyNjQ3OTc2OA==",
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            'Cookie': Cookies1
        }
        payload_Internal = json.dumps({"authTypeId":[-1]})
        Internal_response = requests.post(url_Internal, headers=headers_Internal, data=payload_Internal)

        if Internal_response.status_code == 200:
            try:
                data_Internal = Internal_response.json()
                Internal = data_Internal.get('content-range')
                Internal_Count = Internal.split('/')[-1]
                print("Internal Count", Internal_Count)
            except json.decoder.JSONDecodeError as e:
                print("Error decoding JSON:", e)
        else:
            print("Error fetching user data. Status code:", AppAuth_response.status_code)
            return


        #All Users
        url_All = "{}{}".format(BASE_URL, '/admin/user/list-users.json/?range=items=0-199')
        headers_All = {
            "X-CSRF-Token": "ea1acbd6-f378-4ddb-8699-ebd22e161e0eQASMTY5MzgyNjQ3OTc2OA==",
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            'Cookie': Cookies1
        }
        payload_All = json.dumps({})
        All_response = requests.post(url_All, headers=headers_All, data=payload_All)

        if All_response.status_code == 200:
            try:
                data_All = All_response.json()
                All = data_All.get('content-range')
                All_Count = All.split('/')[-1]
                print("All User Count", All_Count)
            except json.decoder.JSONDecodeError as e:
                print("Error decoding JSON:", e)
        else:
            print("Error fetching user data. Status code:", AppAuth_response.status_code)
            return

        #InActive Users
        url_InActive = "{}{}".format(BASE_URL, '/admin/user/list-users-include-archived.json/?range=items=0-199')
        headers_InActive = {
            "X-CSRF-Token": "ea1acbd6-f378-4ddb-8699-ebd22e161e0eQASMTY5MzgyNjQ3OTc2OA==",
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            'Cookie': Cookies1
        }
        payload_InActive = json.dumps({"status":[3]})
        InActive_response = requests.post(url_InActive, headers=headers_InActive, data=payload_InActive)

        if All_response.status_code == 200:
            try:
                data_InActive = InActive_response.json()
                InActive = data_InActive.get('content-range')
                InActive_Count = InActive.split('/')[-1]
                print("InActive Count", InActive_Count)
            except json.decoder.JSONDecodeError as e:
                print("Error decoding JSON:", e)
        else:
            print("Error fetching user data. Status code:", AppAuth_response.status_code)
            return

        # UI_UserDetails.append([AppAuth_Count, Gtie_Count, Internal_Count, All_Count, InActive_Count])
        # print(UI_UserDetails)
        return AppAuth_Count, Gtie_Count, Internal_Count, All_Count, InActive_Count





    finally:
        # Logout
        url2 = "{}{}".format(BASE_URL, Logout_API)
        payload2 = ""
        headers2 = {
            'Cookie': Cookies1
        }
        response2 = requests.request("GET", url2, headers=headers2, data=payload2)

def Group_Count():
    group_response = requests.get(
        url="{}{}".format(BASE_URL, '/api/v3/groups'),
        headers={
            "Authorization": "Bearer {}".format(QTEST_TOKEN)
        },
        verify=False
    )

    if group_response.status_code == 200:
        try:
            data = group_response.json()
            Total_Group = []
            for item in data:
                Total_Group.append(item.get('id'))
            print("Total_Group:", len(Total_Group))
            Group = len(Total_Group)
            return Group
        except json.decoder.JSONDecodeError as e:
            print("Error decoding JSON:", e)
    else:
        print("Error fetching user data. Status code:", group_response.status_code)
        return
def UserProfile_Count():
    userProfile_response = requests.get(
        url="{}{}".format(BASE_URL, '/api/v3/user-profiles'),
        headers={
            "Authorization": "Bearer {}".format(QTEST_TOKEN)
        },
        verify=False
    )

    if userProfile_response.status_code == 200:
        try:
            data = userProfile_response.json()
            Total_UserProfile = data.get('total_user_profiles')
            print("Total_UserProfile:", Total_UserProfile)
            return Total_UserProfile
        except json.decoder.JSONDecodeError as e:
            print("Error decoding JSON:", e)
    else:
        print("Error fetching user data. Status code:", userProfile_response.status_code)
        return



if __name__ == '__main__':
    main()