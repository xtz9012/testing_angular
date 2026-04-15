# E2E Test Suite - Angular Recruitment App webui

Used: Python, Playwrigh with POM and pytest

## Setup

### Prerequisites
- Python 3.8 or higher
- Bash shell (macOS, Linux) or Git Bash (Windows)

### One-Time Setup

Run the setup script to install dependencies:

```bash
chmod +x setup.sh
./setup.sh
```

This will:
- Create Python virtual environment
- Install testing dependencies (Playwright, pytest, Allure)
- Download Firefox browser for testing
- Create .env configuration file

## Running Tests

Execute tests with Allure report generation:

```bash
chmod +x run_tests.sh
./run_tests.sh
```

The test report will open automatically in your browser.

Alternative (manual execution):

```bash
source .venv/bin/activate
pytest tests/ -v --alluredir=allure-results
allure serve allure-results
```

## Test Coverage

The test suite contains 31 tests across 7 test files:

- test_welcome_page.py: 5 tests
- test_main_page.py: 6 tests
- test_form_page.py: 5 tests
- test_form_validation.py: 4 tests
- test_stepper_page.py: 4 tests
- test_stepper_advanced.py: 4 tests
- test_e2e_journeys.py: 3 tests


## Key Test Scenarios (E2E)

### 1. Complete User Journey: Welcome to Stepper
```
Welcome Page -> Click Start -> Form Page -> Navigate to Stepper Page
Verifies: All pages load correctly, navigation works, UI elements visible
```

### 2. Multi-Page Navigation with Return
```
Start on Form -> Go to Welcome -> Navigate to Stepper -> Return to Form
Verifies: Navigation between pages works, returning maintains URL consistency
```

### 3. Form Fill and Submit
```
Navigate to Form -> Fill first name and last name -> Submit form
Verifies: Form accepts input, submission succeeds or shows appropriate response
```

### 4. Form Validation
```
Submit empty form -> Verify validation error
Fill with valid data -> Submit -> Verify success
Test with special characters and long input -> Verify handling
Verifies: Input validation, special character handling, edge cases
```

### 5. Stepper Component Navigation
```
Navigate to Stepper -> Click Next -> Navigate through steps
Click Previous -> Go backward through steps
Verifies: Step navigation, next/previous buttons work, all steps accessible
```

## Project Structure

```
tests/
  conftest.py                 - Pytest configuration and fixtures
  test_welcome_page.py
  test_main_page.py
  test_form_page.py
  test_form_validation.py
  test_stepper_page.py
  test_stepper_advanced.py
  test_e2e_journeys.py

webui_utilities/
  helpers.py                  - URL constants and navigation helpers
  pages/
    base_page.py             - Base class for all page objects
    welcome_page.py
    form_page.py
    main_page.py
    stepper_page.py
```

## Common Commands

Run all tests:
```bash
pytest tests/ -v
```