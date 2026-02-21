import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем папку с картинками
app.mount("/images", StaticFiles(directory="images"), name="images")

cards = [
    {"name": "Маг", "image": "/images/magician.jpg"},
    {"name": "Императрица", "image": "/images/empress.jpg"},
    {"name": "Влюбленные", "image": "/images/lovers.jpg"},
    {"name": "Шут", "image": "/images/fool.jpg"},
    {"name": "Жрица", "image": "/images/high_priestess.jpg"},
]

# ===== HTML =====

@app.get("/")
def root():
    return FileResponse("webapp/index.html")

@app.get("/single.html")
def single():
    return FileResponse("webapp/single.html")

@app.get("/spread.html")
def spread():
    return FileResponse("webapp/spread.html")

@app.get("/triple.html")
def triple():
    return FileResponse("webapp/triple.html")

@app.get("/draw.html")
def draw():
    return FileResponse("webapp/draw.html")

# ===== API =====

@app.get("/draw-card")
def draw_card():
    return random.choice(cards)

@app.get("/draw-spread")
def draw_spread():
    return random.sample(cards, 3)