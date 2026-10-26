from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import datetime

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument("--incognito")
options.add_argument('--disable-gpu')
options.add_argument("resolution=1920x1080")
options.add_argument('--ignore-certificate-errors')

userac = "svc_npjiratoqtest"
passwd = "*?w2Xt1+uBY3z~A_69v0mNJH"
userac1 = "ServiceqTestGTIE"
passwd1 = "Ytnf3kjr3*64vdb3d"
userac2 = "ewing_lin"
passwd2 = "ZZzz3899316"
summar = "TEST"
summar1 = "TEST1"
jira_url = "https://jira.gtie.dell.com"
# ana = "Barry_C"


chrome_path = "C:\Auto\chromedriver.exe"
jira = webdriver.Chrome(chrome_path, chrome_options=options)
wait = WebDriverWait(jira, 10)
jira.maximize_window()

print
"Go to CEC JIRA"
# jira.get('https://jira.cec.lab.emc.com/login.jsp')
# time.sleep(1)
# print "CEC JIRA Body=" + jira.find_element_by_tag_name("body").get_attribute("outerHTML")

startime = datetime.datetime.now()
# Username = jira.find_element_by_id("login-form-username")
# Username.send_keys(userac)
# Password = jira.find_element_by_id("login-form-password")
# Password.send_keys(passwd)
# jira.find_element_by_xpath('//*[@id="login-form-submit"]').click()
# jira.implicitly_wait(10)
jira.get('https://jira.cec.lab.emc.com/projects/PSIZERES?selectedItem=com.qas.qtest.plugins.jira-plugin:qtest-panel')
time.sleep(15)
# jira.switch_to.frame(iframe)
try:
    iframe = jira.find_elements_by_tag_name('iframe')[0]
    jira.switch_to_frame(iframe)
    qtest = jira.find_element_by_xpath("/html/body/div/div/section/div/div[2]/div[1]/div[1]/div[2]/p/a").text
    qtest2 = jira.find_element_by_xpath("/html/body/div/div/section/div/div[2]/div[1]/div[1]/div[1]/h3").text
    print
    qtest
    print
    qtest2
    time.sleep(1)

except:
    print("Go to qTest to configure integration account.")
    jira.get('https://qtest.gtie.dell.com')
    time.sleep(15)
    # print "qTest Body=" + jira.find_element_by_tag_name("body").get_attribute("outerHTML")
    username2 = jira.find_element_by_xpath('//*[@id="userName"]')
    username2.send_keys(userac2)
    time.sleep(15)
    password2 = jira.find_element_by_xpath('//*[@id="password"]')
    password2.send_keys(passwd2)
    time.sleep(15)
    jira.find_element_by_xpath('//*[@id="loginButton"]').click()
    time.sleep(25)
    jira.get('https://qtest.gtie.dell.com/p/3/portal/project#tab=integration-settings&object=30&id=9')
    jira.implicitly_wait(15)
    time.sleep(20)
    jira.find_element_by_link_text('JIRA PRODUCTION').click()
    # try:
    #	ieolink = jira.find_element_by_css_selector(
    #      ".dojoxGridMasterView "
    #      "table.dojoxGridRowTable "
    #      "tbody "
    #      "tr:nth-child(0) "
    #      "td:nth-child(0) "
    #      "a:nth-child(0)")
    #	print "ieolink=" + ieolink.text
    #	jira.find_element_by_css_selector(
    #      ".dojoxGridMasterView "
    #      "table.dojoxGridRowTable "
    #      "tbody "
    #      "tr:nth-child(0) "
    #      "td:nth-child(0) "
    #      "a:nth-child(0)").click()
    # except:
    #	print "CEC JIRA Body=" + str(jira.find_element_by_tag_name("body").get_attribute("innerHTML"))
    time.sleep(10)
    un = jira.find_element_by_xpath('//*[@id="connectionInforUsername"]')
    un.clear()
    un.send_keys(userac)
    pw = jira.find_element_by_xpath('//*[@id="connectionInforPassword"]')
    pw.clear()
    pw.send_keys(passwd)
    time.sleep(2)
    jira.find_element_by_xpath('//*[@id="addConnectionTest_label"]').click()
    time.sleep(3)
    jira.implicitly_wait(30)
    jira.find_element_by_xpath('//*[@id="addConnectionSave_label"]').click()
    time.sleep(15)
    jira.find_element_by_xpath('//*[@id="userAvatarWrapper"]/p').click()
    time.sleep(2)
    jira.find_element_by_xpath('//*[@id="log-out-link"]').click()

time.sleep(15)
print
"Go to GTIE JIRA"
# jira.get('https://jira.gtie.dell.com/login.jsp')
jira.get(jira_url)
jira.implicitly_wait(25)
time.sleep(30)
# print "GTIE JIRA Body=" + jira.find_element_by_tag_name("body").get_attribute("outerHTML")
# print "Body=" + jira.find_element_by_tag_name("body").text
# divs=jira.find_elements_by_tag_name("div")
# for div in divs:
#	print div.find_element_by_css_selector(".ping-buttons").get_attribute("outerHTML")
#	print div.get_attribute("outerHTML")
try:
    jira.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/div[3]/a[2]').click()
except:
    print
    "Error! GTIE JIRA Body=" + jira.find_element_by_tag_name("body").get_attribute("outerHTML")
    jira.get(jira_url)
    jira.implicitly_wait(10)
    jira.find_element_by_xpath('/html/body/div/div[2]/div[2]/form/div[3]/a[2]').click()
jira.implicitly_wait(10)
time.sleep(5)
Username = jira.find_element_by_id("username")
Username.send_keys(userac1)
Password = jira.find_element_by_id("password")
Password.send_keys(passwd1)
jira.find_element_by_xpath('/html/body/div/div[2]/div/form/div[6]/a').click()
jira.implicitly_wait(20)
time.sleep(20)
# jira.find_element_by_xpath('//*[@value="Non Dell User"]').click()

jira.get(jira_url + '/projects/VXFM?selectedItem=com.qas.qtest.plugins.jira-plugin:qtest-panel')
time.sleep(15)
print
"GTIE JIRA Body=" + str(jira.find_element_by_tag_name("body"))
# jira.switch_to.frame(iframe)
try:
    iframe = jira.find_elements_by_tag_name('iframe')[0]
    jira.switch_to_frame(iframe)
    qtest = jira.find_element_by_xpath("/html/body/div/div/section/div/div[2]/div[1]/div[1]/div[2]/p/a").text
    qtest2 = jira.find_element_by_xpath("/html/body/div/div/section/div/div[2]/div[1]/div[1]/div[1]/h3").text
    print
    qtest
    print
    qtest2
    time.sleep(1)


except:
    print
    "Cannot find qTest info. Trying to refresh connection in qTest."
    time.sleep(2)
    jira.get('https://qtest.gtie.dell.com')
    time.sleep(3)
    username2 = jira.find_element_by_xpath('//*[@id="userName"]')
    username2.send_keys(userac2)
    time.sleep(2)
    password2 = jira.find_element_by_xpath('//*[@id="password"]')
    password2.send_keys(passwd2)
    time.sleep(2)
    jira.find_element_by_xpath('//*[@id="loginButton"]').click()
    time.sleep(3)
    jira.get('https://qtest.gtie.dell.com/p/125/portal/project#tab=integration-settings&object=30&id=9')
    jira.implicitly_wait(10)
    time.sleep(10)
    jira.find_element_by_link_text('GTIE Jira Prod').click()
    time.sleep(4)
    un = jira.find_element_by_xpath('//*[@id="connectionInforUsername"]')
    un.clear()
    un.send_keys(userac1)
    pw = jira.find_element_by_xpath('//*[@id="connectionInforPassword"]')
    pw.clear()
    pw.send_keys(passwd1)
    time.sleep(15)
    jira.find_element_by_xpath('//*[@id="addConnectionTest_label"]').click()
    time.sleep(15)
    jira.implicitly_wait(30)
    jira.find_element_by_xpath('//*[@id="addConnectionSave_label"]').click()
    jira.implicitly_wait(20)
    time.sleep(25)
    jira.find_element_by_xpath('//*[@id="userAvatarWrapper"]/p').click()
    time.sleep(20)
    jira.find_element_by_xpath('//*[@id="log-out-link"]').click()
    time.sleep(3)