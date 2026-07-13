from ui.page_actions import PageActions
from playwright.sync_api import Page


class DynamicContentPage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)

        self.images = page.locator("#content img")

    def get_images_src(self):
        return self.images.evaluate_all(
            "imgs => imgs.map(img => img.src)"
        )

    def wait_for_images_state(self, attempts: int = 10):
        for _ in range(attempts):
            srcs = self.get_images_src()

            if len(set(srcs)) < len(srcs):
                return srcs

            self.page.reload()
            self.page.wait_for_load_state("domcontentloaded")

        return srcs
