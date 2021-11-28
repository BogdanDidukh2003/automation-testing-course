from enum import Enum
from typing import Tuple

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from drivers import Drivers

LocatorType = Tuple[By, str]


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SeleniumConnector(metaclass=SingletonMeta):
    def __init__(self, *args, **kwargs):
        self.driver: WebDriver = None

    @property
    def url(self) -> str:
        return self.driver.current_url

    def configure(self, waiting_time: int = 1, height: int = 1024, width: int = 768) -> None:
        self.driver.set_window_size(height=height, width=width)
        self.driver.implicitly_wait(waiting_time)
        self.driver.switch_to.default_content()

    def navigate_url(self, site_url: str) -> None:
        self.driver.get(site_url)

    def check_if_element_exists(self, locator: LocatorType) -> bool:
        try:
            element = self.find_element_by_locator(locator)
            return element is not None
        except NoSuchElementException:
            return False

    def find_element_by_locator(self, locator: LocatorType) -> WebElement:
        locator_strategy, locator_name = locator
        return self.driver.find_element(locator_strategy, locator_name)

    def close(self) -> None:
        self.driver.close()


class ChromeConnector(SeleniumConnector):
    def __init__(self):
        super(ChromeConnector, self).__init__()
        self.driver: WebDriver = webdriver.Chrome(Drivers.CHROME.value)


class EdgeConnector(SeleniumConnector):
    def __init__(self, *args, **kwargs):
        super(EdgeConnector, self).__init__(*args, **kwargs)
        self.driver: WebDriver = webdriver.Edge(Drivers.EDGE.value)


class ConnectorFactory:
    @staticmethod
    def get_connector(driver: Enum) -> SeleniumConnector:
        if driver == Drivers.CHROME:
            return ChromeConnector()
        elif driver == Drivers.EDGE:
            return EdgeConnector()

        raise ValueError(f"No connector for `{driver}`")
