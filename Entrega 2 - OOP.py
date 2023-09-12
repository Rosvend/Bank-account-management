from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def bank_name(self):
        pass

    @abstractmethod
    def transfer(self,amount):
        pass

class Account(Bank):
    def __init__(self, owner, balance,account_number):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number
        
    def bank_name(self):
        return self.bank_name
    
    def transfer(self,amount):
        if amount > self.balance:
            print("Insufficient funds")
            return self.balance
        else:
            self.balance -= amount
            print("Transferred correctly, your new balance is ${}".format(self.balance))
            return self.balance
    
    def deposit(self,amount):
        self.balance += amount
        print("You have deposited ${}, your new balance is ${}".format(amount,self.balance))
        return self.balance
    
    def withdraw(self, amount):
        self.balance -= amount
        print("You have withdrawn ${}, your new balance is {}".format(amount,self.balance))
        return self.balance

account1 = Account("Luis",10000,"001")
        
class ATM(Bank):
    def __init__(self, location, bank_name,balance):
        self.location = location
        self.bank_name = bank_name
        self.balance = balance
    
    def bank_name(self):
        return self.bank_name
    
    def transfer(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Transferred correctly, your new balance is {}".format(self.balance))
        

ATM1 = ATM("Laureles","Bancolombia", 12000)
account1.transfer(100)
account1.deposit(100)

class customer():
    def __init__(self, name, id, age,cardnumber):
        self.name = name
        self.id = id
        self.age = age
        self.cardnumber = cardnumber

    def insertcard(self,cardnumber):
        if self.cardnumber == 1:
            pass
        else:
            return KeyError