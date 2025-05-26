import os
from dotenv import load_dotenv

load_dotenv()

# Base de datos
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://mi_usuario:mi_password_seguro@localhost:5432/mi_database")

# JWT
SECRET_KEY = os.getenv("SECRET_KEY", "tu_clave_secreta_muy_larga_y_segura_aqui")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))