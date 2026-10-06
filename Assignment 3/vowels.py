#print the number of vowels in a string
a = input("Enter a string: ")
n = ['a','e','i','o','u']
vowels = []

for i in a:
    if i in n:
        vowels.append(i)

print(f"total vowels found: {len(vowels)}")