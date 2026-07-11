import pytest

from logger import setup_logger
from pages.context_menu_page import ContextMenuPage
from pages.javascript_alerts import JavascriptAlerts
from ui.page_actions import PageActions
from playwright.sync_api import Page
from pages.basic_auth_page import BasicAuthPage


@pytest.fixture(scope="session", autouse=True)
def init_logger():
    setup_logger()


@pytest.fixture(scope="function")
def actions(page: Page) -> PageActions:
    return PageActions(page)


@pytest.fixture(scope="function")
def basic_auth_page(page: Page) -> BasicAuthPage:
    return BasicAuthPage(page)


@pytest.fixture(scope="function")
def js_alert_page(page: Page) -> JavascriptAlerts:
    return JavascriptAlerts(page)


@pytest.fixture(scope="function")
def context_menu_page(page: Page) -> ContextMenuPage:
    return ContextMenuPage(page)
