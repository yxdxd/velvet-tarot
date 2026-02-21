import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import BotCommand

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- /start ---
@dp.message(CommandStart())
async def start(message: types.Message):
    text = (
        "✨ <b>Velvet Tarot</b>\n\n"
        "Твой персональный цифровой оракул.\n\n"
        "🔮 Чтобы начать — нажми кнопку <b>«Velvet Tarot»</b> слева внизу.\n\n"
        "Там тебя ждут:\n"
        "• Одна карта\n"
        "• Расклад Прошлое — Настоящее — Будущее\n\n"
        "Готов заглянуть в судьбу?"
    )

    await message.answer(text, parse_mode="HTML")

# --- Убираем все кастомные кнопки ---
async def set_commands():
    commands = [
        BotCommand(command="start", description="Перезапустить бота"),
    ]
    await bot.set_my_commands(commands)

async def main():
    await set_commands()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())