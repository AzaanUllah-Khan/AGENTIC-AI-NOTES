`Topics covered`

- What an API is
- Route vs Endpoint
- API Methods (GET, POST, PUT, PATCH, DELETE)
- What Fetch is (and what it is NOT)

---

`What is an API?`

**API (Application Programming Interface)** is a bridge that lets:
- Frontend talk to Backend
- One app talk to another app

Simple example:
- You (Frontend) order food
- Waiter (API) takes order
- Kitchen (Backend) prepares food

---

`Route vs Endpoint`

### 🔹 Route (Request Address)
A **Route** is the **URL path** where the request is sent.

Example:
```text
https://example.com/users
````

> This is the **address**.

---

### 🔹 Endpoint (Precise Location)

An **Endpoint** is:

* A **route**
* PLUS a **specific method** (GET, POST, etc.)

> Endpoint = Route + Method

Example:

```text
GET https://example.com/users
POST https://example.com/users
```

Same route, **different endpoints**.

---

`API Methods (What Action to Perform)`

> GET - POST - PUT - DELETE are explained in `Class 15`

## 4️⃣ PATCH – Update Part of Data

### 🔹 What it does

* Updates **only selected fields**
* Keeps remaining data unchanged

### 🔹 Real-Life Example

Changing only your profile picture
(Name, email stay same)

📌 Difference from PUT:

* PUT → replaces everything
* PATCH → updates only what you send

## 🧠 Methods Summary Table

| Method | Purpose             | Data Change |
| ------ | ------------------- | ----------- |
| GET    | Read data           | ❌ No        |
| POST   | Add new data        | ✅ Yes       |
| PUT    | Update full data    | ✅ Yes       |
| PATCH  | Update partial data | ✅ Yes       |
| DELETE | Delete data         | ✅ Yes       |

---

## 🌐 What is Fetch?

### 🔹 Important Point

**Fetch is NOT an API method.**

Fetch is a **JavaScript function** used to:

* Call an API
* Send requests
* Receive responses

📌 Fetch is used on the **frontend**.

---

### 🔹 Fetch Example

```javascript
fetch("https://example.com/users")
  .then(res => res.json())
  .then(data => console.log(data))
```

📌 This fetches data from an API using GET by default.

---

### 🔹 Fetch Can Use Any Method

```javascript
fetch("https://example.com/users", {
  method: "POST",
  body: JSON.stringify({ name: "Ali" }),
  headers: {
    "Content-Type": "application/json"
  }
});
```
