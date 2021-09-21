from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

settings = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Змінити запит"),
            KeyboardButton(text="Допомога")
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)


