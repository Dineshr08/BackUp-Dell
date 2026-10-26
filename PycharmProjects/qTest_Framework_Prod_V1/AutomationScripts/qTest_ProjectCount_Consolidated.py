import json
from ldap3 import Server, Connection, ALL
import requests
import urllib3
from base64 import b64encode
from datetime import date
from csv import writer

urllib3.disable_warnings()

# # The qTest dev instance
# BASE_URL = "https://qtest-dev01.cec.lab.emc.com"
# QTEST_TOKEN = "35828588-9edc-4e3f-ba0b-78a1928f3dab"

# # The qTest dev02 instance
# BASE_URL = "https://qtest-dev02.cec.lab.emc.com"
# QTEST_TOKEN = "3b187b52-9d61-452e-8f30-b2fd131cff22"


# # The qTest dev03 instance
# BASE_URL = "https://qtest-dev3.gtie.dell.com"
# QTEST_TOKEN = "2af0e0fe-bdd6-4955-b702-14e66c19c79b"


# # The qTest stage instance
# BASE_URL = "https://qtest-stage.gtie.dell.com"
# TEST_TOKEN = "fdc00b0f-f68e-4d5c-986c-7910645ca62e"

# The qTest production instance
BASE_URL = "https://qtest.gtie.dell.com"
QTEST_TOKEN = "fdc00b0f-f68e-4d5c-986c-7910645ca62e"

API_PROJECTS = "/api/v3/projects?assigned=true"  # assigned=true only for assigned projects && assigned=false for all projects
API_TESTRUNS = "/test-runs?parentId=0&parentType=root&expand=descendants"  # Get Test Runs


# prjID = 0
def qTest_Connection(ldap_user_name, ldap_credential):
    server = Server("appauth.corp.emc.com", 636, use_ssl=True, get_info=ALL)
    with Connection(server, ldap_user_name, ldap_credential) as conn:
        conn.start_tls()
        if conn.bound == True:
            print("Connection Successful")
        else:
            print("Not a Success")


def get_total_TestRuns(ldap_user_name, ldap_credential):
    prjTmp = 0
    trTmp = 0
    tcTmp = 0
    reqTmp = 0

    # Get Multiple Projects API
    response = requests.get(
        url="{}{}".format(BASE_URL, API_PROJECTS),
        headers={
            "Authorization": "Bearer {}".format(QTEST_TOKEN)
        },
        verify=False
    )

    project_info = response.json()
    for item in project_info:

        prjID = item['id']

        if prjID != 0:
            prjTmp = prjTmp + 1

        prjName = item['name']

        response = requests.get(
            url="{}{}{}{}".format(BASE_URL, '/api/v3/projects/', prjID, API_TESTRUNS),
            headers={
                "Authorization": "Bearer {}".format(QTEST_TOKEN)
            },
            verify=False
        )

        testRun_info = response.json()
        if response.status_code == 200:
            if "total" in testRun_info:
                totalTR = (testRun_info["total"])
                trTmp = trTmp + totalTR

            else:
                print("Error :", (testRun_info["message"]))
        else:
            print(response.status_code, ":", (testRun_info["message"]))

        body = {}
        body = {"object_type": "test-cases", "fields": ["id"], "query": ""}
        response1 = requests.post(
            url="{}{}{}{}".format(BASE_URL, '/api/v3/projects/', prjID, '/search?page=1&pageSize=1'),
            headers={
                "Authorization": "Bearer {}".format(QTEST_TOKEN),
                "Content-Type": "application/json"
            },
            json=body,
            verify=False
        )
        testCase_info = response1.json()
        if response.status_code == 200:
            if "total" in testCase_info:
                totalTC = (testCase_info["total"])
                tcTmp = tcTmp + totalTC


            else:
                print("Error :", (testCase_info["message"]))
        else:
            print(response.status_code, ":", (testCase_info["message"]))
        ######

        body = {}
        body = {"object_type": "requirements", "fields": ["id"], "query": ""}
        response1 = requests.post(
            url="{}{}{}{}".format(BASE_URL, '/api/v3/projects/', prjID, '/search?page=1&pageSize=1'),
            headers={
                "Authorization": "Bearer {}".format(QTEST_TOKEN),
                "Content-Type": "application/json"
            },
            json=body,
            verify=False
        )
        req_info = response1.json()
        if response.status_code == 200:
            if "total" in req_info:
                totalReq = (req_info["total"])
                reqTmp = reqTmp + totalReq


            else:
                print("Error :", (req_info["message"]))
        else:
            print(response.status_code, ":", (req_info["message"]))

    # print ("Total Test Runs :", totalTR,  "|", "Total Test Case :", totalTC, "|", "Project ID :",prjID, "|", "Project Name :", prjName ,"|", "Total Reqs :", totalReq)
    print("Total number of projects =", + prjTmp)
    print("Total number of Requirements =", + reqTmp)

    print("Total number of Test Cases =", + tcTmp)
    print("Total number of Test Runs =", + trTmp)

    response = requests.get(
        url="{}{}".format(BASE_URL, '/api/v3/search/user?inactive=true'),
        headers={
            "Authorization": "Bearer {}".format(QTEST_TOKEN)
        },
        verify=False
    )

    user_info = response.json()
    if response.status_code == 200:
        if "total" in user_info:
            userTotal = (user_info["total"])

    print("Total qTest Users :", userTotal)

    response = requests.get(
        url="{}{}".format(BASE_URL, '/api/v3/search/user?inactive=false'),
        headers={
            "Authorization": "Bearer {}".format(QTEST_TOKEN)
        },
        verify=False
    )

    user2_info = response.json()
    if response.status_code == 200:
        if "total" in user2_info:
            userTotal2 = (user2_info["total"])

    print("Total Active qTest Users :", userTotal2)

    today = date.today()
    # print("Today date is: ", today)

    List = [today, prjTmp, reqTmp, tcTmp, trTmp, userTotal, userTotal2, BASE_URL]

    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open('qTestConsolidated.csv', 'a') as f_object:

        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)

        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(List)

        # Close the file object
        f_object.close()


# Disable JIRA integration for either assigned or all projects
get_total_TestRuns("americas\svc_npieoinfra1", "C_*81hPzN~3bJIQTVyaDrwES")


