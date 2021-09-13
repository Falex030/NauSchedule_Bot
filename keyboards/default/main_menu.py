from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сегодня"),
            KeyboardButton(text="Завтра")
        ],
        [
            KeyboardButton(text="Розклад"),
            KeyboardButton(text="Розклад дзвінків")
        ],
        [
            KeyboardButton(text="Настройки"),
            KeyboardButton(text= "Номер неділі")
        ],
        [
            KeyboardButton(text='Налаштування'),
            KeyboardButton(text='Про бота')
        ]
    ],
    resize_keyboard=True
)