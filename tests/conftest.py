# tests/conftest.py

import pytest_asyncio
from playwright.async_api import async_playwright
import datetime

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

