import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from dotenv import load_dotenv

from routes import main_router

load_dotenv()

API_TOKEN = os.getenv('BOT_TOKEN')
proxy_url = os.getenv('PROXY_URL')


async def main():
    logging.basicConfig(level=logging.INFO)


    session = AiohttpSession(proxy=proxy_url)

    bot = Bot(token=API_TOKEN, session=session)
    dp = Dispatcher()

    dp.include_router(main_router)

    print("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())