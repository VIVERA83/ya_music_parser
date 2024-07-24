from time import sleep
from logging import Logger

from typing import Optional

from selenium.webdriver.remote.webelement import WebElement

from parser.frames.welcome import WelcomeFrame, NoSuchElementException
from parser.types import ArtistDict


class ArtistInfoFrame(WelcomeFrame):
    def __init__(self, logger: Logger = None):
        super().__init__(logger)
        self.element: Optional[WebElement] = None

    def parse_artist_info(self, artist_id: str) -> ArtistDict:
        self.driver.get(self.create_url(f"/artist/{artist_id}/info"))
        self.wait()
        self.parse_welcome_frame()
        class_name = "page-artist"
        self.element = self.driver.find_element(self.By.CLASS_NAME, value=class_name)
        sleep(1)

        try:
            return self.get_data_about_artist()
        except NoSuchElementException as e:
            self.logger.warning(f"Не получилось {e.args}, Капча")
        return {}

    def get_data_about_artist(self) -> ArtistDict:
        data: dict[str, str] = {}
        data.update(self._get_artist_name())

        css_selector = ".page-artist__info-cell .page-artist__info-cell_wide"
        elements = self.driver.find_elements(self.By.CSS_SELECTOR, value=css_selector)

        keys = ["listeners", "likes"]
        for el in elements:
            if div_elements := el.find_elements(self.By.TAG_NAME, "div"):
                div_element = div_elements[0]
                if data_b := div_element.get_attribute("data-b"):
                    if keys:
                        data.update(self._data_b_handler(div_element, keys.pop(0)))
                else:
                    self.logger.warning(
                        f"Обработчика для атрибута data-b `{data_b}` не найден"
                    )

            elif a_elements := el.find_elements(self.By.TAG_NAME, "a"):
                a_element = a_elements[0]
                if spans := a_element.find_elements(self.By.TAG_NAME, "span"):
                    if data_type := spans[-1].get_attribute("data-type"):
                        data_type = self.__check_type_website(data_type, data)
                        data.update({data_type: a_element.get_attribute("href")})
                    else:
                        self.logger.warning(
                            f"Атрибут data-type `{data_type}` не найден"
                        )
                else:
                    self.logger.warning(f"Тег span для ссылки не найден")
        return data

    def _get_artist_name(self) -> ArtistDict:
        """Получить имя исполнителя."""
        return {"name": self.element.find_element(self.By.TAG_NAME, "h1").text}

    def _data_b_handler(self, element: WebElement, key: str) -> ArtistDict:
        """Слушателей либо лайков за месяц, в зависимости от ключа"""
        class_name = "artist-trends__total-count"
        text = element.find_element(self.By.CLASS_NAME, value=class_name).text
        return {key: text}

    @staticmethod
    def __check_type_website(data_type: str, data: ArtistDict) -> str:
        """Проверка типа сайта"""
        if data_type == "website" and not data.get("website_1"):
            return f"{data_type}_1"
        return f"{data_type}_2"
