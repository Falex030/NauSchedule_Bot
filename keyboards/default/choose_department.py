from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

choose_department = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ФККПІ"),
            KeyboardButton(text="ФЕБА")
        ],
        [
            KeyboardButton(text="ФАБД"),
            KeyboardButton(text="ФАЕТ")
        ],
        [
            KeyboardButton(text="ФЛСК"),
            KeyboardButton(text="ФМВ")
        ],
        [
            KeyboardButton(text="ЮФ"),
            KeyboardButton(text="AКФ")
        ],
        [
            KeyboardButton(text="ФЕБІТ"),
            KeyboardButton(text= "ФТМЛ")
        ]
    ],
    resize_keyboard=True
)

choose_sub_group = ReplyKeyboardMarkup(
    keyboard = [

        [
            KeyboardButton(text=" Перша підгрупа "),

        ],
        [
            KeyboardButton(text=" Друга підгрупа ")
        ]
    ]
)
