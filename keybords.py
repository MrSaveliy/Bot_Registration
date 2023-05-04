from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove)


markup_start = ReplyKeyboardMarkup(resize_keyboard=True)
start_button = KeyboardButton('Начать')
get_out = KeyboardButton(text='Выход', callback_data='stop')
change_user_list = KeyboardButton(text='Изменить анкету', callback_data='start')
check_user_list = KeyboardButton(text='Проверить анкету')
markup_start.add(start_button,change_user_list,check_user_list, get_out)

markup_gender = ReplyKeyboardMarkup(resize_keyboard=True)
male_button = KeyboardButton('Мужской')
female_button = KeyboardButton('Женский')
get_out = KeyboardButton(text='Выход', callback_data='stop')
markup_gender.add(male_button, female_button, get_out )

markup_chek = ReplyKeyboardMarkup(resize_keyboard=True)
check_user_list = KeyboardButton(text='Проверить анкету')
change_user_list = KeyboardButton(text='Изменить анкету', callback_data='start')
back_button = KeyboardButton(text='Назад')
get_out = KeyboardButton(text='Выход', callback_data='stop')
markup_chek.add(check_user_list, change_user_list, back_button, get_out)


markup_out = ReplyKeyboardMarkup(resize_keyboard=True)
back_button = KeyboardButton(text='Назад')
cancel_registration = KeyboardButton(text='Выход', callback_data='stop')
markup_out.add(back_button, cancel_registration)

markup_city = ReplyKeyboardMarkup(resize_keyboard=True)
moscow_button = KeyboardButton('Москва')
spb_button = KeyboardButton('СПБ')
back_button = KeyboardButton(text='Назад')
cancel_registration = KeyboardButton(text='Выход', callback_data='stop')
markup_city.add(moscow_button, spb_button, back_button, cancel_registration)

markup_back = ReplyKeyboardMarkup(resize_keyboard=True)
back_button = KeyboardButton(text='Назад')
markup_back.add(back_button)