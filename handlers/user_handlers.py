import os

from aiogram import Router, F, types
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message
from keyboards.keyboards import BotKeyBoard, BotKeyBoardHelp
from lexicon.lexicon import lexicon_ru, buttons, cars
from lexicon.classes import ModelD
router = Router()


@router.message(CommandStart())
async def process_start_command(msg: Message):
    help_kb = BotKeyBoardHelp()()
    await msg.answer(text=lexicon_ru['/start'], reply_markup=help_kb)

@router.message(Command(commands='help'))
async def process_help_command(msg: Message):
    help_kb = BotKeyBoardHelp()()
    await msg.answer(text=lexicon_ru['/help'], reply_markup=help_kb)

@router.message(Command(commands='menu'))
async def process_menu_command(msg: Message):
    board = BotKeyBoard(*buttons['/menu'])(menu=False)
    await msg.answer(text=lexicon_ru['/menu'], reply_markup=board)

@router.callback_query(F.data == '/menu')
async def process_main_callback(clbk: CallbackQuery):
    board = BotKeyBoard(*buttons['/menu'])(menu=False)
    await clbk.message.edit_text(text=lexicon_ru['/menu'], reply_markup=board)
    await clbk.answer()

@router.callback_query(F.data == 'Автомобили')
async def process_car_callback(clbk: CallbackQuery):
    # board = BotKeyBoard(*sorted(cars))()
    board = BotKeyBoard(*sorted({x.brand for x in cars}))()
    await clbk.message.edit_text(text=lexicon_ru['Автомобили'], reply_markup=board)
    await clbk.answer()

@router.callback_query(F.data == 'Маршрут')
async def process_map_callback(clbk: CallbackQuery):
    board = BotKeyBoard(*buttons['Маршрут'])()
    await clbk.message.edit_text(text=lexicon_ru['Маршрут'], reply_markup=board)
    await clbk.answer()

# @router.callback_query(F.data.in_({*cars}))
@router.callback_query(F.data.in_({x.brand for x in cars}))
async def process_brand_callback(clbk: CallbackQuery):
    brand = clbk.data
    # board = BotKeyBoard(*cars[brand])()
    board = BotKeyBoard(*[x.model for x in cars if x.brand == brand])()
    await clbk.message.edit_text(text=lexicon_ru[brand], reply_markup=board)# , parse_mode='MarkdownV2')
    await clbk.answer()

# @router.callback_query(F.data.in_({key for _, elem in cars.items() for key in elem}))
@router.callback_query(F.data.in_({x.model for x in cars}))
async def process_model_callback(clbk: CallbackQuery):
    # _model = clbk.data
    _models = (x for x in cars if x.model == clbk.data)
    _model = next(_models)
    # brand = ''.join(brand for brand, models in cars.items() for m in models if m == model)
    # board = BotKeyBoard(*cars[brand])()
    board = BotKeyBoard(*[x.model for x in cars if x.brand == _model.brand])()
    await clbk.message.delete_reply_markup()
    # await clbk.message.answer(text=cars[brand][model], reply_markup=board)
    await clbk.message.answer(text=str(_model), reply_markup=board)
    if f'{_model.model}.pdf' in os.listdir('specification'):
        await clbk.message.answer_document(types.FSInputFile(path=os.path.join('specification', f'{_model.model}.pdf')),
                                           caption='держи спецификацию')
