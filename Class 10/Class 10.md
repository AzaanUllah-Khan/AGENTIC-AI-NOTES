**Python OOP**

- OOP stands for **O**bject **O**riented **P**rogramming
- OOP allows you to structure your code using classes and objects for better organization and reusability.

**Core Concepts**

- Classes and Objects are two core concepts in object-oriented programming
- Class serves as a blueprint (defines what an object should look like) while objects are created based on classes

> Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods.

**Create Class and Object**

- Create a class named `myClass` having a property x using `class` keyword.

```python
class myClass:
  x = 9;
```

- Create an object `c1` based on the class.

```python
c1 = myClass()
print(c1.x)
```

**Delete Objects**

- We can delete objects using the `del` keyword

```python
del c1
```

**Create Multiple Objects**

- We can create multiple objects from the same class

```python
c1 = myClass()
c2 = myClass()
c3 = myClass()
```

**Pass Statement**

- We can create empty classes (without any content) using pass statement

```python
class myEmpty:
  pass
```

**__init__() Method**

- `__init__()` is a **special method** that runs **when an object is created**.  
- It initializes properties for the new object. :contentReference[oaicite:4]{index=4}

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name, p1.age)
```

**self Parameter**

- `self` refers to the **current object instance** inside class methods.  
- It must be the **first parameter** in instance methods.

```python
class Person:
    def __init__(self, name, age):
        self.name = name     # self links property to the object
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()
```

**Class Properties vs Instance Properties**

- **Class properties** are defined **outside methods** and shared across all objects.  
- **Instance properties** are set inside `__init__()` and are unique to each object.

```python
class Person:
    species = "Human"  # class property

    def __init__(self, name):
        self.name = name  # instance property

p1 = Person("Emil")
print(p1.name, p1.species)
```

**Class Methods (Normal Methods)**

- Methods are **functions inside a class** that define behavior. They always take `self` as the first argument.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name)

p1 = Person("Tobias")
p1.greet()
``` 

**Methods With Parameters**
- You can pass parameters to methods *just like regular functions*.

```python
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(5, 3))
```

## Summary

| Topic | Key Idea |
|-------|----------|
| **Class** | Blueprint for objects. |
| **Object** | Instance of a class. |
| **`__init__()`** | Runs when object is created. |
| **`self`** | Refers to the current object. |
| **Class Property** | Shared across all objects. |
| **Instance Property** | Unique per object. |
| **Class/Instance Methods** | Functions inside a class. |
