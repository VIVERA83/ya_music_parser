from logging import Logger

from selenium.common import NoSuchElementException

from parser import BaseParser


class WelcomeFrame(BaseParser):
    def __init__(self, logger: Logger = None):
        super().__init__(logger)

    def parse_welcome_frame(self):
        """Парсинг окна приветствия."""
        x_path = "/html/body/div[1]/div[22]/div/span"
        try:
            element = self.driver.find_element(by=self.By.XPATH, value=x_path)
            element.click()
            self.logger.info("Приветственное окно выводилось")
        except NoSuchElementException:
            self.logger.info("Приветственное окно не выводилось")
