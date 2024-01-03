from aiogram import Router

from .next_button import router_next as game_message_router

router_keyboard = Router(name="user_keyboard_router")

router_keyboard.include_routers(game_message_router)
