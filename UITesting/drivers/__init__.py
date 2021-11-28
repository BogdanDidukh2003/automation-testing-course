from enum import Enum
import os


def _get_absolute_path(filename: str) -> str:
    return os.path.join(os.path.dirname(__file__), filename)


class Drivers(Enum):
    CHROME = _get_absolute_path("chromedriver.exe")
    EDGE = _get_absolute_path("msedgedriver.exe")
