from aiogram import F, types
import random
from aiogram import Router
from keyboard.main import user_game_keyboard
from templates.setup import render_template

router_next = Router(name="game1_message_router")


@router_next.callback_query(F.data == "1game_message")
async def send_first_message(callback: types.CallbackQuery, **attributes):
    await callback.message.edit_text(
        text=render_template(template_name="gamemessages.j2", data={"state": random.randint(1, 4)}),
        reply_markup=user_game_keyboard(attributes.get("stats"), ["Согласиться", "Отказаться"])
    )