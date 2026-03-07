from locators.login_locator import LoginLocator
from playwright.sync_api import expect
from utils.config import BASE_URL


class LoginPage:

    def __init__(self, page):
        self.page = page

    def open_login_page(self):
        self.page.goto(BASE_URL)

    def input_username(self, username):
        self.page.fill(LoginLocator.input_username, username)

    def input_password(self, password):
        self.page.fill(LoginLocator.input_password, password)

    def click_login(self):
        self.page.click(LoginLocator.button_login)

    def is_dashboard_visible(self):
        expect(self.page.locator(LoginLocator.dashboard)).to_contain_text("Record Manager")