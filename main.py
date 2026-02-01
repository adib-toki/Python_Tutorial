#Dictionaries Access
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

info = {
    "Adib":{
    "Name": "Adib",
    "School": "MZS",
    "Class": 9,
    "Roll": 67
    },
    "Toki":{
        "Name": "Afif",
        "Class": "Nersury",
        "School": "FMS",
        "Roll": 0
    },
    "year":2025
}

print(thisdict)

print(info["year"])

x = info.get("Adib")
print(x)

print(info.keys())

print(info.values())