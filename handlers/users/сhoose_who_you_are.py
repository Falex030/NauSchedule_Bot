import aiofile as aiofile
from aiogram import types
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import Text
from aiogram.utils.emoji import emojize
from keyboards.default import main_menu
from keyboards.default import who_are_you, choose_department,choose_sub_group
from loader import dp
from states.botStates import StatesOfBot


@dp.message_handler(text='Викладач',state='*')
async def search_teacher(message: types.Message,state: FSMContext):
    await message.answer(f'Поки що ця фунція не працює\n'
                         f'Але ми працюємо над тим, щоб підтримувалися всі категорії {emojize(":wink:")}',
                         reply_markup=who_are_you)


@dp.message_handler(text='Студент',state='*')
async def search_department(message: types.Message,state: FSMContext):
    student_welcome = (
        f"Студент{emojize(':sunglasses:')}"
        "\n\nВибери свій департамент."
    )
    await message.answer(student_welcome, reply_markup=choose_department)



#Призначаю департамент
@dp.message_handler(Text(equals=['ФККПІ',"ФЕБА","ФАБД","ФАЕТ","ФЛСК","ФМВ","ЮФ","АКФ","ФЕБІТ","ФТМЛ"]),state='*')
async def search_group(message:types.Message):
    await message.answer("Введи номер своєї групи",reply_markup = ReplyKeyboardRemove())
    await StatesOfBot.who_you_are_state.set()



# Призначаю номер групи
@dp.message_handler(regexp='^[0-9][0-9][0-9]$',state='*')
async def search_subgroup(message: types.Message):
    await message.answer("Вибери підгрупу",reply_markup=choose_sub_group)








