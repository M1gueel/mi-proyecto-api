from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from database import get_db
from models.user import User
from schemas.user import UserCreate, UserLogin, UserResponse
from utils.security import verify_password, get_password_hash
from utils.auth import create_access_token
from config import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    """Registrar nuevo usuario"""
    # Verificar si el usuario ya existe
    existing_user = db.query(User).filter(User.nombre == user.nombre).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya existe"
        )
    
    # Crear nuevo usuario
    hashed_password = get_password_hash(user.contraseña)
    db_user = User(
        nombre=user.nombre,
        contraseña=hashed_password,
        rol=user.rol
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

@router.post("/login")
async def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    """Iniciar sesión"""
    user = db.query(User).filter(User.nombre == user_credentials.nombre).first()
    
    if not user or not verify_password(user_credentials.contraseña, user.contraseña):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.nombre}, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "nombre": user.nombre,
            "rol": user.rol
        }
    }