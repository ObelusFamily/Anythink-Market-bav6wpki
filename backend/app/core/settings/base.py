from enum import Enum

from pydantic import BaseSettings

from dotenv import load_dotenv

class AppEnvTypes(Enum):
    prod: str = "prod"
    dev: str = "dev"
    test: str = "test"


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes.prod

    class Config:
        env_file = ".env"
        load_dotenv(dotenv_path=env_file, override=True)
