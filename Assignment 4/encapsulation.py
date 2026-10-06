class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            print("Current Balance: ", self.balance)

    def withdrawal(self, amount):
        if amount > 0:
            self.balance -= amount
            print (f"Withdrawal amount:{amount}.Remaining Balance:{self.balance}")


    def get_balance(self,):
        return self.balance

account = Bank("A", 100)
account.get_balance()
account.deposit(50)
account.get_balance()
account.withdrawal(30)

print("Final Balance", account.get_balance())