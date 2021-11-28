from selenium.webdriver.common.by import By

from connectors import SeleniumConnector, LocatorType
from utils import enter_text_in_input_field, click_button, get_text_from_element


class BasePage:
    def __init__(self, connector: SeleniumConnector):
        self.connector = connector


class LinkedinHomePage(BasePage):
    URL: str = "https://www.linkedin.com/"
    SIGN_IN_BUTTON_LOCATOR: LocatorType = (
        By.CSS_SELECTOR,
        "body > nav > div > a.nav__button-secondary",
    )

    def get_sign_in_button(self):
        sing_in_button = self.connector.find_element_by_locator(
            self.SIGN_IN_BUTTON_LOCATOR,
        )
        return sing_in_button

    def load(self):
        self.connector.navigate_url(self.URL)

    def click_sign_in_button(self):
        sing_in_button = self.get_sign_in_button()

        click_button(sing_in_button)


class LinkedinSignInPage(BasePage):
    URL: str = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
    JOIN_NOW_BUTTON_LOCATOR: LocatorType = (
        By.CSS_SELECTOR,
        "#join_now",
    )
    EMAIL_INPUT_LOCATOR: LocatorType = (
        By.CSS_SELECTOR,
        "#username",
    )
    PASSWORD_INPUT_LOCATOR: LocatorType = (
        By.CSS_SELECTOR,
        "#password",
    )
    SIGN_IN_BUTTON_LOCATOR: LocatorType = (
        By.CSS_SELECTOR,
        "#organic-div > form > div.login__form_action_container > button",
    )
    SIGN_IN_EMAIL_ERROR_LOCATOR: LocatorType = (
        By.CSS_SELECTOR,
        "#error-for-username",
    )

    def get_join_now_button(self):
        join_now_button = self.connector.find_element_by_locator(
            self.JOIN_NOW_BUTTON_LOCATOR,
        )
        return join_now_button

    def get_email_input_field(self):
        input_field = self.connector.find_element_by_locator(
            self.EMAIL_INPUT_LOCATOR,
        )
        return input_field

    def get_password_input_field(self):
        input_field = self.connector.find_element_by_locator(
            self.PASSWORD_INPUT_LOCATOR,
        )
        return input_field

    def get_sign_in_button(self):
        sign_in_button = self.connector.find_element_by_locator(
            self.SIGN_IN_BUTTON_LOCATOR,
        )
        return sign_in_button

    def get_sign_in_email_error_container(self):
        sign_in_email_error = self.connector.find_element_by_locator(
            self.SIGN_IN_EMAIL_ERROR_LOCATOR,
        )
        return sign_in_email_error

    def load(self):
        self.connector.navigate_url(self.URL)

    def click_join_now_button(self):
        join_now_button = self.get_join_now_button()

        click_button(join_now_button)

    def enter_email(self, email: str):
        input_field = self.get_email_input_field()

        enter_text_in_input_field(
            input_field=input_field,
            text=email,
        )

    def enter_password(self, password: str):
        input_field = self.get_password_input_field()

        enter_text_in_input_field(
            input_field=input_field,
            text=password,
        )

    def click_sign_in_button(self):
        sign_in_button = self.get_sign_in_button()

        click_button(sign_in_button)

    def check_sign_in_email_error(self) -> str:
        sign_in_email_error = self.get_sign_in_email_error_container()

        error = get_text_from_element(sign_in_email_error)
        return error


class LinkedinSignUpPage(BasePage):
    URL: str = "https://www.linkedin.com/signup/cold-join?source=guest_homepage-basic_nav-header-signin"
    EMAIL_INPUT_LOCATOR: LocatorType = (
        By.CSS_SELECTOR,
        "#email-address",
    )
    PASSWORD_INPUT_LOCATOR: LocatorType = (
        By.CSS_SELECTOR,
        "#password",
    )
    JOIN_BUTTON_LOCATOR: LocatorType = (
        By.CSS_SELECTOR,
        "#join-form-submit",
    )
    FIRST_NAME_INPUT_LOCATOR: LocatorType = (
        By.CSS_SELECTOR,
        "#first-name",
    )
    LAST_NAME_INPUT_LOCATOR: LocatorType = (
        By.CSS_SELECTOR,
        "#last-name",
    )
    CONTINUE_BUTTON_LOCATOR: LocatorType = (
        By.CSS_SELECTOR,
        "#join-form-submit",
    )

    def get_email_input_field(self):
        input_field = self.connector.find_element_by_locator(
            self.EMAIL_INPUT_LOCATOR,
        )
        return input_field

    def get_password_input_field(self):
        input_field = self.connector.find_element_by_locator(
            self.PASSWORD_INPUT_LOCATOR,
        )
        return input_field

    def get_join_button(self):
        join_button = self.connector.find_element_by_locator(
            self.JOIN_BUTTON_LOCATOR,
        )
        return join_button

    def get_first_name_input_field(self):
        input_field = self.connector.find_element_by_locator(
            self.FIRST_NAME_INPUT_LOCATOR,
        )
        return input_field

    def get_last_name_input_field(self):
        input_field = self.connector.find_element_by_locator(
            self.LAST_NAME_INPUT_LOCATOR,
        )
        return input_field

    def get_continue_button(self):
        continue_button = self.connector.find_element_by_locator(
            self.CONTINUE_BUTTON_LOCATOR,
        )
        return continue_button

    def enter_email(self, email: str):
        input_field = self.get_email_input_field()

        enter_text_in_input_field(
            input_field=input_field,
            text=email,
        )

    def enter_password(self, password: str):
        input_field = self.get_password_input_field()

        enter_text_in_input_field(
            input_field=input_field,
            text=password,
        )

    def click_join_button(self):
        join_button = self.get_join_button()

        click_button(join_button)

    def enter_first_name(self, first_name: str):
        input_field = self.get_first_name_input_field()

        enter_text_in_input_field(
            input_field=input_field,
            text=first_name,
        )

    def enter_last_name(self, last_name: str):
        input_field = self.get_last_name_input_field()

        enter_text_in_input_field(
            input_field=input_field,
            text=last_name,
        )

    def click_continue_button(self):
        continue_button = self.get_continue_button()

        click_button(continue_button)
