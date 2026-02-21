import asyncio
import os
from datetime import date
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    FSInputFile,
    WebAppInfo
)

from config import BOT_TOKEN
from tarot_cards import get_random_card, cards
from database import (
    init_db,
    add_user,
    save_card,
    get_card_count,
    get_top_card,
    get_monthly_energy,
    save_monthly_energy
)

# ------------------------
# ИНИЦИАЛИЗАЦИЯ
# ------------------------

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

WEB_APP_URL = "https://roaring-pithivier-1a48d9.netlify.app"

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔮 Карта дня")],
        [KeyboardButton(text="💖 Расклад на любовь")],
        [KeyboardButton(text="🌙 Энергия месяца")],
        [KeyboardButton(text="🧬 Мой архетип")],
        [KeyboardButton(
            text="🃏 Открыть приложение",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )]
    ],
    resize_keyboard=True
)

# ------------------------
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ------------------------

def find_card_by_name(name):
    for c in cards:
        if c["name"] == name:
            return c
    return None

def analyze_repetition(user_id, card_name):
    count = get_card_count(user_id, card_name)
    if count == 2:
        return "✨ Эта карта появляется снова. Энергия усиливается."
    elif count >= 3:
        return "🌙 Эта энергия настойчиво возвращается. Здесь важный урок."
    return ""

# ------------------------
# ОБРАБОТЧИКИ
# ------------------------

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    user = message.from_user
    add_user(user.id, user.username, user.first_name)

    await message.answer(
        f"Привет, {user.first_name} 🌙\n\n"
        "Я — твой личный оракул.\n"
        "Выбери действие ✨",
        reply_markup=keyboard
    )

# 🔥 WEB APP ROUTER
@dp.message(lambda message: message.web_app_data is not None)
async def webapp_router(message: types.Message):
    action = message.web_app_data.data
    user = message.from_user

    # 🔮 Карта дня
    if action == "card_day":
        card, is_reversed = get_random_card()
        save_card(user.id, card["name"], str(date.today()))

        position = "Перевернутая" if is_reversed else "Прямая"
        meaning = card["reversed"] if is_reversed else card["meaning"]

        text = (
            f"🔮 Карта дня\n\n"
            f"{card['name']} ({position})\n\n"
            f"{meaning}\n\n"
            f"Совет:\n{card['advice']}"
        )

        image_path = os.path.join(BASE_DIR, card["image"])
        await message.answer_photo(FSInputFile(image_path), caption=text)

    # 💖 Любовный расклад
    elif action == "love_spread":
        cards_drawn = [get_random_card() for _ in range(3)]
        titles = ["Мысли", "Чувства", "Действия"]

        for i, (card, is_reversed) in enumerate(cards_drawn):
            save_card(user.id, card["name"], str(date.today()))

            position = "Перевернутая" if is_reversed else "Прямая"
            meaning = card["reversed"] if is_reversed else card["meaning"]

            text = (
                f"💖 {titles[i]}\n\n"
                f"{card['name']} ({position})\n\n"
                f"{meaning}"
            )

            image_path = os.path.join(BASE_DIR, card["image"])
            await message.answer_photo(FSInputFile(image_path), caption=text)

    # ⚡ На ситуацию
    elif action == "situation_spread":
        card, is_reversed = get_random_card()
        save_card(user.id, card["name"], str(date.today()))

        position = "Перевернутая" if is_reversed else "Прямая"
        meaning = card["reversed"] if is_reversed else card["meaning"]

        text = (
            f"⚡ На ситуацию\n\n"
            f"{card['name']} ({position})\n\n"
            f"{meaning}\n\n"
            f"Совет:\n{card['advice']}"
        )

        image_path = os.path.join(BASE_DIR, card["image"])
        await message.answer_photo(FSInputFile(image_path), caption=text)

    # 🧬 Архетип
    elif action == "archetype":
        result = get_top_card(user.id)
        if not result:
            await message.answer("Сделай несколько раскладов.")
        else:
            card_name, count = result
            await message.answer(
                f"🧬 Твой архетип — {card_name}\n"
                f"Проявлялся {count} раз."
            )

    # 🌙 Энергия месяца
    elif action == "month_energy":
        current_month = date.today().strftime("%Y-%m")
        existing = get_monthly_energy(user.id, current_month)

        if existing:
            card = find_card_by_name(existing[0])
        else:
            card, _ = get_random_card()
            save_monthly_energy(user.id, current_month, card["name"])

        text = (
            f"🌙 Энергия месяца — {card['name']}\n\n"
            f"{card['meaning']}"
        )

        image_path = os.path.join(BASE_DIR, card["image"])
        await message.answer_photo(FSInputFile(image_path), caption=text)

# ------------------------

async def main():
    init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())