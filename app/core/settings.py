"""Все настройки приложения."""

import os

from core.types import LOG_LEVEL

from pydantic_settings import BaseSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))


class Base(BaseSettings):
    class Config:
        """Настройки для чтения переменных среды из файла."""

        env_nested_delimiter = "__"
        env_file = os.path.join(BASE_DIR, ".env")
        enf_file_encoding = "utf-8"
        extra = "ignore"


class LogSettings(Base):
    """Setting logging.

    level (str, optional): уровень логирования. По умолчанию "INFO".
    guru (bool, optional): Следует ли включать режим 'гуру'. По умолчанию установлено значение True.
    traceback (bool, optional): Следует ли включать данные отслеживания в журналы.
    По умолчанию установлено значение True.
    """

    level: LOG_LEVEL = "INFO"
    guru: bool = True
    traceback: bool = True
