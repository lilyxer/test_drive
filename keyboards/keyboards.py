from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from lexicon.lexicon import lexicon_ru


class BotKeyBoard:
    def __init__(self, *keys: tuple) -> None:
        self._buttons = [InlineKeyboardButton(text=x, callback_data=x) for x in keys]

    def __call__(self, width: int=3, menu: bool=True) -> InlineKeyboardMarkup:
        board = InlineKeyboardBuilder()
        board.row(*self._buttons, width=width)
        if menu:
            board.row(InlineKeyboardButton(text='Меню', callback_data='/menu'))
        return board.as_markup()


class BotKeyBoardHelp:
    def __call__(self) -> ReplyKeyboardMarkup:
        board = ReplyKeyboardBuilder()
        board.row(KeyboardButton(text='/menu'))
        return board.as_markup(one_time_keyboard=True, resize_keyboard=True)