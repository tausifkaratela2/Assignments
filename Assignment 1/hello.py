print ("Hello World!")
x = int(input("Enter first"))
y  = int(input("Enter second"))
z = int(input("Enter third"))
w = int(input("Enter four"))

if x >= y and x >= z and x >= w:
    greatest = x
elif y >= z and y >= w:
    greatest = y
elif z >= w:
    greatest = z
else: greatest = w

print ("The greates num is ",{greatest})