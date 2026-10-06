#take the user input
n = int(input("enter a number: "))

#if the number is less than 2, it is not a prime
if n < 2:
    print(f"{n} is not a prime number")

#assume the number is prime
else: 
    prime = True
    #Check possible divisors from 2 up to the square root of n
    for i in range(2, int(n * 0.5) + 1):
        #check if n can be divided evenly by i
        if n % i == 0:
            #printing the divisor found
            print(f"{n} is divisible by {i}")
            #number is not a prime
            prime = False
            #stop because divisor is fount.
            break
    #printing the reulting values.
    if prime:
        print(n, "is prime")

    else:
        print (f"{n}, is not a prime")