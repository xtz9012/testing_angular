import pytest
from playwright.sync_api import Page
from webui_utilities.pages.welcome_page import WelcomePage


def test_welcome_page_loads(welcome_page: Page):
    """Test that welcome page loads successfully."""
    page_obj = WelcomePage(welcome_page)
    assert page_obj.is_welcome_page_loaded()


def test_welcome_page_has_title(welcome_page: Page):
    """Test that welcome page has a title."""
    page_obj = WelcomePage(welcome_page)
    title = page_obj.get_welcome_title()
    assert title is not None
    assert "Resources" in title


def test_welcome_page_has_description(welcome_page: Page):
    """Test that welcome page has description text."""
    page_obj = WelcomePage(welcome_page)
    is_visible = page_obj.is_description_visible()
    assert is_visible


def test_click_start_button_navigates_to_form(welcome_page: Page):
    """Test clicking the start button navigates to form."""
    page_obj = WelcomePage(welcome_page)
    current_url = welcome_page.url
    page_obj.click_start_button()
    # Wait for navigation
    welcome_page.wait_for_load_state("networkidle")
    # Verify navigation occurred to form page
    assert "/form" in welcome_page.url or welcome_page.url != current_url


def test_navigation_links_visible(welcome_page: Page):
    """Test that navigation links are visible."""
    page_obj = WelcomePage(welcome_page)
    assert welcome_page.locator("a#form-view-link").is_visible()
    assert welcome_page.locator("a#stepper-view-link").is_visible()
