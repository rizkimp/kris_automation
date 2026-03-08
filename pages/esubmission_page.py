from locators.esubmmission_locator import EsubmissionLocator
from locators.dashboard_locator import DashboardLocator
from playwright.sync_api import expect

class EsubmissionPage:
    def __init__(self, page):
        self.page = page

    def click_button_modul(self):
        self.page.click(DashboardLocator.button_modul)

    def click_button_esubmission(self):
        self.page.click(DashboardLocator.button_esubmission)

    def click_button_new_submission(self):
        self.page.click(EsubmissionLocator.button_new_submission)
        
    def click_button_new_submission(self):
        self.page.click(EsubmissionLocator.button_esubmission)    
        
    def fill_title(self):
        self.page.fill(EsubmissionLocator.input_title,"submission rizzz")

    def upload_pdf(self):
        self.page.set_input_files(EsubmissionLocator.upload_pdf, "files/document_rizz")
        
    def upload_file(self):
        self.page.locator(EsubmissionLocator.upload_file).set_input_files("files/doc")

    def click_button_add_folder(self):
        self.page.click(EsubmissionLocator.button_add_folder)

    def check_box_recent_folder(self):
        self.page.click(EsubmissionLocator.check_box_recent_folder)

    def click_button_add_recent_folder(self):
        self.page.click(EsubmissionLocator.button_add_recent_folder)

    def click_button_step(self):
        self.page.click(EsubmissionLocator.button_add_step)

    def click_dropdown_approval_type(self):
        self.page.click(EsubmissionLocator.dropdown_approval_type)

    def select_for_approval(self):
        self.page.click(EsubmissionLocator.select_for_approval)

    def fill_action_officer(self):
        self.page.locator(EsubmissionLocator.input_action_officer).fill(EsubmissionLocator.action_officer)

    def select_designation(self):
        self.page.get_by_text(EsubmissionLocator.select_designation).click()

    def click_button_add_designation(self):
        self.page.locator(EsubmissionLocator.button_add_designation).click()

    def click_button_submit(self):
        self.page.get_by_text(EsubmissionLocator.button_submit).click()

    def click_button_terminate(self):
        self.page.get_by_text(EsubmissionLocator.button_terminate).click()

    def fill_termination_reason(self):
        self.page.get_by_placeholder(EsubmissionLocator.termination_reason).fill("Automation terminate test")

    def contains_correct_display_message(self):
        self.page.locator("text=Terminated successfully").is_visible()

    def contains_correct_submission_title(self):
        self.page.locator("text=Automation Test Submission").is_visible()

    def contains_correct_submission_id(self):
        self.page.locator("text=Submission ID").is_visible()
        
    
    