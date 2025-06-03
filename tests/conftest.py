# tests/conftest.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.app import app  # O src.main si aún no renombraste
from src.core.database import Base, get_db
from src.core.config import settings

# URL de tu base de datos de testing
SQLALCHEMY_DATABASE_URL = settings.test_database_url

# Crear el engine y la sesión de testing
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear todas las tablas antes de los tests
Base.metadata.create_all(bind=engine)

# Override de la dependencia get_db para usar la base de datos de test
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Aplicamos el override a la app
app.dependency_overrides[get_db] = override_get_db

# Fixture pytest para obtener un cliente de prueba
@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
