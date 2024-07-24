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
