


import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains

Chrome(executable_path='/Users/ayyaz/200Dollar/chromedriver')

def addresses_one():

    url = "https://www.zillow.com/north-myrtle-beach-sc/sold/"
    driver = webdriver.Chrome()
    driver.get(url)
    addresses = []

    try:
        addresses = driver.find_elements_by_tag_name('address')
        print("Going to print addresses:", len(addresses))
        for address in addresses:
            print(address.text)
            addresses.append(address.text)
    except:
        print('no adress 1')

    driver.close()
    return  addresses;

def addresses_two():

    url = """
        https://www.airbnb.com/s/San-Diego--CA--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=september&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=San%20Diego%2C%20CA%2C%20United%20States&place_id=ChIJSx6SrQ9T2YARed8V_f0hOg0&checkin=2021-08-27&checkout=2021-08-31&source=structured_search_input_header&search_type=user_map_move&ne_lat=32.97290073298523&ne_lng=-116.89599082171242&sw_lat=32.575693584747114&sw_lng=-117.44530722796242&zoom=11&search_by_map=true
        """
    driver = webdriver.Chrome()
    driver.get(url)
    addresses = []

    try:
        addresses = driver.find_elements_by_class_name('_mm360j')
        #driver.page_source
        print("Going to print addresses:", len(addresses))
        for address in addresses:
            print(address.get_attribute('outerHTML'))
            #addresses.append(address.text)
    except:
        print('no adress 2')

    return addresses;

addresses = addresses_one()
addresses.append(addresses_two())


import csv

with open('addresses.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(addresses)