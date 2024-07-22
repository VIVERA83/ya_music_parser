import traceback
from core.logger import setup_logging
from parser.parser import YandexMusicParser


def run_parser():
    """Подготовка и запуск приложения"""
    logger = setup_logging()
    clicker = YandexMusicParser(logger)
    try:
        clicker.start()
    except Exception as ex:
        logger.error(f"{ex}\n{traceback.format_exc()}")
    finally:
        clicker.stop()

