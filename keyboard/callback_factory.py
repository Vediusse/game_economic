from aiogram.filters.callback_data import CallbackData
from typing import Optional


class MyCallback(CallbackData, prefix="my"):
    message: int
    agreement: str
    foreign: int
    domestic: int
    money: int
    freedom: int


class ConsequencesCallbackFactory(CallbackData, prefix="my"):
    foreign: int
    domestic: int
    money: int
    freedom: int