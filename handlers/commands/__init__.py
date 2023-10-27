from aiogram import Router

from .start import router as start_router

router = Router(name="user-commands-router")

router.include_routers(start_router)
