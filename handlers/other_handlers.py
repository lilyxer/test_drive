from aiogram import Router
from aiogram.types import Message


router = Router()

@router.message()
async def send_answer(msg: Message):
    await msg.answer(text='Я не знаю таких команд, пожалуйста нажми\n/start - запусти меня и пользуйся клавиатурой')

# @router.message()
# async def send_echo(msg: Message):
#     try:
#         await msg.send_copy(chat_id=msg.chat.id)
#     except TypeError:
#         await msg.reply(text=lexicon_ru['no_echo'])
