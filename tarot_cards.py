import random

cards = [
    {
        "name": "Шут",
        "image": "images/fool.jpg",
        "meaning": "Новое начало, лёгкость, свобода.",
        "advice": "Позволь себе начать с чистого листа.",
        "reversed": "Безрассудство, инфантильность."
    },
    {
        "name": "Маг",
        "image": "images/magician.jpg",
        "meaning": "Сила воли, уверенность, действие.",
        "advice": "Используй свои ресурсы.",
        "reversed": "Манипуляции, сомнения."
    },
    {
        "name": "Верховная Жрица",
        "image": "images/high_priestess.jpg",
        "meaning": "Интуиция, тайна, глубина.",
        "advice": "Доверься внутреннему голосу.",
        "reversed": "Игнорирование интуиции."
    },
    {
        "name": "Императрица",
        "image": "images/empress.jpg",
        "meaning": "Женственность, изобилие, любовь.",
        "advice": "Позволь себе наслаждаться жизнью.",
        "reversed": "Зависимость, излишества."
    },
    {
        "name": "Влюблённые",
        "image": "images/lovers.jpg",
        "meaning": "Выбор, чувства, союз.",
        "advice": "Слушай сердце.",
        "reversed": "Сомнения, разлад."
    }
]

def get_random_card():
    card = random.choice(cards)
    is_reversed = random.choice([True, False])
    return card, is_reversed