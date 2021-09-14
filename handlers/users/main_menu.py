from aiogram.dispatcher.filters.builtin import Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import main_menu
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from states.botStates import StatesOfBot
from keyboards.default import main_menu