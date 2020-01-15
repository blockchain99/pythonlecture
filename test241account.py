class BankAccount:
    def __init__(self, owner, balance = 0.0):
        self.owner = owner
        self.balance = balance
    
    # def __init__(self, owner):  #lec ver
    #     self.owner = owner
    #     self.balance = 0.0
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def getbalance(self):
        return self.balance

acct = BankAccount("Darcy")
print(acct.owner)
print(acct.balance)
print(acct.deposit(10))
print(acct.withdraw(3))
print("-------------------")
print(acct.balance)
print(acct.getbalance())

        