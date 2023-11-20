from aiogram import Router
from .nextbutton import router_next as game1_message_router

router_keyboard = Router(name="user_keyboard_router")

router_keyboard.include_routers(game1_message_router)
