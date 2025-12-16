# Acc Management System

from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self):
        self.__pin = 0
        self.__balance = 0

    def setPin(self,pin):
        if pin < 0:
            print("PIN cannot be negative")
        else: self.__pin = pin

    def getPin(self):
        return self.__pin
    
    def setBalance(self,balance):
        if balance < 0:
            print("Balance cannot be negative")
        else: self.__balance = balance

    def getBalance(self):
        return self.__balance
    
    @abstractmethod
    def calcInt(self):
        pass

class SavingsAccount(Account):
    def calcInt(self):
        print("Interest for savings")

class CurrentAccount(Account):
    def calcInt(self):
        print("Interest for current")

p1 = SavingsAccount()
p2 = CurrentAccount()

p1.calcInt()
p2.calcInt()