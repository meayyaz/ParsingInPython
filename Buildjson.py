import json


heat_json = {
    "name" : "Ayyaz Shaukat",
    "father_name" : "Shaukat Ali",
    "address" : "Pakistan",
}

heat_json["lanuages"] = [ "Java", "PHP", "Python" ]

heat_json["experience"] = [{
    "company" : "Telenor GSS",
    "from" : "2015",
    "to" : "on going"
},{
    "company": "TCZ",
    "from": "2006",
    "to": "2013"
}]

# Serializing json
json_object = json.dumps(heat_json, indent=4)


# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

if __name__ == '__main__':
    pass
