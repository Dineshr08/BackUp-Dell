import json
import sys

import requests
import urllib3
urllib3.disable_warnings()
BASE_URL = "https://qtest.gtie.dell.com"
QTEST_TOKEN = "45a89380-8d45-4143-826c-e0dbda0a1823"
Login_API = "/login?redirect=https://qtest.gtie.dell.com/portal/project&requestNonce=MC44Nzg2ODE5OTM4OTkz1245"
Integration_API = "/portal/defect/integration/setting/connection/list/9?dojo.preventCache=0.1208288477138908"
Logout_API = '/logout'

def TE_Modules():
    Testing_Reason = sys.argv[1]
    TC_Name = sys.argv[2]
    Interface = sys.argv[3]
    env_name = sys.argv[4]

    try:
        # Login
        session = requests.Session()
        response = session.post(
            url="{}{}".format(BASE_URL, Login_API),
            data='j_username=svc_npjiratoqtest&j_password=*%3Fw2Xt1%2BuBY3z%7EA_69v0mNJH&requestNonce=MC44Nzg2ODE5OTM4OTkz1245&service=',
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'JSESSIONID=qtest-stg-app03~3FDD8CF519D907A9805ECE588E8574E4; UserContextToken=ODEwMmIzOWUtZjBlNi00MDFjLTliZWYtMjUxNDJkNzkyMTFj'
            },

            verify=False
        )
        Cookies = session.cookies.get('UserContextToken')
        Cookies1 = 'UserContextToken=' + Cookies
        print(Cookies1)

        if Testing_Reason == 'Full_Upgrade':
            # Get TE list of Modules

            TE_Module_Response = requests.get(
                url="{}{}".format(BASE_URL,
                                  '/p/167/portal/testexecution/project/children/get/167?includeTestRuns=true&filter=true'),
                headers={
                    'Cookie': Cookies1
                },
                verify=False
            )

            if TE_Module_Response.status_code == 200:
                TE_info = TE_Module_Response.json()
                names = []
                name_objId_mapping = {}
                for item in TE_info:
                    names.append(item["name"])
                    name = item.get("name")
                    objId = item.get("objId")

                    if name and objId is not None:
                        name_objId_mapping[name] = objId

                print(names)
                print(name_objId_mapping)

                if TC_Name in names:
                    print('yes its present')

                    if env_name == 'stage' and Interface == 'API':

                        TC_Value = name_objId_mapping[TC_Name]
                        print("TC_Value", TC_Value)

                        get_Existing_TC_Response = requests.get(
                            url="{}{}{}{}".format(BASE_URL,
                                                  '/api/v3/projects/167/test-cycles?parentId=', TC_Value,
                                                  '&parentType=test-cycle&expand=descendants&page=1&pageSize=100'),
                            headers={
                                "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                            },
                            verify=False
                        )

                        if get_Existing_TC_Response.status_code == 200:
                            get_Existing_TC_info = get_Existing_TC_Response.json()
                            get_Existing_TC_info_dict = {}

                            for item in get_Existing_TC_info:
                                name = item["name"]
                                objId = item["id"]
                                get_Existing_TC_info_dict[name] = objId

                            print(get_Existing_TC_info_dict)

                            #get Stage TC response

                            Stage_TC_Value = get_Existing_TC_info_dict['Stage']
                            print("Stage_TC_Value", Stage_TC_Value)

                            get_Stage_TC_Response = requests.get(
                                url="{}{}{}{}".format(BASE_URL,
                                                      '/api/v3/projects/167/test-suites?parentId=', Stage_TC_Value,
                                                      '&parentType=test-cycle&expand=descendants&page=1&pageSize=100'),
                                headers={
                                    "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                },
                                verify=False
                            )

                            if get_Stage_TC_Response.status_code == 200:
                                get_Stage_TC_info = get_Stage_TC_Response.json()
                                get_Stage_TC_info_dict = {}

                                for item in get_Stage_TC_info:
                                    name = item["name"]
                                    objId = item["id"]
                                    get_Stage_TC_info_dict[name] = objId

                                print(get_Stage_TC_info_dict)

                                #Delete Test Suite

                                Stage_TS_Value = get_Stage_TC_info_dict['API']
                                print("Stage_TS_Value", Stage_TS_Value)

                                del_Stage_TC_Response = requests.delete(
                                    url="{}{}{}".format(BASE_URL,
                                                          '/api/v3/projects/167/test-suites/', Stage_TS_Value),
                                    headers={
                                        "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                    },
                                    verify=False
                                )

                                if del_Stage_TC_Response.status_code == 200:
                                    #create test suite
                                    name = 'API'
                                    TS_BODY = {
                                        "name": name,
                                        "properties": [
                                            {
                                                "field_id": -202,
                                                "field_name": "Target Release/Build",
                                                "field_value": "-19046",
                                                "field_value_name": "Jenkins Automation Testing"
                                            },
                                            {
                                                "field_id": -186,
                                                "field_name": "Assigned To",
                                                "field_value": "[10580]",
                                                "field_value_name": "[Dinesh R]"
                                            },
                                            {
                                                "field_id": -191,
                                                "field_name": "Execution Type",
                                                "field_value": "501",
                                                "field_value_name": "Functional"
                                            },
                                            {
                                                "field_id": -189,
                                                "field_name": "Description",
                                                "field_value": ""
                                            }
                                        ]
                                    }
                                    TS_response = requests.post(
                                        url="{}{}{}{}".format(BASE_URL,
                                                              '/api/v3/projects/167/test-suites?parentId=',
                                                              Stage_TC_Value,
                                                              '&parentType=test-cycle'),
                                        headers={
                                            "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                        },
                                        json=TS_BODY,
                                        verify=False
                                    )
                                    TS_parsed_response = json.loads(TS_response.content)
                                    if TS_response.status_code == 200 and "id" in TS_parsed_response:
                                        Stage_TS_id_value = TS_parsed_response['id']
                                        Stage_TS_name_value = TS_parsed_response['name']
                                        print(f"The captured 'Stage_TS_id_value' value is: {Stage_TS_id_value}")
                                        print(f"The captured 'Stage_TS_name_value' value is: {Stage_TS_name_value}")
                                        return Stage_TS_id_value
                                    else:
                                        print(" TestSuite for Stage API was Not Created",
                                              TS_response.status_code)


                                else:
                                    print("Unable to delete test suite",
                                          del_Stage_TC_Response.status_code)



                            else:
                                print("Unable to Capture Stage Testcycle Response",
                                      get_Existing_TC_Response.status_code)

                        else:
                            print("Unable to Capture Existing Testcycle Response",
                                  get_Existing_TC_Response.status_code)

                    elif env_name == 'stage' and Interface == 'UI':

                        TC_Value = name_objId_mapping[TC_Name]
                        print("TC_Value", TC_Value)

                        get_Existing_TC_Response = requests.get(
                            url="{}{}{}{}".format(BASE_URL,
                                                  '/api/v3/projects/167/test-cycles?parentId=', TC_Value,
                                                  '&parentType=test-cycle&expand=descendants&page=1&pageSize=100'),
                            headers={
                                "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                            },
                            verify=False
                        )

                        if get_Existing_TC_Response.status_code == 200:
                            get_Existing_TC_info = get_Existing_TC_Response.json()
                            get_Existing_TC_info_dict = {}

                            for item in get_Existing_TC_info:
                                name = item["name"]
                                objId = item["id"]
                                get_Existing_TC_info_dict[name] = objId

                            print(get_Existing_TC_info_dict)

                            #get Stage TC response

                            Stage_TC_Value = get_Existing_TC_info_dict['Stage']
                            print("Stage_TC_Value", Stage_TC_Value)

                            get_Stage_TC_Response = requests.get(
                                url="{}{}{}{}".format(BASE_URL,
                                                      '/api/v3/projects/167/test-suites?parentId=', Stage_TC_Value,
                                                      '&parentType=test-cycle&expand=descendants&page=1&pageSize=100'),
                                headers={
                                    "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                },
                                verify=False
                            )

                            if get_Stage_TC_Response.status_code == 200:
                                get_Stage_TC_info = get_Stage_TC_Response.json()
                                get_Stage_TC_info_dict = {}

                                for item in get_Stage_TC_info:
                                    name = item["name"]
                                    objId = item["id"]
                                    get_Stage_TC_info_dict[name] = objId

                                print(get_Stage_TC_info_dict)

                                #Delete Test Suite

                                Stage_TS_Value = get_Stage_TC_info_dict['UI']
                                print("Stage_TS_Value", Stage_TS_Value)

                                del_Stage_TC_Response = requests.delete(
                                    url="{}{}{}".format(BASE_URL,
                                                          '/api/v3/projects/167/test-suites/', Stage_TS_Value),
                                    headers={
                                        "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                    },
                                    verify=False
                                )

                                if del_Stage_TC_Response.status_code == 200:
                                    #create test suite
                                    name = 'UI'
                                    TS_BODY = {
                                        "name": name,
                                        "properties": [
                                            {
                                                "field_id": -202,
                                                "field_name": "Target Release/Build",
                                                "field_value": "-19046",
                                                "field_value_name": "Jenkins Automation Testing"
                                            },
                                            {
                                                "field_id": -186,
                                                "field_name": "Assigned To",
                                                "field_value": "[10580]",
                                                "field_value_name": "[Dinesh R]"
                                            },
                                            {
                                                "field_id": -191,
                                                "field_name": "Execution Type",
                                                "field_value": "501",
                                                "field_value_name": "Functional"
                                            },
                                            {
                                                "field_id": -189,
                                                "field_name": "Description",
                                                "field_value": ""
                                            }
                                        ]
                                    }
                                    TS_response = requests.post(
                                        url="{}{}{}{}".format(BASE_URL,
                                                              '/api/v3/projects/167/test-suites?parentId=',
                                                              Stage_TC_Value,
                                                              '&parentType=test-cycle'),
                                        headers={
                                            "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                        },
                                        json=TS_BODY,
                                        verify=False
                                    )
                                    TS_parsed_response = json.loads(TS_response.content)
                                    if TS_response.status_code == 200 and "id" in TS_parsed_response:
                                        Stage_TS_id_value = TS_parsed_response['id']
                                        Stage_TS_name_value = TS_parsed_response['name']
                                        print(f"The captured 'Stage_TS_id_value' value is: {Stage_TS_id_value}")
                                        print(f"The captured 'Stage_TS_name_value' value is: {Stage_TS_name_value}")
                                        return Stage_TS_id_value
                                    else:
                                        print(" TestSuite for Stage API was Not Created",
                                              TS_response.status_code)


                                else:
                                    print("Unable to delete test suite",
                                          del_Stage_TC_Response.status_code)



                            else:
                                print("Unable to Capture Stage Testcycle Response",
                                      get_Existing_TC_Response.status_code)

                        else:
                            print("Unable to Capture Existing Testcycle Response",
                                  get_Existing_TC_Response.status_code)

                    if env_name == 'prod' and Interface == 'API':

                        TC_Value = name_objId_mapping[TC_Name]
                        print("TC_Value", TC_Value)

                        get_Existing_TC_Response = requests.get(
                            url="{}{}{}{}".format(BASE_URL,
                                                  '/api/v3/projects/167/test-cycles?parentId=', TC_Value,
                                                  '&parentType=test-cycle&expand=descendants&page=1&pageSize=100'),
                            headers={
                                "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                            },
                            verify=False
                        )

                        if get_Existing_TC_Response.status_code == 200:
                            get_Existing_TC_info = get_Existing_TC_Response.json()
                            get_Existing_TC_info_dict = {}

                            for item in get_Existing_TC_info:
                                name = item["name"]
                                objId = item["id"]
                                get_Existing_TC_info_dict[name] = objId

                            print(get_Existing_TC_info_dict)

                            #get Stage TC response

                            Prod_TC_Value = get_Existing_TC_info_dict['Prod']
                            print("Prod_TC_Value", Prod_TC_Value)

                            get_Prod_TC_Response = requests.get(
                                url="{}{}{}{}".format(BASE_URL,
                                                      '/api/v3/projects/167/test-suites?parentId=', Prod_TC_Value,
                                                      '&parentType=test-cycle&expand=descendants&page=1&pageSize=100'),
                                headers={
                                    "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                },
                                verify=False
                            )

                            if get_Prod_TC_Response.status_code == 200:
                                get_Prod_TC_info = get_Prod_TC_Response.json()
                                get_Prod_TC_info_dict = {}

                                for item in get_Prod_TC_info:
                                    name = item["name"]
                                    objId = item["id"]
                                    get_Prod_TC_info_dict[name] = objId

                                print(get_Prod_TC_info_dict)

                                #Delete Test Suite

                                Prod_TS_Value = get_Prod_TC_info_dict['API']
                                print("Prod_TS_Value", Prod_TS_Value)

                                del_Prod_TC_Response = requests.delete(
                                    url="{}{}{}".format(BASE_URL,
                                                          '/api/v3/projects/167/test-suites/', Prod_TS_Value),
                                    headers={
                                        "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                    },
                                    verify=False
                                )

                                if del_Prod_TC_Response.status_code == 200:
                                    #create test suite
                                    name = 'API'
                                    TS_BODY = {
                                        "name": name,
                                        "properties": [
                                            {
                                                "field_id": -202,
                                                "field_name": "Target Release/Build",
                                                "field_value": "-19046",
                                                "field_value_name": "Jenkins Automation Testing"
                                            },
                                            {
                                                "field_id": -186,
                                                "field_name": "Assigned To",
                                                "field_value": "[10580]",
                                                "field_value_name": "[Dinesh R]"
                                            },
                                            {
                                                "field_id": -191,
                                                "field_name": "Execution Type",
                                                "field_value": "501",
                                                "field_value_name": "Functional"
                                            },
                                            {
                                                "field_id": -189,
                                                "field_name": "Description",
                                                "field_value": ""
                                            }
                                        ]
                                    }
                                    TS_response = requests.post(
                                        url="{}{}{}{}".format(BASE_URL,
                                                              '/api/v3/projects/167/test-suites?parentId=',
                                                              Prod_TC_Value,
                                                              '&parentType=test-cycle'),
                                        headers={
                                            "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                        },
                                        json=TS_BODY,
                                        verify=False
                                    )
                                    TS_parsed_response = json.loads(TS_response.content)
                                    if TS_response.status_code == 200 and "id" in TS_parsed_response:
                                        Prod_TS_id_value = TS_parsed_response['id']
                                        Prod_TS_name_value = TS_parsed_response['name']
                                        print(f"The captured 'Prod_TS_id_value' value is: {Prod_TS_id_value}")
                                        print(f"The captured 'Prod_TS_name_value' value is: {Prod_TS_name_value}")
                                        return Prod_TS_id_value
                                    else:
                                        print(" TestSuite for Stage API was Not Created",
                                              TS_response.status_code)


                                else:
                                    print("Unable to delete test suite",
                                          del_Prod_TC_Response.status_code)



                            else:
                                print("Unable to Capture Stage Testcycle Response",
                                      get_Existing_TC_Response.status_code)

                        else:
                            print("Unable to Capture Existing Testcycle Response",
                                  get_Existing_TC_Response.status_code)

                    elif env_name == 'prod' and Interface == 'UI':

                        TC_Value = name_objId_mapping[TC_Name]
                        print("TC_Value", TC_Value)

                        get_Existing_TC_Response = requests.get(
                            url="{}{}{}{}".format(BASE_URL,
                                                  '/api/v3/projects/167/test-cycles?parentId=', TC_Value,
                                                  '&parentType=test-cycle&expand=descendants&page=1&pageSize=100'),
                            headers={
                                "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                            },
                            verify=False
                        )

                        if get_Existing_TC_Response.status_code == 200:
                            get_Existing_TC_info = get_Existing_TC_Response.json()
                            get_Existing_TC_info_dict = {}

                            for item in get_Existing_TC_info:
                                name = item["name"]
                                objId = item["id"]
                                get_Existing_TC_info_dict[name] = objId

                            print(get_Existing_TC_info_dict)

                            #get Stage TC response

                            Prod_TC_Value = get_Existing_TC_info_dict['Prod']
                            print("Prod_TC_Value", Prod_TC_Value)

                            get_Prod_TC_Response = requests.get(
                                url="{}{}{}{}".format(BASE_URL,
                                                      '/api/v3/projects/167/test-suites?parentId=', Prod_TC_Value,
                                                      '&parentType=test-cycle&expand=descendants&page=1&pageSize=100'),
                                headers={
                                    "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                },
                                verify=False
                            )

                            if get_Prod_TC_Response.status_code == 200:
                                get_Prod_TC_info = get_Prod_TC_Response.json()
                                get_Prod_TC_info_dict = {}

                                for item in get_Prod_TC_info:
                                    name = item["name"]
                                    objId = item["id"]
                                    get_Prod_TC_info_dict[name] = objId

                                print(get_Prod_TC_info_dict)

                                #Delete Test Suite

                                Prod_TS_Value = get_Prod_TC_info_dict['UI']
                                print("Prod_TS_Value", Prod_TS_Value)

                                del_Prod_TC_Response = requests.delete(
                                    url="{}{}{}".format(BASE_URL,
                                                          '/api/v3/projects/167/test-suites/', Prod_TS_Value),
                                    headers={
                                        "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                    },
                                    verify=False
                                )

                                if del_Prod_TC_Response.status_code == 200:
                                    #create test suite
                                    name = 'UI'
                                    TS_BODY = {
                                        "name": name,
                                        "properties": [
                                            {
                                                "field_id": -202,
                                                "field_name": "Target Release/Build",
                                                "field_value": "-19046",
                                                "field_value_name": "Jenkins Automation Testing"
                                            },
                                            {
                                                "field_id": -186,
                                                "field_name": "Assigned To",
                                                "field_value": "[10580]",
                                                "field_value_name": "[Dinesh R]"
                                            },
                                            {
                                                "field_id": -191,
                                                "field_name": "Execution Type",
                                                "field_value": "501",
                                                "field_value_name": "Functional"
                                            },
                                            {
                                                "field_id": -189,
                                                "field_name": "Description",
                                                "field_value": ""
                                            }
                                        ]
                                    }
                                    TS_response = requests.post(
                                        url="{}{}{}{}".format(BASE_URL,
                                                              '/api/v3/projects/167/test-suites?parentId=',
                                                              Prod_TC_Value,
                                                              '&parentType=test-cycle'),
                                        headers={
                                            "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                        },
                                        json=TS_BODY,
                                        verify=False
                                    )
                                    TS_parsed_response = json.loads(TS_response.content)
                                    if TS_response.status_code == 200 and "id" in TS_parsed_response:
                                        Prod_TS_id_value = TS_parsed_response['id']
                                        Prod_TS_name_value = TS_parsed_response['name']
                                        print(f"The captured 'Stage_TS_id_value' value is: {Prod_TS_id_value}")
                                        print(f"The captured 'Stage_TS_name_value' value is: {Prod_TS_name_value}")
                                        return Prod_TS_id_value
                                    else:
                                        print(" TestSuite for Stage API was Not Created",
                                              TS_response.status_code)


                                else:
                                    print("Unable to delete test suite",
                                          del_Prod_TC_Response.status_code)



                            else:
                                print("Unable to Capture Stage Testcycle Response",
                                      get_Existing_TC_Response.status_code)

                        else:
                            print("Unable to Capture Existing Testcycle Response",
                                  get_Existing_TC_Response.status_code)




                else:
                    print('no not present')

                # Creating Test Cycle for full Upgrade

                name = TC_Name
                BODY = {
                    "name": name
                }

                TC_response = requests.post(
                    url="https://qtest.gtie.dell.com/api/v3/projects/167/test-cycles",
                    headers={
                        "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                    },
                    json=BODY,
                    verify=False
                )

                TC_parsed_response = json.loads(TC_response.content)
                if TC_response.status_code == 200 and "id" in TC_parsed_response:
                    id_value = TC_parsed_response['id']
                    name_value = TC_parsed_response['name']
                    print(f"The captured 'id' value is: {id_value}")
                    print(f"The captured 'id' value is: {name_value}")

                    # Creating Stage and Prod Test Cycle for full Upgrade
                    for i in range(2):



                        if i == 0:
                            name = 'Stage'
                            Sub_TC_BODY = {
                                "name": name
                            }
                            Sub_TC_response = requests.post(
                                url="{}{}{}{}".format(BASE_URL,
                                                      '/api/v3/projects/167/test-cycles?parentId=', id_value,
                                                      '&parentType=test-cycle'),
                                headers={
                                    "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                },
                                json=Sub_TC_BODY,
                                verify=False
                            )
                            Sub_TC_parsed_response = json.loads(Sub_TC_response.content)
                            if Sub_TC_response.status_code == 200 and "id" in Sub_TC_parsed_response:
                                Stage_TC_id_value = Sub_TC_parsed_response['id']
                                Stage_TC_name_value = Sub_TC_parsed_response['name']
                                print(f"The captured 'Stage_TC_id_value' value is: {Stage_TC_id_value}")
                                print(f"The captured 'Stage_TC_name_value' value is: {Stage_TC_name_value}")

                                # Create Test Suite for both API and UI
                                for j in range(2):
                                    if j == 0:
                                        name = 'API'
                                        TS_BODY = {
                                            "name": name,
                                            "properties": [
                                                {
                                                    "field_id": -202,
                                                    "field_name": "Target Release/Build",
                                                    "field_value": "-19046",
                                                    "field_value_name": "Jenkins Automation Testing"
                                                },
                                                {
                                                    "field_id": -186,
                                                    "field_name": "Assigned To",
                                                    "field_value": "[10580]",
                                                    "field_value_name": "[Dinesh R]"
                                                },
                                                {
                                                    "field_id": -191,
                                                    "field_name": "Execution Type",
                                                    "field_value": "501",
                                                    "field_value_name": "Functional"
                                                },
                                                {
                                                    "field_id": -189,
                                                    "field_name": "Description",
                                                    "field_value": ""
                                                }
                                            ]
                                        }
                                        TS_response = requests.post(
                                            url="{}{}{}{}".format(BASE_URL,
                                                                  '/api/v3/projects/167/test-suites?parentId=',
                                                                  Stage_TC_id_value,
                                                                  '&parentType=test-cycle'),
                                            headers={
                                                "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                            },
                                            json=TS_BODY,
                                            verify=False
                                        )
                                        TS_parsed_response = json.loads(TS_response.content)
                                        if TS_response.status_code == 200 and "id" in Sub_TC_parsed_response:
                                            Stage_TS_id_value = TS_parsed_response['id']
                                            Stage_TS_name_value = TS_parsed_response['name']
                                            print(f"The captured 'Stage_TS_id_value' value is: {Stage_TS_id_value}")
                                            print(f"The captured 'Stage_TS_name_value' value is: {Stage_TS_name_value}")
                                        else:
                                            print(" TestSuite for Stage API was Not Created",
                                                  TS_response.status_code)
                                    else:
                                        name = 'UI'
                                        TS_BODY = {
                                            "name": name,
                                            "properties": [
                                                {
                                                    "field_id": -202,
                                                    "field_name": "Target Release/Build",
                                                    "field_value": "-19046",
                                                    "field_value_name": "Jenkins Automation Testing"
                                                },
                                                {
                                                    "field_id": -186,
                                                    "field_name": "Assigned To",
                                                    "field_value": "[10580]",
                                                    "field_value_name": "[Dinesh R]"
                                                },
                                                {
                                                    "field_id": -191,
                                                    "field_name": "Execution Type",
                                                    "field_value": "501",
                                                    "field_value_name": "Functional"
                                                },
                                                {
                                                    "field_id": -189,
                                                    "field_name": "Description",
                                                    "field_value": ""
                                                }
                                            ]
                                        }
                                        TS_response = requests.post(
                                            url="{}{}{}{}".format(BASE_URL,
                                                                  '/api/v3/projects/167/test-suites?parentId=',
                                                                  Stage_TC_id_value,
                                                                  '&parentType=test-cycle'),
                                            headers={
                                                "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                            },
                                            json=TS_BODY,
                                            verify=False
                                        )
                                        TS_parsed_response = json.loads(TS_response.content)
                                        if TS_response.status_code == 200 and "id" in Sub_TC_parsed_response:
                                            Stage_TS_id_value = TS_parsed_response['id']
                                            Stage_TS_name_value = TS_parsed_response['name']
                                            print(f"The captured 'Stage_TS_id_value' value is: {Stage_TS_id_value}")
                                            print(f"The captured 'Stage_TS_name_value' value is: {Stage_TS_name_value}")
                                        else:
                                            print(" TestSuite for Stage UI was Not Created",
                                                  TS_response.status_code)

                            else:
                                print("Sub TestCycle for Stage and Prod was Not Created", Sub_TC_parsed_response.status_code)

                        else:
                            name = 'Prod'
                            Sub_TC_BODY = {
                                "name": name
                            }
                            Sub_TC_response = requests.post(
                                url="{}{}{}{}".format(BASE_URL,
                                                      '/api/v3/projects/167/test-cycles?parentId=', id_value,
                                                      '&parentType=test-cycle'),
                                headers={
                                    "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                },
                                json=Sub_TC_BODY,
                                verify=False
                            )
                            Sub_TC_parsed_response = json.loads(Sub_TC_response.content)
                            if Sub_TC_response.status_code == 200 and "id" in Sub_TC_parsed_response:
                                Prod_TC_id_value = Sub_TC_parsed_response['id']
                                Prod_TC_name_value = Sub_TC_parsed_response['name']
                                print(f"The captured 'Prod_TC_id_value' value is: {Prod_TC_id_value}")
                                print(f"The captured 'Prod_TC_name_value' value is: {Prod_TC_name_value}")

                                # Create Test Suite for both API and UI
                                for j in range(2):
                                    if j == 0:
                                        name = 'API'
                                        TS_BODY = {
                                            "name": name,
                                            "properties": [
                                                {
                                                    "field_id": -202,
                                                    "field_name": "Target Release/Build",
                                                    "field_value": "-19046",
                                                    "field_value_name": "Jenkins Automation Testing"
                                                },
                                                {
                                                    "field_id": -186,
                                                    "field_name": "Assigned To",
                                                    "field_value": "[10580]",
                                                    "field_value_name": "[Dinesh R]"
                                                },
                                                {
                                                    "field_id": -191,
                                                    "field_name": "Execution Type",
                                                    "field_value": "501",
                                                    "field_value_name": "Functional"
                                                },
                                                {
                                                    "field_id": -189,
                                                    "field_name": "Description",
                                                    "field_value": ""
                                                }
                                            ]
                                        }
                                        TS_response = requests.post(
                                            url="{}{}{}{}".format(BASE_URL,
                                                                  '/api/v3/projects/167/test-suites?parentId=',
                                                                  Prod_TC_id_value,
                                                                  '&parentType=test-cycle'),
                                            headers={
                                                "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                            },
                                            json=TS_BODY,
                                            verify=False
                                        )
                                        TS_parsed_response = json.loads(TS_response.content)
                                        if TS_response.status_code == 200 and "id" in Sub_TC_parsed_response:
                                            Prod_TS_id_value = TS_parsed_response['id']
                                            Prod_TS_name_value = TS_parsed_response['name']
                                            print(f"The captured 'Prod_TS_id_value' value is: {Prod_TS_id_value}")
                                            print(f"The captured 'Prod_TS_name_value' value is: {Prod_TS_name_value}")
                                        else:
                                            print(" TestSuite for Stage API was Not Created",
                                                  TS_response.status_code)
                                    else:
                                        name = 'UI'
                                        TS_BODY = {
                                            "name": name,
                                            "properties": [
                                                {
                                                    "field_id": -202,
                                                    "field_name": "Target Release/Build",
                                                    "field_value": "-19046",
                                                    "field_value_name": "Jenkins Automation Testing"
                                                },
                                                {
                                                    "field_id": -186,
                                                    "field_name": "Assigned To",
                                                    "field_value": "[10580]",
                                                    "field_value_name": "[Dinesh R]"
                                                },
                                                {
                                                    "field_id": -191,
                                                    "field_name": "Execution Type",
                                                    "field_value": "501",
                                                    "field_value_name": "Functional"
                                                },
                                                {
                                                    "field_id": -189,
                                                    "field_name": "Description",
                                                    "field_value": ""
                                                }
                                            ]
                                        }
                                        TS_response = requests.post(
                                            url="{}{}{}{}".format(BASE_URL,
                                                                  '/api/v3/projects/167/test-suites?parentId=',
                                                                  Prod_TC_id_value,
                                                                  '&parentType=test-cycle'),
                                            headers={
                                                "Authorization": "Bearer 45a89380-8d45-4143-826c-e0dbda0a1823"
                                            },
                                            json=TS_BODY,
                                            verify=False
                                        )
                                        TS_parsed_response = json.loads(TS_response.content)
                                        if TS_response.status_code == 200 and "id" in Sub_TC_parsed_response:
                                            Prod_TS_id_value = TS_parsed_response['id']
                                            Prod_TS_name_value = TS_parsed_response['name']
                                            print(f"The captured 'Prod_TS_id_value' value is: {Prod_TS_id_value}")
                                            print(f"The captured 'Prod_TS_name_value' value is: {Prod_TS_name_value}")
                                        else:
                                            print(" TestSuite for Stage UI was Not Created",
                                                  TS_response.status_code)

                            else:
                                print("Sub TestCycle for Stage and Prod was Not Created",
                                      Sub_TC_parsed_response.status_code)

                else:
                    print("TestCycle was Not Created", TC_response.status_code)

            else:
                print("Unable to find the Module names in TestExecution Tab", TE_Module_Response.status_code)

        elif Testing_Reason == 'Minor_Fix':
            pass


    finally:
        # Logout
        url2 = "{}{}".format(BASE_URL, Logout_API)
        payload2 = ""
        headers2 = {
            'Cookie': Cookies1
        }

        response2 = requests.request("GET", url2, headers=headers2, data=payload2)


TE_Modules()