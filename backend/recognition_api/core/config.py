from functools import lru_cache
from os.path import abspath
from typing import List

from pydantic import EmailStr, IPvAnyAddress, field_validator
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
    DEV_MODE : bool
        Режим разработки.
    INITIALIZE_DB : bool
        Пересоздание базы данных.
    BACKEND_CORS_ORIGINS : List[str]
        Список источников для CORS Middleware.
    DOMAIN : str | IPvAnyAddress
        IP домена, на котором расположено приложение.
    BACKEND_PORT : int
        Порт приложения.
    """

    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str
    APP_SUMMARY: str

    ADMIN_NAME: str
    ADMIN_EMAIL: EmailStr

    DEV_MODE: bool

    INITIALIZE_DB: bool

    BACKEND_CORS_ORIGINS: List[str]

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")  # noqa
    @classmethod
    def assemble_cors_origins(cls, value: List[str] | str) -> List[str] | str:
        if isinstance(value, str) and not value.startswith("["):
            return [i.strip() for i in value.split(",")]

        if isinstance(value, (list, str)):
            return value

        raise ValueError(value)

    DOMAIN: str | IPvAnyAddress

    BACKEND_PORT: int

    CURRENT_API_URL: str

    model_config = SettingsConfigDict(
        env_file=abspath(".env"),
        env_file_encoding="utf-8",
        case_sensitive=True,
        enable_decoding=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
