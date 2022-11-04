from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

calc_trans_button = KeyboardButton('/Рассчитать перевозку')
faq_button = KeyboardButton('FAQ - Вопросы и ответы')
hours_button = KeyboardButton('Адреса и режим работы')

main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)

main_menu_kb.add(calc_trans_button).add(faq_button).add(hours_button)