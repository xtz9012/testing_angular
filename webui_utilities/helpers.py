"""Navigation and utility helpers for E2E tests."""
import os
from playwright.sync_api import Page

# URL Constants
BASE_URL = os.getenv("BASE_URL", "https://angular-qa-recruitment-app.netlify.app/")
FORM_URL = f"{BASE_URL}form"
STEPPER_URL = f"{BASE_URL}stepper"
WELCOME_URL = BASE_URL


def navigate_to_form(page: Page) -> None:
    """Navigate to form page and wait for load."""
    page.goto(FORM_URL)
    page.wait_for_load_state("networkidle")


def navigate_to_stepper(page: Page) -> None:
    """Navigate to stepper page and wait for load."""
    page.goto(STEPPER_URL)
    page.wait_for_load_state("networkidle")


def navigate_to_welcome(page: Page) -> None:
    """Navigate to welcome page and wait for load."""
    page.goto(WELCOME_URL)
    page.wait_for_load_state("networkidle")
