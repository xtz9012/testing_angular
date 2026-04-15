import pytest
import allure
from playwright.sync_api import Page
from webui_utilities.pages.main_page import MainPage


@allure.description("Verify that the Main page loads successfully")
def test_main_page_loads(main_page: Page):
    """Test that main page loads successfully."""
    with allure.step("Initialize main page object"):
        page_obj = MainPage(main_page)
    
    with allure.step("Verify main page is loaded"):
        assert page_obj.is_main_page_loaded()


@allure.description("Verify that the navigation menu is visible on the main page")
def test_navigation_menu_visible(main_page: Page):
    """Test that navigation menu is visible."""
    with allure.step("Initialize main page object"):
        page_obj = MainPage(main_page)
    
    with allure.step("Check if navigation menu is visible"):
        is_nav_visible = page_obj.is_navigation_visible()
        assert is_nav_visible


@allure.description("Verify that the main page has a title")
def test_page_has_title(main_page: Page):
    """Test that main page has a title."""
    with allure.step("Initialize main page object"):
        page_obj = MainPage(main_page)
    
    with allure.step("Get page title"):
        title = page_obj.get_page_title()
    
    with allure.step("Verify title exists"):
        assert title is not None


@allure.description("Verify that navigation from main page to form page works")
def test_can_navigate_to_form(main_page: Page):
    """Test that we can navigate to form page."""
    with allure.step("Initialize main page object"):
        page_obj = MainPage(main_page)
    
    with allure.step("Click on form navigation link"):
        page_obj.click_jobs()
    
    with allure.step("Wait for form page to load"):
        main_page.wait_for_load_state("networkidle")
    
    with allure.step("Verify form page URL"):
        assert "/form" in main_page.url


@allure.description("Verify that navigation from main page to stepper page works")
def test_can_navigate_to_stepper(main_page: Page):
    """Test that we can navigate to stepper page."""
    with allure.step("Initialize main page object"):
        page_obj = MainPage(main_page)
    
    with allure.step("Click on stepper navigation link"):
        page_obj.click_stepper()
    
    with allure.step("Wait for stepper page to load"):
        main_page.wait_for_load_state("networkidle")
    
    with allure.step("Verify stepper page URL"):
        assert "/stepper" in main_page.url


@allure.description("Verify that navigation back to welcome page works")
def test_can_navigate_back_to_welcome(main_page: Page):
    """Test that we can navigate back to welcome page."""
    with allure.step("Initialize main page object"):
        page_obj = MainPage(main_page)
    
    with allure.step("Click on welcome navigation link"):
        page_obj.click_profile()
    
    with allure.step("Wait for welcome page to load"):
        main_page.wait_for_load_state("networkidle")
    
    with allure.step("Verify welcome/home page URL"):
        assert main_page.url.endswith("/") or "?" in main_page.url or len(main_page.url.split("/").pop()) == 0
