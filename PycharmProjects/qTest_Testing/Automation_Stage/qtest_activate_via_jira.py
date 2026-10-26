import json
from ldap3 import Server, Connection, ALL
import requests;

requests.packages.urllib3.disable_warnings()
import re
import argparse

ADD_USER_BY_LDAP_URL = "/api/v3/auth-systems/ldap/1/import"
# BASE_URL = "https://qtest-dev3.gtie.dell.com"
# service_account = "svc_npqtestauthrr2"
DEV3_TOKEN = "a8c2f2ad-9d04-489e-a2c9-2eb4721a82b8"
PROD_TOKEN = "a5023327-1321-4b8d-a3c2-cefd4e9ecb1e"
DEV2_TOKEN = "6ad19375-6569-4839-9eec-b0eb119da95d"
STG_TOKEN = "fda0002f-500a-47c6-b617-0381dc027b39"


dell_ldap_user_name = "americas\svc_npieoinfra1"
dell_ldap_credential = 'Dh?9+i78E2MAF*_jKGnoL3pq'
gtie_ldap_user_name = "serviceAD"
gtie_ldap_credential = 'P0werEdge'

def main():
    input_user = ""
    qtest_site = ""
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user',
                        action='store',
                        help="list of users to be added csv, whitespace, ';', or '|' delimited",
                        dest="input_user")
    parser.add_argument('-s', '--site',
                        action='store',
                        help="qtest environment to add user too",
                        dest="qtest_site")
    parser.add_argument('-st', '--status',
                        action='store',
                        help="qtest environment to activate/deactivate user",
                        dest="user_status")
    parser.add_argument('-l', '--ldap',
                        action='store',
                        help="qtest authentication method",
                        dest="ldap")
    args, unknown = parser.parse_known_args()
    #args.qtest_site = "stage"
    #args.input_user = "Crusher_Chang"
    #args.user_status = "Activate"
    #args.ldap = "NonDell"
    sites = [
        "prod",
        "dev3",
        "dev2",
        "stage"
    ]

    if (not args.qtest_site) and (not args.input_user) and (not args.user_status) and (not args.ldap):
        print("Qtest site, user, ldap or status not specified")
        exit(1)
    else:
        input_user = args.input_user
        qtest_site_shortened = args.qtest_site
        user_status = args.user_status
        ldap = args.ldap
    if qtest_site_shortened not in sites:
        print("Qtest site not a valid option. Please specify one of these options: {}".format(sites))
        exit(1)
        token = ""
    if qtest_site_shortened == "prod":
        qtest_site = "https://qtest.gtie.dell.com"
        token = PROD_TOKEN
    elif qtest_site_shortened == "dev3":
        qtest_site = "https://qtest-dev3.gtie.dell.com"
        token = DEV3_TOKEN
    elif qtest_site_shortened == "dev2":
        qtest_site = "https://qtest-dev02.cec.lab.emc.com"
        token = DEV2_TOKEN
    elif qtest_site_shortened == "stage":
        qtest_site = "https://qtest-stage.gtie.dell.com"
        token = STG_TOKEN
    if input_user:
        user_info_list = []
        nonexistent_users = []
        if ldap == "Dell":
            #user_info_list, nonexistent_users = get_all_user_info_dell(input_user,
            #                                                           dell_ldap_user_name,
            #                                                           dell_ldap_credential)
            user_info_list, nonexistent_users = get_all_user_info_corp(input_user)
        elif ldap == "NonDell":
            user_info_list, nonexistent_users = get_all_user_info_nondell(input_user,
                                                                          gtie_ldap_user_name,
                                                                          gtie_ldap_credential)
        boolErrorUsers = False
        if nonexistent_users:
            print("[ERROR] Input users not found!")
            print(nonexistent_users)
            boolErrorUsers = True

        # print(f"qtest site = {qtest_site}")
        # print(f"token = {token}")
        # add_users_by_ldap(user_info_list, token, qtest_site)
        for user in user_info_list:
            activation(user, token, qtest_site, user_status, ldap)
    if boolErrorUsers:
        exit(1)

def capitalize_name(name):
    strings = name.split("_")
    new_name = ""
    for str in strings:
        new_name = new_name + str.capitalize() + "_"
    new_name = new_name[:-1]
    #print(f"new name={new_name}")
    return new_name

def get_all_user_info_corp(user_list):
    user_info_list = []
    nonexistent_users = []
    split_user_list = re.split("\s|[,;|]", user_list)
    for user in split_user_list:
        found_user = False
        res = requests.get("https://portal.gtie.dell.com/cgi-bin/UserLookup.pl?str=" + user, verify=False)
        print("    ldap_username=",res.text.split('sAMAccountName')[1].split('?str=')[1].split('\"')[0])
        print(f"    first_name={res.text.split('givenName')[1].split('<td>')[1].split('</td>')[0]}")
        print(f"    last_name={res.text.split('cn</td>')[1].split('<td>')[1].split('</td>')[0].split('_')[-1]}")
        print(f"    email={res.text.split('mail</td>')[1].split('<td>')[1].split('</td>')[0]}")
        try:
            current_user = {}
            current_user["ldap_username"] = res.text.split('sAMAccountName')[1].split('?str=')[1].split('\"')[0]
            current_user["first_name"] = res.text.split('givenName')[1].split('<td>')[1].split('</td>')[0]
            current_user["last_name"] = res.text.split('cn</td>')[1].split('<td>')[1].split('</td>')[0].split('_')[-1]
            current_user["email"] = res.text.split('mail</td>')[1].split('<td>')[1].split('</td>')[0]
            user_info_list.append(current_user)
            found_user = True
        except:
            nonexistent_users.append("no user" + user)
    return user_info_list, nonexistent_users

def get_all_user_info(user_list, token, BASE_URL):
    user_info_list = []
    nonexistent_users = []
    pattern = r'[0-9]'
    split_user_list = re.split("\s|[,;|]", user_list)
    for user in split_user_list:
        print(f"current user = {user}")
        user = re.sub(pattern, '', user)
        print(f"user search string = {user}")
        found_user = False
        try:
            response = requests.get(
                url="{}{}{}".format(BASE_URL, '/api/v3/users/search?includeInactiveUsers=True&username=', user),
                headers={
                    "Authorization": "Bearer {}".format(token)
                },
                verify=False
            )
            users_info = response.json()
            assert users_info.get('total') > 0
            print(f"Found with original string.")
        except:
            try:
                response = requests.get(
                    url="{}{}{}".format(BASE_URL, '/api/v3/users/search?includeInactiveUsers=True&username=', user.lower()),
                    headers={
                        "Authorization": "Bearer {}".format(token)
                    },
                    verify=False
                )
                users_info = response.json()
                assert users_info.get('total') > 0
                print(f"Found with all lowercase.")
            except:
                try:
                    response = requests.get(
                        url="{}{}{}".format(BASE_URL, '/api/v3/users/search?includeInactiveUsers=True&username=', capitalize_name(user)),
                        headers={
                            "Authorization": "Bearer {}".format(token)
                        },
                        verify=False
                    )
                    users_info = response.json()
                    assert users_info.get('total') > 0
                    print("Found with first character capitalized.")
                except:
                    try:
                        response = requests.get(
                            url="{}{}{}".format(BASE_URL, '/api/v3/users/search?includeInactiveUsers=True&username=', user.upper()),
                            headers={
                                "Authorization": "Bearer {}".format(token)
                            },
                            verify=False
                        )
                        users_info = response.json()
                        assert users_info.get('total') > 0
                    except:
                        print(f"User {user} not found in qTest!")
                        pass
        #response = requests.get(
        #    url="{}{}{}".format(BASE_URL, '/api/v3/users/search?includeInactiveUsers=True&username=', user),
        #    headers={
        #        "Authorization": "Bearer {}".format(token)
        #    },
        #    verify=False
        #)
        #users_info = response.json()
        print(f"found user info = {users_info}")
        if users_info.get("total") > 0:
            found_user = True
            current_user = {}
            for temp_user in users_info.get("items"):
                if user.lower() in temp_user["external_username"].lower():
                    print(f"user info = {temp_user}")
                    print(f"found username = {temp_user[0]['username']}")
                    current_user["username"] = temp_user[0]['username']
                    current_user["id"] = temp_user[0]['id']
                    user_info_list.append(current_user)
        if not found_user:
            nonexistent_users.append(user)
    return user_info_list, nonexistent_users

def get_all_user_info_nondell(user_list, ldap_user_name, ldap_credential):
    user_info_list = []
    nonexistent_users = []
    server = Server("ad1-cec.gtie.dell.com", 636, use_ssl=True, get_info=ALL)
    with Connection(server, ldap_user_name, ldap_credential) as conn:
        conn.start_tls()
        assert conn.bound, '''ldap connection wasn't established'''
        split_user_list = re.split("\s|[,;|]", user_list)
        for user in split_user_list:
            filters = [
                "samaccountname",
            ]
            found_user = False
            for filter in filters:
                search_filter = '(&({}={})(objectclass=user))'.format(filter, user)
                conn.search(search_base='DC=gtie,DC=dell,DC=com',
                            search_filter=search_filter,
                            attributes=["cn",
                                        "mail",
                                        "sAMAccountName",
                                        "givenName",
                                        "sn",
                                        ]
                            )
                if len(conn.entries) > 0:
                    text = json.loads(conn.entries[0].entry_to_json())
                    if text is not None or not "":
                        current_user = {}
                        current_user["ldap_username"] = text["attributes"]["sAMAccountName"][0]
                        cname = text["attributes"]["cn"][0]
                        current_user["first_name"] = text["attributes"]["givenName"][0]
                        current_user["last_name"] = text["attributes"]["sn"][0]
                        current_user["email"] = text["attributes"]["mail"][0]

                        if not current_user["email"]:
                            nonexistent_users.append("no dell mail" + user)
                            continue
                        user_info_list.append(current_user)
                        found_user = True
                        break
            if not found_user:
                nonexistent_users.append(user)
    return user_info_list, nonexistent_users

def get_all_user_info_dell(user_list, ldap_user_name, ldap_credential):
    user_info_list = []
    nonexistent_users = []
    server = Server("appauth.dell.com", 636, use_ssl=True, get_info=ALL, )
    with Connection(server, ldap_user_name, ldap_credential) as conn:
        conn.start_tls()
        assert conn.bound, '''ldap connection wasn't established'''
        split_user_list = re.split("\s|[,;|]", user_list)
        for user in split_user_list:
            filters = [
                "samaccountname",
                "mail",
                "extensionAttribute6",
                "extensionAttribute14",
                "employeeID",
                "cn"
            ]
            found_user = False
            for filter in filters:
                search_filter = '(&({}={})(objectclass=user))'.format(filter, user)
                conn.search(search_base='DC=dell,DC=com',
                            search_filter=search_filter,
                            attributes=["cn",
                                        "mail",
                                        "sAMAccountName",
                                        "givenName",
                                        "sn",
                                        "extensionAttribute6",
                                        "extensionAttribute14",
                                        "employeeID"
                                        ]
                            )
                if len(conn.entries) > 0:
                    text = json.loads(conn.entries[0].entry_to_json())
                    if text is not None or not "":
                        current_user = {}
                        current_user["ldap_username"] = text["attributes"]["sAMAccountName"][0]
                        cname = text["attributes"]["cn"][0]
                        current_user["first_name"] = text["attributes"]["givenName"][0]
                        current_user["last_name"] = text["attributes"]["sn"][0]
                        current_user["email"] = text["attributes"]["mail"][0]

                        if not current_user["email"]:
                            nonexistent_users.append("no dell mail" + user)
                            continue
                        user_info_list.append(current_user)
                        found_user = True
                        break
            if not found_user:
                nonexistent_users.append(user)
    return user_info_list, nonexistent_users

def activation(user, token, BASE_URL, status, ldap):
    u = user["email"]
    #id = user["id"]
    #print(f"user id = {id}")
    print(f"Search string is {u}.")
    ### The user is case sensitive here !!! ###
    try:
        response = requests.get(
            url="{}{}{}".format(BASE_URL, '/api/v3/users/search?includeInactiveUsers=True&username=', u),
            headers={
                "Authorization": "Bearer {}".format(token)
            },
            verify=False
        )
        users_info = response.json()
        assert users_info.get('total') > 0
        print(f"Found with original string.")
    except:
        try:
            response = requests.get(
                url="{}{}{}".format(BASE_URL, '/api/v3/users/search?includeInactiveUsers=True&username=', u.lower()),
                headers={
                    "Authorization": "Bearer {}".format(token)
                },
                verify=False
            )
            users_info = response.json()
            assert users_info.get('total') > 0
            print("Found with string lowercased.")
        except:
            try:
                response = requests.get(
                    url="{}{}{}".format(BASE_URL, '/api/v3/users/search?includeInactiveUsers=True&username=', capitalize_name(u)),
                    headers={
                        "Authorization": "Bearer {}".format(token)
                    },
                    verify=False
                )
                users_info = response.json()
                assert users_info.get('total') > 0
                print("Found with first character capitalized")
            except:
                try:
                    response = requests.get(
                        url="{}{}{}".format(BASE_URL, '/api/v3/users/search?includeInactiveUsers=True&username=', u.upper()),
                        headers={
                            "Authorization": "Bearer {}".format(token)
                        },
                        verify=False
                    )
                    users_info = response.json()
                    assert users_info.get('total') > 0
                    print("Found with string uppwercased.")
                except:
                    print(f"user {u} not found in qTest.")
                    exit(1)
    users_info = response.json()
    for i in users_info.get("items"):
        if i["username"].lower() == user["email"].lower():
            print(f"item = {i}")
            users_info = i
    #users_info = users_info.get("items")[0]
    print(f"user info={users_info}")
    user_id = ""
    user_email = ""
    user_fname = ""
    user_lname = ""
    user_uname = ""
    user_ext = ""
    user_ext_config_id = ""
    # auth = ""
    user_state = ""
    user_timezone = ""
    user_country_name = ""
    if BASE_URL == "https://qtest.gtie.dell.com":
        if "dell" in users_info["username"].split("@")[1].lower() or "emc" in users_info["username"].split("@")[1].lower():
            auth = "APPAUTH"
            user_ext_config_id = 1
        else:
            auth = "GTIE"
            user_ext_config_id = 3
    elif BASE_URL == "https://qtest-dev3.gtie.dell.com":
        if "dell" in users_info["username"].split("@")[1].lower() or "emc" in users_info["username"].split("@")[1].lower():
            auth = "APPAUTH"
            user_ext_config_id = 1
        else:
            auth = "GTIE"
            user_ext_config_id = 3
    elif BASE_URL == "https://qtest-dev02.cec.lab.emc.com":
        auth = "LDAP(1)"
        user_ext_config_id = 1
    elif BASE_URL == "https://qtest-stage.gtie.dell.com":
        if "dell" in users_info["username"].split("@")[1].lower() or "emc" in users_info["username"].split("@")[1].lower():
            auth = "APPAUTH"
            user_ext_config_id = 1
        else:
            auth = "GTIE"
            user_ext_config_id = 3
    else:
        print("error trying to choose auth source in rest api")
        exit(1)
    #print(f"auth system={auth}")
    #print(f"external config id = {user_ext_config_id}")
    #exit(1)
    # auth_config_id = 1 # in prod 1 = appauth; 3 = gtie
    # if BASE_URL == "https://qtest.gtie.dell.com":
    #    if
    #    auth = "APPAUTH"
    # elif BASE_URL == "https://qtest-dev3.gtie.dell.com":
    #    auth = "APPAUTH DELL"
    # auth_config_id = 3 # in dev3 3=appauth; 1 = gtie
    # elif BASE_URL == "https://qtest-dev02.cec.lab.emc.com":
    #    auth = "LDAP1"
    # elif BASE_URL == "https://qtest-stage.gtie.dell.com":
    #    auth = "APPAUTH"
    # else:
    #    print("error trying to choose auth source in rest api")
    #    exit(1)
    if status == 'Activate':
        user_state = 1
    elif status == 'Deactivate':
        user_state = 3
        ### Deactivation function is not working becasue a bug that once deactivated authentication will be rmeoved from user.
    #print(f"user name={users_info['username']}")
    user_id = users_info["id"]
    user_email = users_info["username"]
    user_fname = users_info["first_name"]
    user_lname = users_info["last_name"]
    user_uname = users_info["username"]
    user_ext = user["ldap_username"]
    #auth = users_info["authentication_system"]
    #user_ext_config_id = users_info["external_auth_config_id"]
    user_timezone = users_info["timezone_offset"]
    user_country_name = users_info["country_name"]
    #print(f"user id = {user_id}")
    #print(f"user email = {user_email}")
    #print(f"user name = {user_uname}")
    body = {
        "id": user_id,
        "username": user_uname,
        "email": user_email,
        "first_name": user_fname,
        "last_name": user_lname,
        "status": user_state,
        "avatar": "{}/api/v3/users/{}/avatar".format(BASE_URL, user_id),
        "external_user_name": user_ext,
        "external_auth_config_id": user_ext_config_id,
        "timezone_offset": user_timezone,
        "country_name": user_country_name
    }
    # print(json.dumps(body, indent=4))
    url = "{}{}{}".format(BASE_URL, '/api/v3/users/', user_id)
    # print(url)
    response2 = requests.put(
        url=url,
        headers={
            "Authorization": "Bearer {}".format(token),
            "Content-Type": "application/json"
        },
        verify=False,
        data=json.dumps(body)
    )
    # print(response2.status_code)
    if response2.status_code != 200:
        print("Non-standard status code: {}".format(response.status_code))
        print(response2.json())


if __name__ == '__main__':
    main()