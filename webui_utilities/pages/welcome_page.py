import allure
from .base_page import BasePage


class WelcomePage(BasePage):
    """Page Object for Welcome/Home page."""

    # Selectors - updated based on actual page structure
    WELCOME_TITLE = "h2:has-text('Resources')"
    START_BUTTON = "a#form-view-link"  # Form link
    GET_STARTED_BUTTON = "a#form-view-link"
    DESCRIPTION_TEXT = "h2:has-text('Next Steps')"

    def is_welcome_page_loaded(self) -> bool:
        """Verify welcome page is loaded."""
        with allure.step("Verify Welcome page is loaded"):
            return self.is_element_visible(self.WELCOME_TITLE)

    def get_welcome_title(self) -> str:
        """Get welcome page title."""
        with allure.step("Get welcome page title"):
            return self.get_text(self.WELCOME_TITLE)

    def click_start_button(self):
        """Click start/get started button - navigate to form."""
        with allure.step("Click start button to navigate to form"):
            try:
                self.click(self.START_BUTTON)
            except:
                self.click(self.GET_STARTED_BUTTON)

    def is_description_visible(self) -> bool:
        """Check if description text is visible."""
        with allure.step("Verify description text is visible"):
            return self.is_element_visible(self.DESCRIPTION_TEXT)
