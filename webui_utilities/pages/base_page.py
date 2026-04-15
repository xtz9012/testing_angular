import allure
from playwright.sync_api import Page
from typing import Optional


class BasePage:
    """Base class for all page objects."""

    def __init__(self, page: Page):
        self.page = page

    def wait_for_element(self, selector: str, timeout: int = 3000):
        """Wait for an element to be visible."""
        with allure.step(f"Wait for element with selector: {selector}"):
            self.page.wait_for_selector(selector, timeout=timeout)

    def click(self, selector: str):
        """Click on an element."""
        with allure.step(f"Click element: {selector}"):
            self.page.click(selector)

    def fill(self, selector: str, text: str):
        """Fill text input."""
        with allure.step(f"Fill field: {selector} with text: {text}"):
            self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        """Get text from an element."""
        with allure.step(f"Get text from element: {selector}"):
            return self.page.text_content(selector)

    def is_element_visible(self, selector: str) -> bool:
        """Check if element is visible."""
        try:
            self.page.wait_for_selector(selector, timeout=1000)
            return True
        except:
            return False

    def get_attribute(self, selector: str, attr: str) -> Optional[str]:
        """Get element attribute."""
        with allure.step(f"Get attribute '{attr}' from element: {selector}"):
            return self.page.get_attribute(selector, attr)

    def select_option(self, selector: str, value: str):
        """Select option from dropdown."""
        with allure.step(f"Select option '{value}' from dropdown: {selector}"):
            self.page.select_option(selector, value)

    def take_screenshot(self, name: str):
        """Take a screenshot."""
        with allure.step(f"Take screenshot: {name}"):
            self.page.screenshot(path=f"screenshots/{name}.png")
