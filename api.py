import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tarot_cards import cards

app = FastAPI()

# Разрешаем запросы с Mini App
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/draw-card")
def draw_card():
    card = random.choice(cards)
    is_reversed = random.choice([True, False])

    return {
        "name": card["name"],
        "meaning": card["reversed"] if is_reversed else card["meaning"],
        "advice": card["advice"],
        "image": card["image"],
        "reversed": is_reversed
    }

@app.get("/love-spread")
def love_spread():
    spread = []
    titles = ["Мысли", "Чувства", "Действия"]

    for i in range(3):
        card = random.choice(cards)
        is_reversed = random.choice([True, False])

        spread.append({
            "title": titles[i],
            "name": card["name"],
            "meaning": card["reversed"] if is_reversed else card["meaning"],
            "image": card["image"],
            "reversed": is_reversed
        })

    return spread