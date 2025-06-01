
# 📚 Estudio de Dependencias Usadas en Kartax API (Python 3.12)

Este documento tiene como objetivo explicar cada una de las librerías instaladas en el proyecto `Kartax API`, su propósito y ejemplos básicos de uso.

---

## 📦 Librerías Instaladas

### 1. `fastapi`
- **Uso:** Framework web moderno para crear APIs con Python 3.7+ basado en anotaciones de tipo.
- **Instalación:** `pip install fastapi`
- **Ejemplo:**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

---

### 2. `uvicorn`
- **Uso:** Servidor ASGI para ejecutar aplicaciones FastAPI o Starlette.
- **Instalación:** `pip install uvicorn`
- **Ejemplo:**
```bash
uvicorn main:app --reload
```

---

### 3. `sqlalchemy`
- **Uso:** ORM (Object Relational Mapper) que permite interactuar con bases de datos mediante objetos de Python.
- **Instalación:** `pip install sqlalchemy`
- **Ejemplo:**
```python
from sqlalchemy import Column, Integer, String, create_engine, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
```

---

### 4. `psycopg2-binary`
- **Uso:** Driver para conectarse a bases de datos PostgreSQL desde Python.
- **Instalación:** `pip install psycopg2-binary`
- **Ejemplo:**
```python
import psycopg2

conn = psycopg2.connect(
    dbname="mydb", user="myuser", password="mypassword", host="localhost"
)
```

---

### 5. `python-dotenv`
- **Uso:** Carga variables de entorno desde archivos `.env`.
- **Instalación:** `pip install python-dotenv`
- **Ejemplo:**
```python
from dotenv import load_dotenv
import os

load_dotenv()
db_user = os.getenv("DB_USER")
```

---

### 6. `pydantic-settings`
- **Uso:** Nueva forma de manejar configuración basada en clases con validación de tipos usando Pydantic v2+.
- **Instalación:** `pip install pydantic-settings`
- **Ejemplo:**
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Kartax API"
    db_url: str

    class Config:
        env_file = ".env"
```

### 7. Ingenieria inversa Tablas BD a models.py
```bash
pip install sqlacodegen
```
```bash
sqlacodegen postgresql://testing:testing@localhost:5432/db_testing > models.py
```

---

## 📌 Recomendaciones
- Usa `pip freeze > requirements.txt` para guardar tus dependencias.
- Usa un entorno virtual con `venv` para aislar tus paquetes.
- No subas tu archivo `.env` al repositorio por seguridad.

---

## 🧠 Consejos para Estudio
- Lee la documentación oficial de cada librería.
- Prueba ejemplos pequeños y aislados.
- Usa `IPython` o `Jupyter Notebooks` para practicar.

---

© Kartax API - Estudio Personal
