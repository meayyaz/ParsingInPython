#!/usr/bin/python3 

import csv
import pandas as pd 

win= {
    "Australia":0, "England" : 0,
    "South Africa":0, "India":0, 
    "Sri Lanka":0, 
    "New Zealand":0 , "West Indies":0
}
lost= {
    "Australia":0, "England" : 0,
    "South Africa":0, "India":0, 
    "Sri Lanka":0, 
    "New Zealand":0 , "West Indies":0
}
drawn= {
    "Australia":0, "England" : 0,
    "South Africa":0, "India":0, 
    "Sri Lanka":0, 
    "New Zealand":0 , "West Indies":0
}

teams_data = list()

with open('/Users/ayyaz/pakistan_test.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    
    for row in csv_reader:
        if row['Result'] =='Won' and row['Team'] !='Pakistan':
            win[row['Team']] += 1
        if row['Result'] =='Lost' and row['Team'] !='Pakistan':
            lost[row['Team']] += 1
        if row['Result'] =='Drawn' and row['Team'] !='Pakistan':
            drawn[row['Team']] += 1

for team in win.keys():
    teams_data.append([ team, win[team], lost[team], drawn[team] ])

df = pd.DataFrame(teams_data, columns = ['Team', 'Win','Lost','Drawn']) 

print(df)
