from logging import Logger, getLogger
from urllib.parse import urlencode

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from parser.utils import get_chrome_driver_options

BASE_URL = "https://music.yandex.ru"


class BaseParser:
    def __init__(self, logger: Logger = None):
        self.BASE_URL = "https://music.yandex.ru"
        self.timeout = 10
        self.logger = logger or getLogger(name=__name__)
        self.driver = webdriver.Chrome(options=get_chrome_driver_options())
        self._wait = WebDriverWait(self.driver, self.timeout)
        self.By = By

    def stop(self):
        """Остановить парсинг."""
        self.driver.quit()

    def create_url(self, path: str, **kwargs) -> str:
        if kwargs:
            return "?".join([self.BASE_URL + path, urlencode(kwargs)])
        return self.BASE_URL + path

    def wait(self):
        self._wait.until(
            lambda driver: driver.execute_script("return document.readyState")
                           == "complete"
        )
