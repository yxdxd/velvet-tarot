import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    }
]

@app.get("/draw-card")
def draw_card():
    card = random.choice(cards)
    return card

@app.get("/draw-spread")
def draw_spread():
    return random.sample(cards, 3)