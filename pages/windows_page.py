from ui.page_actions import PageActions
from playwright.sync_api import Page

from ui.web_element import WebElement


class WindowsPage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)

        self.link_click_here = WebElement(
            locator=page.get_by_text("Click Here"),
            description="Ссылка открытия новой вкладки"
        )

    def click_open_new_tab(self) -> None:
        self.link_click_here.click()


class NewWindowPage:
    def __init__(self, page: Page):
        self.page = page

        self.header = WebElement(
            locator=page.locator("h3"),
            description="Заголовок"
        )

    def get_text(self) -> str:
        return self.header.get_inner_text()
