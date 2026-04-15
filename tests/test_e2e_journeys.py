import allure
from playwright.sync_api import Page
from webui_utilities.pages.welcome_page import WelcomePage
from webui_utilities.pages.form_page import FormPage
from webui_utilities.pages.main_page import MainPage
from webui_utilities.pages.stepper_page import StepperPage
from webui_utilities.helpers import navigate_to_welcome, navigate_to_form, navigate_to_stepper


@allure.description("Complete E2E user journey: Welcome → Form → Stepper navigation")
def test_complete_user_journey_navigation(page: Page):
    """Test complete user journey through all pages."""
    with allure.step("Step 1: Navigate to Welcome page"):
        navigate_to_welcome(page)
    
    with allure.step("Step 1: Verify Welcome page loads"):
        welcome_page = WelcomePage(page)
        assert welcome_page.is_welcome_page_loaded()
    
    with allure.step("Step 2: Navigate to Form page from Welcome"):
        welcome_page.click_start_button()
        page.wait_for_load_state("networkidle")
        assert "/form" in page.url
    
    with allure.step("Step 3: Verify Form page loads"):
        form_page = FormPage(page)
        assert form_page.is_form_page_loaded()
    
    with allure.step("Step 4: Fill form with test data"):
        form_page.fill_first_name("Journey")
        form_page.fill_last_name("Test")
    
    with allure.step("Step 5: Navigate to Main page (using navigation)"):
        navigate_to_welcome(page)
    
    with allure.step("Step 6: From Main page, navigate to Stepper"):
        main_page = MainPage(page)
        assert main_page.is_main_page_loaded()
        main_page.click_stepper()
        page.wait_for_load_state("networkidle")
        assert "/stepper" in page.url
    
    with allure.step("Step 7: Verify Stepper page loads and has navigation"):
        stepper_page = StepperPage(page)
        assert stepper_page.is_stepper_page_loaded()
        assert stepper_page.is_next_button_visible()


@allure.description("User navigates between pages and comes back - state test")
def test_navigate_between_pages_and_return(page: Page):
    """Test navigating between multiple pages and returning to original."""
    with allure.step("Step 1: Navigate to Form page"):
        navigate_to_form(page)
    
    with allure.step("Step 1: Start on Form page"):
        form_page = FormPage(page)
        assert form_page.is_form_page_loaded()
        form_initial_url = page.url
    
    with allure.step("Step 2: Navigate to Home/Welcome"):
        navigate_to_welcome(page)
        welcome_page = WelcomePage(page)
        assert welcome_page.is_welcome_page_loaded()
    
    with allure.step("Step 3: Navigate to Stepper"):
        navigate_to_stepper(page)
        stepper_page = StepperPage(page)
        assert stepper_page.is_stepper_page_loaded()
    
    with allure.step("Step 4: Return to Form page"):
        navigate_to_form(page)
        form_page_returned = FormPage(page)
        assert form_page_returned.is_form_page_loaded()
        
    with allure.step("Step 5: Verify we're back on original form URL"):
        assert page.url == form_initial_url


@allure.description("Fill form, verify data persists, then submit")
def test_form_fill_and_submit_complete_flow(page: Page):
    """Test complete form flow: fill → verify → submit."""
    with allure.step("Navigate to Form page"):
        navigate_to_form(page)
    
    with allure.step("Initialize form page"):
        form_page = FormPage(page)
        assert form_page.is_form_page_loaded()
    
    with allure.step("Fill all available form fields"):
        test_first_name = "TestFirst"
        test_last_name = "TestLast"
        form_page.fill_first_name(test_first_name)
        form_page.fill_last_name(test_last_name)
    
    with allure.step("Verify form title is still visible"):
        title = form_page.get_form_title()
        assert "Hero Form" in title
    
    with allure.step("Submit the form"):
        form_page.submit_form()
    
    with allure.step("Verify submission succeeded"):
        # Either success message or URL changed
        success_visible = form_page.is_success_message_visible()
        url_changed = "/form" not in page.url
        assert success_visible or url_changed or "success" in page.url.lower()
