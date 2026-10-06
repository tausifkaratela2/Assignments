mark = []
for i in range(1,11):
    marks = input(f"enter marks {i} out of 100: ")
    mark.append(marks)

highes = mark[0]
lowest = mark[0]

for m in mark:
    if m > highes:
        highes = m
    if m < lowest:
        lowest = m
print (f"Highest: {highes}")
print (f"lowest: {lowest}")