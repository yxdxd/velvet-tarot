import random
import os
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

# 🔥 Абсолютный путь к images
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
images_path = os.path.join(BASE_DIR, "images")

app.mount("/images", StaticFiles(directory=images_path), name="images")


@app.get("/draw-card")
def draw_card():
    card = random.choice(cards)
    is_reversed = random.choice([True, False])

    return {
        "name": card["name"],
        "meaning": card["reversed"] if is_reversed else card["meaning"],
        "advice": card["advice"],
        "image": f"https://velvet-tarot.onrender.com/images/{card['image'].split('/')[-1]}",
        "reversed": is_reversed
    }