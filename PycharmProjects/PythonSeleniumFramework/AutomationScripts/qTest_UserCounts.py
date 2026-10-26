import json

import requests
import urllib3

urllib3.disable_warnings()
BASE_URL = "https://qtest-stage.gtie.dell.com"
QTEST_TOKEN = "cbe60e5b-7969-4505-84a9-d42d3015b0da"

def UserCounts():

    response = requests.get(
        url="{}{}".format(BASE_URL, '/api/v3/search/user?inactive=true&pagination=false'),
        headers={
            "Authorization": "Bearer {}".format(QTEST_TOKEN)
        },
        verify=False
    )
    Active_Count = 0
    Deactive_Count = 0

    if response.status_code == 200:
        try:
            data = response.json()
            Total_User = data.get('total')
            for item in data['items']:
                if item['status'] == 1:
                    Active_Count += 1
                elif item['status'] == 3:
                    Deactive_Count += 1
            print("Total_User:", Total_User)
            print("Active_User:", Active_Count)
            print("InActive_User:", Deactive_Count)
        except json.decoder.JSONDecodeError as e:
            print("Error decoding JSON:", e)
    else:
        print("Error fetching user data. Status code:", response.status_code)
        return

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
        except json.decoder.JSONDecodeError as e:
            print("Error decoding JSON:", e)
    else:
        print("Error fetching user data. Status code:", userProfile_response.status_code)
        return

UserCounts()
Group_Count()
UserProfile_Count()
