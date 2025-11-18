# crud-app
# 🧑‍💻 Flask User Management API

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=yellow)
![Flask](https://img.shields.io/badge/Flask-1.1.2-lightgrey?logo=flask)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🔹 Project Overview

This is a **simple and efficient User Management API** built with **Flask**.  
It allows you to **create, read, update, and delete users**, with persistent storage in a **JSON file**. Perfect for learning API development or testing frontend integrations.

---

## 🛠 Features

- ✅ **CRUD Operations**: Create, Read, Update, Delete users  
- ✅ **Persistent Storage**: Users saved in `users.json`  
- ✅ **JSON-based API**: Easy to integrate with any frontend or tool  
- ✅ **Unique User IDs** for each user  
- ✅ **Lightweight & Simple**: No database required  

---

## 🚀 API Endpoints

| Method | Endpoint            | Description                 |
|--------|-------------------|-----------------------------|
| GET    | `/users`           | Get all users               |
| GET    | `/users/<id>`      | Get a single user by ID     |
| POST   | `/users`           | Create a new user           |
| PUT    | `/users/<id>`      | Update an existing user     |
| DELETE | `/users/<id>`      | Delete a user by ID         |

🎯 Future Improvements
Auto-generate unique user IDs.
Add search and filter functionality.
Connect to a database like SQLite or MongoDB for large-scale usage.
Add authentication and authorization.

**Example POST JSON Body**:

```json
{
    "id": 1,
    "name": "Niharikaa Singh",
    "email": "niharikaa21@gmail.com"
}'''

