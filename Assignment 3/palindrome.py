n = input("Enter a string: ")
a = list(n)

if a == a[::-1]:
    print("It's a Palindrom")

else:
    print("Not a Palindrom")
