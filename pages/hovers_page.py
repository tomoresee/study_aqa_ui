from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions
from playwright.sync_api import Page


class HoverPage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)

        self.figures = MultiWebElement(
            page=page,
            locator=page.locator("figure"),
            description="Аватары пользователей"
        )

        self.figcaptions = MultiWebElement(
            page=page,
            locator=page.locator("figcaption"),
            description="Подписи пользователей"
        )

    def get_users_count(self) -> int:
        return self.figures.count()

    def hover_user(self, index: int):
        self.figures.nth(index).hover()

    def get_user_text(self, index: int) -> str:
        return self.figcaptions.nth(index).get_inner_text()

    def get_all_users_texts(self) -> list[str]:
        texts = []

        for i, figure in enumerate(self.figures):
            figure.hover()
            text = self.figcaptions.nth(i).get_inner_text()
            texts.append(text)

        return texts
