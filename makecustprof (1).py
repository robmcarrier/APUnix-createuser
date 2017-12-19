from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
##You need to download the chromedriver(google "chromedriver") and put directory below
chrome = webdriver.Chrome("DIRECTORY FOR CHROMEDRIVER", chrome_options=chrome_options)

def isAlertPresent():
    try:
        chrome.switch_to_alert().accept()
        return True
    except NoAlertPresentException as e:
        return False

sv2 = ["2401", "2206", "0011A", "2143", "2225", "2201", "3503C", "3503D", "3206", "3140", "3415", "3151", "3132", "2402", "3627", "3625", "3626", "3152", "2203", "3424"]

una = ["3702", "3704", "3118", "3601", "3701", "3705", "3703", "2110A"]

def customerFunctions(model):
    chrome.find_element_by_xpath('//*[@id="LevelList"]/option[2]').click()
    '''

    chrome.find_element_by_xpath('//*[@id="2401"]').click()
    chrome.find_element_by_xpath('//*[@id="2206"]').click()
    chrome.find_element_by_xpath('//*[@id="0011A"]').click()
    chrome.find_element_by_xpath('//*[@id="2143"]').click()
    chrome.find_element_by_xpath('//*[@id="2225"]').click()
    chrome.find_element_by_xpath('//*[@id="2201"]').click()


    #Add manager functions to manager level
    chrome.find_element_by_xpath('//*[@id="3503C"]').click()
    chrome.find_element_by_xpath('//*[@id="3503D"]').click()
    chrome.find_element_by_xpath('//*[@id="3206"]').click()
    chrome.find_element_by_xpath('//*[@id="3140"]').click()
    chrome.find_element_by_xpath('//*[@id="3415"]').click()
    chrome.find_element_by_xpath('//*[@id="3151"]').click()
    chrome.find_element_by_xpath('//*[@id="3152"]').click()
    chrome.find_element_by_xpath('//*[@id="3132"]').click()
    chrome.find_element_by_xpath('//*[@id="2402"]').click()
    chrome.find_element_by_xpath('//*[@id="3627"]').click()
    chrome.find_element_by_xpath('//*[@id="3625"]').click()
    chrome.find_element_by_xpath('//*[@id="3626"]').click()
    '''

    if model == "s":
        for s in sv2:
            chrome.find_element_by_xpath('//*[@id="%s"]' % s).click()
    else:
        for s in sv2:
            chrome.find_element_by_xpath('//*[@id="%s"]' % s).click()
        for u in una:
            chrome.find_element_by_xpath('//*[@id="%s"]' % u).click()

    chrome.find_element_by_xpath('//*[@id="update_function_level_div_id"]/button[1]').click()

'''dont need this
def unaCustomer():
    chrome.find_element_by_xpath('//*[@id="LevelList"]/option[2]').click()

    chrome.find_element_by_xpath('//*[@id="2401"]').click()
    chrome.find_element_by_xpath('//*[@id="3702"]').click()
    chrome.find_element_by_xpath('//*[@id="2206"]').click()
    chrome.find_element_by_xpath('//*[@id="0011A"]').click()
    chrome.find_element_by_xpath('//*[@id="2143"]').click()
    chrome.find_element_by_xpath('//*[@id="2225"]').click()
    chrome.find_element_by_xpath('//*[@id="2201"]').click()


    #Add manager functions to manager level
    chrome.find_element_by_xpath('//*[@id="3503C"]').click()
    chrome.find_element_by_xpath('//*[@id="3704"]').click()
    chrome.find_element_by_xpath('//*[@id="3503D"]').click()
    chrome.find_element_by_xpath('//*[@id="3118"]').click()
    chrome.find_element_by_xpath('//*[@id="3601"]').click()
    chrome.find_element_by_xpath('//*[@id="3206"]').click()
    chrome.find_element_by_xpath('//*[@id="3140"]').click()
    chrome.find_element_by_xpath('//*[@id="3415"]').click()
    chrome.find_element_by_xpath('//*[@id="3701"]').click()
    chrome.find_element_by_xpath('//*[@id="3151"]').click()
    chrome.find_element_by_xpath('//*[@id="3152"]').click()
    chrome.find_element_by_xpath('//*[@id="3132"]').click()
    chrome.find_element_by_xpath('//*[@id="2402"]').click()
    chrome.find_element_by_xpath('//*[@id="3627"]').click()
    chrome.find_element_by_xpath('//*[@id="3705"]').click()
    chrome.find_element_by_xpath('//*[@id="3703"]').click()
    chrome.find_element_by_xpath('//*[@id="3625"]').click()
    chrome.find_element_by_xpath('//*[@id="3626"]').click()

    for s in sv2:
        chrome.find_element_by_xpath('//*[@id="%s"]' % s).click()

    for u in una:
        chrome.find_element_by_xpath('//*[@id="%s"]' % u).click()
    chrome.find_element_by_xpath('//*[@id="update_function_level_div_id"]/button[1]').click()
'''
# Log in
controlversion = ""
#Currently only works with new web service
def oldOrNew():
    print("Old Web Service or New Summit Control");
    controlversion = input().lower()
    if controlversion[:3] == "new":
        chrome.get('WEB SERVICE URL')
        username = chrome.find_element_by_id('user')
        password = chrome.find_element_by_id('password')
        username.send_keys('#USERNAME')
        password.send_keys('#PASSWORD')
        chrome.find_element_by_xpath('//*[@id="loginform"]/div[3]/input').click()
    else:
        chrome.get('WEBSERVICE URL')
        username = chrome.find_element_by_id('user')
        password = chrome.find_element_by_id('password')
        username.send_keys('USERNAME')
        password.send_keys('PASSWORD')
        chrome.find_element_by_xpath('/html/body/form[1]/table[1]/tbody/tr[1]/td/table/tbody/tr/td[2]/table/tbody/tr[6]/td[2]/div/input').click()


def createCustomer():
    # Create Customer
    oldOrNew();
    chrome.find_element_by_xpath('//*[@id="left_column"]/nav/ul/li[4]/a').click()
    chrome.find_element_by_xpath('//*[@id="left_column"]/nav/ul/ul/li[1]/a').click()
    print(chrome.title)
    chrome.find_element_by_xpath('//*[@id="customer_id"]/option[2]').click()

    a = """enter customer name
Format = Version Num + Model + Safe Num
ex. 2.01.020.rc1 SV2B 15"""
    print(a)
    custname = input()
    custname = custname[0:32]
    chrome.find_element_by_xpath('//*[@id="CustomerName"]').send_keys(custname)
    chrome.find_element_by_xpath('//*[@id="lang_pack_en"]').click()
    chrome.find_element_by_xpath('//*[@id="curr_pack_USD"]').click()
    chrome.find_element_by_xpath('//*[@id="syncprof_on_chk"]').click()
    chrome.find_element_by_xpath('//*[@id="newcustomer_div_id"]/button').click()
    while isAlertPresent():
        chrome.find_element_by_xpath('//*[@id="customer_id"]/option[2]').click()
        print("enter a differnt customer name")
        custname = input()
        custname = custname[0:32]
        chrome.find_element_by_xpath('//*[@id="CustomerName"]').send_keys(custname)
        chrome.find_element_by_xpath('//*[@id="lang_pack_en"]').click()
        chrome.find_element_by_xpath('//*[@id="curr_pack_USD"]').click()
        chrome.find_element_by_xpath('//*[@id="newcustomer_div_id"]/button').click()

    print("SV2 or UNA-ST?")
    a = input().lower()[0]
    customerFunctions(a)



    #Config Profile
    chrome.find_element_by_xpath('//*[@id="left_column"]/nav/ul/ul/li[2]/a').click()

    chrome.find_element_by_xpath('//*[@id="profile_id"]/option[2]').click()
    profilename = custname + " Profile"
    profilename = profilename[0:30]
    chrome.find_element_by_xpath('//*[@id="new_profile_name"]').send_keys(profilename)
    chrome.find_element_by_xpath('//*[@id="EODAutoYN"]/option[2]').click()
    chrome.find_element_by_xpath('//*[@id="EODAutoTime"]').send_keys('08:00')
    chrome.find_element_by_xpath('//*[@id="shift_mode"]/option[2]').click()
    chrome.find_element_by_xpath('//*[@id="useBagIds"]/option[2]').click()
    chrome.find_element_by_xpath('//*[@id="useCasIds"]/option[2]').click()
    chrome.find_element_by_xpath('//*[@id="allowForce"]/option[2]').click()
    chrome.find_element_by_xpath('//*[@id="citChgDelivery"]/option[2]').click()
    chrome.find_element_by_xpath('//*[@id="manageSameLevel"]/option[2]').click()
    chrome.find_element_by_xpath('//*[@id="detail_shift_report"]/option[2]').click()
    chrome.find_element_by_xpath('//*[@id="eod_balance_supplement"]/option[2]').click()
    chrome.find_element_by_xpath('//*[@id="rcf_mode"]/option[2]').click()
    chrome.find_element_by_xpath('//*[@id="create_profile"]/button').click()
    chrome.switch_to_alert().accept()

    chrome.find_element_by_xpath('//*[@id="pcnt_manual_deposit"]').clear()
    chrome.find_element_by_xpath('//*[@id="pcnt_manual_deposit"]').send_keys("1")
    chrome.find_element_by_xpath('//*[@id="pcnt_content_removal"]').clear()
    chrome.find_element_by_xpath('//*[@id="pcnt_content_removal"]').send_keys("1")
    chrome.find_element_by_xpath('//*[@id="pcnt_maintenance"]').clear()
    chrome.find_element_by_xpath('//*[@id="pcnt_maintenance"]').send_keys("1")
    chrome.find_element_by_xpath('//*[@id="updatePrints"]').click()
# oldOrNew()
createCustomer()

while True:
    print("Do you wanna make more customers?(Yes or No)")
    answer = input().lower()[0]
    if answer = "" or answer == "y":
        createCustomer()
    else:
        break

print('Done')
chrome.close()

'''
'//*[@id="pcnt_manual_deposit"]'
'//*[@id="pcnt_content_removal"]'
'//*[@id="pcnt_maintenance"]'
'''
