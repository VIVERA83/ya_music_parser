from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_chrome_driver_options() -> Options:
    """Получить параметры для запуска браузера Chrome."""

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-running-insecure-content")
    user_agent = UserAgent(browsers=["chrome"]).getRandom.get("useragent")
    options.add_argument(f"user-agent={user_agent}")
    return options
