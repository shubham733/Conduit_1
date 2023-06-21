import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from pages.homepage import HomePage
from pages.userpage import UserPage


@pytest.mark.smoke
def test_sign_in(login_set_up) -> None:
    page = login_set_up

    home_page = HomePage(page)
    user_page = UserPage(page)

    expect(user_page.my_profile_header).to_be_visible()
    expect(user_page.my_feed_header).to_be_visible()
