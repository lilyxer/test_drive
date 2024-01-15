import os

from aiogram import Router, F, types
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import *

from lexicon.lexicon import lexicon_ru, cars

router = Router()


@router.message(CommandStart())
async def process_start_command(msg: Message):
    try:
        name = msg.from_user.username
    except Exception:
        name = 'у тебя нет имени? :/'
    await msg.answer(text=f'<b>Привет</b>, {name}!', parse_mode='html')
    await msg.answer(text=lexicon_ru['/start'], parse_mode='html',
                     reply_markup=main_menu_board)

@router.message(F.text == '⏎ Меню')
@router.message(Command(commands='menu'))
async def process_menu(msg: Message):
    await msg.answer(text=lexicon_ru['menu'],
                     reply_markup=main_menu_board)

@router.message(F.text == '🗺 Маршрут')
async def process_map(msg: Message):
    await msg.answer(text=lexicon_ru['map'],
                     reply_markup=main_menu_board)

@router.message(F.text.in_({'🚗 Другой автомобиль', 'Автомобили'}))
async def process_other_answer(msg: Message):
    await msg.answer(text=lexicon_ru['choice'], parse_mode='html',
                     reply_markup=brand_boards)

@router.message(Command(commands='help'))
async def process_help_command(msg: Message):
    await msg.answer(text=lexicon_ru['/help'])

@router.message(F.text.in_({*cars}))
async def process_chery_answer(msg: Message):
    match msg.text:
        case 'Chery':
            await msg.answer(text=lexicon_ru['choice'], reply_markup=models_chery_boards)
        case 'Jetour':
            await msg.answer(text=lexicon_ru['choice'], reply_markup=models_jetour_boards)
        case 'Omoda':
            await msg.answer(text=lexicon_ru['choice'], reply_markup=models_omoda_boards)
        case 'Jaecoo':
            await msg.answer(text=lexicon_ru['choice'], reply_markup=models_jaecoo_boards)
        case 'Haval':
            await msg.answer(text=lexicon_ru['choice'], reply_markup=models_haval_boards)
        case 'Changan':
            await msg.answer(text=lexicon_ru['choice'], reply_markup=models_changan_boards)
        case 'Geely':
            await msg.answer(text=lexicon_ru['choice'], reply_markup=models_jeely_boards)
        case 'Москвич':
            await msg.answer(text=lexicon_ru['choice'], reply_markup=models_jac_boards)
        case _ :
            await msg.answer(text='в разработке', reply_markup=brand_boards)

@router.message(F.text.in_({key for _, elem in cars.items() for key in elem}))
async def process_chery_answer(msg: Message):
    model = msg.text
    for key, value in cars.items():
        if model in value:
            await msg.answer(text=cars[key][model])
            await msg.answer_document(types.FSInputFile(path=os.path.join('specification', f'{model}.pdf')),
                                      caption='держи спецификацию'
    )
            # link = f'{model}.pdf'
            # print(os.path.join(os.getcwd(), 'specification', link))
            # if link in os.listdir('specification'):
            #     l = os.path.join(os.getcwd(), 'specification', link)
            #     await msg.answer_document(document='https://storage.yandexcloud.net/s3-moskvich-new/cms/1ee6/67/f93b0bc84e78c15184f59c2f636ec4cb8b0e7814.pdf')
                #(msg.chat.id, os.path.join(os.getcwd(), 'specification', link))
                                            # open(l, 'rb'))
            #     with open(os.path.join(os.getcwd(), 'specification', link), 'rb') as file:
            #         await msg.bot.send_document(msg.chat.id, file)
