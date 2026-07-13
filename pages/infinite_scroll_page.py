from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions
from playwright.sync_api import Page


class InfiniteScrollPage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)

        self.paragraphs = MultiWebElement(
            page=page,
            locator=page.locator(".jscroll-added"),
            description="Infinite scroll paragraphs"
        )

    def get_paragraphs_count(self) -> int:
        return self.paragraphs.count()

    def scroll_down(self):
        self.page.mouse.wheel(0, 2000)

    def scroll_until(self, target: int, max_attempts: int = 10):
        for _ in range(max_attempts):
            count = self.get_paragraphs_count()

            if count >= target:
                return count

            self.scroll_down()
            self.page.wait_for_timeout(300)

        return self.get_paragraphs_count()
