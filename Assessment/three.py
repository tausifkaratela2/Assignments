import csv

details = [
    {"name": "Tausif", "subject": "Python", "marks": 98},
    {"name": "Girish", "subject": "Python", "marks": 85},
    {"name": "Abhi", "subject": "Python", "marks": 72},
    {"name": "Abhay", "subject": "Python", "marks": 91},
    {"name": "Ayush", "subject": "Python", "marks": 64},
]

with open("marks.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "subject", "marks"])
    writer.writeheader()
    writer.writerows(details)

with open("marks.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

highest = 0
top = None
for i in details:
    marks = float(i["marks"])
    if marks > highest:
        highest = marks
        top = i["name"]

print (f"{top}    {highest}")

    