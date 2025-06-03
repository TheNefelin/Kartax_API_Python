# Kartax API – FastAPI Project with PostgreSQL

Kartax API is a backend project built with **Python 3.12.10**, **FastAPI**, and **PostgreSQL** using **SQLAlchemy ORM**. This project demonstrates the setup of a clean API architecture with environment management, testing, and modular code organization.

## 🚀 Getting Started

### 🧪 Check Python Version & Installed Packages

```bash
py --version
py -m pip list
```

### 📦 Create and Activate Virtual Environment

```bash
py -m venv venv
```
```bash
venv\Scripts\activate  # On Windows
```
```bash
source venv/bin/activate  # On macOS/Linux
```

### 🔧 Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have the `requirements.txt`, install dependencies manually:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv pydantic-settings
```

Then, save them:

```bash
pip freeze > requirements.txt
```

## ▶️ Run the API Server

```bash
python run.py
```

Open in browser:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Root: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🗂️ Project Structure

```
my_api/
├── src/
│   ├── api/
│   │   ├── categories/
│   │   │   ├── crud.py      # Database operations for categories
│   │   │   ├── models.py    # SQLAlchemy models
│   │   │   ├── routes.py    # API routes
│   │   │   └── schemas.py   # Pydantic schemas
│   │   ├── groups/
│   │   │   └── models.py
│   │   ├── products/
│   │   │   └── models.py
│   │   └── stock_movements/
│   │       └── models.py
│   │
│   ├── core/
│   │   ├── config.py        # Environment and settings
│   │   ├── database.py      # DB connection setup
│   │   └── security.py      # Security and hashing utils
│   │
│   ├── shared/
│   │   └── responses.py
│   │
│   └── main.py              # FastAPI app instance
│
├── tests/
│   ├── __init__.py
│   ├── test_users.py
│   └── test_products.py
│
├── .env                    # Environment variables
├── .gitignore
├── LICENSE.txt
├── postgre.sql
├── README.md              # Project documentation
├── requirements.txt
├── run.py                 # App entry point
└── vercel.json
```

---

## 🐘 Dockerized PostgreSQL Setup

Launch PostgreSQL container:

```bash
docker run --name PostgreSQL -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
```

Manually create a development database and user:

```sql
CREATE DATABASE db_testing;
CREATE USER testing WITH PASSWORD 'testing';
GRANT ALL PRIVILEGES ON DATABASE db_testing TO testing;
GRANT USAGE ON SCHEMA public TO testing;
GRANT CREATE ON SCHEMA public TO testing;
-- Super Admin
GRANT ALL ON SCHEMA public TO testing;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO testing;
```

---

## 🧪 Testing

Tests are located in the `tests/` directory and should follow the structure of your API modules. Use `pytest` or `unittest` to execute them.

```bash
pip install pytest httpx
```
```bash
pytest
```

---

## 🔄 Reverse Engineering – Generate `models.py` from Database

To automatically generate SQLAlchemy models from an existing PostgreSQL database, you can use `sqlacodegen`.

### 1. Install `sqlacodegen`

```bash
pip install sqlacodegen
```

### 2. Generate models from the database

Make sure your PostgreSQL container is running and accessible, then run:

```bash
sqlacodegen postgresql://testing:testing@localhost:5432/db_testing > models.py
```

---

## 📄 License

This project is open source and available under a [Modified MIT License](LICENSE) that prohibits commercial use without explicit permission.
