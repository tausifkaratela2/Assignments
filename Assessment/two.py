Students = [
    "Tausif",
    "Girish",
    "Abhi",
    "Abhay",
    "Ayush"
]

with open("classmates.txt", "w", encoding="utf-8") as file:
    for name in Students:
        file.write(name + "\n")

with open("classmates.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)

print(len(content))

for name in content:
    if len(name) > 5:
        print(name)