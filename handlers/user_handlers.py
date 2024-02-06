import os

from aiogram import Router, F, types
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message, ContentType
from keyboards.keyboards import BotKeyBoard, BotKeyBoardHelp
from lexicon.lexicon import lexicon_ru, buttons, cars
from config_data.config import Config, load_config


router = Router()
config: Config = load_config()

@router.message(CommandStart())
async def process_start_command(msg: Message):
    help_kb = BotKeyBoardHelp()()
    await msg.bot.send_message(chat_id=config.admin_id, text=f'{msg.from_user.id}_{msg.from_user.full_name} запустил бота')
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
    board = BotKeyBoard(*sorted({x.brand for x in cars}))()
    await clbk.message.edit_text(text=lexicon_ru['Автомобили'], reply_markup=board)
    await clbk.answer()

@router.callback_query(F.data == 'Маршрут')
async def process_map_callback(clbk: CallbackQuery):
    board = BotKeyBoard(*buttons['Маршрут'])()
    await clbk.message.edit_text(text=lexicon_ru['Маршрут'], reply_markup=board)
    await clbk.answer()

@router.callback_query(F.data.in_({*os.listdir('pres'), 'Презентации'}))
# @router.callback_query(F.data == 'Презентации')
async def process_map_callback(clbk: CallbackQuery):
    board = BotKeyBoard(*os.listdir('pres'))()
    if clbk.data in os.listdir('pres'):
        await clbk.message.delete_reply_markup()
        await clbk.message.answer(text=f'Загружаю {clbk.data[:-4]}... Ещё нужна какая преза?', reply_markup=board)
        await clbk.message.answer_document(types.FSInputFile(path=os.path.join('pres', clbk.data)),
                                           caption=f'держи презентацию по {clbk.data[:-4]}')
    else:
        await clbk.message.edit_text(text=lexicon_ru['Презентации'], reply_markup=board)
    await clbk.answer()

@router.callback_query(F.data.in_({'До обеда', 'После обеда'}))
async def process_get_point(clbk: CallbackQuery):
    btn = 'До обеда' if clbk.data == 'После обеда' else 'После обеда'
    board = BotKeyBoard(btn)()
    await clbk.message.edit_text(text=lexicon_ru[clbk.data], reply_markup=board)
    await clbk.answer()

@router.callback_query(F.data.in_({x.brand for x in cars}))
async def process_brand_callback(clbk: CallbackQuery):
    brand = clbk.data
    board = BotKeyBoard(*[x.model for x in cars if x.brand == brand])()
    await clbk.message.edit_text(text=lexicon_ru[brand], reply_markup=board)
    await clbk.answer()

@router.callback_query(F.data.in_({x.model for x in cars}))
async def process_model_callback(clbk: CallbackQuery):
    _models = (x for x in cars if x.model == clbk.data)
    _model = next(_models)
    board = BotKeyBoard(*[x.model for x in cars if x.brand == _model.brand])()
    await clbk.message.delete_reply_markup()
    await clbk.message.answer(text=str(_model), reply_markup=board)
    if f'{_model.model}.pdf' in os.listdir('specification'):
        await clbk.message.answer_document(types.FSInputFile(path=os.path.join('specification', f'{_model.model}.pdf')),
                                           caption='держи спецификацию')

@router.message(F.document)
async def process_save_doc(msg: Message):
    file = await msg.bot.get_file(msg.document.file_id)
    await msg.answer(text=f'документ {msg.document.file_name} получил')
    await msg.bot.download_file(file.file_path, f'{os.path.join("downloads", msg.document.file_name)}')