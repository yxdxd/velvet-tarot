import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from tarot_cards import tarot_cards

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Если потом добавим изображения
app.mount("/images", StaticFiles(directory="images"), name="images")


def prepare_card(card):
    is_reversed = random.choice([True, False])

    return {
        "name": card["name"],
        "position": "Перевёрнутая" if is_reversed else "Прямая",
        "meaning": card["reversed"] if is_reversed else card["meaning"],
        "advice": card["advice"],
        "reversed": is_reversed
    }


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