from selenium.webdriver.remote.webelement import WebElement


def click_button(button: WebElement):
    button.click()


def enter_text_in_input_field(input_field: WebElement, text: str):
    input_field.clear()
    input_field.send_keys(text)


def get_text_from_element(element: WebElement):
    return element.text


def get_text_from_input_field(input_field: WebElement):
    return input_field.get_attribute("value")
