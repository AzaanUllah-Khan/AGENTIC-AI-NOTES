from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, health):
        self._health = health

    def get_health(self):
        return self._health

    def set_health(self, health):
        if health < 0:
            print("Health can't be negative!")
        else:
            self._health = health
    
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def __init__(self, health):
        super().__init__(health)
    
    def sound(self):
        print("Bark")


class Cat(Animal):
    def __init__(self, health):
        super().__init__(health)
    
    def sound(self):
        print("Meow")


class Lion(Animal):
    def __init__(self, health):
        super().__init__(health)
    
    def sound(self):
        print("Roar")


a1 = Dog(100)
a2 = Cat(80)
a3 = Lion(120)

print("Dog Health:", a1.get_health())
print("Cat Health:", a2.get_health())
print("Lion Health:", a3.get_health())

a1.sound()
a2.sound()
a3.sound()