from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions
from playwright.sync_api import Page


class DownloadPage(Page):
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)

        self.files = MultiWebElement(
            page=page,
            locator=page.locator("#content a"),
            description="Download files"
        )

    def get_third_file_name(self):
        return self.files.nth(2).get_inner_text()

    def download_third_file(self):
        with self.page.expect_download() as download_info:
            self.files.nth(2).click()

        return download_info.value
