## 🚀 Roadmap

### 🧩 Backend & Databases
- FastAPI  
- PostgreSQL  
- MySQL  

### 🤖 AI Concepts
- AI Prompt Engineering  
- Prompt Engineering  
- Context Engineering  

### ⚙️ Automation & Tools
- N8N  
- Agent Kit  
- OpenAI SDK  

---

## 📘 Class Notes

### 🧾 Git & GitHub Basics

#### Installation
- [Install Git](https://git-scm.com/install/windows)

#### Key Differences
- **Git** → Version control system (hosted locally)  
- **GitHub** → Cloud-based hosting platform for Git repositories  

#### GitHub Overview
- **Repositories**  
- **README.md**  
- **Overview Section**

#### 🔗 Linking Git with GitHub

```bash
git config --global user.name "[your-username]"
git config --global user.email "[your-email]"
````

#### 📥 Cloning a Repository

```bash
git clone "[repository-url]"
```

> Get the repo URL from the **Code** button and copy the HTTPS link.

#### 🧩 Assignment

1. Download and install Git
2. Create a GitHub profile
3. Create a `README.md` file
4. Create a repository named **agentic-ai**

---

### Functions in Python

`Definition`

A **function** is a block of code that runs only when it is called.

`Syntax`

```python
def function_name():
    # code block
```

`Calling a Function`

```python
function_name()
```

`Function Hoisting`

Not supported in Python.

`Return Statement`

```python
def my_function():
    return "Welcome"
```

`Function Components`

* **Parameters** → Placeholders in function definition
* **Arguments** → Actual values passed when calling the function

`Function Naming Conventions`

* Use lowercase words with underscores → `my_function_name`
* Be descriptive and concise

`pass Statement`

Used as a placeholder when a function body is intentionally left empty.

```python
def placeholder():
    pass
```

### Parameter Types

* **Default Parameters**

  ```python
  def greet(name="User"):
      print("Hello", name)
  ```

* **Keyword Arguments**

  ```python
  greet(name="Azzy")
  ```

* **Positional Arguments**

  ```python
  greet("Azzy")
  ```

* **Mixing Keyword & Positional**

  ```python
  def intro(name, age):
      print(name, age)

  intro("Azzy", age=22)
  ```

* **Passing Lists as Arguments**

  ```python
  def show_items(items):
      for item in items:
          print(item)

  show_items(["AI", "FastAPI", "Git"])
  ```

### Summary

`This session covered: `

* Core Git and GitHub setup for version control
* Function basics and conventions in Python
* Understanding parameters, arguments, and returns
