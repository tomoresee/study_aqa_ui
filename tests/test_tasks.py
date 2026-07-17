from pathlib import Path

from pages.context_menu_page import ContextMenuPage
from pages.download_page import DownloadPage
from pages.dynamic_content_page import DynamicContentPage
from pages.frames_page import FramePage
from pages.horizontal_slider_page import HorizontalSliderPage
from pages.hovers_page import HoverPage
from pages.infinite_scroll_page import InfiniteScrollPage
from pages.javascript_alerts import JavascriptAlerts
from pages.upload_image_page import UploadImagePage
from pages.windows_page import WindowsPage, NewWindowPage
from ui.page_actions import PageActions
from utils.data import fake
from utils.url_utils import embed_credentials_in_url
from pages.basic_auth_page import BasicAuthPage

from utils.config_reader import ConfigReader
import random

# Это бы я сохранил в .env
login = "admin"
password = "admin"

URL = ConfigReader.get("base_url")


def test_basic_auth(basic_auth_page: BasicAuthPage, actions: PageActions):
    """
    1. Перейти по URL
    2. Выполнить авторизацию с корректными учетными данными
    login: admin
    password: admin

    3. Получить текст, отображаемый на странице
    Текст соответствует: Congratulations! You must have the proper credentials.
    """

    actions.goto(embed_credentials_in_url(f"{URL}/basic_auth", login, password))

    actual_text = basic_auth_page.get_text_message()

    assert actual_text == (
        "Congratulations! You must have the proper credentials."
    ), (
        f"Неверный текст сообщения. "
        f"Ожидалось: 'Congratulations! You must have the proper credentials.', "
        f"Фактически: '{actual_text}'"
    )


def test_alerts(js_alert_page: JavascriptAlerts, actions: PageActions):
    random_text = fake.pystr()

    actions.goto(f"{URL}/javascript_alerts")

    alert_text = js_alert_page.accept_js_alert()

    assert alert_text == "I am a JS Alert", (
        f"Неожиданный текст alert. "
        f"Ожидалось: 'I am a JS Alert', Фактически: '{alert_text}'"
    )

    result = js_alert_page.get_result_text()

    assert result == "You successfully clicked an alert", (
        f"Неожидательный текст результата. "
        f"Ожидалось: 'You successfully clicked an alert', "
        f"Фактически: '{result}'"
    )

    dialog_text = js_alert_page.accept_js_confirm()

    assert dialog_text == "I am a JS Confirm", (
        f"Неожиданный текст confirm. "
        f"Ожидалось: 'I am a JS Confirm', Фактически: '{dialog_text}'"
    )

    result = js_alert_page.get_result_text()

    assert result == "You clicked: Ok", (
        f"Неожиданный текст результата. "
        f"Ожидалось: 'You clicked: Ok', Фактически: '{result}'"
    )

    prompt_text = js_alert_page.enter_prompt_text(random_text)

    assert prompt_text == "I am a JS prompt", (
        f"Неожиданный текст prompt. "
        f"Ожидалось: 'I am a JS prompt', Фактически: '{prompt_text}'"
    )

    result = js_alert_page.get_result_text()

    assert result == f"You entered: {random_text}", (
        f"Неожиданный текст результата. "
        f"Ожидалось: 'You entered: {random_text}', "
        f"Фактически: '{result}'"
    )


def test_context_click(context_menu_page: ContextMenuPage, actions: PageActions):
    """
    1. Перейти по URL
    2. Выполнить клик правой кнопкой мыши (ПКМ) по выделенной области
    Отображается alert с текстом You selected a context menu

    3. В alert нажать кнопку OK

    """
    actions.goto(f"{URL}/context_menu")

    alert_text = context_menu_page.get_hot_spot_alert_text()

    assert alert_text == "You selected a context menu", (
        f"Неожиданный текст alert. "
        f"Ожидалось: 'You selected a context menu', "
        f"Фактически: '{alert_text}'"
    )


def test_slider(horizontal_slider_page: HorizontalSliderPage,
                actions: PageActions, ):
    actions.goto(
        f"{URL}/horizontal_slider"
    )

    min_value, max_value, step = horizontal_slider_page.get_slider_range()

    values = [
        round(min_value + step * i, 1)
        for i in range(int((max_value - min_value) / step) + 1)
    ]

    expected_value = random.choice(values)

    horizontal_slider_page.set_value(expected_value)

    actual_value = horizontal_slider_page.get_value()

    assert float(actual_value) == float(expected_value), (
        f"Значение слайдера неверное. "
        f"Ожидалось: '{expected_value}', "
        f"Фактически: '{actual_value}'"
    )


def test_hovers(hover_page: HoverPage, actions: PageActions):
    """
    1. Перейти по URL
    2. Навести курсор на изображение пользователя
    3. Получить текст, отображаемый при наведении
    Отображается имя пользователя в формате: name: userN, где N — порядковый номер

    4. Повторить шаги 2–3 для каждого пользователя (список пользователей определяется динамически)
    Для каждого пользователя выполняются те же проверки
    """
    actions.goto(f'{URL}/hovers')

    texts = hover_page.get_all_users_texts()

    for i, text in enumerate(texts):
        expected = f"name: user{i + 1}"

        assert text == expected, (
            f"Неверный текст для пользователя {i + 1}. "
            f"Ожидалось: '{expected}', Фактически: '{text}'"
        )


def test_windows(windows_page: WindowsPage, actions: PageActions):
    actions.goto(f"{URL}/windows")

    new_tab_1 = actions.open_new_tab(
        windows_page.click_open_new_tab
    )

    assert "/windows/new" in new_tab_1.url, (
        f"Неверный URL новой вкладки. "
        f"Ожидалось наличие: '/windows/new', "
        f"Фактически: '{new_tab_1.url}'"
    )

    new_window_page_1 = NewWindowPage(new_tab_1)

    text_1 = new_window_page_1.get_text()

    assert text_1 == "New Window", (
        f"Неверный текст на первой новой вкладке. "
        f"Ожидалось: 'New Window', "
        f"Фактически: '{text_1}'"
    )

    actions.bring_to_front()

    new_tab_2 = actions.open_new_tab(
        windows_page.click_open_new_tab
    )

    assert "/windows/new" in new_tab_2.url, (
        f"Неверный URL второй новой вкладки. "
        f"Ожидалось наличие: '/windows/new', "
        f"Фактически: '{new_tab_2.url}'"
    )

    new_window_page_2 = NewWindowPage(new_tab_2)

    text_2 = new_window_page_2.get_text()

    assert text_2 == "New Window", (
        f"Неверный текст на второй новой вкладке. "
        f"Ожидалось: 'New Window', "
        f"Фактически: '{text_2}'"
    )

    actions.bring_to_front()

    new_tab_1.close()
    new_tab_2.close()

    pages = windows_page.page.context.pages

    assert len(pages) == 1, (
        f"Неверное количество открытых вкладок. "
        f"Ожидалось: 1, Фактически: {len(pages)}"
    )


def test_frames(frame_page: FramePage, actions: PageActions):
    """
    1. Перейти по URL
    2. Получить текст из левого frame
        Текст равен: LEFT

    3. Получить текст из правого frame
        Текст равен: RIGHT

    4. Получить текст из нижнего frame
        Текст равен: BOTTOM

    5. Получить текст из центрального frame
        Текст равен: MIDDLE
    """
    actions.goto(f"{URL}/nested_frames")

    left_text = frame_page.get_left_text()
    assert left_text == "LEFT", (
        f"Неверный текст в левом frame. "
        f"Ожидалось: 'LEFT', Фактически: '{left_text}'"
    )

    right_text = frame_page.get_right_text()
    assert right_text == "RIGHT", (
        f"Неверный текст в правом frame. "
        f"Ожидалось: 'RIGHT', Фактически: '{right_text}'"
    )

    bottom_text = frame_page.get_bottom_text()
    assert bottom_text == "BOTTOM", (
        f"Неверный текст в нижнем frame. "
        f"Ожидалось: 'BOTTOM', Фактически: '{bottom_text}'"
    )

    middle_text = frame_page.get_middle_text()
    assert middle_text == "MIDDLE", (
        f"Неверный текст в центральном frame. "
        f"Ожидалось: 'MIDDLE', Фактически: '{middle_text}'"
    )


def test_dynamic_content(dynamic_page: DynamicContentPage, actions: PageActions):
    """
    1. Перейти по URL
    2. Обновлять страницу до тех пор, пока любые два изображения из трёх не совпадут
        Найдены два одинаковых изображения среди трёх
    """

    actions.goto(f"{URL}/dynamic_content")

    srcs = dynamic_page.wait_for_images_state()

    assert len(set(srcs)) < len(srcs), (
        f"Не найдены одинаковые изображения. "
        f"Полученные src: {srcs}"
    )


def test_scroll(infinite_scroll_page: InfiniteScrollPage, actions: PageActions):
    """
    1. Перейти по URL
    2. Прокручивать страницу вниз до тех пор, пока количество абзацев не станет ≥ 10
        Количество абзацев на странице ≥ 10
    """
    min_paragraphs = 10

    actions.goto(f"{URL}/infinite_scroll")

    count = infinite_scroll_page.scroll_until(target=min_paragraphs)

    assert count >= min_paragraphs, (
        f"Количество абзацев меньше ожидаемого. "
        f"Ожидалось: не менее 10, Фактически: {count}"
    )


def test_upload_image(upload_image_page: UploadImagePage, actions: PageActions):
    """
    1. Перейти по URL
    2. Загрузить файл на страницу
        Страница обновлена. На странице отображается текст: File Uploaded!
        Отображается имя загруженного файла
    """
    actions.goto(f"{URL}/upload")

    file_name = "test_image.png"
    file_path = Path("tests/files/test_image.png")

    upload_image_page.upload_file(file_path)

    message = upload_image_page.get_success_message()
    uploaded_file = upload_image_page.get_uploaded_file_name()

    assert message == "File Uploaded!", (
        f"Неверное сообщение после загрузки файла. "
        f"Ожидалось: 'File Uploaded!', "
        f"Фактически: '{message}'"
    )

    assert uploaded_file == file_name, (
        f"Неверное имя загруженного файла. "
        f"Ожидалось: '{file_name}', "
        f"Фактически: '{uploaded_file}'"
    )


def test_download(download_page: DownloadPage, actions: PageActions):
    """
    1. Перейти по URL страницы со списком файлов
    2. Получить имя третьего файла сверху
    3. Инициировать скачивание третьего файла сверху
    4. Проверить имя скачанного файла
        Имя скачанного файла равно имени, полученному на шаге 2
    """
    actions.goto(f"{URL}/download")

    file_index = 2

    expected_file_name = download_page.get_file_name(file_index)
    download = download_page.download_file(file_index)

    actual_file_name = Path(download.suggested_filename).name

    assert actual_file_name == expected_file_name, (
        f"Неверное имя скачанного файла. "
        f"Ожидалось: '{expected_file_name}', "
        f"Фактически: '{actual_file_name}'"
    )
