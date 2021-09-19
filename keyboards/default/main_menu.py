from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="На сьогодні"),
            KeyboardButton(text="На завтра")
        ],
        [
            KeyboardButton(text="Розклад"),
            KeyboardButton(text="Розклад дзвінків")
        ],
        [
            KeyboardButton(text="Придумати навіщо ця кнопка"),
            KeyboardButton(text= "Номер неділі")
        ],
        [
            KeyboardButton(text='Налаштування'),
            KeyboardButton(text='Про бота')
        ]
    ],
    resize_keyboard=True
)