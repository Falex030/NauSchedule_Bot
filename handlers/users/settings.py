from aiogram.types import Message
from handlers.users.about_bot import bot_about
from loader import dp
from keyboards.default.about_bot_key import keyboard_about


@dp.message_handler(text='На сьогодні')
async def schedule_today(message: Message):
    # функціонал виводу інформації про цьогоднішній розклад
    await message.answer('Розклад на сьогодні')


@dp.message_handler(text="На завтра")
async def schedule_tomorrow(message: Message):
    # функціонал виводу інформації про завтрішній  розклад
    await message.answer('Розклад на завтра')


from aiogram.dispatcher.filters.builtin import Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import main_menu
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from states.botStates import StatesOfBot
from keyboards.default import main_menu
from aiogram.types import Message
from aiogram.utils.emoji import emojize



@dp.message_handlers(text='Налаштування')
async def settings_menu(message: Message):
    text = (
        'Розклад')
    await message.answer(text)
