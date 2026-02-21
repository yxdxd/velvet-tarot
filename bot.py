import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import CommandStart
from config import BOT_TOKEN


# ⚠️ ВСТАВЬ СЮДА СВОЮ ССЫЛКУ NETLIFY
WEB_APP_URL = "https://roaring-pithivier-1a48d9.netlify.app"


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):

    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="✨ Открыть Velvet Tarot",
                    web_app=WebAppInfo(url=WEB_APP_URL)
                )
            ]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "✨ Velvet Tarot\n\n"
        "Твой персональный цифровой оракул.\n\n"
        "Нажми кнопку ниже, чтобы открыть приложение.",
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())