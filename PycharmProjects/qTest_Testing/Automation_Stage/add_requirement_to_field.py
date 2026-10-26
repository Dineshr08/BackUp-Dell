import json
from ldap3 import Server, Connection, ALL
import requests;
import time

requests.packages.urllib3.disable_warnings()
import re
import argparse

ADD_USER_BY_LDAP_URL = "/api/v3/auth-systems/ldap/1/import"
# BASE_URL = "https://qtest-dev3.gtie.dell.com"
# service_account = "svc_npqtestauthrr2"
DEV3_TOKEN = "a8c2f2ad-9d04-489e-a2c9-2eb4721a82b8"
PROD_TOKEN = "a4f9ceff-cbe1-45d5-8974-8d3f35c670db"
DEV2_TOKEN = "6ad19375-6569-4839-9eec-b0eb119da95d"
STG_TOKEN = "f8ac1f3a-51ba-4826-94b1-181bfd9f409a"


# feature field id
# field_id = 77964 # feature field for CAT_POC_New project
# field_id = 74179 # feature field for CAT_POC project

# project CAT_POC = 386
# project_id = 386

### field value example
# {
#    "links": [],
#    "value": 1,
#    "label": "Laurel: PF-7521 Support for FC/NVMe on PowerMax 2500 and 8500 on WarmSpringX",
#    "order": 1,
#    "is_default": false,
#    "is_active": true
# },


def main():
    input_user = ""
    qtest_site = ""
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--module',
                        action='store',
                        help="module to get requirements from",
                        dest="module")
    parser.add_argument('-s', '--site',
                        action='store',
                        help="qtest environment to add user too",
                        dest="qtest_site")
    parser.add_argument('-p', '--project',
                        action='store',
                        help="qtest project id to be worked on",
                        dest="qtest_project")
    parser.add_argument('-f', '--field',
                        action='store',
                        help="qtest field id to be worked on",
                        dest="qtest_field")
    args, unknown = parser.parse_known_args()
    # args.qtest_site = "stage"
    # args.module = "506261"
    # args.qtest_project = 386 # CAT_POC project
    # args.qtest_field = 74179 # CAT_POC feature field
    valid_request = False
    if args.qtest_project == "cat_poc_new" and args.qtest_site == "stage":
        # this project only exist in staging
        project_id = 409
        field_id = 77964
        valid_request = True
    elif args.qtest_project == "powerstore_copy" and args.qtest_site == "stage":
        # this setting only existing in staging
        project_id = 350
        field_id = 79762
        valid_request = True
    elif args.qtest_project == "powerstore" and args.qtest_site in ("prod", "stage"):
        project_id = 349
        field_id = 89605
        valid_request = True
    elif args.qtest_project == "powermax" and args.qtest_site in ("prod", "stage"):
        project_id = 442
        field_id = 90735
        valid_request = True
    else:
        valid_request = False
    # args.qtest_project = 409 # CAT_POC_NEW project
    # args.qtest_field = 77964 # CAT_POC_New feature field
    # args.qtest_project = 45 # Akt_test
    # args.qtest_field = 48965 # akt_test Tag field under test suite
    sites = [
        "prod",
        "dev3",
        "dev2",
        "stage"
    ]

    if (not args.qtest_site) or (not args.module) or (not args.qtest_project) or (not valid_request):
        print("Qtest site, module or project not specified or wrong combination.")
        print("Support CAT_POC_New only in stage.")
        print("Support Powerstore_Copy only in stage.")
        print("Support Powerstore only in prod.")
        print("Support PowerMax only in prod.")
        exit(1)
    else:
        qtest_site_shortened = args.qtest_site
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
    split_module_list = re.split("\s|[,;|]", args.module)
    # print(f"module list = {split_module_list}")
    for module in split_module_list:
        add_requirements_to_field(token, qtest_site, project_id, field_id, module)


def get_module_by_id(token, site, project, module, descendants):
    if descendants:
        get_module_api = f"{site}/api/v3/projects/{project}/modules/{module}?expand=descendants"
    else:
        get_module_api = f"{site}/api/v3/projects/{project}/modules/{module}"
    exit_loop = False
    error_count = 0
    while not exit_loop:
        try:
            get_response = requests.get(
                url=get_module_api,
                headers={
                    "Authorization": "Bearer {}".format(token),
                    "Content-Type": "application/json"
                },
                verify=False
            )
            # print(f"update response = {get_response.text}")
            if get_response.status_code == 200:
                exit_loop = True
                get_response = get_response.json()
                if len(get_response) > 0:
                    return get_response
                else:
                    return False
            else:
                error_count += 1
        except:
            error_count += 1
        if error_count >= 5:
            print(
                f"API to get module failed 5 times. Please check if there's network issue or qtest server issue.")
            exit_loop = True
            exit(1)


def get_requirements_by_module(token, site, project, module):
    get_req_api = f"{site}/api/v3/projects/{project}/requirements"
    error_count = 0
    requirement_list = []
    page = 1
    page_end = False
    while not page_end:
        # print(f"get requirement page = {page}")
        exit_loop = False
        while exit_loop == False:
            try:
                get_response = requests.get(
                    url=get_req_api,
                    headers={
                        "Authorization": "Bearer {}".format(token),
                        "Content-Type": "application/json"
                    },
                    params={"page": page,
                            "size": 50,
                            "parentId": module},
                    verify=False
                )
                # print(f"update response = {get_response.text}")
                if get_response.status_code == 200:
                    exit_loop = True
                    get_response = get_response.json()
                    if len(get_response) > 0:
                        for requirement in get_response:
                            current_req = {}
                            # print(f"requirement name = {requirement['name']}")
                            current_req["id"] = requirement["id"]
                            current_req["name"] = requirement["name"]
                            current_req["pid"] = requirement["pid"]
                            requirement_list.append(current_req)
                else:
                    error_count += 1
                # print(f"requirement count of page {page} = {len(get_response)}")
            except:
                error_count += 1
            if error_count >= 5:
                print(
                    f"API to get requirement failed 5 times. Please check if there's network issue or qtest server issue.")
                exit_loop = True
                exit(1)
        # print(f"error count = {error_count}")
        if len(get_response) == 50:
            page = page + 1
        else:
            page_end = True
    return requirement_list


def get_project_suite_field_values_by_id(token, site, project, field_id):
    field_value_api = f"{site}/api/v3/projects/{project}/settings/test-suites/fields/{field_id}/allowed-values"
    error_count = 0
    page = 1
    values_list = []
    page_end = False
    while not page_end:
        # time.sleep(1)
        # print(f"get value page = {page}")
        exit_loop = False
        while not exit_loop:
            get_response = ""
            try:
                get_response = requests.get(
                    url=field_value_api,
                    headers={
                        "Authorization": "Bearer {}".format(token),
                        "Content-Type": "application/json"
                    },
                    params={"page": page,
                            "pageSize": 200},
                    verify=False
                )
                # print(f"update response = {get_response.text}")
                if get_response.status_code in (200, 201, 202):
                    exit_loop = True
                    get_response = get_response.json()
                    if len(get_response) > 0:
                        for value in get_response:
                            if int(value["order"]) > 0 and value["label"] != "NA|NA":
                                current_value = {"order": value["order"], "label": value["label"],
                                                 "is_active": value["is_active"], "id": value["value"]}
                                # print(f"requirement name = {requirement['name']}")
                                values_list.append(current_value)
                else:
                    print(f"response status = {get_response.status_code}")
                    error_count += 1
                # print(f"response size = {len(get_response)}.")
            except:
                error_count += 1
            # print(f"get feautre values page {page} size {len(get_response)}.")
            if error_count >= 10:
                print(
                    f"API to get suite field values failed 5 times. Please check if there's network issue or qtest server issue.")
                exit_loop = True
                exit(1)
        # print(f"get feautre values page {page} size {len(get_response)}.")
        if len(get_response) == 200:
            page = page + 1
        else:
            page_end = True
    print(f"Collected all {len(values_list)} field values.")
    return values_list


def update_value_to_project_suite_field(token, site, project, field_id, value_id, order, temp_value):
    # print(f"current value count = {current_value_count}")
    add_value_api = f"{site}/api/v3/projects/{project}/settings/test-suites/fields/{field_id}/allowed-values/{value_id}"
    exit_loop = False
    error_count = 0
    body = {
        "value": value_id,
        "label": temp_value,
        "order": order,
        "is_default": False,
        "is_active": True
    }
    while not exit_loop:
        try:
            get_response = requests.put(
                url=add_value_api,
                headers={
                    "Authorization": "Bearer {}".format(token),
                    "Content-Type": "application/json"
                },
                json=body,
                verify=False
            )
            # print(f"update response = {get_response.text}")
            # print(f" status code = {get_response.status_code}")
            if get_response.status_code in (200, 201, 202):
                exit_loop = True
                get_response = get_response.json()
                if len(get_response) > 0:
                    return get_response
                else:
                    return False
            else:
                error_count += 1
        except:
            error_count += 1
        if error_count >= 5:
            print(
                f"API to update value failed 5 times. Please check if there's network issue or qtest server issue.")
            exit_loop = True
            return False


def add_value_to_project_suite_field(token, site, project, field_id, temp_value):
    current_values = get_project_suite_field_values_by_id(token, site, project, field_id)
    current_value_count = len(current_values)
    # print(f"current value count = {current_value_count}")
    add_value_api = f"{site}/api/v3/projects/{project}/settings/test-suites/fields/{field_id}/allowed-values"
    exit_loop = False
    error_count = 0
    body = [{
        "label": temp_value,
        "order": current_value_count + 1,
        "is_default": False,
        "is_active": True
    }]
    while not exit_loop:
        try:
            get_response = requests.post(
                url=add_value_api,
                headers={
                    "Authorization": "Bearer {}".format(token),
                    "Content-Type": "application/json"
                },
                json=body,
                verify=False
            )
            # print(f"update response = {get_response.text}")
            # print(f" status code = {get_response.status_code}")
            if "200" in str(get_response.status_code) or "201" in str(get_response.status_code):
                exit_loop = True
                get_response = get_response.json()
                if len(get_response) > 0:
                    return get_response
                else:
                    return False
            else:
                error_count += 1
        except:
            error_count += 1
        if error_count >= 5:
            print(
                f"API to add value failed 5 times. Please check if there's network issue or qtest server issue.")
            exit_loop = True
            return False


def add_requirements_to_field(token, site, project, field_id, module: int):
    # get requirements from module
    # print(f"module id = {module}")
    main_module = False
    module_obj = get_module_by_id(token, site, project, module, True)
    if module_obj:
        parent_module = get_module_by_id(token, site, project, module_obj["parent_id"], False)
        if parent_module["name"] == "Imported from JIRA":
            module_name = module_obj["name"]
            main_module = True
        else:
            module_name = parent_module["name"] + "|" + module_obj["name"]
        if "children" in module_obj:
            for child_module in module_obj["children"]:
                # print(f"child module name = {child_module['name']}")
                add_requirements_to_field(token, site, project, field_id, child_module['id'])
        # print(f"module_obj = {module_obj}")
        # print(f"module name = {module_name}")
    else:
        print(f"No module found, please check if the module id is correct or not!")
        exit(1)
    requirement_list = get_requirements_by_module(token, site, project, module)
    print(f"module name = {module_name}")
    print(f"total requirements count = {len(requirement_list)}")
    # get current field values
    # field_id = 74179    # Feature field
    print(f"Project id and Field id = {project}, {field_id}")
    field_values = get_project_suite_field_values_by_id(token, site, project, field_id)
    # print(f"field values = {field_values}")
    # if any("PF-7521" in value['label'] for value in field_values):
    #    print(f"PF-7521 exist!")

    # test_value_count = 0
    pass_count = 0
    fail_count = 0
    update_pass_count = 0
    update_fail_count = 0
    for requirement in requirement_list:
        req_exist = False
        for value in field_values:
            if requirement['name'].split(' ')[0] in value['label'].split(' ')[1]:
                req_exist = True
                exist_order = value['order']
                exist_id = value['id']
                exist_value = value['label']
        temp_value = module_name + "| " + requirement['name'].replace(":", "-")
        # print(f"Checking requirement {requirement['name'].split(' ')[0]}")
        if req_exist:
            print(f"Requirement value {requirement['name'].split(' ')[0]} exists!")
            # validate the string if match the policy
            # print(f"Current value = {exist_value}")
            # print(f"New value = {temp_value}")
            if main_module:
                if temp_value.split('|')[0] != exist_value.split('|')[0]:
                    update_value = update_value_to_project_suite_field(token, site, project, field_id, exist_id,
                                                                       exist_order, temp_value)
                    if update_value:
                        print(f"Update exist feature {temp_value} to Feature field successfully!")
                        update_pass_count += 1
                    else:
                        print(f"Update exist feature {temp_value} to Feature field failed!")
                        update_fail_count += 1
            else:
                if temp_value.split('|')[0] != exist_value.split('|')[0] or temp_value.split('|')[1] != \
                        exist_value.split('|')[1]:
                    update_value = update_value_to_project_suite_field(token, site, project, field_id, exist_id,
                                                                       exist_order, temp_value)
                    if update_value:
                        print(f"Update exist feature {temp_value} to Feature field successfully!")
                        update_pass_count += 1
                    else:
                        print(f"Update exist feature {temp_value} to Feature field failed!")
                        update_fail_count += 1
        else:
            # print(f"Adding requirement {requirement['name'].split(' ')[0]} to Feature field.")
            add_value = add_value_to_project_suite_field(token, site, project, field_id, temp_value)
            if add_value:
                print(f"Adding requirement {temp_value} to Feature field successfully!")
                pass_count = pass_count + 1
            else:
                print(f"Adding requirement {temp_value} to Feature field failed!")
                fail_count = fail_count + 1
        # test_value_count = test_value_count + 1
        # if test_value_count >= 3:
        #    break
    print(f"{pass_count} requirement(s) added successfully!")
    if fail_count > 0:
        print(f"{fail_count} requirement(s) added failed!")
    print(f"{update_pass_count} requirement(s) updated successfully!")
    if update_fail_count > 0:
        print(f"{update_fail_count} requirement(s) updated failed!")


if __name__ == '__main__':
    main()