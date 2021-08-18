import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains

Chrome(executable_path='/Users/ayyaz/200Dollar/chromedriver')

url = "http://willcountysoa.com/propertysearch/detail?Mpin=01-24-02-100-001-0000"
driver = webdriver.Chrome()
driver.get(url)
all_rows = []

for _ in range(1, 3):

    row = []
    p = driver.find_element_by_id('FormView1_pinLabel').text
    row.append(p)
    print(p)
    p = driver.find_element_by_id('FormView1_OwnerLabel').text
    row.append(p)
    print(p)

    try:
        d1 = driver.find_element_by_id('FormView1_DataList1_address1Label_0').text
        d2 = driver.find_element_by_id('FormView1_DataList1_address2Label_0').text
        row.append(d1 + ' ' + d2)
        print(d1 + ' ' + d2)
    except:
        row.append('')
        print('no adress')

    #######

    all_rows.append(row)

    driver.find_element_by_name("FormView1$ButtonNext").click()
    time.sleep(5)
    print("##############")

import csv

with open('properties.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(all_rows)