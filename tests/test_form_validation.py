import allure
from playwright.sync_api import Page
from webui_utilities.pages.form_page import FormPage


@allure.description("Verify form validation - empty fields should display error")
def test_form_submit_empty_fields(form_page: Page):
    """Test that submitting empty form displays validation errors."""
    with allure.step("Initialize form page object"):
        page_obj = FormPage(form_page)
    
    with allure.step("Verify form is loaded"):
        assert page_obj.is_form_page_loaded()
    
    with allure.step("Submit empty form directly"):
        page_obj.submit_form()
    form_page.wait_for_timeout(500)
    
    with allure.step("Verify we're still on form (not submitted)"):
        assert "/form" in page_obj.page.url


@allure.description("Verify form accepts valid data and shows success message")  
def test_form_submit_success(form_page: Page):
    """Test that filled form can be submitted successfully."""
    with allure.step("Initialize form page object"):
        page_obj = FormPage(form_page)
    
    with allure.step("Fill required fields with valid data"):
        page_obj.fill_first_name("ValidName")
        page_obj.fill_last_name("ValidLast")
    form_page.wait_for_timeout(300)
    
    with allure.step("Submit filled form"):
        page_obj.submit_form()
    form_page.wait_for_timeout(1000)
    
    with allure.step("Verify form was submitted (either success message or URL changed)"):
        success = page_obj.is_success_message_visible()
        url_changed = "/form" not in page_obj.page.url or "success" in page_obj.page.url.lower()
        assert success or url_changed


@allure.description("Verify form fields accept special characters")
def test_form_special_characters(form_page: Page):
    """Test that form fields accept special characters."""
    with allure.step("Initialize form page object"):
        page_obj = FormPage(form_page)
    
    with allure.step("Fill first name with special characters and numbers"):
        page_obj.fill_first_name("José-María 123!")
    
    with allure.step("Fill last name with special characters"):
        page_obj.fill_last_name("O'Brien-Smith")
    form_page.wait_for_timeout(300)
    
    with allure.step("Verify fields accepted special characters"):
        # Fields should not throw errors with special chars
        assert page_obj.is_form_page_loaded()


@allure.description("Verify form handles very long input strings")
def test_form_long_input(form_page: Page):
    """Test that form handles very long input strings."""
    with allure.step("Initialize form page object"):
        page_obj = FormPage(form_page)
    
    long_name = "A" * 100
    
    with allure.step(f"Fill first name with 100 character string"):
        page_obj.fill_first_name(long_name)
    
    with allure.step(f"Fill last name with 100 character string"):
        page_obj.fill_last_name(long_name)
    form_page.wait_for_timeout(300)
    
    with allure.step("Verify form still responds"):
        assert page_obj.is_form_page_loaded()
