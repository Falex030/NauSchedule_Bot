from aiogram.types import Message
from handlers.users.about_bot import bot_about
from keyboards.default.settings_key import settings
from loader import dp
from keyboards.default.about_bot_key import keyboard_about




@dp.message_handler(text='Налаштування')
async def settings_menu(message: Message):
    text = (
        'Розклад')
    await message.answer(text,reply_markup=settings)
