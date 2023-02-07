class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdrawal failed. Available balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")


account = Account("Magzhan Akhmadi", 1000)


