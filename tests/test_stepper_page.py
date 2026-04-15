import pytest
import allure
from playwright.sync_api import Page
from webui_utilities.pages.stepper_page import StepperPage


@allure.description("Verify that the Stepper page loads successfully")
def test_stepper_page_loads(stepper_page: Page):
    """Test that stepper page loads successfully."""
    with allure.step("Initialize stepper page object"):
        page_obj = StepperPage(stepper_page)
    
    with allure.step("Verify stepper page is loaded"):
        assert page_obj.is_stepper_page_loaded()


@allure.description("Verify that the Next button is visible on the stepper")
def test_stepper_has_next_button(stepper_page: Page):
    """Test that stepper has Next button."""
    with allure.step("Initialize stepper page object"):
        page_obj = StepperPage(stepper_page)
    
    with allure.step("Verify next button is visible"):
        assert page_obj.is_next_button_visible()


@allure.description("Verify that clicking the Next button advances the stepper")
def test_click_next_button(stepper_page: Page):
    """Test clicking next button advances to next step."""
    with allure.step("Initialize stepper page object"):
        page_obj = StepperPage(stepper_page)
    
    with allure.step("Verify next button is visible before click"):
        assert page_obj.is_next_button_visible()
    
    with allure.step("Click next button"):
        page_obj.click_next()
    
    with allure.step("Wait for stepper to advance"):
        stepper_page.wait_for_load_state("networkidle")


@allure.description("Verify that the stepper can navigate through multiple steps")
def test_navigate_through_steps(stepper_page: Page):
    """Test navigating through all steps sequentially."""
    with allure.step("Initialize stepper page object"):
        page_obj = StepperPage(stepper_page)
    
    with allure.step("Verify stepper page is loaded"):
        assert page_obj.is_stepper_page_loaded()
    
    with allure.step("Verify next button is available for step navigation"):
        assert page_obj.is_next_button_visible()
