import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from menu import *

bot_token = os.getenv('bot_token')
API_TOKEN = bot_token

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"👋Добрый день, {message.from_user.first_name}\n"
                        f"Вас приветствует телеграмм-канал грузоперевозок по России, Азии и Европе\n"
                        f"На данной странице вы можете:\n"
                        f"🕖Расчитать и заказать перевозку\n"
                        f"🔥Узнать ответы на интересующие вас вопросы",
                        reply_markup=main_menu_kb)

@dp.message_handler(text="Адреса и режим работы")
async def working_mode(message: types.Message):
    await bot.send_message(message.from_user.id, 'Компания: Грузики.РФ\n'
                                                 'Улица Ленина, дом 16\n'
                                                 'С 8:00 до 19:00')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(working_mode, commands=['Адреса и режим работы'])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)