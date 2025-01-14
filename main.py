import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router


async def main():
    bot = Bot(token='7740369738:AAF8T6rAlItSurtIQN4I9oCHrs-A8yOIW9A')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print('Бот запущен!!!')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
