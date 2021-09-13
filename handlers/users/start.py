import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Text

from keyboards.default import who_are_you
from loader import dp
from utils.db_api import quick_commands as commands
from aiogram.dispatcher import FSMContext
from states.botStates import StatesOfBot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # try:
    #     await commands.add_user(id=message.from_user.id,name=name)
    # except asyncpg.exceptions.UniqueViolationError:
    #     pass

    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         "Ким ти явлаєшся?",
                         reply_markup= who_are_you)
    # await StatesOfBot.start_state.set()
