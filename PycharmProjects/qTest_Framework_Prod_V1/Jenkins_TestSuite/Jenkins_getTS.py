import json
import sys
import requests
import urllib3
urllib3.disable_warnings()
BASE_URL = "https://qtest.gtie.dell.com"




def Jenkins_getTS():

    # TC_Name = sys.argv[1]
    # env_name = sys.argv[2]
    TC_Name = 'test'
    env_name = 'stage'

    if env_name == 'stage':
        Env_Value = 'Stage'
    elif env_name == 'prod':
        Env_Value = 'Prod'

    # Get all TestCycle details from root

    get_List_TC_Response = requests.get(
        url="{}{}".format(BASE_URL, '/api/v3/projects/167/test-cycles?parentType=root'),
        headers={
            "Authorization": "Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e"
        },
        verify=False
    )
    if get_List_TC_Response.status_code == 200:
        get_List_TC_info = get_List_TC_Response.json()
        get_List_TC_info_dict = {}

        for item in get_List_TC_info:
            name = item["name"]
            objId = item["id"]
            get_List_TC_info_dict[name] = objId
        # print(get_List_TC_info_dict)

        # Get details of Test cycle which we created from Jenkins

        Created_TC_Value = get_List_TC_info_dict[TC_Name]

        get_Created_TC_Response = requests.get(
            url="{}{}{}{}".format(BASE_URL,
                                  '/api/v3/projects/167/test-cycles?parentId=', Created_TC_Value,
                                  '&parentType=test-cycle&expand=descendants&page=1&pageSize=100'),
            headers={
                "Authorization": "Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e"
            },
            verify=False
        )

        if get_Created_TC_Response.status_code == 200:
            get_Created_TC_info = get_Created_TC_Response.json()
            get_Created_TC_info_dict = {}

            for item in get_Created_TC_info:
                name = item["name"]
                objId = item["id"]
                get_Created_TC_info_dict[name] = objId
            # print(get_Created_TC_info_dict)

            #Get TestSuite detils

            Created_TC_Value = get_Created_TC_info_dict[Env_Value]
            # print("Stage_TC_Value", Stage_TC_Value)

            get_TS_Response = requests.get(
                url="{}{}{}{}".format(BASE_URL,
                                      '/api/v3/projects/167/test-suites?parentId=', Created_TC_Value,
                                      '&parentType=test-cycle&expand=descendants&page=1&pageSize=100'),
                headers={
                    "Authorization": "Bearer a5023327-1321-4b8d-a3c2-cefd4e9ecb1e"
                },
                verify=False
            )

            TS_parsed_response = json.loads(get_TS_Response.content)

            if get_TS_Response.status_code == 200:
                TS_Value = TS_parsed_response[0]["id"]
                print(TS_Value)
                return TS_Value

            else:
                print("Unable to fetch TestSuite details", get_TS_Response.status_code)
        else:
            print("Unable to fetch Created TestCycle details", get_Created_TC_Response.status_code)

    else:
        print("Unable to fetch TestCycle from root level", get_List_TC_Response.status_code)


Jenkins_getTS()
