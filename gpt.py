import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = 'YOUR_BOT_API_TOKEN'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Функция для отправки кнопок
async def send_keyboard(chat_id):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    # Кнопка "Назад"
    back_button = KeyboardButton("⏪Orqaga")
    keyboard.add(back_button)
    await bot.send_message(chat_id, "Выберите действие", reply_markup=keyboard)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await send_keyboard(message.chat.id)

# Обработчик нажатия на кнопки
@dp.message_handler(lambda message: message.text == "⏪Orqaga")
async def process_back_button(message: types.Message):
    try:
        # Выполняем нужное действие, например, отправляем другое сообщение или меняем состояние
        await bot.send_message(message.chat.id, "Вы нажали '⏪Orqaga', выполняю действие...")
        # Например, можно снова отправить клавиатуру или выполнить другие действия
        await send_keyboard(message.chat.id)
    except Exception as e:
        # Обрабатываем ошибки
        await bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")

if name == 'main':
    executor.start_polling(dp, skip_updates=True)