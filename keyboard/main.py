from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def user_game_keyboard(stats: dict, agreement: list) -> InlineKeyboardMarkup:
    """(example) stats = {"Иностранные отношения":100, "Поддержка правительства":200,
    "Экономика":150, "Стабильность":50},
    agreement = ["Согласиться", "Отказаться"]"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🌍", callback_data="None"),
                InlineKeyboardButton(text="👍", callback_data="None"),
                InlineKeyboardButton(text="💰", callback_data="None"),
                InlineKeyboardButton(text="🏛️", callback_data="None"),
            ],
            [
                InlineKeyboardButton(
                    text=str(stats.get("Иностранные отношения")), callback_data="None"
                ),
                InlineKeyboardButton(
                    text=str(stats.get("Поддержка правительства")), callback_data="None"
                ),
                InlineKeyboardButton(text=str(stats.get("Экономика")), callback_data="None"),
                InlineKeyboardButton(
                    text=str(stats.get("Стабильность")), callback_data="None"
                ),
            ],
            [
                InlineKeyboardButton(text=agreement[0], callback_data="Yes"),
                InlineKeyboardButton(text=agreement[1], callback_data="No"),
            ]
        ]
    )
