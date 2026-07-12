import pytest

from logger import setup_logger
from pages.context_menu_page import ContextMenuPage
from pages.frames_page import FramePage
from pages.horizontal_slider_page import HorizontalSliderPage
from pages.hovers_page import HoverPage
from pages.javascript_alerts import JavascriptAlerts
from pages.windows_page import WindowsPage
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


@pytest.fixture(scope="function")
def horizontal_slider_page(page: Page) -> HorizontalSliderPage:
    return HorizontalSliderPage(page)


@pytest.fixture(scope="function")
def hover_page(page: Page) -> HoverPage:
    return HoverPage(page)


@pytest.fixture(scope="function")
def windows_page(page: Page) -> WindowsPage:
    return WindowsPage(page)


@pytest.fixture(scope="function")
def frame_page(page: Page) -> FramePage:
    return FramePage(page)
