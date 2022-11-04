import logging
import os
from random import randint

from aiogram import Bot, Dispatcher, executor, types
from menu import *

bot_token = os.getenv('bot_token')
API_TOKEN = bot_token

logging.basicConfig(level=logging.INFO)

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

@dp.message_handler(text=['Рассчитать перевозку'])
async def calc_trans(message: types.Message):
    await bot.send_message(message.from_user.id, f"test")


@dp.message_handler(text=['FAQ - Вопросы и ответы'])
async def call_faq(message: types.Message):
    await bot.send_message(message.from_user.id, f"1️⃣❓ Сколько идет моя посылка?\n"
                                                 f"Ваша посылка будет от 3 дней в зависимости от вашего региона\n\n"
                                                 f"2️⃣❓ Могу я оплатить наложенным платежем?\n"
                                                 f"Да, можете\n\n"
                                                 f"3️⃣❓ Могу ли я застраховать посылку?\n"
                                                 f"Да, можете, стоиость страхования от 150р\n\n"
                                                 f"4️⃣❓ Есть ли у вас экспресс доставка?\n"
                                                 f"Да, есть от 1 до 3 дней\n\n"
                                                 f"🆘Больше информации на нашем сайте Грузики.РФ🆘",reply_markup=call_support)

@dp.callback_query_handler(lambda c: c.data == 'call_support')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.send_message(-714795919, "Обращение №")
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Ваше сообщение успешно отправлено в техническую поддержку')


@dp.message_handler(text="Адреса и режим работы")
async def working_mode(message: types.Message):
    await bot.send_message(message.from_user.id, '📍Компания: Грузики.РФ\n'
                                                 'Улица Ленина, дом 16\n'
                                                 'Будние дни: с 8:00 до 19:00\n'
                                                 'Выходные дни: с 9:00 до 13:00\n\n'
                                                 '📍Компания: Грузики.РФ\n'
                                                 'Улица Кутузовская, дом 55\n'
                                                 'Будние дни: с 8:00 до 19:00\n'
                                                 'Выходные дни: с 10:00 до 15:00\n\n'
                                                 '📍Компания: Грузики.РФ\n'
                                                 'Улица Арбатская, дом 8\n'
                                                 'Будние дни: с 7:00 до 19:00\n'
                                                 'Выходные дни: с 8:00 до 15:00')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(calc_trans, commands=['Рассчитать перевозку'])
    dp.register_message_handler(working_mode, commands=['Адреса и режим работы'])
    dp.register_message_handler(call_faq, commands=['FAQ - Вопросы и ответы'])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)