from behave import given, when, then
from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD


@given('user opens login page')
def step_open_login(context):
    context.login_page = LoginPage(context.page)
    context.login_page.open_login_page()

@when('user enters valid username and password')
def step_input_login(context):
    context.login_page.input_username(USERNAME)
    context.login_page.input_password(PASSWORD)

@when('user clicks login button')
def step_click_login(context):
    context.login_page.click_login()

@then('user should see dashboard')
def step_verify_login(context):
    context.login_page.is_dashboard_visible()