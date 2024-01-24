#!python3

import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config

from handlers import other_handlers,user_handlers


logger = logging.getLogger(name = __name__)

async def main() -> None:
    logging.basicConfig(
        level=logging.WARNING,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.warning('Starting bot')

    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # await bot.delete_webhook(drop_pending_updates=True)
    # await dp.start_polling(bot)


    await bot.delete_webhook(drop_pending_updates=True)
    wb_info = await bot.get_webhook_info()

    if wb_info.allowed_updates:
        await dp.start_polling(bot, allowed_updates=[])

    else:
        await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())