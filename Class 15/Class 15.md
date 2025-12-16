`What You’ll Learn`

In this class, you’ll understand **how APIs work** using **FastAPI** and learn the **4 most important HTTP methods**:
- GET
- POST
- PUT
- DELETE

By the end, you’ll know **when to use which method** and **why it matters**.

---

`What is FastAPI?`

**FastAPI** is a Python framework used to:
- Build APIs
- Send & receive data
- Connect frontend with backend

> Think of FastAPI as a **waiter**

---

`What are HTTP Methods?`

HTTP methods define **WHAT ACTION** you want to perform on data.
Example:
- Get data
- Add data
- Update data
- Delete data

---

`GET – Fetch Data`

### What does GET do?

GET is used to **READ or FETCH data**.
> It does **NOT** change anything.

### Real-Life Example
Opening Instagram feed  
> You are **getting posts**, not changing them

### FastAPI Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users():
    return {"users": ["Ali", "Sara", "Ahmed"]}
````

> When someone opens `/users`, they receive data.

### ✅ Use GET when:

* You want to read data
* You want to display information
* No data change is needed

---

`POST – Send / Create Data`

### What does POST do?

POST is used to **SEND new data** to the server.
> It **creates something new**.

### Real-Life Example

Signing up on a website
> You are **sending your name & email**

### FastAPI Example

```python
@app.post("/create-user")
def create_user(name: str):
    return {"message": f"User {name} created"}
```

> Data is sent to the server and stored/processed.

### Use POST when:

* Creating a new user
* Submitting a form
* Sending data to backend

---

`PUT – Update Data`

### What does PUT do?

PUT is used to **UPDATE existing data**.

### Real-Life Example

Editing your Instagram bio
> Data already exists, you are changing it

### FastAPI Example

```python
@app.put("/update-user")
def update_user(name: str):
    return {"message": f"User updated to {name}"}
```

> Old data is replaced with new data.

### Use PUT when:

* Updating profile info
* Editing records
* Changing existing data

---

`DELETE - Remove Data`

### What does DELETE do?

DELETE removes data from the server.

### Real-Life Example

Deleting a WhatsApp message
> Message is **gone forever**

### FastAPI Example

```python
@app.delete("/delete-user")
def delete_user(name: str):
    return {"message": f"User {name} deleted"}
```

> Data is permanently removed.

### Use DELETE when:

* Removing users
* Deleting posts
* Clearing records

---

`Quick Comparison Table`

| Method | Action      | Changes Data? | Example Use Case |
| ------ | ----------- | ------------- | ---------------- |
| GET    | Read data   | ❌ No          | Fetch users      |
| POST   | Create data | ✅ Yes         | Signup form      |
| PUT    | Update data | ✅ Yes         | Edit profile     |
| DEL    | Delete data | ✅ Yes         | Remove account   |

---

`Mini Practice Task`

### Task

Create an API with:

* GET → show list of products
* POST → add a product
* PUT → update product name
* DELETE → delete a product
