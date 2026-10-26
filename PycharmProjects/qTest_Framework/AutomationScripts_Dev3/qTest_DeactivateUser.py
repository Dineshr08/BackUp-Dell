import json

import requests
import urllib3

urllib3.disable_warnings()
BASE_URL = "https://qtest-dev3.gtie.dell.com"
QTEST_TOKEN = "29421d63-7c39-437f-83df-c9ac63ab774a"

def Activate():

    UserID = [13281,13282,13283,13284,13285,13286,13287,13288,13289,13290,13291,13292,13293,13294,13295,13296,13297,13298,13299,13300]

    for User in UserID:
        try:
            response = requests.put(
                url="{}{}{}".format(BASE_URL, '/api/v3/users/', User),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer {}".format(QTEST_TOKEN)
                },
                data='{"status": 3}',
                verify=False
            )
            if response.status_code == 200:
                print(f"User {User} updated successfully.")
            else:
                print(f"User {User} update failed with status code {response.status_code}.")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while updating User {User}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while updating User {User}: {e}")



Activate()

