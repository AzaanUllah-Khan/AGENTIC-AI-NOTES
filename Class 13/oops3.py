#library Management System

from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self,author,price):
        self.author = author
        self.price = price
        self.__quantity = 0
    
    def setQuant(self,quantity):
        if quantity < 0:
            print("Quantity can't be less than 0")
        else: self.__quantity = quantity

    def getQuant(self):
        return self.__quantity
    
    def checkout(self):
        pass
    
class Book(Item):
    def __init__(self, author, price):
        super().__init__(author, price)
        
    def checkout(self):
        print("Checkout for Book")

class Magazine(Item):
    def __init__(self, author, price):
        super().__init__(author, price)
        
    def checkout(self):
        print("Checkout for magazine")
    
b1 = Book("William",200)
m1 = Magazine("Holding",350)

b1.checkout()
m1.checkout()