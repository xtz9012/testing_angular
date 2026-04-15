import allure
from .base_page import BasePage


class MainPage(BasePage):
    """Page Object for Main page."""

    # Selectors - updated based on actual page structure
    PAGE_HEADING = "h2"
    NAVIGATION_MENU = "a[id*='view-link']"
    LOGOUT_BUTTON = "button:has-text('Logout'), button:has-text('Sign Out')"
    PROFILE_LINK = "a#main-view-link"  # Welcome link
    JOBS_LINK = "a#form-view-link"  # Form link
    STEPPER_LINK = "a#stepper-view-link"

    def is_main_page_loaded(self) -> bool:
        """Verify main page is loaded."""
        with allure.step("Verify main page is loaded"):
            return self.is_element_visible(self.PAGE_HEADING)

    def get_page_title(self) -> str:
        """Get page heading."""
        with allure.step("Get page title"):
            return self.get_text(self.PAGE_HEADING)

    def is_navigation_visible(self) -> bool:
        """Check if navigation menu is visible."""
        with allure.step("Verify navigation menu is visible"):
            return self.is_element_visible(self.NAVIGATION_MENU)

    def click_logout(self):
        """Click logout button."""
        with allure.step("Click logout button"):
            self.click(self.LOGOUT_BUTTON)

    def click_profile(self):
        """Click profile link - navigate to Welcome page."""
        with allure.step("Navigate to Welcome page via profile link"):
            self.click(self.PROFILE_LINK)

    def click_jobs(self):
        """Click jobs/form link."""
        with allure.step("Navigate to Form page via jobs link"):
            self.click(self.JOBS_LINK)

    def click_stepper(self):
        """Click stepper link."""
        with allure.step("Navigate to Stepper page via stepper link"):
            self.click(self.STEPPER_LINK)

    def is_logout_button_visible(self) -> bool:
        """Check if logout button is visible."""
        with allure.step("Verify logout button is visible"):
            return self.is_element_visible(self.LOGOUT_BUTTON)
