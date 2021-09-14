from aiogram import types
from aiogram.utils.emoji import emojize
from states.botStates import StatesOfBot
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Text
from loader import dp,bot

from keyboards.default import who_are_you,main_menu
from loader import dp


@dp.message_handler(text='Викладач')
async def search_teacher(message: types.Message):
    await message.answer(f'Поки що ця фунція не працює\n'
                         f'Але ми працюємо над тим, щоб підтримувалися всі категорії {emojize(":wink:")}',
                         reply_markup=who_are_you)

@dp.message_handler(text= 'Студент')
async def search_group(message: types.Message):
    student_welcome = (
        f"Студент{emojize(':sunglasses:')}"
        "\n\nНапиши мені шифр твоєї групи (або ж його частину)."
    )
    await message.answer(student_welcome)





