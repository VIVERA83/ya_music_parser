from logging import Logger

from icecream import ic
from selenium.common import NoSuchElementException

from parser.frames.welcome import WelcomeFrame


class SearchFrame(WelcomeFrame):
    def __init__(self, logger: Logger = None):
        super().__init__(logger)

    def parse_search_frame(self, text: str) -> str:
        self.driver.get(self.create_url("/search", text=text))
        self.wait()
        self.parse_welcome_frame()
        artist_id = self._get_first_article().split("/")[-1]
        return artist_id

    def _get_first_article(self) -> str:
        class_name = "artist"
        try:
            element = self.driver.find_element(by=self.By.CLASS_NAME, value=class_name)
            return element.find_element(by=self.By.TAG_NAME, value="a").get_attribute(
                "href"
            )
        except NoSuchElementException:
            self.logger.info("Элементы поиска не найдены")

    def search_by_params(self, genre: str, type_artist: str, page: int = None) -> list[str]:
        if page:
            self.driver.get(self.create_url("/search", text=genre, type=type_artist, page=page))
        else:
            self.driver.get(self.create_url("/search", text=genre, type=type_artist))
        self.wait()
        self.parse_welcome_frame()
        self._click_link_all_artists()
        links = self._get_artists_articles()
        print(links)
        return [artist_id.split("/")[-1] for artist_id in links]

    def _get_artists_articles(self) -> list[str]:
        class_name = "artist"
        try:
            self.driver.refresh()
            print(self.driver.current_url)
            elements = self.driver.find_elements(
                by=self.By.CLASS_NAME, value=class_name
            )
            ic(elements)
            return [
                element.find_element(by=self.By.TAG_NAME, value="a").get_attribute(
                    "href"
                )
                for element in elements
            ]
        except NoSuchElementException:
            self.logger.info("Элементы поиска не найдены")

    def _click_link_all_artists(self):
        x_path = "/html/body/div[1]/div[16]/div[2]/div/div/div[1]/nav/a[2]"
        element = self.driver.find_element(by=self.By.XPATH, value=x_path)
        element.click()
        self.wait()
        print("click")