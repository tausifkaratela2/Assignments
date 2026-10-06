#taking user input
n = int(input("Enter a number:"))
#store original to use it in final output
num = n
#count the steps
steps = 0
#to store the largest number reached.
peak = n 

# continue to loop until n is 1
while n !=1:
    #if n is even, divide it by 2
    if n % 2 == 0:
        n = n // 2
    else:
        # if n is odd, multiplay it by 3 and add 1
        n = n * 3 + 1

    #increase the step count
    steps += 1
    #check if current larger number is greater than the previous peak.
    if n > peak:
        peak = n

print (f"{num} reached 1 in {steps} steps.")
print (f"peak value was {peak}")