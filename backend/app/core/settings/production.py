import os

import openai
from dotenv import load_dotenv

from app.core.settings.app import AppSettings


class ProdAppSettings(AppSettings):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    class Config(AppSettings.Config):
        env_file = "prod.env"
        load_dotenv(dotenv_path=env_file, override=True)
