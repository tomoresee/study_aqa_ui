from ui.page_actions import PageActions
from ui.web_element import WebElement
from playwright.sync_api import Page


class ContextMenuPage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)

        self.hot_spot = WebElement(
            locator=page.locator("#hot-spot"),
            description="Hot spot")

    def get_hot_spot_alert_text(self):
        return self.actions.run_and_accept_alert(
            self.hot_spot.right_click
        )
