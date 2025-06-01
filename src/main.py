from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session
# Importamos lo necesario para la base:
from src.core.database import Base, engine, get_db
# 👇 Importamos todos los modelos para que SQLAlchemy los registre
from src.api.categories.models import Category
from src.api.groups.models import Group
from src.api.products.models import Product as ProductModel
from src.api.stock_movements.models import StockMovement
# Rutas
from src.api.categories.routes import router as category_router

app = FastAPI(title="Kartax API")

# Creamos las tablas (si no existen) al arrancar la app
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Api Running"}

@app.get("/db-version")
def read_db_version(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT version()")).scalar()
    return {"postgres_version": result}

app.include_router(category_router)