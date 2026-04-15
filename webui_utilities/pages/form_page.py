import allure
from .base_page import BasePage


class FormPage(BasePage):
    """Page Object for Form page (Hero Form)."""

    # Selectors - updated based on actual page structure
    FORM_TITLE = "h1:has-text('Hero Form')"
    FIRST_NAME_INPUT = "input[name='name']"
    LAST_NAME_INPUT = "input[name='alterEgo']"
    POWER_SELECT = "select[name='power']"
    EMAIL_INPUT = "input[type='email']"
    PHONE_INPUT = "input[type='tel']"
    SUBMIT_BUTTON = "button:has-text('Submit')"
    NEW_HERO_BUTTON = "button:has-text('New Hero')"
    SUCCESS_MESSAGE = "h2:has-text('submitted')"
    ERROR_MESSAGE = ".error, .alert-danger, .form-error"

    def is_form_page_loaded(self) -> bool:
        """Verify form page is loaded."""
        with allure.step("Verify Hero Form page is loaded"):
            return self.is_element_visible(self.FORM_TITLE)

    def get_form_title(self) -> str:
        """Get form title."""
        with allure.step("Get form title"):
            return self.get_text(self.FORM_TITLE)

    def fill_first_name(self, name: str):
        """Fill first name field."""
        with allure.step(f"Fill first name with: {name}"):
            self.fill(self.FIRST_NAME_INPUT, name)

    def fill_last_name(self, name: str):
        """Fill last name/alter ego field."""
        with allure.step(f"Fill last name with: {name}"):
            self.fill(self.LAST_NAME_INPUT, name)

    def select_power(self, power: str):
        """Select a power from dropdown."""
        with allure.step(f"Select power: {power}"):
            self.select_option(self.POWER_SELECT, power)

    def fill_email(self, email: str):
        """Fill email field if present."""
        try:
            self.fill(self.EMAIL_INPUT, email)
        except:
            pass

    def fill_phone(self, phone: str):
        """Fill phone field if present."""
        try:
            self.fill(self.PHONE_INPUT, phone)
        except:
            pass

    def submit_form(self):
        """Submit the form."""
        with allure.step("Submit the form"):
            self.click(self.SUBMIT_BUTTON)

    def click_new_hero(self):
        """Click new hero button."""
        self.click(self.NEW_HERO_BUTTON)

    def is_success_message_visible(self) -> bool:
        """Check if success message is visible."""
        return self.is_element_visible(self.SUCCESS_MESSAGE)

    def get_success_message(self) -> str:
        """Get success message text."""
        return self.get_text(self.SUCCESS_MESSAGE)

    def is_error_message_visible(self) -> bool:
        """Check if error message is visible."""
        return self.is_element_visible(self.ERROR_MESSAGE)

    def get_error_message(self) -> str:
        """Get error message text."""
        return self.get_text(self.ERROR_MESSAGE)

    def fill_form_complete(self, first_name: str, last_name: str, power: str = "", email: str = "", phone: str = ""):
        """Fill complete form with all available fields."""
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        if power:
            self.select_power(power)
        if email:
            self.fill_email(email)
        if phone:
            self.fill_phone(phone)
