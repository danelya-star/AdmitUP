from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import users, auth, plan, university
from .db import connect_to_mongo, close_mongo_connection
from .. import essay_checker
from .. import motivation_letter

app = FastAPI(
    title="AdmitUP API",
    description="API для подготовки к поступлению и IELTS с помощью ИИ."
)

# Настройка CORS
origins = [
    # Localhost для разработки
    "http://localhost:3000",      # React (Create React App)
    "http://localhost:5173",      # React (Vite) / Vue
    "http://localhost:3001",      # Nuxt 3 лендинг
    "http://localhost:8080",      # Другие варианты
    # Production
    "https://tvoj-frontend.onrender.com",  # Замените на реальный URL фронтенда
    # Для локальной сети (если нужно)
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# События старта и остановки базы
@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

@app.get("/")
async def root():
    return {"message": "Welcome to AdmitUP API! Visit /docs for Swagger UI"}

# Подключаем роуты
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(plan.router, prefix="/plan", tags=["plan"])
app.include_router(university.router, prefix="/university", tags=["university"])
app.include_router(essay_checker.router, prefix="/api", tags=["IELTS Checker"])
app.include_router(motivation_letter.router, prefix="/api", tags=["Motivation Letter"])
