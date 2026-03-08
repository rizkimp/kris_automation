from behave import when
from pages.login_page import LoginPage

@given(u'user is on the "E-submission" module')
def step_impl(context):
    context.dashboard_page.click_button_modul()
    context.dashboard_page.click_button_esubmission()

@when(u'user clicks "New Submission" and selects "For Approval"')
def step_impl(context):
    context.esubmission_page.click_button_new_submission()
    context.esubmission_page.click_button_submission()

@when(u'user fills all mandatory fields with valid data')
def step_impl(context):
    context.esubmission_page.fill_title()

@when(u'user uploads a valid pdf file as the main paper')
def step_impl(context):
    context.esubmission_page.upload_pdf()

@when(u'user uploads at least one attachment file')
def step_impl(context):
    context.esubmission_page.upload_file()

@when(u'user adds at least one folder from the "Recent" tab')
def step_impl(context):
    context.esubmission_page.click_button_add_folder()
    context.esubmission_page.check_box_recent_folder()
    context.esubmission_page.click_button_add_recent_folder()

@when(u'user adds "t2user5" as the action officer in routing type')
def step_impl(context):
    context.esubmission_page.click_button_step()
    context.esubmission_page.click_dropdown_approval_type()
    context.esubmission_page.select_for_approval()
    context.esubmission_page.fill_action_officer()
    context.esubmission_page.select_designation()
    context.esubmission_page.click_button_add_designation()

@when(u'user clicks the "Submit" button')
def step_impl(context):
    context.esubmission_page.click_button_submit()

@when(u'user confirms the submission in the confirmation popup')
def step_impl(context):
    context.esubmission_page.click_button_submit()

@then(u'the submission should be created successfully')
def step_impl(context):
    context.esubmission_page.contains_correct_display_message()
    context.esubmission_page.contains_correct_submission_title()
    context.esubmission_page.contains_correct_submission_id()

@when(u'user clicks the "Terminate" button')
def step_impl(context):
    context.esubmission_page.click_button_terminate()

@when(u'user enters a valid termination reason')
def step_impl(context):
    context.esubmission_page.fill_termination_reason()

@when(u'user confirms the termination')
def step_impl(context):
    context.esubmission_page.click_button_terminate()

@then(u'the submission should be terminated successfully')
def step_impl(context):
    context.esubmission_page.contains_correct_display_message()
    context.esubmission_page.contains_correct_submission_title()
    context.esubmission_page.contains_correct_submission_id()