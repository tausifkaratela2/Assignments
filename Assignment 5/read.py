import csv
import json

# with open("Assignment 5/hello.txt", "r", encoding="utf-8") as file:
#     content = file.read()

# print(content)

# with open("greeting.txt", "w", encoding="utf-8") as file:
#     content = file.write("Good Morrow!")

# with open("greeting.txt", "r", encoding="utf-8") as file:
#     content = file.read()

# print(content)


Students = [
    {"name": "Tausif", "marks": 99},
    {"name": "Girish", "marks": 96},
    {"name": "Anmol", "marks": 88},
    {"name": "Dipak", "marks": 78},
    {"name": "Moin", "marks": 66},
    ]

# with open("Students.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "marks"])
#     writer.writeheader()
#     writer.writerows(Students)

# print("Done")

with open("Students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
        print("^^^^^^")
        print(row["name"], row["marks"])


Subject = [
    {"Course": "Python"},
    {"Passing Marks": "90"},
    {"topics": ["txt", "json", "csv"]}
    ]

with open("Subject.json", "w", encoding="utf-8") as file:
    json.dump(Subject, file, indent = 2)

print("Subject added")

with open("Subject.json", "r", encoding="utf-8") as file:
    read_subject = json.load(file)

print(read_subject)
print(read_subject["Course"])
print(read_subject["Passing Marks"])