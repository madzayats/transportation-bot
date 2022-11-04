from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

# main menu

calc_trans_button = KeyboardButton('Рассчитать перевозку')
faq_button = KeyboardButton('FAQ - Вопросы и ответы')
hours_button = KeyboardButton('Адреса и режим работы')

main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)

main_menu_kb.add(calc_trans_button).add(faq_button).add(hours_button)



# technical support

call_tech_support = InlineKeyboardButton('🆘Написать в техническую поддержку🆘', callback_data='call_support')
call_support = InlineKeyboardMarkup().add(call_tech_support)
