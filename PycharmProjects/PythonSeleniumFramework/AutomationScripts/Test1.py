import json
from ldap3 import Server, Connection, ALL
import requests
import urllib3
from base64 import b64encode
from datetime import date
from csv import writer
import openpyxl
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

urllib3.disable_warnings()

# # The qTest dev instance
# BASE_URL = "https://qtest-dev01.cec.lab.emc.com"
# QTEST_TOKEN = "35828588-9edc-4e3f-ba0b-78a1928f3dab"

# # The qTest dev02 instance
# BASE_URL = "https://qtest-dev02.cec.lab.emc.com"
# QTEST_TOKEN = "3b187b52-9d61-452e-8f30-b2fd131cff22"


# # The qTest dev03 instance
BASE_URL = "https://qtest-stage.gtie.dell.com"
QTEST_TOKEN = "cbe60e5b-7969-4505-84a9-d42d3015b0da"

# # The qTest stage instance
# BASE_URL = "https://qtest-stage.gtie.dell.com"
# QTEST_TOKEN = "fdc00b0f-f68e-4d5c-986c-7910645ca62e"

# The qTest production instance
# BASE_URL = "https://qtest.gtie.dell.com"
# QTEST_TOKEN = "fdc00b0f-f68e-4d5c-986c-7910645ca62e"

ldap_user_name = 'americas\svc_npieoinfra1'
ldap_credential = 'C_*81hPzN~3bJIQTVyaDrwES'

API_PROJECTS = "/api/v3/projects?assigned=true"  # assigned=true only for assigned projects && assigned=false for all projects
API_TESTRUNS = "/test-runs?parentId=0&parentType=root&expand=descendants"  # Get Test Runs


def main():
    prjTmp = 0
    trTmp = 0
    tcTmp = 0
    reqTmp = 0
    List = []

    for item in get_Project_Info(ldap_user_name, ldap_credential):
        prjID = item['id']
        if prjID != 0:
            prjTmp = prjTmp + 1

        prjName = item['name']

        totalTR = get_testRun_Info(ldap_user_name, ldap_credential, prjID)[0]
        trTmp = trTmp + totalTR

        totalTC = get_testCase_Info(ldap_user_name, ldap_credential, prjID)[0]
        tcTmp = tcTmp + totalTC

        totalReq = get_requirements_Info(ldap_user_name, ldap_credential, prjID)[0]
        reqTmp = reqTmp + totalReq

        List = [prjName, totalReq, totalTC, totalTR]
        print(List)

    userTotal = total_users(ldap_user_name, ldap_credential)
    userTotal2 = active_users(ldap_user_name, ldap_credential)
    print("Total Projects : ", prjTmp)
    print("Total Requirements :", reqTmp)
    print("Total Test cases :", tcTmp)
    print("Total Test Runs : ", trTmp)
    print("Total qTest Users :", userTotal)
    print("Total Active qTest Users :", userTotal2)


def qTest_Connection(ldap_user_name, ldap_credential):
    server = Server("appauth.corp.emc.com", 636, use_ssl=True, get_info=ALL)
    with Connection(server, ldap_user_name, ldap_credential) as conn:
        conn.start_tls()
        if conn.bound == True:
            print("Connection Successful")
        else:
            print("Not a Success")


def get_Project_Info(ldap_user_name, ldap_credential):
    response = requests.get(
        url="{}{}".format(BASE_URL, API_PROJECTS),
        headers={
            "Authorization": "Bearer {}".format(QTEST_TOKEN)
        },
        verify=False
    )

    project_info = response.json()
    return project_info
    return prjID


def get_testRun_Info(ldap_user_name, ldap_credential, prjID):
    trTmp = 0

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
    trTmp = trTmp + totalTR
    return totalTR, trTmp


def get_testCase_Info(ldap_user_name, ldap_credential, prjID):
    tcTmp = 0
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
    if response1.status_code == 200:
        if "total" in testCase_info:
            totalTC = (testCase_info["total"])
            tcTmp = tcTmp + totalTC


        else:
            print("Error :", (testCase_info["message"]))
    else:
        print(response1.status_code, ":", (testCase_info["message"]))
    tcTmp = tcTmp + totalTC
    return totalTC, tcTmp


def get_requirements_Info(ldap_user_name, ldap_credential, prjID):
    reqTmp = 0
    body = {}
    body = {"object_type": "requirements", "fields": ["id"], "query": ""}
    response2 = requests.post(
        url="{}{}{}{}".format(BASE_URL, '/api/v3/projects/', prjID, '/search?page=1&pageSize=1'),
        headers={
            "Authorization": "Bearer {}".format(QTEST_TOKEN),
            "Content-Type": "application/json"
        },
        json=body,
        verify=False
    )
    req_info = response2.json()
    if response2.status_code == 200:
        if "total" in req_info:
            totalReq = (req_info["total"])
            reqTmp = reqTmp + totalReq


        else:
            print("Error :", (req_info["message"]))
    else:
        print(response2.status_code, ":", (req_info["message"]))
    reqTmp = reqTmp + totalReq
    return totalReq, reqTmp


def total_users(ldap_user_name, ldap_credential):
    userTotal = 0

    responseTU = requests.get(
        url="{}{}".format(BASE_URL, '/api/v3/search/user?inactive=true'),
        headers={
            "Authorization": "Bearer {}".format(QTEST_TOKEN)
        },
        verify=False
    )

    user_info = responseTU.json()
    if responseTU.status_code == 200:
        if "total" in user_info:
            userTotal = (user_info["total"])

    return userTotal


def active_users(ldap_user_name, ldap_credential):
    userTotal2 = 0
    responseAU = requests.get(
        url="{}{}".format(BASE_URL, '/api/v3/search/user?inactive=false'),
        headers={
            "Authorization": "Bearer {}".format(QTEST_TOKEN)
        },
        verify=False
    )

    user2_info = responseAU.json()
    if responseAU.status_code == 200:
        if "total" in user2_info:
            userTotal2 = (user2_info["total"])

    return userTotal2


if __name__ == '__main__':
    main()