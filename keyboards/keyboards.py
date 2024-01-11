from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import cars


class BotKeyBoard:
    def __init__(self, *keys: tuple) -> None:
        self._buttons = [KeyboardButton(text=x) for x in keys]
        self._entres = KeyboardButton(text='🚗 Другой автомобиль')

    def __call__(self, width: int=2, time: bool=False) -> ReplyKeyboardMarkup:
        board = ReplyKeyboardBuilder()
        board.row(*self._buttons, width=width)
        board.row(self._entres)
        return board.as_markup(one_time_keyboard=time, resize_keyboard=True)


brand_boards = BotKeyBoard(*cars)(time=True)
models_chery_boards = BotKeyBoard(*cars['Chery'])(time=False)
models_omoda_boards = BotKeyBoard(*cars['Omoda'])(time=False)
models_getour_boards = BotKeyBoard(*cars['Getour'])(time=False)

# print(brand_boards)