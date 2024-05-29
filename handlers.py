import random
from aiogram import types
from aiogram.dispatcher import Dispatcher


user_data = {}


async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот для игры 'Угадай число'. Введите /game, чтобы начать игру.")


async def start_game(message: types.Message):
    user_id = message.from_user.id
    number_to_guess = random.randint(1, 100)
    user_data[user_id] = number_to_guess
    await message.reply("Игра началась! Я загадал число от 1 до 100. Попробуйте угадать его!")


async def guess_number(message: types.Message):
    user_id = message.from_user.id

    if user_id not in user_data:
        await message.reply("Введите /game, чтобы начать новую игру.")
        return

    try:
        guess = int(message.text)
    except ValueError:
        await message.reply("Пожалуйста, введите целое число.")
        return

    number_to_guess = user_data[user_id]

    if guess < number_to_guess:
        await message.reply("Загаданное число больше. Попробуйте еще раз.")
    elif guess > number_to_guess:
        await message.reply("Загаданное число меньше. Попробуйте еще раз.")
    else:
        await message.reply(f"Поздравляю! Вы угадали число {number_to_guess}.")
        del user_data[user_id]

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start', 'help'])
    dp.register_message_handler(start_game, commands=['game'])
    dp.register_message_handler(guess_number)