import logging
import os

from aiogram import Bot, Dispatcher, executor, types

bot_token = os.getenv('bot_token')
API_TOKEN = bot_token

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"👋Добрый день, {message.from_user.first_name}\n"
                        f"Вас приветствует телеграмм-канал грузоперевозок по России, Азии и Европе\n"
                        f"На данной странице вы можете:\n"
                        f"🕖Расчитать и заказать перевозку\n"
                        f"🔥Узнать ответы на интересующие вас вопросы")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)