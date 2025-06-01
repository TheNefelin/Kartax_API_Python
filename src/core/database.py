from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.core.config import settings

# Engine de SQLAlchemy, usando la URL que vino de settings.database_url
engine = create_engine(settings.database_url)

# Crea un "SessionLocal" que será tu sesión con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para tus modelos, para que luego "Category" u otros puedan heredar
Base = declarative_base()

# Esta función se usa en FastAPI como dependencia para obtener una sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
