#!/usr/bin/python3 

import json
import csv

with open('/Users/ayyaz/Downloads/Provincial_Constituency_Boundary.json') as f:
  data = json.load(f)
  print(len(data['features']))

  count = 0
  with open('/Users/ayyaz/DataScience/PunjabCoordinates.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["District", "Coordinates"])
    for f in data['features']:
        print(f['properties']['PROVINCE'] , end=", ")
        if(f['properties']['PROVINCE'] == 'PUNJAB'):
            writer.writerow([ f['properties']['DISTRICT'] , f['geometry']['coordinates']])

        
