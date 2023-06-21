from random_credentials import username, email


class UserPage:
    def __init__(self, page):
        self.my_feed_header = page.locator("text='Your Feed'")
        self.my_profile_header = page.locator("text='Bunty.123'")
        self.random_profile_header = page.locator(f"text='{username}'")