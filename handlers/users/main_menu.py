from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import main_menu
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from states.botStates import StatesOfBot
from keyboards.default import main_menu
from aiogram.types import Message
from aiogram.utils.emoji import emojize
from loader import dp


@dp.message_handler(text='На сьогодні')
async def schedule_today(message: Message):
    # функціонал виводу інформації про цьогоднішній розклад
    await message.answer('Розклад на сьогодні')


@dp.message_handler(text="На завтра")
async def schedule_tomorrow(message: Message):
    # функціонал виводу інформації про завтрішній  розклад
    await message.answer('Розклад на завтра')



@dp.message_handlers(text='Розклад')
async def serch_schedue(message : Message):
    text = (
        f'{emojize(":bell:")} 1 пара \n {emojize(":alarm_clock:")} 8:00 - 9:35 \n' 
        f'{emojize(":bell:")} 2 пара \n {emojize(":alarm_clock:")} 9:50-11:25 \n'
        f'{emojize(":bell:")} 3 пара \n {emojize(":alarm_clock:")} 11:40 - 13:15 \n'
        f'{emojize(":bell:")} 4 пара \n {emojize(":alarm_clock:")} 13:30-15:05 \n'
        f'{emojize(":bell:")} 5 пара \n {emojize(":alarm_clock:")} 15:20-16:55 \n'
        f'{emojize(":bell:")} 6 пара \n {emojize(":alarm_clock:")} 17:10-18:45 \n'
        f'{emojize(":bell:")} 7 пара \n {emojize(":alarm_clock:")} 19:00-20:35')
    await message.answer(text)



@dp.message_handler(text="Розклад дзвінків")
async def schedule_bell(message: Message):
    # функціонал виводу інформації про завтрішній  розклад
    await message.answer('Розклад дзвінків ')


@dp.message_handler(text="Налаштування")
async def setup_keyboard(message: Message):
    # функціонал виводу інформації про завтрішній  розклад
    await message.answer('Налаштування ')


@dp.message_handler(text="Номер неділі")
async def num_week(message: Message):
    # функціонал виводу інформації про завтрішній  розклад
    await message.answer('Номер неділі ')


@dp.message_handler(text="Про бота")
async def about(message: Message):
    # функціонал виводу інформації про завтрішній  розклад
    await message.answer('/about')
