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

    def scroll_to_last_paragraph(self):
        if self.paragraphs.count() > 0:
            last_element = self.paragraphs.locator.last
            last_element.scroll_into_view_if_needed()

    def scroll_until(self, target: int, max_attempts: int = 20):
        for attempt in range(max_attempts):
            count = self.get_paragraphs_count()

            if count >= target:
                return count

            self.scroll_to_last_paragraph()

            try:
                self.paragraphs.locator.nth(count).wait_for(state="attached", timeout=5000)
            except PlaywrightTimeoutError:
                pass

        final_count = self.get_paragraphs_count()
        return final_count
