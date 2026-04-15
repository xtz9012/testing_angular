import pytest
import allure
from playwright.sync_api import Page
from webui_utilities.pages.form_page import FormPage


@allure.description("Verify that the Hero Form page loads successfully by checking for the form title")
def test_form_page_loads(form_page: Page):
    """Test that form page loads successfully."""
    with allure.step("Initialize form page object"):
        page_obj = FormPage(form_page)
    
    with allure.step("Verify form page is loaded"):
        assert page_obj.is_form_page_loaded()


@allure.description("Verify that the form has the correct title 'Hero Form'")
def test_form_has_title(form_page: Page):
    """Test that form has a title."""
    with allure.step("Initialize form page object"):
        page_obj = FormPage(form_page)
    
    with allure.step("Get form title"):
        title = page_obj.get_form_title()
    
    with allure.step("Verify title is present and contains 'Hero Form'"):
        assert title is not None
        assert "Hero Form" in title


@allure.description("Verify that form input fields can be filled successfully")
def test_fill_form_with_valid_data(form_page: Page):
    """Test filling form with valid data."""
    with allure.step("Initialize form page object"):
        page_obj = FormPage(form_page)
    
    with allure.step("Fill first name field with 'John'"):
        page_obj.fill_first_name("John")
    
    with allure.step("Fill last name field with 'Doe'"):
        page_obj.fill_last_name("Doe")
    
    form_page.wait_for_timeout(300)


@allure.description("Verify that the form can be submitted successfully")
def test_submit_form(form_page: Page):
    """Test form submission."""
    with allure.step("Initialize form page object"):
        page_obj = FormPage(form_page)
    
    with allure.step("Fill form with test data"):
        page_obj.fill_first_name("Jane")
        page_obj.fill_last_name("Smith")
    form_page.wait_for_timeout(300)
    
    with allure.step("Submit the form"):
        page_obj.submit_form()
    form_page.wait_for_timeout(1000)


@allure.description("Verify that individual form fields can be populated independently")
def test_form_individual_fields(form_page: Page):
    """Test filling individual form fields."""
    with allure.step("Initialize form page object"):
        page_obj = FormPage(form_page)
    
    with allure.step("Fill first name field with 'TestUser'"):
        page_obj.fill_first_name("TestUser")
    
    with allure.step("Fill last name field with 'TestLast'"):
        page_obj.fill_last_name("TestLast")
