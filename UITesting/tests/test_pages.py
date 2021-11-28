import pytest

from connectors import ConnectorFactory, SeleniumConnector
from drivers import Drivers
from pages import LinkedinHomePage, LinkedinSignInPage, LinkedinSignUpPage
from utils import get_text_from_input_field


@pytest.fixture(scope="class")
def connector():
    """Return connector to a wrapper for Selenium driver."""
    sc = ConnectorFactory.get_connector(driver=Drivers.EDGE)
    sc.configure()
    yield sc
    sc.close()


@pytest.fixture()
def homepage(connector):
    page = LinkedinHomePage(connector=connector)
    yield page


@pytest.fixture()
def sign_in_page(connector):
    page = LinkedinSignInPage(connector=connector)
    yield page


@pytest.fixture()
def sign_up_page(connector):
    page = LinkedinSignUpPage(connector=connector)
    yield page


@pytest.mark.usefixtures("connector")
class TestLinkedinEndToEnd:
    TEST_EMAIL: str = "my.email@gmail.com"
    TEST_PASSWORD: str = "wFnsfni32efwnl2n3"
    TEST_FIRST_NAME: str = "Den"
    TEST_LAST_NAME: str = "Surname"
    EXPECTED_SIGN_IN_FAILURE_ERROR: str = (
        "Couldn’t find a LinkedIn account associated with this email. Please try again.")

    @pytest.mark.order(1)
    def test_homepage(self, connector: SeleniumConnector, homepage: LinkedinHomePage):
        homepage.load()
        assert connector.url == LinkedinHomePage.URL

        homepage.click_sign_in_button()
        assert connector.url == LinkedinSignInPage.URL

    @pytest.mark.order(2)
    def test_go_to_sign_up(self, connector: SeleniumConnector, sign_in_page: LinkedinSignInPage):
        sign_in_page.click_join_now_button()
        assert connector.url == LinkedinSignUpPage.URL

    @pytest.mark.order(3)
    def test_enter_user_credentials(self, connector: SeleniumConnector, sign_up_page: LinkedinSignUpPage):
        sign_up_page.enter_email(self.TEST_EMAIL)
        entered_email = get_text_from_input_field(
            input_field=sign_up_page.get_email_input_field(),
        )
        assert entered_email == self.TEST_EMAIL

        sign_up_page.enter_password(self.TEST_PASSWORD)
        entered_password = get_text_from_input_field(
            input_field=sign_up_page.get_password_input_field(),
        )
        assert entered_password == self.TEST_PASSWORD

        sign_up_page.click_join_button()
        assert connector.url == LinkedinSignUpPage.URL

    @pytest.mark.order(4)
    def test_enter_user_info(self, connector: SeleniumConnector, sign_up_page: LinkedinSignUpPage):
        sign_up_page.enter_first_name(self.TEST_FIRST_NAME)
        entered_first_name = get_text_from_input_field(
            input_field=sign_up_page.get_first_name_input_field(),
        )
        assert entered_first_name == self.TEST_FIRST_NAME

        sign_up_page.enter_last_name(self.TEST_LAST_NAME)
        entered_last_name = get_text_from_input_field(
            input_field=sign_up_page.get_last_name_input_field(),
        )
        assert entered_last_name == self.TEST_LAST_NAME

        sign_up_page.click_continue_button()
        assert connector.url == LinkedinSignUpPage.URL

    @pytest.mark.order(5)
    def test_sign_in(self, connector: SeleniumConnector, sign_in_page: LinkedinSignInPage):
        sign_in_page.load()
        assert connector.url == LinkedinSignInPage.URL

        sign_in_page.enter_email(self.TEST_EMAIL)
        entered_email = get_text_from_input_field(
            input_field=sign_in_page.get_email_input_field(),
        )
        assert entered_email == self.TEST_EMAIL

        sign_in_page.enter_password(self.TEST_PASSWORD)
        entered_password = get_text_from_input_field(
            input_field=sign_in_page.get_password_input_field(),
        )
        assert entered_password == self.TEST_PASSWORD

        sign_in_page.click_sign_in_button()

    @pytest.mark.skip(
        reason="Linkedin requires security verification during login due to a ban on action repetition.")
    @pytest.mark.order(6)
    def test_sign_in_failure(self, connector: SeleniumConnector, sign_in_page: LinkedinSignInPage):
        error = sign_in_page.check_sign_in_email_error()
        assert error == self.EXPECTED_SIGN_IN_FAILURE_ERROR
