def rectangle(length, width):
    return length * width

g = rectangle(4,5)
print(g)

def max_of_two(a,b):
    return a if a > b else b

def is_even(num):
    return num%2 == 0

a = max_of_two(34,88)
print(a)

b = is_even(20)
print(b)