from aiogram.types import Message

from loader import dp


@dp.message_handler(text='На сьогодні')
async def schedule_today(message: Message):
    # функціонал виводу інформації про цьогоднішній розклад
    await message.answer('Розклад на сьогодні')


@dp.message_handler(text="На завтра")
async def schedule_tomorrow(message: Message):
    # функціонал виводу інформації про завтрішній  розклад
    await message.answer('Розклад на завтра')


@dp.message_handler(text="Розклад")
async def schedule(message: Message):
    # функціонал виводу інформації про завтрішній  розклад
    await message.answer('Розклад ')


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
