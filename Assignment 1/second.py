age = int(input("Age: "))
ticket_price = 300
if age < 5:
    ticket = 0
    catagory = "free"
elif 4 < age < 18:
    ticket = ticket_price * 0.5
    catagory = "half"
elif 18 < age < 60:
    ticket = ticket = ticket_price
    catagory = "full"
else:
    ticket = ticket_price * 0.7
    catagory = "consession"

print (f"Catagory: {catagory}")
print(f"ticket Price: {ticket_price}")



