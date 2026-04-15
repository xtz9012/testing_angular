import allure
from .base_page import BasePage


class StepperPage(BasePage):
    """Page Object for Stepper/Multi-step form page."""

    # Selectors - updated for Material Stepper
    STEPPER_CONTAINER = "mat-stepper, .mat-stepper"
    STEP_1_HEADER = "button[type='button']:nth-of-type(1)"
    STEP_2_HEADER = "button[type='button']:nth-of-type(2)"
    STEP_3_HEADER = "button[type='button']:nth-of-type(3)"
    ACTIVE_STEP = ".mat-step-header-selected, [aria-selected='true']"
    NEXT_BUTTON = "button:has-text('Next')"
    PREVIOUS_BUTTON = ".mat-stepper-previous"
    FINISH_BUTTON = "button:has-text('Finish'), button:has-text('Submit')"
    STEP_CONTENT = ".mat-step-content"
    STEP_FORM = "form"

    def is_stepper_page_loaded(self) -> bool:
        """Verify stepper page is loaded."""
        with allure.step("Verify stepper page is loaded"):
            return self.is_element_visible(self.STEPPER_CONTAINER)

    def click_step_1(self):
        """Click on step 1 header."""
        with allure.step("Navigate to Step 1"):
            self.click(self.STEP_1_HEADER)

    def click_step_2(self):
        """Click on step 2 header."""
        with allure.step("Navigate to Step 2"):
            self.click(self.STEP_2_HEADER)

    def click_step_3(self):
        """Click on step 3 header."""
        with allure.step("Navigate to Step 3"):
            self.click(self.STEP_3_HEADER)

    def get_active_step(self) -> str:
        """Get currently active step."""
        with allure.step("Get currently active step"):
            try:
                return self.get_text(self.ACTIVE_STEP)
            except:
                return None

    def click_next(self):
        """Click next button."""
        with allure.step("Click next button to advance stepper"):
            self.click(self.NEXT_BUTTON)

    def click_previous(self):
        """Click previous button."""
        with allure.step("Click previous button to go back in stepper"):
            self.click(self.PREVIOUS_BUTTON)

    def click_finish(self):
        """Click finish button."""
        with allure.step("Click finish button to complete stepper"):
            self.click(self.FINISH_BUTTON)

    def is_next_button_visible(self) -> bool:
        """Check if next button is visible."""
        with allure.step("Verify next button is visible"):
            return self.is_element_visible(self.NEXT_BUTTON)

    def is_previous_button_visible(self) -> bool:
        """Check if previous button is visible."""
        with allure.step("Verify previous button is visible"):
            return self.is_element_visible(self.PREVIOUS_BUTTON)

    def is_finish_button_visible(self) -> bool:
        """Check if finish button is visible."""
        with allure.step("Verify finish button is visible"):
            return self.is_element_visible(self.FINISH_BUTTON)

    def navigate_to_step(self, step_number: int):
        """Navigate to specific step (1, 2, or 3)."""
        with allure.step(f"Navigate to step {step_number}"):
            if step_number == 1:
                self.click_step_1()
            elif step_number == 2:
                self.click_step_2()
            elif step_number == 3:
                self.click_step_3()
            self.page.wait_for_load_state("networkidle")
