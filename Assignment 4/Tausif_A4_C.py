from Tausif_A4_B import Student
import csv
import json

Student = [("Tausif", 98),
            ("Girish", 77),
            ("Abhi", 67)
]
with open("Students.txt", "w", encoding="utf-8") as file:
    for names, marks in Student:
        file.write(f"{names}, {marks}")

with open("Students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "marks"])
    writer.writerows(Student)

with open("Students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

St_data = [
    {"name": "Tausif", "marks": 85, "grade": "A"},
    {"name": "Girish", "marks": 92, "grade": "A+"},
    {"name": "Abhay", "marks": 78, "grade": "B"}
]

with open("Students.json", "w", encoding="utf-8") as file:
    json.dump(St_data, file, indent= 3)

with open("Students.json", "r", encoding="utf-8") as file:
    read = json.load(file)

print (read)