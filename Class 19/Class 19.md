`Topics covered:`
- API Flow
- Endpoints
- Tips to Design APIs properly


### What is API Flow?

**API Flow** explains how:
Frontend → Backend → Database → Backend → Frontend

> It shows the **complete journey of a request**.

`Step-by-Step API Flow`

1. User clicks a button (Frontend)
2. Frontend sends request using Fetch/Axios
3. API endpoint receives request
4. Backend validates data
5. Database is read/updated
6. Backend sends response
7. Frontend shows result to user

> This happens in milliseconds.

`Real-Life Example: Login Flow`

1. User enters email & password
2. POST request sent to `/login`
3. Backend checks credentials
4. Database confirms user
5. Success or error response returned

### What are Endpoints?

`Definition`

An **Endpoint** is:
> A specific URL + a specific HTTP method

- **Endpoint = Route + Method**

`Example`

```text
GET    /users
POST   /users
PATCH  /users/{id}
DELETE /users/{id}
````

> Same route, different endpoints.

`Why Endpoints Matter`

* They define **what actions are allowed**
* They keep APIs organized
* They make frontend-backend communication clear

### Tips to Design a Good API

`Use Clear & Meaningful Names`

- ❌ /getAllUsersData
- ✅ /users

`Use Correct HTTP Methods`

* GET → Read
* POST → Create
* PUT → Replace
* PATCH → Update part
* DELETE → Remove

> Don’t misuse methods.

`Keep Routes Consistent`

- ❌ /user, /usersList, /getUsers
- ✅ /users

`Use IDs for Specific Resources`

```text
GET /users/5
PATCH /users/5
DELETE /users/5
```

> Makes APIs predictable.

`Don’t Expose Logic in URLs`

- ❌ /deleteUserById
- ✅ DELETE /users/{id}

`Return Meaningful Responses`

* Success message
* Error message
* Status code (200, 404, 401)

> Frontend relies on responses.

`Design Before Coding`

Before writing code:

* List features
* Identify endpoints
* Choose methods

> Planning saves time.

### Mini Practice Task

Design APIs for a **Blog App**:

* Create post
* View posts
* Edit post
* Delete post

Write:

* Route
* Method

### Key Takeaways

* API flow shows how data travels
* Endpoints define actions
* Good API design = clean + consistent
* Always plan APIs before coding
