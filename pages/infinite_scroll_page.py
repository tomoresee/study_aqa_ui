from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError


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
        old_count = self.get_paragraphs_count()
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        try:
            self.page.wait_for_function(
                f"document.querySelectorAll('.jscroll-added').length > {old_count}",
                timeout=5000
            )
            self.get_paragraphs_count()
        except PlaywrightTimeoutError:
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_until(self, target: int, max_attempts: int = 15):
        for attempt in range(max_attempts):
            count = self.get_paragraphs_count()

            if count >= target:
                return count

            self.scroll_down()

        final_count = self.get_paragraphs_count()
        return final_count
