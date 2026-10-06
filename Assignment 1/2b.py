#electricity_Bill
units = int(input("enter units consumed: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    (100*5) + (100 *7) + ((units - 200) * 10)

print (f"your total bill amount is: Rs{bill: .2f}")