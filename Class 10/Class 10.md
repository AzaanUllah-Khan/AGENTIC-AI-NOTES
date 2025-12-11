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
