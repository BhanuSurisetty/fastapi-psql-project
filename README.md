# FastAPI + PostgreSQL CRUD API

This is a backend project built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. It provides basic user management operations (Create and Read).

---
## 📁 Project Structure
fastapi_psql_project/
├── app/
│ ├── main.py # FastAPI application entry point
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── crud.py # CRUD logic
│ ├── database.py # DB session and engine
│ └── init.py # Package initializer
├── requirements.txt # Python dependencies
├── README.md # Project overview


---

## 🚀 Features

- Add new users (`/add_user`)
- Get all users (`/get_users`)
- Auto-creates tables on startup
- Prevents duplicate users
- Uses PostgreSQL with SQLAlchemy ORM

---

## 🛠 Setup Instructions

### 1. Clone the repository

git clone https://github.com/your-username/fastapi-psql-project.git  
cd fastapi-psql-project

---

### 2. Create virtual environment and activate

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

---

### 3. Install dependencies
pip install -r requirements.txt

---
### 4. Configure Database
In database.py, update your PostgreSQL URL:
DATABASE_URL = "postgresql://username:password@localhost/dbname"

---

### 5. Run the app
uvicorn app.main:app --reload

---

### 📬 API Endpoints
- Method	Endpoint	Description
- POST	/add_user	Add a new user
- GET	/get_users	List all users
 ---
### 📘 Visit Swagger Docs:
http://127.0.0.1:8000/docs

---
### Sample Request Body (POST /add_user)
{
  "name": "bhanu",
  "email": "bhanu123@gmail.com"
}

---
### 🔒 To-Do Features
- Add update/delete endpoints

- Add authentication (JWT)

- Dockerize the app

---


### 📄 License
MIT License © 2025 Bhanu Surisetty

---

Let me know if you also want:

- `.gitignore`
- `requirements.txt`
- Dockerfile setup  
I can help generate those too.


