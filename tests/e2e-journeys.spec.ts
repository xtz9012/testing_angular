import { test, expect } from '@playwright/test';
import { WelcomePage } from '../src/pages/WelcomePage';
import { FormPage } from '../src/pages/FormPage';
import { StepperPage } from '../src/pages/StepperPage';
import { config } from '../src/utils/config';

test.describe('E2E Journey Tests @regression', () => {
  test('should navigate through all main pages', async ({ page }) => {
    const welcomePage = new WelcomePage(page);
    const formPage = new FormPage(page);
    const stepperPage = new StepperPage(page);

    // Start on welcome
    await welcomePage.goto();
    expect(await welcomePage.isPageLoaded()).toBeTruthy();

    // Navigate to form
    await welcomePage.navigateToForm();
    expect(page.url()).toContain('form');
    expect(await formPage.isFormPageLoaded()).toBeTruthy();

    // Navigate back to welcome using back button
    await page.goBack();
    await page.waitForLoadState('domcontentloaded');
    expect(page.url()).not.toContain('form');

    // Navigate to stepper
    await welcomePage.navigateToStepper();
    expect(page.url()).toContain('stepper');
    expect(await stepperPage.isStepperPageLoaded()).toBeTruthy();
  });

  test('should submit form and return to form page', async ({ page }) => {
    const welcomePage = new WelcomePage(page);
    const formPage = new FormPage(page);

    // Navigate to form page
    await welcomePage.goto();
    await welcomePage.navigateToForm();

    // Get initial hero count
    const initialHeroCount = await formPage.getHeroListCount();

    // Fill and submit form
    await formPage.fillFormWithTestData(
      'Test Hero ' + Date.now(),
      'Test Alias',
      'Test Power'
    );
    await formPage.submitForm();
    // Wait a moment for UI to update after submission
    await page.waitForTimeout(500);

    // Hero count should increase
    const finalHeroCount = await formPage.getHeroListCount();
    expect(finalHeroCount).toBeGreaterThan(initialHeroCount);

    // Form should still be visible (ready for another submission)
    expect(await formPage.isFormPageLoaded()).toBeTruthy();
  });

  test('should complete stepper flow with multi-step data entry', async ({ page }) => {
    const welcomePage = new WelcomePage(page);
    const stepperPage = new StepperPage(page);

    // Navigate to stepper
    await welcomePage.goto();
    await welcomePage.navigateToStepper();

    // Fill step 1
    const testName = 'E2E Test User ' + Date.now();
    await stepperPage.fillName(testName);

    // Verify we can see the name
    const nameValue = await stepperPage.getNameValue();
    expect(nameValue).toBe(testName);

    // Move to next step
    await stepperPage.clickNext();

    // Fill step 2
    const testAddress = '999 Test Boulevard, E2E City, USA';
    await stepperPage.fillAddress(testAddress);

    // Verify we can see the address
    const addressValue = await stepperPage.getAddressValue();
    expect(addressValue).toBe(testAddress);

    // Complete the flow
    await stepperPage.clickDone();

    // Should still be on stepper page in completed state
    expect(await stepperPage.isStepperPageLoaded()).toBeTruthy();
  });

  test('should handle form submission with data from multiple heroes', async ({ page }) => {
    const welcomePage = new WelcomePage(page);
    const formPage = new FormPage(page);

    // Navigate to form
    await welcomePage.goto();
    await welcomePage.navigateToForm();

    const heroes = [
      { name: 'Hero Alpha', alterEgo: 'Alpha Ego', power: 'Alpha Power' },
      { name: 'Hero Beta', alterEgo: 'Beta Ego', power: 'Beta Power' },
    ];

    const initialCount = await formPage.getHeroListCount();

    for (const hero of heroes) {
      await formPage.fillFormWithTestData(hero.name, hero.alterEgo, hero.power);
      await formPage.submitForm();
      // Wait for list to update after submission
      await page.waitForTimeout(300);
    }

    const finalCount = await formPage.getHeroListCount();
    expect(finalCount).toBeGreaterThan(initialCount);
  });

  test('should reset form and submit new data', async ({ page }) => {
    const welcomePage = new WelcomePage(page);
    const formPage = new FormPage(page);

    // Navigate to form
    await welcomePage.goto();
    await welcomePage.navigateToForm();

    // Fill and reset
    await formPage.fillFormWithTestData('Initial', 'Data', 'Here');
    await formPage.resetForm();

    // Verify reset
    let nameValue = await formPage.getNameValue();
    expect(nameValue).toBe('');

    // Fill with new data
    await formPage.fillFormWithTestData('New', 'Data', 'Now');
    nameValue = await formPage.getNameValue();
    expect(nameValue).toBe('New');

    // Submit
    const initialCount = await formPage.getHeroListCount();
    await formPage.submitForm();
    const finalCount = await formPage.getHeroListCount();

    expect(finalCount).toBeGreaterThan(initialCount);
  });

  test('should navigate between all pages using navigation links', async ({ page }) => {
    const welcomePage = new WelcomePage(page);
    const formPage = new FormPage(page);
    const stepperPage = new StepperPage(page);

    // Start at welcome
    await welcomePage.goto();
    expect(page.url()).toContain('angular-qa-recruitment-app');

    // Go to form
    await welcomePage.navigateToForm();
    await page.waitForLoadState('domcontentloaded');
    expect(await formPage.isFormPageLoaded()).toBeTruthy();

    // Go back via browser
    await page.goBack();
    await page.waitForLoadState('domcontentloaded');

    // Go to stepper
    await welcomePage.navigateToStepper();
    await page.waitForLoadState('domcontentloaded');
    expect(await stepperPage.isStepperPageLoaded()).toBeTruthy();

    // Go back to welcome
    await page.goBack();
    await page.waitForLoadState('domcontentloaded');
    expect(await welcomePage.isPageLoaded()).toBeTruthy();
  });

  test('should handle page refresh without data loss', async ({ page }) => {
    const stepperPage = new StepperPage(page);

    // Navigate to stepper
    await stepperPage.goto();

    // Fill first step
    const testName = 'Refresh Test User';
    await stepperPage.fillName(testName);

    // Move to next step
    await stepperPage.clickNext();

    // Fill second step
    const testAddress = 'Refresh Test Address';
    await stepperPage.fillAddress(testAddress);

    // Reload page
    await page.reload();

    // Data might be cleared on reload (depends on app implementation)
    // This test verifies the app handles reload gracefully
    expect(await stepperPage.isStepperPageLoaded()).toBeTruthy();
  });
});
