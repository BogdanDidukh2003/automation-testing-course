from enum import Enum
from typing import Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from drivers import Drivers

LocatorType = Tuple[By, str]


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SeleniumConnector(metaclass=Singleton):
    def __init__(self, *args, **kwargs):
        self.driver: WebDriver = None

    @property
    def url(self) -> str:
        return self.driver.current_url

    def navigate_url(self, site_url: str):
        self.driver.get(site_url)

    def find_element_by_locator(self, locator: LocatorType) -> WebElement:
        locator_strategy, locator_name = locator
        return self.driver.find_element(locator_strategy, locator_name)

    def find_element_by_css_id(self, element_id: str) -> WebElement:
        return self.driver.find_element(By.ID, element_id)

    def close(self):
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
