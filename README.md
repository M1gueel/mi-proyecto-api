
# 📦 Mi Proyecto API

API REST desarrollada con **FastAPI**, **PostgreSQL**, **JWT**, **Docker** y **SQLAlchemy**, diseñada para manejar autenticación, usuarios y productos.

---

## 🚀 Características

- 🔐 Autenticación con JWT
- 👤 Gestión de usuarios
- 📦 Gestión de productos
- 🐳 Contenedores Docker
- 🛠 Migraciones con Alembic
- 🌍 CORS habilitado
- 🧪 Endpoints de salud (`/health`)

---

## 📁 Estructura del proyecto

```

mi-proyecto-api/
│
├── app/
│   ├── main.py             # Punto de entrada de FastAPI
│   ├── database.py         # Conexión a la base de datos
│   ├── config.py           # Variables de entorno
│   └── routers/            # Rutas divididas por módulos
│       ├── auth.py
│       ├── users.py
│       └── products.py
│
├── alembic/                # Migraciones de base de datos
├── .env                    # Variables de entorno
├── .env.template           # Plantilla de variables de entorno
├── requirements.txt
├── Dockerfile
└── docker-compose.yml

````

---

## ⚙️ Variables de entorno

Crea un archivo `.env` a partir del siguiente `.env.template`:

```env
DATABASE_URL=postgresql://usuario:contraseña@postgres_db_productos:5432/nombre_db
SECRET_KEY=pon_aqui_tu_clave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
````

---

## 🐳 Cómo correr con Docker

1. Asegúrate de tener Docker y Docker Compose instalados
2. Levanta los contenedores:

```bash
docker compose up --build
```

3. Accede a la API en [http://localhost:8000](http://localhost:8000)

---

## 🔧 Alembic (migraciones)

Dentro del contenedor de FastAPI:

```bash
docker exec -it fastapi_app_productos bash
alembic revision --autogenerate -m "create tables"
alembic upgrade head
```

---

## 🌐 Endpoints útiles

| Método | Ruta          | Descripción      |
| ------ | ------------- | ---------------- |
| GET    | `/`           | Bienvenida       |
| GET    | `/health`     | Health check     |
| POST   | `/auth/login` | Iniciar sesión   |
| POST   | `/users/`     | Crear usuario    |
| GET    | `/products/`  | Listar productos |

---

## 📄 Licencia

MIT

---

## 👨‍💻 Autor

Desarrollado por Miguel Guilca
