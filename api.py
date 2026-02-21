import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from tarot_cards import cards

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 Подключаем папку images
app.mount("/images", StaticFiles(directory="images"), name="images")


@app.get("/draw-card")
def draw_card():
    card = random.choice(cards)
    is_reversed = random.choice([True, False])

    return {
        "name": card["name"],
        "meaning": card["reversed"] if is_reversed else card["meaning"],
        "advice": card["advice"],
        "image": f"https://velvet-tarot.onrender.com/{card['image']}",
        "reversed": is_reversed
    }