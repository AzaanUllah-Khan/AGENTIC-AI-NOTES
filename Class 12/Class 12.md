`Topics`

- API and backend fundamentals
- FastAPI framework overview
- Application architecture
- Development setup and tooling
- API structure and documentation
- Basic data handling and CRUD operations

`Overview`

- In this class, we cover **FastAPI**, a modern Python framework specially designed for building **high-performance APIs**. `FastAPI` acts as a **bridge between the frontend and backend**, allowing smooth communication between user interfaces, server logic, and databases.

- By the end of this topic, you should understand **how APIs work**, **why FastAPI is powerful**, and **how to structure a clean backend project**.

`What is an API?`

An **API (Application Programming Interface)** allows two systems to communicate with each other.

**Example:**

* Frontend sends a request → API
* Backend processes logic → API
* API returns a response → Frontend

FastAPI helps us **create these APIs efficiently and safely**.

`What is FastAPI?`

**FastAPI** is a Python web framework used to build APIs quickly with:

* High performance
* Built-in type safety
* Automatic API documentation
* Easy integration with databases

It is commonly used for:

* REST APIs
* Backend services
* Microservices
* Full-stack applications

`Application Architecture`

A typical application consists of three main parts:

- ### Frontend

* User interface (UI)
* Technologies: HTML, CSS, JavaScript, React, etc.
* Sends requests to the backend

- ### Backend

* Business logic
* Handles requests & responses
* Built using FastAPI (Python)

- ### Database

* Stores data
* Examples: MySQL, PostgreSQL, MongoDB

`Requirements for FastAPI`

To work with FastAPI, we need the following:

- ### Python

FastAPI is built on **Python**, so Python must be installed.

- ### Uvicorn

* Acts as a **web server**
* Similar to how **Node.js** runs JavaScript servers
* Responsible for running FastAPI applications

- ### Pydantic

* A library for **type safety & data validation**
* Ensures incoming data matches expected formats

`Virtual Environment Setup`

A **virtual environment** keeps project dependencies isolated.

- ### Create a Virtual Environment

```bash
python -m venv .venv
```

- ### Activate Virtual Environment

```bash
.venv\Scripts\activate   # Windows
source .venv/bin/activate # Mac/Linux
```

`Installing Dependencies` 

```bash
pip install fastapi uvicorn
```

`Save Dependencies`

```bash
pip freeze > requirements.txt
```

This allows others to install the same dependencies later.

`Folder Structure`

```
project-name/
│
├── app/
│   ├── main.py
│
├── .venv/
├── requirements.txt
└── README.md
```

`Running the FastAPI Server`

```bash
uvicorn main:app --reload
```

* `--reload` automatically restarts the server on code changes

`Core Concepts to Learn Under This Topic`

- ### HTTP Methods

* GET → Fetch data
* POST → Create data
* PUT → Update data
* DELETE → Remove data

- ### Request & Response Models

* Using **Pydantic** classes
* Ensures clean and validated data

- ### Status Codes

* 200 → Success
* 201 → Created
* 400 → Bad Request
* 404 → Not Found
* 500 → Server Error
