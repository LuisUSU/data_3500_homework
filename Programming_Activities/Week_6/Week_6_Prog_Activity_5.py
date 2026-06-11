#Week 5 Activity 5
import json
person = {}
person["age"] = 33

json.dump(person, open("person.json", "w"))

adjustAge = json.load(open("person.json", "r"))

person["age"] +=1

json.dump(person, open("person.json", "w"))
adjustedAge = json.load(open("person.json", "r"))

print("Adjusted Age:  ", adjustedAge)