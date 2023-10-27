from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboard.start import user_game_keyboard
from templates.setup import render_template

router = Router(name="start-router")


@router.message(Command(commands=["start"]))
async def cmd_start(message: Message) -> None:
    await message.answer(
        text=render_template(template_name="start.j2", data={"state": 1}),
        reply_markup=user_game_keyboard(),
    )
