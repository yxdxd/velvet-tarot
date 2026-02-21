import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from tarot_cards import tarot_cards

app = FastAPI()

# -------------------------
# CORS (для Telegram WebApp)
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Функция подготовки карты
# -------------------------
def prepare_card(card):
    is_reversed = random.choice([True, False])

    return {
        "name": card["name"],
        "position": "Перевёрнутая" if is_reversed else "Прямая",
        "meaning": card["reversed"] if is_reversed else card["meaning"],
        "advice": card["advice"]
    }

# -------------------------
# API endpoints
# -------------------------

@app.get("/draw-card")
def draw_card():
    card = random.choice(tarot_cards)
    return prepare_card(card)


@app.get("/draw-spread")
def draw_spread():
    cards = random.sample(tarot_cards, 3)

    return {
        "past": prepare_card(cards[0]),
        "present": prepare_card(cards[1]),
        "future": prepare_card(cards[2])
    }

# -------------------------
# Статические файлы
# -------------------------

# картинки
app.mount("/images", StaticFiles(directory="images"), name="images")

# HTML (главная, single, spread и т.д.)
app.mount("/", StaticFiles(directory="webapp", html=True), name="webapp")