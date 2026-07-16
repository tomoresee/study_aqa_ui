from ui.page_actions import PageActions
from ui.web_element import WebElement
from playwright.sync_api import Page
import random


class HorizontalSliderPage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)

        self.slider = WebElement(locator=page.locator("input[type='range']"),
                                 description="Horizontal slider")

        self.slider_value = WebElement(
            locator=page.locator("#range"),
            description="Slider value"
        )

    def get_slider_range(self) -> tuple[float, float, float]:
        min_value = float(self.slider.get_attribute("min"))
        max_value = float(self.slider.get_attribute("max"))
        step = float(self.slider.get_attribute("step"))
        return min_value, max_value, step

    def set_value(self, target_value: float) -> None:
        self.slider.focus()

        current_value = float(self.slider.get_attribute("value"))
        step = float(self.slider.get_attribute("step"))

        presses = int(abs(target_value - current_value) / step)

        key = "ArrowRight" if target_value > current_value else "ArrowLeft"

        for _ in range(presses):
            self.slider.press(key)

    def get_value(self) -> str:
        return self.slider_value.get_inner_text()
