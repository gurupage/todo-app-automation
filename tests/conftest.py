# tests/conftest.py
import os
import pytest
import pytest_asyncio
from playwright.async_api import async_playwright
import datetime
from pytest_html import extras

# get a current time
now = datetime.datetime.now()
formatted_time = now.strftime("%Y%m%d_%H%M%S")  # format for file name
formatted_title_time = now.strftime("%Y-%m-%d %H:%M:%S")  # format for title of report

@pytest_asyncio.fixture
async def page():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)  # When headless=True, browser won't be shown
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await browser.close()

# config for file name
def pytest_configure(config):
    config.option.htmlpath = f"report_{formatted_time}.html"

# config for title of report
def pytest_html_report_title(report):
    report.title = f"My Test Report - {formatted_title_time}"

class ScreenshotHelper:
        def __init__(self, test_name, screenshot_dir="screenshots"):
                self.test_name = test_name
                self.screenshot_dir = screenshot_dir
                self.step = 1
                self.screenshots = [] #取得したスクリーンショットのパスを保存するリスト
                os.makedirs(screenshot_dir, exist_ok=True)
        
        async def capture(self, page, step_description="step"):
                filename = f"{self.test_name}_step{self.step:02d}_step{step_description}.png"
                path = os.path.join(self.screenshot_dir, filename)
                await page.screenshot(path=path)
                self.screenshots.append(path)
                self.step += 1


# fixtureを定義して、各テストでscreenshot_helperを利用できるようにする
@pytest.fixture
def screenshot_helper(request):
    helper = ScreenshotHelper(request.node.name)
    request.node.screenshot_helper = helper # テストノードにhelperを添付
    return helper

# pytest-html用のhookを定義し、テストレポートにスクリーンショットを追加
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    # テストの実行(call)フェーズが終了した後に実行
    if rep.when == "call":
        helper = getattr(item, "screenshot_helper", None)
        if helper and helper.screenshots:
            extra = getattr(rep, "extra", [])
            # 各スクリーンショットをレポートに追加
            for screenshot in helper.screenshots:
                extra.append(extras.image(screenshot, mime_type="image/png"))

            rep.extra = extra