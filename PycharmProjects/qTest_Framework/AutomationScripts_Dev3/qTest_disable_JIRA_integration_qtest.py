import json
from ldap3 import Server, Connection, ALL
import requests
import urllib3
from base64 import b64encode

urllib3.disable_warnings()




# # The qTest dev3 instance
BASE_URL = "https://qtest-dev3.gtie.dell.com"
QTEST_TOKEN = "29421d63-7c39-437f-83df-c9ac63ab774a"





API = "/api/v3/projects?assigned=true"   # assigned=true only for assigned projects && assigned=false for all projects

def qTest_Connection(ldap_user_name, ldap_credential):
    server = Server("appauth.corp.emc.com", 636, use_ssl=True, get_info=ALL)
    with Connection(server, ldap_user_name, ldap_credential) as conn:
        conn.start_tls()
        if conn.bound == True:
            print("Connection Successful")
        else:
            print("Not a Success")
            
def disable_JIRA_integration(ldap_user_name, ldap_credential):
    # Get Multiple Projects API
    response = requests.get(
        url="{}{}".format(BASE_URL, API), 
        headers={
            "Authorization": "Bearer {}".format(QTEST_TOKEN)
        },
        verify=False
    )
    project_info = response.json()
    for item in project_info:
        jiraconn = item['defect_tracking_systems']
        for ite in jiraconn:
            connDict = {ite['id'] : item['id']}
            for x, y in connDict.items():
                               
                # Deactivate a JIRA connection API
                response = requests.put(
                    url="{}{}{}{}{}{}".format(BASE_URL, '/api/v3/projects/',y,'/settings/integration/connections/',x,'?active=false'), 
                    headers={
                        "Authorization": "Bearer {}".format(QTEST_TOKEN)
                    },
                    verify=False
                )
                if response.status_code == 200:
                    print ("Disabled JIRA connection for project ID", y)
                else:
                    print ("Error when disabling JIRA connection for project ID", y )


            
        

		
# Disable JIRA integration for either assigned or all projects
disable_JIRA_integration("dinesh.r1@emc.com", "Password@9")

                             