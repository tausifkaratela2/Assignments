#take the user input
rows = int(input("Enter rows: "))

#creating each row of the pyramid
for i in range(1, rows + 1):
    #calculating spaces needed to centre the current row
    spaces = " " * (rows - i)
    #empty sting for numbers
    numbers = ""

    #adding nos from 1 to current row number
    for j in range(1, i + 1):
        numbers += str(j) + " "

    #printing result
    print(spaces + numbers)