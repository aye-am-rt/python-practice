import json

# dir(json)  in cmd line

# dump == for file
# dumps === for string

pyDict = {"person":
              {"fname": "ritesh",
               "lname": "tiwari",
               "age": 21}
          }

print("printing dictionary object ",pyDict)
with open("JsFile.json", "w") as myFile:
    json.dump(pyDict, myFile)  # if none is present in dictonary it will become null in json.

with open("JsFile.json", "r") as myFile:
    data = json.load(myFile)  # if none is present in dictonary it will become null in json. vise versa
    print("data from file type is dictionary")
    print(data)
