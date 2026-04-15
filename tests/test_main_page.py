import pytest
from playwright.sync_api import Page
from webui_utilities.pages.main_page import MainPage


def test_main_page_loads(main_page: Page):
    """Test that main page loads successfully."""
    page_obj = MainPage(main_page)
    assert page_obj.is_main_page_loaded()


def test_navigation_menu_visible(main_page: Page):
    """Test that navigation menu is visible."""
    page_obj = MainPage(main_page)
    is_nav_visible = page_obj.is_navigation_visible()
    assert is_nav_visible


def test_page_has_title(main_page: Page):
    """Test that main page has a title."""
    page_obj = MainPage(main_page)
    title = page_obj.get_page_title()
    assert title is not None


def test_can_navigate_to_form(main_page: Page):
    """Test that we can navigate to form page."""
    page_obj = MainPage(main_page)
    page_obj.click_jobs()
    main_page.wait_for_load_state("networkidle")
    assert "/form" in main_page.url


def test_can_navigate_to_stepper(main_page: Page):
    """Test that we can navigate to stepper page."""
    page_obj = MainPage(main_page)
    page_obj.click_stepper()
    main_page.wait_for_load_state("networkidle")
    assert "/stepper" in main_page.url


def test_can_navigate_back_to_welcome(main_page: Page):
    """Test that we can navigate back to welcome page."""
    page_obj = MainPage(main_page)
    page_obj.click_profile()
    main_page.wait_for_load_state("networkidle")
    assert main_page.url.endswith("/") or "?" in main_page.url or len(main_page.url.split("/").pop()) == 0
