from aiogram.types import Message

from keyboards.default.settings_key import settings
from loader import dp
from utils.misc import rate_limit



@dp.message_handler(text='Налаштування')
async def settings_menu(message: Message):
    text = (
        'Обирай')
    await message.answer(text,reply_markup=settings)

@dp.message_handler(text='Змінити запит')
async def change_query(message: Message):
    await message.answer(text='/change_query')

@dp.message_handler(text='Допомога')
async def help(message: Message):
    text = ("Список команд: ",
            "/start - Для початку спілкування з ботом",
            "/help - Допомога по командам бота",
            '/about - Інформація про бота',
            '/change_query - Змінити запит')
    await message.answer(text=text,reply_markup=settings)

@dp.message_handler()
async def empty(message: Message):
    await message.answer(text='Нічого не вдалось знайти, спробуй ще раз')