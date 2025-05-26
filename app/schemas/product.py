from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from decimal import Decimal

class ProductBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: Optional[Decimal] = None
    stock: Optional[int] = 0
    categoria: Optional[str] = None
    activo: Optional[bool] = True

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[Decimal] = None
    stock: Optional[int] = None
    categoria: Optional[str] = None
    activo: Optional[bool] = None

class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True