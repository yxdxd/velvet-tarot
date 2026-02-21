import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 Подключаем папку images
app.mount("/images", StaticFiles(directory="images"), name="images")

cards = [
    {"name": "Маг", "image": "/images/magician.jpg"},
    {"name": "Императрица", "image": "/images/empress.jpg"},
    {"name": "Влюбленные", "image": "/images/lovers.jpg"}
]

@app.get("/draw-card")
def draw_card():
    return random.choice(cards)

@app.get("/draw-spread")
def draw_spread():
    return random.sample(cards, 3)