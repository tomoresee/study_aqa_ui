from pages.context_menu_page import ContextMenuPage
from pages.horizontal_slider_page import HorizontalSliderPage
from pages.javascript_alerts import JavascriptAlerts
from ui.page_actions import PageActions
from utils.data import random_text
from utils.url_utils import embed_credentials_in_url
from playwright.sync_api import Page
from pages.basic_auth_page import BasicAuthPage

from utils.config_reader import ConfigReader

# Это бы я сохранил в .env
login = "admin"
password = "admin"

URL = ConfigReader.get("base_url")


def test_basic_auth(basic_auth_page: BasicAuthPage, actions: PageActions):
    """
    1. Перейти по URL
    2. Выполнить авторизацию с корректными учетными данными
    login: admin
    password: admin

    3. Получить текст, отображаемый на странице
    Текст соответствует: Congratulations! You must have the proper credentials.
    """

    actions.goto(embed_credentials_in_url(f"{URL}/basic_auth", login, password))

    assert basic_auth_page.assert_text_message()


def test_alerts(js_alert_page: JavascriptAlerts, actions: PageActions):
    actions.goto(f"{URL}/javascript_alerts")

    alert_text = js_alert_page.accept_js_alert()

    assert alert_text == "I am a JS Alert", (
        f"Неожиданный текст alert. "
        f"Ожидалось: 'I am a JS Alert', Фактически: '{alert_text}'"
    )

    result = js_alert_page.get_result_text()

    assert result == "You successfully clicked an alert", (
        f"Неожидательный текст результата. "
        f"Ожидалось: 'You successfully clicked an alert', "
        f"Фактически: '{result}'"
    )

    dialog_text = js_alert_page.accept_js_confirm()

    assert dialog_text == "I am a JS Confirm", (
        f"Неожиданный текст confirm. "
        f"Ожидалось: 'I am a JS Confirm', Фактически: '{dialog_text}'"
    )

    result = js_alert_page.get_result_text()

    assert result == "You clicked: Ok", (
        f"Неожиданный текст результата. "
        f"Ожидалось: 'You clicked: Ok', Фактически: '{result}'"
    )

    prompt_text = js_alert_page.enter_prompt_text(random_text)

    assert prompt_text == "I am a JS prompt", (
        f"Неожиданный текст prompt. "
        f"Ожидалось: 'I am a JS Prompt', Фактически: '{prompt_text}'"
    )

    result = js_alert_page.get_result_text()

    assert result == f"You entered: {random_text}", (
        f"Неожиданный текст результата. "
        f"Ожидалось: 'You entered: {random_text}', "
        f"Фактически: '{result}'"
    )


def test_context_click(context_menu_page: ContextMenuPage, actions: PageActions):
    """
    1. Перейти по URL
    2. Выполнить клик правой кнопкой мыши (ПКМ) по выделенной области
    Отображается alert с текстом You selected a context menu

    3. В alert нажать кнопку OK

    """
    actions.goto(f"{URL}/context_menu")

    alert_text = context_menu_page.get_hot_spot_alert_text()

    assert alert_text == "You selected a context menu", (
        f"Неожиданный текст alert. "
        f"Ожидалось: 'You selected a context menu', "
        f"Фактически: '{alert_text}'"
    )


def test_slider(horizontal_slider_page: HorizontalSliderPage,
                actions: PageActions, ):
    actions.goto(
        f"{URL}/horizontal_slider"
    )

    expected_value = horizontal_slider_page.set_random_slider_value()

    actual_value = (
        horizontal_slider_page.slider_value.get_inner_text()
    )

    assert float(actual_value) == float(expected_value), (
        f"Значение слайдера неверное. "
        f"Ожидалось: '{expected_value}', "
        f"Фактически: '{actual_value}'"
    )
