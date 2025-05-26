from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, users, products
from database import engine, Base
# IMPORTANTE: Importar los modelos para que SQLAlchemy los reconozca
from models import user, product
import uvicorn

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mi API REST",
    description="API con PostgreSQL, JWT y Docker",
    version="1.0.0",
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(products.router, prefix="/products", tags=["products"])

@app.get("/")
async def root():
    return {"message": "¡API funcionando correctamente!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
