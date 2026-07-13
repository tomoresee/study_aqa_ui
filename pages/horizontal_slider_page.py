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

    def set_random_slider_value(self) -> str:
        min_value = float(self.slider.get_attribute("min"))
        max_value = float(self.slider.get_attribute("max"))
        step = float(self.slider.get_attribute("step"))

        values = [
            round(min_value + step * i, 1)
            for i in range(
                1,
                int((max_value - min_value) / step)
            )
        ]

        random_value = random.choice(values)

        self.slider.focus()

        current_value = float(
            self.slider.get_attribute("value")
        )

        presses = int(
            abs(random_value - current_value) / step
        )

        key = (
            "ArrowRight"
            if random_value > current_value
            else "ArrowLeft"
        )

        for _ in range(presses):
            self.slider.press(key)

        return str(random_value)
