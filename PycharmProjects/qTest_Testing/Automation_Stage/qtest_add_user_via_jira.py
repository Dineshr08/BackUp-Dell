import json
from ldap3 import Server, Connection, ALL
import requests; requests.packages.urllib3.disable_warnings()
import re
import argparse

ADD_USER_BY_LDAP_URL = "/api/v3/auth-systems/ldap/1/import"
#BASE_URL = "https://qtest-dev3.gtie.dell.com"
#service_account = "svc_npqtestauthrr2"
DEV3_TOKEN = "a8c2f2ad-9d04-489e-a2c9-2eb4721a82b8"
PROD_TOKEN = "a4f9ceff-cbe1-45d5-8974-8d3f35c670db"
DEV2_TOKEN = "6ad19375-6569-4839-9eec-b0eb119da95d"
STG_TOKEN = "f8ac1f3a-51ba-4826-94b1-181bfd9f409a"
DEV1_TOKEN = "deb4c25d-d744-4b2e-bd55-a9c7ef2f80ac"
ldap_user_name = "americas\svc_npieoinfra1"
ldap_credential = 'Dh?9+i78E2MAF*_jKGnoL3pq'



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
    args, unknown = parser.parse_known_args()
    sites = [
        "prod",
        "dev3",
        "dev2",
        "dev1",
      	"stage"
    ]

    if (not args.qtest_site) and (not args.input_user):
        print("Qtest site or user not specified")
        exit(1)
    else:
        input_user = args.input_user
        qtest_site_shortened = args.qtest_site
    if qtest_site_shortened not in sites:
        print("Qtest site not a valid option. Please specify one of these options: {}".format(sites))
        exit(1)
    if input_user:
        #user_info_list, nonexistent_users = get_all_user_info(input_user, ldap_user_name, ldap_credential)
        user_info_list, nonexistent_users = get_all_user_info_corp(input_user)
        boolErrorUsers = False
        if nonexistent_users:
            print("[ERROR] Input users not found!")
            print(nonexistent_users)
            boolErrorUsers = True
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
        elif qtest_site_shortened == "dev1":
          qtest_site = "https://qtest-dev01.cec.lab.emc.com"
          token = DEV1_TOKEN
        print(f"qtest site = {qtest_site}")
        print(f"token = {token}")
        add_users_by_ldap(user_info_list, token, qtest_site)
        for user in user_info_list:
            update_to_appauth(user, token, qtest_site)
    if boolErrorUsers:
        exit(1)

def get_all_user_info_corp(user_list):
    user_info_list = []
    nonexistent_users = []
    split_user_list = re.split("\s|[,;|]", user_list)
    for user in split_user_list:
        found_user = False
        res = requests.get("https://portal.gtie.dell.com/cgi-bin/UserLookup.pl?str=" + user, verify=False)
        #print("    ldap_username=",res.text.split('sAMAccountName')[1].split('?str=')[1].split('\"')[0])
        #print(f"    first_name={res.text.split('givenName')[1].split('<td>')[1].split('</td>')[0]}")
        #print(f"    last_name={res.text.split('cn</td>')[1].split('<td>')[1].split('</td>')[0].split('_')[-1]}")
        #print(f"    email={res.text.split('mail</td>')[1].split('<td>')[1].split('</td>')[0]}")
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

def get_all_user_info(user_list, ldap_user_name, ldap_credential):
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


def add_users_by_ldap(user_info_list, token, BASE_URL):
    for user in user_info_list:
        print("Adding user to Qtest: {}".format(user))
        user_info = []
        user_info.append(user)
        response = requests.post(
            url="{}{}".format(BASE_URL, ADD_USER_BY_LDAP_URL),
            headers={
                "Authorization": "Bearer {}".format(token),
                "Content-Type": "application/json"
            },
            json=user_info,
            verify=False
        )
        print("Status Code: {} | format response is:{}".format(response.status_code, response.json()))


def update_to_appauth(user, token, BASE_URL):
    u = user["ldap_username"]
    ### The user is case sensitive here !!! ###
    response = requests.get(
        url="{}{}{}".format(BASE_URL, '/api/v3/users/search?username=', u),
        headers={
            "Authorization": "Bearer {}".format(token)
        },
        verify=False
    )
    users_info = response.json()
    user_id = ""
    user_email = ""
    user_fname = ""
    user_lname = ""
    user_uname = ""
    user_ext = ""
    auth = ""
    auth_config_id = 1 # in prod 1 = appauth; 3 = gtie
    if BASE_URL == "https://qtest.gtie.dell.com":
        auth = "APPAUTH"
    elif BASE_URL == "https://qtest-dev3.gtie.dell.com":
        auth = "APPAUTH"
        #auth_config_id = 1 # in dev3 1=appauth; 3 = gtie
    elif BASE_URL == "https://qtest-dev02.cec.lab.emc.com":
        auth = "LDAP(1)"
        #auth_config_id = 1 # in dev2 1 = EMC; 2 = DELL
    elif BASE_URL == "https://qtest-dev01.cec.lab.emc.com":
        auth = "LDAP(1)"
    elif BASE_URL == "https://qtest-stage.gtie.dell.com":
        auth = "APPAUTH"
    else:
        print("error trying to choose auth source in rest api")
        exit(1)
    for i in users_info.get("items"):
        if i["username"] == user["email"]:
            user_id = i["id"]
            user_email = i["username"]
            user_fname = i["first_name"]
            user_lname = i["last_name"]
            user_uname = i["username"]
            user_ext = i["external_username"]
    body = {
        "id": user_id,
        "username": user_uname,
        "email": user_email,
        "first_name": user_fname,
        "last_name": user_lname,
        "status": 1,
        "avatar": "{}/api/v3/users/{}/avatar".format(BASE_URL,user_id),
        "external_user_name": user_ext,
        "external_auth_config_id": auth_config_id,
        "authentication_system": auth,
        "timezone_offset": "+00:00",
        "country_name": "St. Barthélemy"
    }
    #print(json.dumps(body, indent=4))
    url = "{}{}{}".format(BASE_URL, '/api/v3/users/', user_id)
    #print(url)
    response2 = requests.put(
        url=url,
        headers={
            "Authorization": "Bearer {}".format(token),
            "Content-Type": "application/json"
        },
        verify=False,
        data=json.dumps(body)
    )
    print(response2.status_code)
    if response2.status_code != 200:
        print("Non-standard status code: {}".format(response2.status_code))
        print(response2.text)


if __name__ == '__main__':
    main()