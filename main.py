from aiogram import executor
from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove
from keybords import markup_city, markup_chek, markup_gender, markup_back, markup_out, markup_start
from database import add_user, add_user_gender, add_user_city, add_user_name, add_user_age, add_user_phone, add_user_university
from database import get_user_gender, get_user_age, get_user_city, get_user_name, get_user_phone, get_user_university
bot = Bot("6167889920:AAGRVlVBgK27zIXWuDRybgZ70Wh14-1pKf4")

dp = Dispatcher(bot, storage=MemoryStorage())

class States(StatesGroup):
    gender = State()
    name = State()
    phone = State()
    age = State()
    city = State()
    university = State()
    pass
user_states = {}

@dp.message_handler(state=States.gender)
async def add_gender(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    await state.finish()
    if message.text == "Выход":
        await bot.send_message(chat_id, f"Регистрация завершена", reply_markup=ReplyKeyboardRemove())
        dp.stop_polling()
    else:    
        add_user_gender(message)
        message = f"Дабавьте имя"
        await bot.send_message(chat_id, message, reply_markup=markup_out)
        await States.name.set()
        

@dp.message_handler(state=States.name)
async def add_name(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    await state.finish()
    if message.text == "Назад":
        await States.gender.set()
        await bot.send_message(chat_id, f"Дабавьте ваш пол", reply_markup=markup_gender) 
    elif message.text == "Выход":
        await bot.send_message(chat_id, f"Регистрация завершена", reply_markup=ReplyKeyboardRemove())
        dp.stop_polling()
    else: 
        add_user_name(message)   
        message = f"Дабавьте телефон"
        await bot.send_message(chat_id, message, reply_markup=markup_out)
        await States.phone.set()

@dp.message_handler(state=States.phone)
async def add_phone(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    await state.finish()
    if message.text == "Назад":
        await States.name.set()
        await bot.send_message(chat_id, f"Дабавьте имя", reply_markup=markup_out) 
    elif message.text == "Выход":
        await bot.send_message(chat_id, f"Регистрация завершена", reply_markup=ReplyKeyboardRemove())
        dp.stop_polling()
    else: 
        add_user_phone(message)
        message = f"Дабавьте ваш возраст"
        await bot.send_message(chat_id, message, reply_markup=markup_out)
        await States.age.set()
    
@dp.message_handler(state=States.age)
async def add_age(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    await state.finish()
    if message.text == "Назад":
        await States.phone.set()
        await bot.send_message(chat_id, f"Дабавьте телефон", reply_markup=markup_out) 
    elif message.text == "Выход":
        await bot.send_message(chat_id, f"Регистрация завершена", reply_markup=ReplyKeyboardRemove())
        dp.stop_polling()
    else: 
        add_user_age(message)
        message = f"Дабавьте город проживания"
        await bot.send_message(chat_id, message, reply_markup=markup_city)
        await States.city.set()

@dp.message_handler(state=States.city)
async def add_city(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    await state.finish()
    if message.text == "Назад":
        await States.age.set()
        await bot.send_message(chat_id, f"Дабавьте ваш возраст", reply_markup=markup_out) 
    elif message.text == "Выход":
        await bot.send_message(chat_id, f"Регистрация завершена", reply_markup=ReplyKeyboardRemove())
        dp.stop_polling()
    else:     
        add_user_city(message)
        message = f"Дабавьте университет"
        await bot.send_message(chat_id, message, reply_markup=markup_out)
        await States.university.set()

@dp.message_handler(state=States.university)
async def add_university(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    await state.finish()
    if message.text == "Назад":
        await States.city.set()
        await bot.send_message(chat_id, f"Дабавьте город проживания", reply_markup=markup_city) 
    elif message.text == "Выход":
        await bot.send_message(chat_id, f"Регистрация завершена", reply_markup=ReplyKeyboardRemove())
        dp.stop_polling()    
    else:    
        add_user_university(message)
        await bot.send_message(chat_id, f"Регистрация завершена", reply_markup=markup_start)           

@dp.message_handler(commands=['start'])
async def start_command_handler(message: types.Message):
    chat_id = message.chat.id
    await message.answer("Привет! Я бот для регистрации. Нажми 'Начать', чтобы начать регистрацию.", reply_markup=markup_start)
    if message.text == "Выход":
        await bot.send_message(chat_id, f"Регистрация завершена", reply_markup=ReplyKeyboardRemove())
        dp.stop_polling()
@dp.message_handler(text='Начать')
async def begin_message_handler(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    user_status = add_user(message)
    if user_status == False:
        message = f"Ваша уже заполнена. Нажмите кнопку посмотреть анкету" 
        await bot.send_message(chat_id, message)
    else:   
        message = f"Давай начнем регистрацию \n" \
                f"Напиши свой пол"
        await bot.send_message(chat_id, message, reply_markup=markup_gender)
        await States.gender.set()

@dp.message_handler(text='Проверить анкету')
async def start_message_handler(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    user_status = add_user(message)
    if user_status == False:
        user_gender = get_user_gender(chat_id)
        user_name = get_user_name(chat_id)
        user_phone = get_user_phone(chat_id)
        user_age = get_user_age(chat_id)
        user_city = get_user_city(chat_id)
        user_university = get_user_university(chat_id)
        message = f"Ваша анкета: \n" \
                f"Ваш пол: {user_gender} \n" \
                f"Ваше имя: {user_name} \n" \
                f"Ваш телефон: {user_phone} \n" \
                f"Ваш возраст: {user_age} \n" \
                f"Ваш город: {user_city} \n" \
                f"Ваш университет : {user_university} \n"
        await bot.send_message(chat_id, message)
    else:   
        message = f"Вы не были зарегестрированы, Давай начнем регистрацию \n" \
                f"Напиши свой пол"
        await bot.send_message(chat_id, message, reply_markup=markup_chek)
        await States.gender.set()        

@dp.message_handler(text='Изменить анкету')
async def change_handler(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    message = f"Давай начнем регистрацию \n" \
                f"Напиши свой пол"
    await bot.send_message(chat_id, message, reply_markup=markup_gender)
    await States.gender.set()

@dp.message_handler(text='Выход')
async def change_handler(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    await message.answer("Бот остановлен", reply_markup=ReplyKeyboardRemove())
    dp.stop_polling()

@dp.message_handler(commands=['stop'])
async def stop_bot_handler(message: types.Message):
    chat_id = message.chat.id
    await message.answer("Бот остановлен", reply_markup=ReplyKeyboardRemove())
    dp.stop_polling()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)