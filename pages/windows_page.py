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

    def open_new_tab(self) -> Page:
        with self.page.context.expect_page() as new_page_event:
            self.link_click_here.click()

        new_page = new_page_event.value
        new_page.wait_for_load_state()

        return new_page


class NewWindowPage:
    def __init__(self, page: Page):
        self.page = page

        self.header = WebElement(
            locator=page.locator("h3"),
            description="Заголовок"
        )

    def get_text(self) -> str:
        return self.header.get_inner_text()
