from ui.page_actions import PageActions
from ui.web_element import WebElement
from playwright.sync_api import Page


class JavascriptAlerts:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)

        self.button_js_alert = WebElement(
            locator=page.get_by_text("Click for JS Alert"),
            description="Кнопка открытия js alert"
        )

        self.button_js_confirm = WebElement(
            locator=page.get_by_text("Click for JS Confirm"),
            description="Кнопка открытия js confirm"
        )

        self.button_js_prompt = WebElement(
            locator=page.get_by_text("Click for JS Prompt"),
            description="Кнопка открытия js prompt"
        )

        self.result = WebElement(
            locator=page.locator("#result"),
            description="Result message"
        )

    def accept_js_alert(self) -> str:
        return self.actions.run_and_accept_alert(
            self.button_js_alert.click
        )

    def accept_js_confirm(self) -> str:
        return self.actions.run_and_accept_alert(
            self.button_js_confirm.click
        )

    def dismiss_js_confirm(self) -> str:
        return self.actions.run_and_dismiss_alert(
            self.button_js_confirm.click
        )

    def enter_prompt_text(self, text: str) -> str:
        return self.actions.run_and_accept_prompt(
            self.button_js_prompt.click,
            text,
        )

    def get_result_text(self) -> str:
        return self.result.get_inner_text()
