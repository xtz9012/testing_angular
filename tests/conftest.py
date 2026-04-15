import pytest
import os
from dotenv import load_dotenv
from playwright.sync_api import Page, Browser

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://angular-qa-recruitment-app.netlify.app/")


@pytest.fixture
def page(browser: Browser) -> Page:
    """Create a page and navigate to base URL."""
    page = browser.new_page()
    page.goto(BASE_URL)
    yield page
    page.close()


@pytest.fixture
def form_page(page: Page) -> Page:
    """Navigate to form page and wait for load."""
    page.goto("https://angular-qa-recruitment-app.netlify.app/form")
    page.wait_for_load_state("networkidle")
    yield page


@pytest.fixture
def stepper_page(page: Page) -> Page:
    """Navigate to stepper page and wait for load."""
    page.goto("https://angular-qa-recruitment-app.netlify.app/stepper")
    page.wait_for_load_state("networkidle")
    yield page


@pytest.fixture
def welcome_page(page: Page) -> Page:
    """Ensure on welcome page and wait for load."""
    page.wait_for_load_state("networkidle")
    yield page


@pytest.fixture
def main_page(page: Page) -> Page:
    """Ensure on main page and wait for load."""
    page.wait_for_load_state("networkidle")
    yield page
