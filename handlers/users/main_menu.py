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



<<<<<<< HEAD
@dp.message_handlers(text='Розклад')
=======
@dp.message_handler(text='Розклад')
>>>>>>> ebf36c4 (Add change in main_menu)
async def schedue(message: Message):
    text = (
        'Розклад')
    await message.answer(text)

<<<<<<< HEAD

@dp.message_handlers(text='Розклад дзвінків')
async def search_schedule(message: Message):
=======
@dp.message_handler(text='Розклад дзвінків')
async def serch_schedue(message: Message):
>>>>>>> ebf36c4 (Add change in main_menu)
    text = (
        f'{emojize(":bell:")} 1 пара \n {emojize(":alarm_clock:")} 8:00 - 9:35 \n\n' 
        f'{emojize(":bell:")} 2 пара \n {emojize(":alarm_clock:")} 9:50-11:25 \n\n'
        f'{emojize(":bell:")} 3 пара \n {emojize(":alarm_clock:")} 11:40 - 13:15 \n\n'
        f'{emojize(":bell:")} 4 пара \n {emojize(":alarm_clock:")} 13:30-15:05 \n\n'
        f'{emojize(":bell:")} 5 пара \n {emojize(":alarm_clock:")} 15:20-16:55 \n\n'
        f'{emojize(":bell:")} 6 пара \n {emojize(":alarm_clock:")} 17:10-18:45 \n\n'
        f'{emojize(":bell:")} 7 пара \n {emojize(":alarm_clock:")} 19:00-20:35')
    await message.answer(text)


@dp.message_handler(text="Налаштування")
async def setup_keyboard(message: Message):
    # функціонал виводу інформації про завтрішній  розклад
    await message.answer('Налаштування ')


# functional to know num of week
@dp.message_handler(text="Номер неділі")
async def num_week(message: Message):
    import datetime
    today = str(datetime.date.today())
    week = list(today.replace('-', ' ').split(' '))
    week_now = datetime.date(int(week[0]), int(week[1]), int(week[2])).isocalendar()[1]
    if week_now % 2 == 0:
        await message.answer('Тиждень №2')
    else:
        await message.answer("Тиждень №1")


@dp.message_handler(text="Про бота")
async def about(message: Message):
    about = (
        (
            f"Бот, який створений, щоб спростити життя"
            f" студентам і не тільки {emojize(':wink:')}"

            f"\n\nБільше не потрібно використовувати застарілий і незрозумілий сайт, "
            f"щоб дізнатись, чи є завтра пари, доки можна поспати, а, можливо,"
            f" й прогуляти {emojize(':see_no_evil:')}"

            f"\n\nЩось не працює, "
            f"або знаєш як покращити мене?{emojize(':sunglasses:')}"
            f"\nНе соромся, пиши мені [ @falex03 ]."

        )
    )
    await message.answer(text=about, reply_markup=keyboard_about)
