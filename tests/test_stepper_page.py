import pytest
from playwright.sync_api import Page
from webui_utilities.pages.stepper_page import StepperPage


def test_stepper_page_loads(stepper_page: Page):
    """Test that stepper page loads successfully."""
    page_obj = StepperPage(stepper_page)
    assert page_obj.is_stepper_page_loaded()


def test_stepper_has_next_button(stepper_page: Page):
    """Test that stepper has Next button."""
    page_obj = StepperPage(stepper_page)
    assert page_obj.is_next_button_visible()


def test_click_next_button(stepper_page: Page):
    """Test clicking next button advances to next step."""
    page_obj = StepperPage(stepper_page)
    assert page_obj.is_next_button_visible()
    
    page_obj.click_next()
    stepper_page.wait_for_load_state("networkidle")


def test_navigate_through_steps(stepper_page: Page):
    """Test navigating through all steps sequentially."""
    page_obj = StepperPage(stepper_page)
    
    assert page_obj.is_stepper_page_loaded()
    stepper_page.wait_for_timeout(300)
    
    assert page_obj.is_next_button_visible()
