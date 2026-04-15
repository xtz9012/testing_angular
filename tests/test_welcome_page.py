import pytest
import allure
from playwright.sync_api import Page
from webui_utilities.pages.welcome_page import WelcomePage


@allure.description("Verify that the Welcome page loads successfully")
def test_welcome_page_loads(welcome_page: Page):
    """Test that welcome page loads successfully."""
    with allure.step("Initialize welcome page object"):
        page_obj = WelcomePage(welcome_page)
    
    with allure.step("Verify welcome page is loaded"):
        assert page_obj.is_welcome_page_loaded()


@allure.description("Verify that the Welcome page has the correct title")
def test_welcome_page_has_title(welcome_page: Page):
    """Test that welcome page has a title."""
    with allure.step("Initialize welcome page object"):
        page_obj = WelcomePage(welcome_page)
    
    with allure.step("Get welcome page title"):
        title = page_obj.get_welcome_title()
    
    with allure.step("Verify title is present and contains 'Resources'"):
        assert title is not None
        assert "Resources" in title


@allure.description("Verify that the Welcome page displays description text")
def test_welcome_page_has_description(welcome_page: Page):
    """Test that welcome page has description text."""
    with allure.step("Initialize welcome page object"):
        page_obj = WelcomePage(welcome_page)
    
    with allure.step("Verify description is visible"):
        is_visible = page_obj.is_description_visible()
        assert is_visible


@allure.description("Verify that clicking the start button navigates to the Form page")
def test_click_start_button_navigates_to_form(welcome_page: Page):
    """Test clicking the start button navigates to form."""
    with allure.step("Initialize welcome page object"):
        page_obj = WelcomePage(welcome_page)
    
    with allure.step("Record current URL"):
        current_url = welcome_page.url
    
    with allure.step("Click start button"):
        page_obj.click_start_button()
    
    with allure.step("Wait for navigation"):
        welcome_page.wait_for_load_state("networkidle")
    
    with allure.step("Verify navigation to form page"):
        assert "/form" in welcome_page.url or welcome_page.url != current_url


@allure.description("Verify that navigation links to Form and Stepper pages are visible")
def test_navigation_links_visible(welcome_page: Page):
    """Test that navigation links are visible."""
    with allure.step("Initialize welcome page object"):
        page_obj = WelcomePage(welcome_page)
    
    with allure.step("Verify form navigation link is visible"):
        assert welcome_page.locator("a#form-view-link").is_visible()
    
    with allure.step("Verify stepper navigation link is visible"):
        assert welcome_page.locator("a#stepper-view-link").is_visible()
