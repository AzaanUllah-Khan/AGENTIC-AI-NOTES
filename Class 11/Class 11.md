### OOP (Object-Oriented Programming)

`Inheritance • Encapsulation • Polymorphism • Abstraction`

### 1️⃣ Inheritance

`What is Inheritance?`

**Inheritance** means one class **gets the properties and methods** of another class.

* Class being inherited from → **Parent / Base class**
* Class that inherits → **Child / Derived class**

> Helps in **code reuse** and avoids writing the same code again.

`Real-Life Example`

👨 Father → 👦 Son

* Son inherits father’s surname
* Son may also inherit habits, property, etc.

`Why We Use Inheritance?`

* Reusability of code
* Cleaner and shorter programs
* Easy to manage large programs

`Code Example`

```python
class Parent:
    car = "Honda"

class Child(Parent):
    pass

c = Child()
print(c.car)
```

**Output:**

```
Honda
```

> Child automatically got `car` from `Parent`.

## 2️⃣ Encapsulation

### What is Encapsulation?

Encapsulation means **wrapping data and methods together** and **hiding sensitive data**.

In Python, it is done using:

* `__` (double underscore) → **Private data**

---

### Real-Life Example

🔐 **ATM Machine**

* You can withdraw money
* You cannot see or change the PIN logic

---

### Why Encapsulation?

* Protects data
* Prevents misuse
* Improves security

---

### Example (Without Encapsulation)

```python
class Account:
    password = 1234

a = Account()
print(a.password)
```

❌ Anyone can access the password.

---

### Example (With Encapsulation)

```python
class Account:
    __password = 1234
```

➡️ `__password` is private
➡️ Cannot be accessed directly

---

### Key Point (Exam Ready)

**Encapsulation** is used to hide data and control access to variables.

---

## 3️⃣ Polymorphism

### What is Polymorphism?

**Polymorphism** means:

* *One thing, many forms*
* Same function or method name behaves differently in different situations

---

### Real-Life Example

👤 A person:

* Student in school
* Son at home
* Friend outside

Same person, different roles.

---

### Polymorphism Example in Python

**Same function, different objects**

```python
print(len("Hello"))
print(len([1, 2, 3, 4]))
```

**Output:**

```
5
4
```

➡️ `len()` works differently for strings and lists.

---

### Another Example

```python
def add(a, b):
    return a + b

print(add(2, 3))
print(add("Hello ", "World"))
```

➡️ Same function, different behavior.

---

### Why Polymorphism?

* Flexible code
* Easy to extend programs
* Less complexity

---

### Exam Line

**Polymorphism** allows methods to perform different tasks using the same name.

---

## 4️⃣ Abstraction

### What is Abstraction?

Abstraction means:

* Showing only important details
* Hiding internal working

User knows **what to do**, not **how it works**.

---

### Real-Life Example

🚗 **Driving a car**

* Press accelerator → Car moves
* You don’t know engine logic

---

### Why Abstraction?

* Reduces complexity
* Makes code user-friendly
* Focuses on functionality

---

### Conceptual Code Example

```python
def sendMessage():
    print("Message sent")

sendMessage()
```

➡️ User only calls the function
➡️ Internal logic is hidden

---

### Abstraction in OOP (Idea Level – Class 11)

* User uses methods
* Programmer hides complex logic inside classes

---

### Exam Line

**Abstraction** hides unnecessary details and shows only essential features.

---

## 🔁 Final Revision Table

| Concept       | Meaning                               | Real-Life Example      |
| ------------- | ------------------------------------- | ---------------------- |
| Inheritance   | Getting properties from another class | Child from parent      |
| Encapsulation | Hiding data                           | ATM PIN                |
| Polymorphism  | One thing, many forms                 | One person, many roles |
| Abstraction   | Hide internal logic                   | Driving a car          |

---

## 📝 One-Paragraph Exam Answer (Bonus)

Object-Oriented Programming uses concepts like inheritance, encapsulation, polymorphism, and abstraction. Inheritance allows one class to acquire properties of another. Encapsulation protects data by hiding it. Polymorphism allows methods to behave differently in different situations. Abstraction hides internal details and shows only necessary features.
