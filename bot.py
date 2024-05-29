import logging
from aiogram import Bot, Dispatcher, executor
from handlers import register_handlers

API_TOKEN = 'token'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)