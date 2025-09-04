class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be greater than 0")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw must be greater than 0")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        self.balance = balance
        self.min_balance = min_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw must be greater than 0")
        if self.balance - amount < self.min_balance:
            raise ValueError("Withdrawal would drop balance below minimum allowed")
        self.balance -= amount


account = SavingsAccount(balance=500, min_balance=100)
account.deposit(200)
print("Balance:", account.get_balance()) 

account.withdraw(500)
print("Balance:", account.get_balance()) 

