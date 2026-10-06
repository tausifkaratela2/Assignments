#outer loop to create rows 1-5
for i in range(1, 6):
    #empty string for current row
    row = ""

    #inner loop to create 5 multiplication results.
    for j in range(1, 6):
        #calculate multiplications and make each column 5 characters wide 
        row += f"{i * j:5}"

    #print it
    print(row)