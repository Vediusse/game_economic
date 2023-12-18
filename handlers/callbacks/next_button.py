import random

from aiogram import F, types
from aiogram import Router

from keyboard.callback_factory import MyCallback, ConsequencesCallbackFactory
from keyboard.main import user_game_keyboard, get_consequences
from templates.setup import render_template

router_next = Router(name="game1_message_router")


@router_next.callback_query(F.data == "game_message")
async def send_first_message(callback: types.CallbackQuery, **attributes):
    attributes["message_number"] = random.randint(1, 4)

    await callback.message.edit_text(
        text= ("Текущий год: " + "1929\n") + render_template(
            template_name="game_messages.j2",
            data={"state": attributes.get("message_number")},
        ),
        reply_markup=user_game_keyboard(
            attributes.get("stats"),
            [
                render_template(
                    template_name="answer_button.j2",
                    data={
                        "state": attributes.get("message_number"),
                        "agreement": "Yes",
                    },
                ),
                render_template(
                    template_name="answer_button.j2",
                    data={"state": attributes.get("message_number"), "agreement": "No"},
                ),
            ],
            attributes["message_number"],
        ),
    )


@router_next.callback_query(MyCallback.filter())
async def send_first_message(
    callback: types.CallbackQuery, callback_data: MyCallback, **attributes
):
    consequences = render_template(
        template_name="impact.j2",
        data={"state": callback_data.message, "agreement": callback_data.agreement},
    )
    stats = {
        "foreign": callback_data.foreign,
        "domestic": callback_data.domestic,
        "money": callback_data.money,
        "freedom": callback_data.freedom,
        "year": callback_data.year,
    }
    values = [int(x) for x in str(consequences).split(",")]

    for i, key in enumerate(stats):
        if key == "year":
            stats[key] += 1
            continue
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
                    data={"state": random.randint(1, 4)},
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
            [
                render_template(
                    template_name="answer_button_consequences.j2",
                    data={
                        "state": callback_data.message,
                        "agreement": callback_data.agreement,
                    },
                )
            ],
            callback_data.message,
        ),
    )


@router_next.callback_query(ConsequencesCallbackFactory.filter())
async def send_first_message(
    callback: types.CallbackQuery,
    callback_data: ConsequencesCallbackFactory,
    **attributes
):
    stats = {
        "foreign": callback_data.foreign,
        "domestic": callback_data.domestic,
        "freedom": callback_data.freedom,
        "money": callback_data.money,
        "year": callback_data.year,
    }
    attributes["message_number"] = random.randint(1, 4)
    await callback.message.edit_text(
        text=("Текущий год: " + str(stats.get("year")) + "\n") + render_template(
            template_name="game_messages.j2",
            data={"state": attributes["message_number"]},
        ),
        reply_markup=user_game_keyboard(
            stats,
            [
                render_template(
                    template_name="answer_button.j2",
                    data={
                        "state": attributes.get("message_number"),
                        "agreement": "Yes",
                    },
                ),
                render_template(
                    template_name="answer_button.j2",
                    data={"state": attributes.get("message_number"), "agreement": "No"},
                ),
            ],
            attributes["message_number"],
        ),
    )
