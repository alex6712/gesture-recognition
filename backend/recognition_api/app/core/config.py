from functools import lru_cache
from os.path import abspath
from typing import List

from pydantic import EmailStr, field_validator
from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    """Класс конфигурации проекта.

    Использует `pydantic`_ + `python-dotenv`_ для загрузки настроек приложения из .env-файла.

    .. _`pydantic`:
        https://docs.pydantic.dev/
    .. _`python-dotenv`:
        https://pypi.org/project/python-dotenv/

    See Also
    --------
    pydantic
    python-dotenv

    Attributes
    ----------
    APP_NAME : str
        Название приложения.
    APP_VERSION : str
        Текущая версия приложения.
    APP_DESCRIPTION : str
        Полное описание приложения.
    APP_SUMMARY : str
        Краткое описание приложения.
    ADMIN_NAME : str
        Имя ответственного лица.
    ADMIN_EMAIL : EmailStr
        Email для связи с ответственным лицом.
    BACKEND_CORS_ORIGINS : List[str]
        Список источников для CORS Middleware.
    CURRENT_API_URL : str
        Добавочная строка текущей версии API.
    MODEL_SERVER_DOMAIN : str
        Домен gRPC-сервера модели компьютерного зрения.
    """

    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str
    APP_SUMMARY: str

    ADMIN_NAME: str
    ADMIN_EMAIL: EmailStr

    BACKEND_CORS_ORIGINS: List[str]

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")  # noqa
    @classmethod
    def assemble_cors_origins(cls, value: List[str] | str) -> List[str] | str:
        if isinstance(value, str) and not value.startswith("["):
            return [i.strip() for i in value.split(",")]

        if isinstance(value, (list, str)):
            return value

        raise ValueError(value)

    CURRENT_API_URL: str

    MODEL_SERVER_DOMAIN: str

    model_config = SettingsConfigDict(
        env_file=abspath("../.env"),
        env_file_encoding="utf-8",
        case_sensitive=True,
        enable_decoding=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
