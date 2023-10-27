from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def user_game_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✝️", callback_data=f"charity_btns "),
                InlineKeyboardButton(text="💰", callback_data=f"charity_btns "),
                InlineKeyboardButton(text="🤷", callback_data=f"charity_btns"),
                InlineKeyboardButton(text="⚔️", callback_data=f"charity_btns "),
            ],
            [
                InlineKeyboardButton(text="500", callback_data=f"charity_btns"),
                InlineKeyboardButton(text="647", callback_data=f"charity_btns"),
                InlineKeyboardButton(text="298", callback_data=f"charity_btns"),
                InlineKeyboardButton(text="120", callback_data=f"charity_btns"),
            ],
            [
                InlineKeyboardButton(text="Согласиться", callback_data=f"charity_btns"),
                InlineKeyboardButton(text="Отказаться", callback_data=f"charity_btns"),
            ],
        ]
    )
