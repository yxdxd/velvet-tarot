import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# ---------------------------
# CORS (чтобы WebApp мог обращаться к API)
# ---------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# Карты
# ---------------------------
cards = [
    {
        "name": "Маг",
        "image": "/images/magician.jpg",
        "meaning": "Сила воли, уверенность, действие.",
        "advice": "Используй свои ресурсы."
    },
    {
        "name": "Императрица",
        "image": "/images/empress.jpg",
        "meaning": "Женственность, забота, изобилие.",
        "advice": "Позволь себе принять и насладиться."
    },
    {
        "name": "Влюбленные",
        "image": "/images/lovers.jpg",
        "meaning": "Выбор, чувства, союз.",
        "advice": "Слушай сердце."
    },
    {
        "name": "Жрица",
        "image": "/images/high_priestess.jpg",
        "meaning": "Интуиция, тайна, внутренний голос.",
        "advice": "Доверься внутреннему знанию."
    },
    {
        "name": "Шут",
        "image": "/images/fool.jpg",
        "meaning": "Новое начало, свобода, риск.",
        "advice": "Не бойся сделать первый шаг."
    }
]

# ---------------------------
# API endpoints
# ---------------------------

@app.get("/draw-card")
def draw_card():
    return random.choice(cards)


@app.get("/draw-spread")
def draw_spread():
    return random.sample(cards, 3)


# ---------------------------
# Подключаем картинки
# ---------------------------
app.mount("/images", StaticFiles(directory="images"), name="images")

# ---------------------------
# Подключаем webapp (HTML страницы)
# ---------------------------
app.mount("/", StaticFiles(directory="webapp", html=True), name="webapp")