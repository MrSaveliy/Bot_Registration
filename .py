from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keybords import markup
from database import add_user, add_user_gender, add_user_city, add_user_name, add_user_age, add_user_phone, add_user_university

@dp.message_handler(Command("start"))
async def start_message(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    await message.answer("Привет! Я бот для регистрации. Нажми 'Начать', чтобы начать регистрацию.", reply_markup=markup)
    user_status = add_user(message)
    if user_status == False:
        pass
    else:
        await bot.send_message(chat_id, f"Привет, {message.chat.first_name}! \n"
                                            f"Давай начнем регистрацию \n"
                                            f"Напиши свой пол")
        await States.gender.set()