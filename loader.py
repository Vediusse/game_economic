from typing import Tuple

from aiogram import Bot, Dispatcher

from config import Config
from handlers import commands_router, callbacks_router
from middleware import DbSessionMiddleware


async def init_bot() -> Tuple[Bot, Dispatcher]:
    bot = Bot(Config.bot_token)
    dp = Dispatcher()
    dp.include_routers(commands_router, callbacks_router)

    stats = {
        "foreign": 20,
        "domestic": 20,
        "freedom": 20,
        "money": 20,
    }
    dp.update.middleware(DbSessionMiddleware(stats=stats))
    return bot, dp
