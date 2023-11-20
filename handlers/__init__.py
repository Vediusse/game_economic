from aiogram import Router
from .callbacks import router_keyboard as callbacks_router
from .commands import router as commands_router

router = Router(name="user")

__all__ = ["commands_router", "callbacks_router"]
