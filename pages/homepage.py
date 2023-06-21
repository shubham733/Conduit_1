

class HomePage:
    def __init__(self, page):
        self.conduit_home = page.locator("app-header").get_by_role("link", name="conduit")
        self.global_feed = page.get_by_role("link", name="Global Feed")
        self.conduit_signin = page.get_by_role("link", name="Sign in")
        self.conduit_signup = page.get_by_role("link", name="Sign up")
        self.conduit_heading = page.get_by_role("heading", name="conduit")
        self.conduit_heading_description = page.get_by_text("A place to share your knowledge.")

