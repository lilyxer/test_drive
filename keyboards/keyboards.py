from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import cars


class BotKeyBoard:
    def __init__(self, *keys: tuple) -> None:
        self._buttons = [KeyboardButton(text=x) for x in keys]
        self._entres = [KeyboardButton(text='🚗 Другой автомобиль'),
                        KeyboardButton(text='⏎ Меню')]

    def __call__(self, width: int=3, time: bool=False) -> ReplyKeyboardMarkup:
        board = ReplyKeyboardBuilder()
        board.row(*self._buttons, width=width)
        board.row(*self._entres)
        return board.as_markup(one_time_keyboard=time, resize_keyboard=True)

main_menu_board = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Автомобили'),
                        KeyboardButton(text='🗺 Маршрут')]], one_time_keyboard=True,
                        resize_keyboard=True)

brand_boards = BotKeyBoard(*cars)(time=True)
models_chery_boards = BotKeyBoard(*cars['Chery'])(time=False)
models_omoda_boards = BotKeyBoard(*cars['Omoda'])(time=False)
models_jetour_boards = BotKeyBoard(*cars['Jetour'])(time=False)
models_jaecoo_boards = BotKeyBoard(*cars['Jaecoo'])(time=False)
models_haval_boards = BotKeyBoard(*cars['Haval'])(time=False)
models_changan_boards = BotKeyBoard(*cars['Changan'])(time=False)
models_jeely_boards = BotKeyBoard(*cars['Geely'])(time=False)
models_jac_boards = BotKeyBoard(*cars['Москвич'])(time=False)
models_evloute_boards = BotKeyBoard(*cars['Evolute'])(time=False)

# print(brand_boards)