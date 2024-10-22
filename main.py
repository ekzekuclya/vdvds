import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

import asyncio
import logging


async def main():
    from aiogram.enums.parse_mode import ParseMode
    from aiogram.fsm.storage.memory import MemoryStorage
    from aiogram import Bot, Dispatcher
    from tg.handlers import router
    # bot = Bot(token="8091789023:AAHDvYm08g8kAbauGN5eATubQuNwImg88xg")
    # bot = Bot(token="7247759023:AAER3nI6wzzD_ijJ9qY3WAWogPm_62vGcd8")
    bot = Bot(token="7552096251:AAFZM_RU7Bnqd41fsE2UAq7l_-7wriLJYmI")
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(router)
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
