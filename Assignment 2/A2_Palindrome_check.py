#taking input from the user
n = (int(input("Enter any number: ")))
#sotre the original number for intended output
originl = n
# setting the value for r as zero initially.
r = 0

while n>0:
    #removing the last digit with modulo and storing it in d.
    d = n % 10
    #shifting one digit left in r and adding d at the end
    r = r * 10 + d
    #removing the last digit from n
    n = n//10

print (f"reverse is: {r}")

if originl == r:
    print("Palindrome")
else:
    print("not a palindrome")



