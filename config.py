import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    bot_token = os.getenv("BOT_TOKEN", "")
