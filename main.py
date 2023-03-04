import defined_messages
from aiogram import Bot, Dispatcher, executor, types as aiogram_types
import os
from quoter import Quoter

bot = Bot(token=os.environ['API_TOKEN'])
dp = Dispatcher(bot)
quote = Quoter()


@dp.message_handler(commands=['start'])
async def send_welcome(message: aiogram_types.Message):
    await bot.send_message(message.chat.id, defined_messages.GREETING)


@dp.message_handler(commands=['get_quote'])
async def send_random_quote(message: aiogram_types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    random_quote = await quote.get_random_quote()
    await bot.send_message(message.chat.id, defined_messages.RANDOM_QUOTE + random_quote["content"])


if __name__ == '__main__':
    while True:
        try:
            executor.start_polling(dp, skip_updates=True)
        except Exception as e:
            print(e)
