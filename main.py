import asyncio
from config import bot, dispatcher
from aiogram.filters.command import Command
from data_base.database import new_user, get_user_by_id
from aiogram.types.web_app_info import WebAppInfo


@dispatcher.message(Command("start"))
async def cmd_start(message):
    current_user = get_user_by_id(message.chat.id)
    if not current_user:
        await message.answer("What is your name?")
    else:
        await message.answer(f"Hello, duude!",
                             web_app=WebAppInfo(url="https://market.yandex.ru/?clid=2288477"))


@dispatcher.message(Command("reg"))
async def default_message_handler(message):
    await message.answer("Here is registration")
    new_user(message.chat.id, message.text)
    await message.answer("Done")


async def main():
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
