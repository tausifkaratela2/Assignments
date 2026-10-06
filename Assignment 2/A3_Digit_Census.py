#get the user input
n = int(input("Enter a series of numbers: "))
#counters for zero, evens, and odds.
zeroes = 0
even = 0
odd = 0

#loop till all digits have been checked.
while n > 0:
    # get the last digit
    d = n % 10
    #remove last digit from the number
    n = n // 10
    #checking if the digit is 0
    if d == 0:
        zeroes+=1
    #check if digit is even
    elif d % 2 == 0:
        even+=1
    #if not zero or even, it must be odd.
    else:
        odd+=1

#print the values.
print (f"Zeros = {zeroes}")
print (f"Even = {even}")
print (f"odd = {odd}")
