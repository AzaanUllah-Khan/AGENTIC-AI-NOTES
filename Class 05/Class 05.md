`Topics Covered`

- Overview of last class (variables, data types, etc.)
- Dictionary inside list (and vice versa)
- Control Flow  
  - Conditional Statements  
    - if  
    - else
    - Nested if  
    - break, continue
- Operators  
  - Arithmetic  
  - Logical  
  - Assignment  
- Taking Input from User

`Notes`

- A dictionary can be placed inside a list and vice versa.

**Example:**
```python
data = [
  {
    "name": "John",
    "id": {
      "ID": 10,
      "age": 16,
      "courses": ["Web Development", "Agentic AI"]
    }
  }
]
```
- Use the input() function to take input from the user.

Example:

``` python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
```
- `Note` input() always returns a string, so use type casting like int() or float() when needed.

- `Control Flow` As the name suggests, Control Flow is used to “control” the flow of your code.

Example:

``` python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

- `Note: Indentation is very important in Python. It defines which block of code belongs to which statement.`

- Operators

| **Type**        | **Operators**                | **Example**              |
|-----------------|------------------------------|---------------------------|
| Arithmetic      | `+` `-` `*` `/` `%` `**` `//` | `a + b` `a ** b`        |
| Logical         | `and` `or` `not`           | `x > 5 and x < 10`       |
| Assignment      | `=` `+=` `-=` `*=` `/=` `%=` | `x += 2`                 |
| Comparison      | `==` `!=` `<` `>` `<=` `>=` | `a == b`                 |
