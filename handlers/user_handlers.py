from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from keyboards.keyboards import (brand_boards, models_chery_boards,
                                 models_getour_boards, models_omoda_boards)

from lexicon.lexicon import lexicon_ru, cars


router = Router()

@router.message(F.text == '🚗 Другой автомобиль')
@router.message(CommandStart())
async def process_start_command(msg: Message):
    await msg.answer(text=lexicon_ru['/start'], parse_mode='html',
                     reply_markup=brand_boards)

@router.message(Command(commands='help'))
async def process_help_command(msg: Message):
    await msg.answer(text=lexicon_ru['/help'])

@router.message(F.text.in_({*cars}))
async def process_chery_answer(msg: Message):
    match msg.text:
        case 'Chery':
            await msg.answer(text=lexicon_ru['choice'], reply_markup=models_chery_boards)
        case 'Getour':
            await msg.answer(text=lexicon_ru['choice'], reply_markup=models_getour_boards)
        case 'Omoda':
            await msg.answer(text=lexicon_ru['choice'], reply_markup=models_omoda_boards)
        case _ :
            await msg.answer(text='в разработке')

@router.message(F.text.in_({key for _, elem in cars.items() for key in elem}))
async def process_chery_answer(msg: Message):
    model = msg.text
    for key, value in cars.items():
        if model in value:
            await msg.answer(text=cars[key][model])

# @router.message(F.text == 'Haval')
# async def process_chery_answer(msg: Message):
#     await msg.answer(text=lexicon_ru['Chery'], reply_markup=models_chery_boards)
