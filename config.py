import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    bot_token = os.getenv("BOT_TOKEN", "6937361230:AAHRXNR3ye7fDm7hgsyWP_zh8Z3-ule619g")
