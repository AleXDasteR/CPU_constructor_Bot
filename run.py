import asyncio
import logging

from aiogram import Bot, Dispatcher
from apps.handlers import router
from token import token


bot = Bot(token)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('End of the script')
