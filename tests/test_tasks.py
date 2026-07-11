from pages.javascript_alerts import JavascriptAlerts
from utils.url_utils import embed_credentials_in_url
from playwright.sync_api import Page
from pages.basic_auth_page import BasicAuthPage
from faker import Faker

url = "http://the-internet.herokuapp.com/basic_auth"

# Это бы я сохранил в .env
login = "admin"
password = "admin"


def test_basic_auth(basic_auth_page: BasicAuthPage, actions):
    """
    1. Перейти по URL
    2. Выполнить авторизацию с корректными учетными данными
    login: admin
    password: admin

    3. Получить текст, отображаемый на странице
    Текст соответствует: Congratulations! You must have the proper credentials.
    """

    actions.goto(embed_credentials_in_url(url, login, password))

    assert basic_auth_page.assert_text_message()


def test_alerts(js_alert_page: JavascriptAlerts, actions):
    # TODO вынести в config URL
    actions.goto("https://the-internet.herokuapp.com/javascript_alerts")

    # TODO вынести faker куда нибудь
    fake = Faker()

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

    random_text = fake.pystr()

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
