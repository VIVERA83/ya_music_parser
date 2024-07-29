from logging import Logger

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

    def move_to_page_by_params(self, genre: str, type_artist: str, page: int):
        self.driver.get(
            self.create_url("/search", text=genre, type=type_artist, page=page)
        )
        self.wait()
        self.parse_welcome_frame()

    def _get_artists_articles(self) -> list[str]:
        class_name = "artist"
        try:
            elements = self.driver.find_elements(
                by=self.By.CLASS_NAME, value=class_name
            )
            return [
                element.find_element(by=self.By.TAG_NAME, value="a")
                .get_attribute("href")
                .split("/")[-1]
                for element in elements
            ]
        except NoSuchElementException:
            self.logger.error("Элементы поиска не найдены")

    def _click_link_all_artists(self) -> int:
        x_path = "/html/body/div[1]/div[16]/div[2]/div/div/div[1]/nav/a[2]"
        element = self.driver.find_element(by=self.By.XPATH, value=x_path)
        count_artists = int(element.text.split(" ")[0])
        element.click()
        self.wait()
        return count_artists
