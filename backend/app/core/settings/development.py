import logging
import os

import openai
from dotenv import load_dotenv

from app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    debug: bool = True

    title: str = "Dev FastAPI example application"

    logging_level: int = logging.DEBUG

    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    class Config(AppSettings.Config):
        env_file = ".env"
        load_dotenv(dotenv_path=env_file, override=True)
