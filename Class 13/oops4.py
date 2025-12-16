# Vehical Rental System

from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self, availability):
        self.availability = availability
        self.__price = 0
        
    def setPrice(self,price):
        if price < 0:
            print("Price cannot be less than 0")
        else:
            self.__price = price
            
    def getPrice(self):
        return self.__price
    
    @abstractmethod
    def rental(self):
        pass
    
class Bike(Vehicle):
    def __init__(self, availability):
        super().__init__(availability)
        
    def rental(self):
        print("Rental for Bike")
        
class Truck(Vehicle):
    def __init__(self, availability):
        super().__init__(availability)
        
    def rental(self):
        print("Rental for Truck")
        
class Car(Vehicle):
    def __init__(self, availability):
        super().__init__(availability)
        
    def rental(self):
        print("Rental for Car")
        
bike = Bike("Yes")
car = Car("No")
truck = Truck("No")