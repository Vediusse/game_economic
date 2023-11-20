from typing import Tuple

from aiogram import Bot, Dispatcher


from config import Config

from handlers import commands_router
from middleware import DbSessionMiddleware


async def init_bot() -> Tuple[Bot, Dispatcher]:
    bot = Bot(Config.bot_token)
    dp = Dispatcher()
    dp.include_routers(
        commands_router,
    )

    stats = {"Иностранные отношения": 0, "Поддержка правительства": 0, "Экономика": 0, "Стабильность": 0}
    dp.update.middleware(DbSessionMiddleware(stats))
    return bot, dp
