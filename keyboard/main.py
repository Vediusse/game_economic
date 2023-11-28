from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboard.callback_factory import MyCallback, ConsequencesCallbackFactory


def user_game_keyboard(
    stats: dict, agreement: list, message: int
) -> InlineKeyboardMarkup:
    """(example) stats = {"foreign":100, "domestic":200,
    "money":150, "freedom":50},
    agreement = ["Согласиться", "Отказаться"]"""
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text="💰", callback_data="None"),
    )
    builder.row(
        InlineKeyboardButton(text=str(stats.get("money")), callback_data="None"),
    )

    builder.row(
        InlineKeyboardButton(text="🌍", callback_data="None"),
        InlineKeyboardButton(text="👍", callback_data="None"),
        InlineKeyboardButton(text="🪽", callback_data="None"),
    )
    builder.row(
        InlineKeyboardButton(
            text=str(stats.get("foreign")), callback_data="None"
        ),
        InlineKeyboardButton(
            text=str(stats.get("domestic")), callback_data="None"
        ),
        InlineKeyboardButton(
            text=str(stats.get("freedom")), callback_data="None"
        ),
    )

    builder.row(
        InlineKeyboardButton(
            text=agreement[0],
            callback_data=MyCallback(
                message=message,
                agreement="Yes",
                foreign=str(stats.get("foreign")),
                domestic=str(stats.get("domestic")),
                money=str(stats.get("money")),
                freedom=str(stats.get("freedom")),
            ).pack(),
        ),
        InlineKeyboardButton(
            text=agreement[1],
            callback_data=MyCallback(
                message=message,
                agreement="No",
                foreign=str(stats.get("foreign")),
                domestic=str(stats.get("domestic")),
                money=str(stats.get("money")),
                freedom=str(stats.get("freedom")),
            ).pack(),
        ),
    )

    return builder.as_markup()




def get_consequences(
    stats: dict, agreement: list, message: int
) -> InlineKeyboardMarkup:
    """(example) stats = {"foreign":100, "domestic":200,
    "money":150, "freedom":50},
    agreement = ["Согласиться", "Отказаться"]"""
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text="💰", callback_data="None"),
    )

    builder.row(
        InlineKeyboardButton(text=str(stats.get("money")), callback_data="None"),
    )

    builder.row(
        InlineKeyboardButton(text="🌍", callback_data="None"),
        InlineKeyboardButton(text="👍", callback_data="None"),
        InlineKeyboardButton(text="🪽", callback_data="None"),
    )
    builder.row(
        InlineKeyboardButton(
            text=str(stats.get("foreign")), callback_data="None"
        ),
        InlineKeyboardButton(
            text=str(stats.get("domestic")), callback_data="None"
        ),
        InlineKeyboardButton(
            text=str(stats.get("freedom")), callback_data="None"
        ),
    )

    builder.row(
        InlineKeyboardButton(
            text=agreement[0],
            callback_data=ConsequencesCallbackFactory(
                foreign=str(stats.get("foreign")),
                domestic=str(stats.get("domestic")),
                money=str(stats.get("money")),
                freedom=str(stats.get("freedom")),
            ).pack(),
        )
    )

    return builder.as_markup()
