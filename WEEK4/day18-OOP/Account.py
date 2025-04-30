#create a class called Account
# the class should have the following attributes: accNo, accName, accBal
# the class should have the following methods: deposit, withdraw
class Account:
    def __init__(self, accNo, accName, accBal):
        self.accNo = accNo
        self.accName = accName
        self.accBal = accBal
    def deposit(self, amount):
        if amount < 0:
            print("enter a positive amount")    
        else:
            self.accBal += amount
            print(f"amount deposited successfully, new balance after deposit: {self.accBal}")
    def withdraw(self, amount):
        if amount > self.accBal:
            print("insufficient balance")
        else:
            self.accBal -= amount
            print(f"succeful withdrawal, new balance after withdrawal: {self.accBal}")
    def getAccNo(self):
        return self.accNo
    def getAccName(self):
        return self.accName
    def getAccBal(self):
        return self.accBal