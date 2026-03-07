from behave import when
from pages.login_page import LoginPage
from utils.config import USERNAME_APPROVER, PASSWORD_APPROVER

@when(u'user enters valid username and password as approver')
def step_impl(context):
    context.login_page.input_username(USERNAME_APPROVER)
    context.login_page.input_password(PASSWORD_APPROVER)