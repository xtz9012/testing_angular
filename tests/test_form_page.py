import pytest
from playwright.sync_api import Page
from webui_utilities.pages.form_page import FormPage


def test_form_page_loads(form_page: Page):
    """Test that form page loads successfully."""
    page_obj = FormPage(form_page)
    assert page_obj.is_form_page_loaded()


def test_form_has_title(form_page: Page):
    """Test that form has a title."""
    page_obj = FormPage(form_page)
    title = page_obj.get_form_title()
    assert title is not None
    assert "Hero Form" in title


def test_fill_form_with_valid_data(form_page: Page):
    """Test filling form with valid data."""
    page_obj = FormPage(form_page)
    
    page_obj.fill_first_name("John")
    page_obj.fill_last_name("Doe")
    form_page.wait_for_timeout(300)


def test_submit_form(form_page: Page):
    """Test form submission."""
    page_obj = FormPage(form_page)
    
    page_obj.fill_first_name("Jane")
    page_obj.fill_last_name("Smith")
    form_page.wait_for_timeout(300)
    
    page_obj.submit_form()
    form_page.wait_for_timeout(1000)


def test_form_individual_fields(form_page: Page):
    """Test filling individual form fields."""
    page_obj = FormPage(form_page)
    
    page_obj.fill_first_name("TestUser")
    page_obj.fill_last_name("TestLast")
