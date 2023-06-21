from playwright.sync_api import Playwright, sync_playwright, expect
from pages.homepage import HomePage
from pages.userpage import UserPage
from random_credentials import username, email
import pytest


@pytest.mark.integration
def test_sign_up(set_up) -> None:
    page = set_up

    home_page = HomePage(page)
    user_page = UserPage(page)
    page.get_by_role("link", name="Sign up").click()
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Email").fill(email)
    page.get_by_placeholder("Password").fill("new123")
    page.get_by_placeholder("Password").press("Enter")

    expect(user_page.random_profile_header).to_be_visible()
    expect(user_page.my_feed_header).to_be_visible()



@pytest.mark.regression
@pytest.mark.xfail(reason='URL Not Ready')
def test_sign_up_1(set_up) -> None:
    page = set_up

    home_page = HomePage(page)
    user_page = UserPage(page)
    page.get_by_role("link", name="Sign up").click()
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Email").fill(email)
    page.get_by_placeholder("Password").fill("new123")
    page.get_by_placeholder("Password").press("Enter")

    expect(user_page.random_profile_header).to_be_visible()
    expect(user_page.my_feed_header).to_be_visible()