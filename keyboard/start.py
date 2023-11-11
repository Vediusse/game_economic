from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def user_game_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Далее", callback_data=f"start_button "),
            ]
        ]
    )
