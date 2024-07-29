import traceback
from core.logger import setup_logging
from core.utils import save_data_to_csv
from parser.parser import YandexMusicParser


def input_search_data() -> dict:
    search_data = {}
    try:
        search_data["genre"] = input("Введите жанр: ")
        search_data["listeners_from"] = int(
            input("Количеству прослушиваний в течении месяца, от (число от 0): ")
        )
        assert (
            search_data["listeners_from"] >= 0
        ), "Количество прослушиваний не может быть меньше 0"
        search_data["listeners_to"] = int(
            input("Количеству прослушиваний в течении месяца, до (число от 0): ")
        )
        assert (
            search_data["listeners_to"] >= 0
        ), "Количество прослушиваний не может быть меньше 0"
    except ValueError:
        print("Ошибка ввода. Ожидался ввод целого числа.")
        search_data = {}
    except AssertionError as ex:
        print(ex.args[0])
        search_data = {}
    return search_data


def run_parser():
    """Подготовка и запуск приложения"""
    logger = setup_logging()
    clicker = YandexMusicParser(logger)
    try:
        if search_data := input_search_data():
            result = clicker.search_params(search_data)
            if result:
                save_data_to_csv(result, f"{search_data['genre']}.csv")
    except Exception as ex:
        logger.error(f"{ex}\n{traceback.format_exc()}")
    finally:
        clicker.stop()
