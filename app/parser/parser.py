from logging import Logger, getLogger

from selenium import webdriver

from parser.utils import get_chrome_driver_options


class YandexMusicParser:
    def __init__(self, logger: Logger = None):
        self.logger = logger or getLogger(name=__name__)
        self.driver = webdriver.Chrome(options=get_chrome_driver_options())

    def start(self):
        """Начать парсинг."""

    def stop(self):
        """Остановить парсинг."""
        self.driver.quit()
