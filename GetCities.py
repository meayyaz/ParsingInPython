#!/usr/bin/python3 

from bs4 import BeautifulSoup 
from bs4 import BeautifulSoup
import requests

url="https://en.wikipedia.org/wiki/List_of_populated_places_in_Punjab_(Pakistan)"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "html")
#print(soup.prettify()) # print the parsed data of html

gdp_table = soup.find("table", attrs={"class": "wikitable"})
gdp_table_data = gdp_table.tbody.find_all("tr")  # contains 2 rows

print(len(gdp_table_data))


# Get all the headings of Lists
all_cities = []

count = 1
for tr in gdp_table_data:
    
    if( len(tr.find_all('td')) > 1 ):
        city = list()
        for td in tr.find_all('td'):
            #print(td.text)
            city.append(td.text.strip())
        all_cities.append(city)
    else:
       print("....")#tr.find_all('td')) 

import csv

with open('cities.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerows(all_cities)