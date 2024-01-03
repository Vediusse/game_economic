from aiogram.filters.callback_data import CallbackData


class MyCallback(CallbackData, prefix="my"):
    message: int
    agreement: str
    foreign: int
    domestic: int
    money: int
    freedom: int
    year: int


class ConsequencesCallbackFactory(CallbackData, prefix="my"):
    foreign: int
    domestic: int
    money: int
    freedom: int
    year: int
