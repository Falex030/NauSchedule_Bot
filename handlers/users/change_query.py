import asyncpg
from aiogram import types
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound
from  loader import dp
from states.botStates import StatesOfBot
from keyboards.default.who_are_you import who_are_you

@dp.message_handler(text='/change_query',state='*')
async def cmd_change_query(message: types.Message):
    """
    Change query type
    """
    await message.answer(
        text="Вибери для кого шукати розклад цього разу",
        reply_markup= who_are_you,
        parse_mode='HTML'
    )
    await StatesOfBot.search_department.set()
    try:
        await message.delete()
    except (MessageCantBeDeleted, MessageToDeleteNotFound):
        pass