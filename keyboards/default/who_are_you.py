from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

who_are_you = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Студент")
        ],
        [
            KeyboardButton(text="Викладач")
        ]
    ],
    resize_keyboard=True
)


