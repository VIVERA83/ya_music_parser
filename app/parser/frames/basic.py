import re
from logging import Logger

from selenium.common import NoSuchElementException

from parser.frames.welcome import WelcomeFrame
from parser.types import ArtistDict


class BasicArtistFrame(WelcomeFrame):
    def __init__(self, logger: Logger = None):
        super().__init__(logger)

    def parse_basic_artist_frame(self, artist_id: str) -> ArtistDict:
        self.driver.get(self.create_url(f"/artist/{artist_id}"))
        self.wait()
        self.parse_welcome_frame()
        return self._get_last_release()

    def _get_last_release(self) -> ArtistDict:
        try:
            css_selector = "page-artist__latest-album"
            element = self.driver.find_element(
                by=self.By.CLASS_NAME, value=css_selector
            )
            class_name = "album__bottom"
            element = element.find_element(
                by=self.By.CLASS_NAME, value=class_name
            )
            results = re.findall(r"[0-9]{2} [a-я]* [0-9]{4}", element.text)
            return {"last_release": results[0] or "data not found"}
        except NoSuchElementException:
            self.logger.warning("Данных по последнему релизу нет")
            return {"last_release": "data not found"}
