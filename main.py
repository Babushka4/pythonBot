import asyncio
from config import bot, dispatcher
from aiogram.filters.command import Command


@dispatcher.message(Command("start"))
async def cmd_start(message):
    await message.answer("Hello!")


async def main():
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
