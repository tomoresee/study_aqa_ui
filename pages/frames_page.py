from ui.page_actions import PageActions
from playwright.sync_api import Page


class FramePage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)

        self.top_frame = page.frame_locator(
            "frame[name='frame-top']"
        )

        self.bottom_frame = page.frame_locator(
            "frame[name='frame-bottom']"
        )

        self.left_frame = (
            self.top_frame
            .frame_locator("frame[name='frame-left']")
        )

        self.middle_frame = (
            self.top_frame
            .frame_locator("frame[name='frame-middle']")
        )

        self.right_frame = (
            self.top_frame
            .frame_locator("frame[name='frame-right']")
        )

    def get_left_text(self) -> str:
        return self.left_frame.locator("body").inner_text()

    def get_middle_text(self) -> str:
        return self.middle_frame.locator("body").inner_text()

    def get_right_text(self) -> str:
        return self.right_frame.locator("body").inner_text()

    def get_bottom_text(self) -> str:
        return self.bottom_frame.locator("body").inner_text()

    def get_left_text(self) -> str:
        return self.left_frame.locator("body").inner_text()

    def get_middle_text(self) -> str:
        return self.middle_frame.locator("body").inner_text()

    def get_right_text(self) -> str:
        return self.right_frame.locator("body").inner_text()

    def get_bottom_text(self) -> str:
        return self.bottom_frame.locator("body").inner_text()
