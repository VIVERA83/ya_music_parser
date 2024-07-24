import traceback
from core.logger import setup_logging
from core.utils import save_data_to_csv
from parser.parser import YandexMusicParser


def run_parser():
    """Подготовка и запуск приложения"""
    logger = setup_logging()
    clicker = YandexMusicParser(logger)
    try:
        data = clicker.start(input("Введите ариста, важно не полное имя (пример Киркоров): "))
        save_data_to_csv(data, f"{data["name"]}.csv")
    except Exception as ex:
        logger.error(f"{ex}\n{traceback.format_exc()}")
    finally:
        clicker.stop()
