from pydantic_settings import BaseSettings, SettingsConfigDict

from api.v1 import todo


class Settings(BaseSettings):
    app_name: str = "Todo API"
    debug: bool = False

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()