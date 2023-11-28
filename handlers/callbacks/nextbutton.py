from aiogram import F, types
import random
from aiogram import Router

from keyboard.callback_factory import MyCallback, ConsequencesCallbackFactory
from keyboard.main import user_game_keyboard, get_consequences
from templates.setup import render_template

router_next = Router(name="game1_message_router")


@router_next.callback_query(F.data == "1game_message")
async def send_first_message(callback: types.CallbackQuery, **attributes):
    attributes["message_number"] = random.randint(1, 4)

    await callback.message.edit_text(
        text=render_template(
            template_name="gamemessages.j2",
            data={"state": attributes.get("message_number")},
        ),
        reply_markup=user_game_keyboard(
            attributes.get("stats"),
            ["Согласиться", "Отказаться"],
            attributes["message_number"],
        ),
    )


@router_next.callback_query(MyCallback.filter())
async def send_first_message(
        callback: types.CallbackQuery, callback_data: MyCallback, **attributes
):
    consequences = render_template(
        template_name="negativeorpositive.j2",
        data={"state": callback_data.message, "agreement": callback_data.agreement},
    )
    stats = {
        "foreign": callback_data.foreign,
        "domestic": callback_data.domestic,
        "money": callback_data.money,
        "freedom": callback_data.freedom,
    }
    values = [int(x) for x in str(consequences).split(",")]
    for i, key in enumerate(stats):
        stats[key] += values[i]
        if key != "money" and (stats[key] <= 0 or stats[key] >= 100):
            await callback.message.edit_text(
                text=render_template(
                    template_name="lose.j2",
                    data={"reason": key},
                ),
            )
            return
        if key == "money" and (stats[key] <= 0):
            await callback.message.edit_text(
                text=render_template(
                    template_name="lose.j2",
                    data={"reason": key},
                ),
            )
            return
        if key == "money" and (stats[key] >= 100):
            await callback.message.edit_text(
                text=render_template(
                    template_name="win.j2",
                    data={"state": random.randint(1,4)},
                ),
            )
            return

    await callback.message.edit_text(
        text=render_template(
            template_name="consequences.j2",
            data={"state": callback_data.message, "agreement": callback_data.agreement},
        ),
        reply_markup=get_consequences(
            stats,
            ["ЧТООООО?"],
            callback_data.message,
        ),
    )


@router_next.callback_query(ConsequencesCallbackFactory.filter())
async def send_first_message(
        callback: types.CallbackQuery, callback_data: ConsequencesCallbackFactory, **attributes
):
    stats = {
        "foreign": callback_data.foreign,
        "domestic": callback_data.domestic,
        "freedom": callback_data.freedom,
        "money": callback_data.money,
    }
    attributes["message_number"] = random.randint(1, 4)
    await callback.message.edit_text(
        text=render_template(
            template_name="gamemessages.j2",
            data={"state": attributes["message_number"]},
        ),
        reply_markup=user_game_keyboard(
            stats,
            ["Согласиться", "Отказаться"],
            attributes["message_number"],
        ),
    )
