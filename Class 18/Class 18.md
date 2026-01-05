`What We Covered in Class 18`
- In this class, we connected **backend theory** with **real-life usage**.

`Topics discussed:`
- What Backend is
- What APIs do in Backend
- API Designing
- Identifying correct API methods
- API flow in a real-life project

`What is Backend?`

**Backend** is the part of an application that:
- Stores data
- Handles logic
- Manages users
- Talks to the database

> Backend works **behind the scenes**.

### Backend Handles:
- Login & Signup
- Saving data
- Fetching data
- Updating data
- Deleting data

> Example: When you like a post, backend saves that like.

`What are APIs in Backend?`

APIs are used by backend to:
- Receive requests from frontend
- Process data
- Send responses back

> Frontend **cannot directly access database**  
> API is the **safe middle layer**.

`API Designing (Thinking Before Coding)`

### What is API Designing?
API designing means:
- Planning routes
- Choosing methods
- Deciding what data is needed

Good APIs are:
- Clear
- Predictable
- Easy to use

### Example: User API Design
```text
GET    /users        → get all users
POST   /users        → create new user
PUT    /users/{id}   → update full user
PATCH  /users/{id}   → update part of user
DELETE /users/{id}   → delete user
```
