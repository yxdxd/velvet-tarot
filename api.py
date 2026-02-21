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
        "image": "/images/magician.jpg"
    },
    {
        "name": "Императрица",
        "image": "/images/empress.jpg"
    },
    {
        "name": "Влюбленные",
        "image": "/images/lovers.jpg"
    },
    {
        "name": "Жрица",
        "image": "/images/high_priestess.jpg"
    },
    {
        "name": "Шут",
        "image": "/images/fool.jpg"
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