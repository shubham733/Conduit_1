import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from pages.homepage import HomePage
from pages.userpage import UserPage

# @pytest.mark.parametrize("email, password", [("bunty.shelar619@gmail.com", "Bunty@123"),
# #                                              pytest.param("bunty.shelar", "XYZ", marks=pytest.mark.xfail),
# #                                              pytest.param("bunty.shelar619@gmail.com", "XYZ", marks=pytest.mark.xfail),
# #                                              pytest.param("bunty.shelar", "Bunty@123", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("email", ["bunty.shelar619@gmail.com",
                                   pytest.param("bunty.shelar", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("password", ["Bunty@123",
                                      pytest.param("XYZ", marks=pytest.mark.xfail)])
def test_sign_in_parameterize(set_up, email, password) -> None:
    page = set_up

    home_page = HomePage(page)
    user_page = UserPage(page)

    page.get_by_role("link", name="Sign in").click()
    page.get_by_placeholder("Email").fill(email)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_placeholder("Password").press("Enter")

    expect(user_page.my_profile_header).to_be_visible()
    expect(user_page.my_feed_header).to_be_visible()
