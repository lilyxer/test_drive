from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from lexicon.lexicon import lexicon_ru


router = Router()

@router.message(CommandStart())
async def process_start_command(msg: Message):
    await msg.answer(text=lexicon_ru['/start'], parse_mode='html')


@router.message(Command(commands='help'))
async def process_help_command(msg: Message):
    await msg.answer(text=lexicon_ru['/help'])