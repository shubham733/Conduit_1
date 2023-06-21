import os

import pytest
from playwright.sync_api import Playwright

# import utils.secret_config
PASSWORD = os.environ['PASSWORD']

@pytest.fixture(scope="function")
def set_up(page):
    # browser = playwright.chromium.launch(headless=False, slow_mo=400)
    # context = browser.new_context()
    # page = context.new_page()
    page.set_default_timeout(15000)
    page.goto("https://demo.realworld.io/#/")

    yield page
    page.close()

@pytest.fixture(scope="function")
def login_set_up(set_up):
    page = set_up
    # browser = playwright.chromium.launch(headless=False, slow_mo=400)
    # context = browser.new_context()
    # page = context.new_page()
    page.get_by_role("link", name="Sign in").click()
    page.get_by_placeholder("Email").fill("bunty.shelar619@gmail.com")
    page.get_by_placeholder("Password").fill(PASSWORD)
    page.get_by_placeholder("Password").press("Enter")

    yield page