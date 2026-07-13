from ui.page_actions import PageActions
from ui.web_element import WebElement
from playwright.sync_api import Page


class UploadImagePage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)

        self.file_input = WebElement(
            locator=page.locator("#file-upload"),
            description="Поле загрузки файла"
        )

        self.upload_button = WebElement(
            locator=page.locator("#file-submit"),
            description="Кнопка загрузки файла"
        )

        self.uploaded_file_name = WebElement(
            locator=page.locator("#uploaded-files"),
            description="Имя загруженного файла"
        )

        self.success_message = WebElement(
            locator=page.get_by_text("File Uploaded!"),
            description="Сообщение об успешной загрузке"
        )

    def upload_file(self, file_path):
        self.file_input.set_input_files(file_path)
        self.upload_button.click()

    def get_uploaded_file_name(self):
        return self.uploaded_file_name.get_inner_text()

    def get_success_message(self):
        return self.success_message.get_inner_text()
