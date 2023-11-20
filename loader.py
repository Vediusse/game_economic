from typing import Tuple
from aiogram import Bot, Dispatcher


from config import Config

from handlers import commands_router, callbacks_router


async def init_bot() -> Tuple[Bot, Dispatcher]:
    bot = Bot(Config.bot_token)
    dp = Dispatcher()
    dp.include_routers(
        commands_router,
        callbacks_router
    )
    return bot, dp
