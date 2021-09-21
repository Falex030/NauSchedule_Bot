from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import Text
from aiogram.utils.emoji import emojize
from keyboards.default import main_menu
from keyboards.default import who_are_you, choose_department,choose_sub_group
from loader import dp
from states.botStates import StatesOfBot


@dp.message_handler(text='Викладач',state=StatesOfBot.start_state)
async def search_teacher(message: types.Message,state: FSMContext):
    await message.answer(f'Поки що ця фунція не працює\n'
                         f'Але ми працюємо над тим, щоб підтримувалися всі категорії {emojize(":wink:")}',
                         reply_markup=who_are_you)


@dp.message_handler(text='Студент',state=StatesOfBot.start_state)
async def search_department(message: types.Message,state: FSMContext):
    student_welcome = (
        f"Студент{emojize(':sunglasses:')}"
        "\n\nВибери свій департамент."
    )
    person = message.text
    await state.update_data(who_you = person)
    await message.answer(student_welcome, reply_markup=choose_department)
    await StatesOfBot.search_department.set()



#Призначаю департамент
@dp.message_handler(Text(equals=['ФККПІ',"ФЕБА","ФАБД","ФАЕТ","ФЛСК","ФМВ","ЮФ","АКФ","ФЕБІТ","ФТМЛ"]),state=StatesOfBot.search_department)
async def search_group(message:types.Message,state: FSMContext):
    await state.update_data(department = message.text)
    await message.answer("Введи номер своєї групи",reply_markup = ReplyKeyboardRemove())
    await StatesOfBot.search_groups_state.set()



# Призначаю номер групи
@dp.message_handler(regexp='^[0-9][0-9][0-9]$',state=StatesOfBot.search_groups_state)
async def search_subgroup(message: types.Message,state: FSMContext):
    await state.update_data(group = message.text)
    await message.answer("Вибери підгрупу",reply_markup=choose_sub_group)
    await StatesOfBot.next()

# Пошук підгрупи

@dp.message_handler(Text(equals=['Перша підгрупа','Друга підгрупа']),state=StatesOfBot.search_subgroup)
async def get_data(message: types.Message,state: FSMContext):
    await state.update_data(subgroup = message.text)
    data = await state.get_data()
    person = data.get('person')
    department = data.get('department')
    group = data.get('group')
    subgroup = data.get('subgroup')
    data_file = []
    try:
        with open(f'schedule/{department}/{group}/{subgroup}.json','r',encoding='utf-8') as read_file:
            for line in read_file:
                data_file.append(line.strip())
        await message.answer(f"Група {department}-{group} успішно знайдена!",reply_markup=main_menu)
        await StatesOfBot.search_subgroup.set()
        await state.finish()
    except FileNotFoundError as ex:
        await message.answer(f"Група {department}-{group} не знайдена \n Спробуйде ще раз")
        await StatesOfBot.who_you_are_state.set()








