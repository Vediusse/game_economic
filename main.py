import asyncio
import logging

from loader import init_bot
from logs import setup_logger

logger = logging.getLogger(__name__)


async def main():
    bot, dp = await init_bot()
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    setup_logger()
    try:
        asyncio.run(main())
    except Exception:
        import traceback

        logger.warning(traceback.format_exc())
