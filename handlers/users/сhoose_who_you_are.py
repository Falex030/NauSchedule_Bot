import aiofile as aiofile
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
import re
from aiogram.utils.emoji import emojize

from keyboards.default import who_are_you, choose_department,choose_sub_group
from loader import dp
from states.botStates import StatesOfBot


@dp.message_handler(text='Викладач')
async def search_teacher(message: types.Message):
    await message.answer(f'Поки що ця фунція не працює\n'
                         f'Але ми працюємо над тим, щоб підтримувалися всі категорії {emojize(":wink:")}',
                         reply_markup=who_are_you)


@dp.message_handler(text='Студент')
async def search_department(message: types.Message):
    student_welcome = (
        f"Студент{emojize(':sunglasses:')}"
        "\n\nВибери свій департамент."
    )
    await message.answer(student_welcome, reply_markup=choose_department)

#Призначаю департамент
@dp.message_handler(text='ФККПІ')
async def input_group(message:types.Message):
    await message.answer("Введи номер своєї групи",reply_markup = ReplyKeyboardRemove())

# Призначаю номер групи
@dp.message_handler()
async def search_group(message: types.Message):
    num_group = message.text
    await message.answer("Вибери підгрупу",reply_markup=choose_sub_group)




