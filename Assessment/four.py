import json

my_dict = {
    "name": "Tausif",
    "city": "Porbandar",
    "skills": ["Python", "Cyber Security", "Testing"],
}

with open("profile.json", "w", encoding="utf-8") as file:
    json.dump(my_dict, file, indent=4)

with open("profile.json", "r", encoding="utf-8") as file:
    read = json.load(file)
    print(read)

print(read["skills"][1])
read["course"] = "Agentic AI"

with open("profile.json", "w", encoding="utf-8") as file:
    json.dump(my_dict, file, indent=4)

print(read)