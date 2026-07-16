from ui.page_actions import PageActions
from playwright.sync_api import Page

from ui.web_element import WebElement


class FramePage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)

        self.top_frame = WebElement(
            locator=page.frame_locator("frame[name='frame-top']"),
            description="Top frame"
        )

        self.bottom_frame = WebElement(
            locator=page.frame_locator("frame[name='frame-bottom']"),
            description="Bottom frame"
        )

        self.left_frame = WebElement(
            locator=page.frame_locator("frame[name='frame-top']").frame_locator("frame[name='frame-left']"),
            description="Left frame"
        )

        self.middle_frame = WebElement(
            locator=page.frame_locator("frame[name='frame-top']").frame_locator("frame[name='frame-middle']"),
            description="Middle frame"
        )

        self.right_frame = WebElement(
            locator=page.frame_locator("frame[name='frame-top']").frame_locator("frame[name='frame-right']"),
            description="Right frame"
        )

        self.left_body = WebElement(
            locator=self.left_frame.locator.locator("body"),
            description="Body in left frame"
        )

        self.middle_body = WebElement(
            locator=self.middle_frame.locator.locator("body"),
            description="Body in middle frame"
        )

        self.right_body = WebElement(
            locator=self.right_frame.locator.locator("body"),
            description="Body in right frame"
        )

        self.bottom_body = WebElement(
            locator=self.bottom_frame.locator.locator("body"),
            description="Body in bottom frame"
        )

    def get_left_text(self) -> str:
        return self.left_body.get_inner_text()

    def get_middle_text(self) -> str:
        return self.middle_body.get_inner_text()

    def get_right_text(self) -> str:
        return self.right_body.get_inner_text()

    def get_bottom_text(self) -> str:
        return self.bottom_body.get_inner_text()
