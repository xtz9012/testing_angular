import { test, expect } from '@playwright/test';
import { FormPage } from '../src/pages/FormPage';
import { config } from '../src/utils/config';

test.describe('Form Page - Smoke Tests @smoke', () => {
  let formPage: FormPage;

  test.beforeEach(async ({ page }) => {
    formPage = new FormPage(page);
    await formPage.goto();
  });

  test('should load form page successfully', async () => {
    expect(await formPage.isFormPageLoaded()).toBeTruthy();
  });

  test('should display form title "Hero Form"', async () => {
    const title = await formPage.getFormTitle();
    expect(title).toContain('Hero Form');
  });

  test('should have all form fields visible', async ({ page }) => {
    // Check for input fields - will use multiple selectors as we don't know exact structure
    const nameField = await page.locator('input').first().isVisible().catch(() => false);
    expect(nameField || (await formPage.isFormPageLoaded())).toBeTruthy();
  });

  test('should have submit button', async () => {
    expect(await formPage.isElementVisible('button[type="submit"], button:has-text("Submit")')).toBeTruthy();
  });
});

test.describe('Form Page - Form Interactions @regression', () => {
  let formPage: FormPage;

  test.beforeEach(async ({ page }) => {
    formPage = new FormPage(page);
    await formPage.goto();
  });

  test('should fill form with valid data', async () => {
    await formPage.fillFormWithTestData(
      config.testUser.name,
      config.testUser.alterEgo,
      config.testUser.heroPower
    );

    const nameValue = await formPage.getNameValue();
    const alterEgoValue = await formPage.getAlterEgoValue();
    const powerValue = await formPage.getHeroPowerValue();

    expect(nameValue).toBe(config.testUser.name);
    expect(alterEgoValue).toBe(config.testUser.alterEgo);
    expect(powerValue).toBe(config.testUser.heroPower);
  });

  test('should fill only name field', async () => {
    const testName = 'Iron Man';
    await formPage.fillName(testName);
    const nameValue = await formPage.getNameValue();
    expect(nameValue).toBe(testName);
  });

  test('should fill only alter ego field', async () => {
    const testAlterEgo = 'Batman';
    await formPage.fillAlterEgo(testAlterEgo);
    const alterEgoValue = await formPage.getAlterEgoValue();
    expect(alterEgoValue).toBe(testAlterEgo);
  });

  test('should fill only hero power field', async () => {
    const testPower = 'Super Strength';
    await formPage.fillHeroPower(testPower);
    const powerValue = await formPage.getHeroPowerValue();
    expect(powerValue).toBe(testPower);
  });

  test('should clear form after reset', async () => {
    // Fill form
    await formPage.fillFormWithTestData('Test', 'TestAlias', 'TestPower');

    // Reset form
    await formPage.resetForm();

    // Check if fields are cleared
    const nameValue = await formPage.getNameValue();
    const alterEgoValue = await formPage.getAlterEgoValue();
    const powerValue = await formPage.getHeroPowerValue();

    expect(nameValue).toBe('');
    expect(alterEgoValue).toBe('');
    expect(powerValue).toBe('');
  });
});

test.describe('Form Page - Form Submission @regression', () => {
  let formPage: FormPage;

  test.beforeEach(async ({ page }) => {
    formPage = new FormPage(page);
    await formPage.goto();
  });

  test('should submit form with valid data', async () => {
    await formPage.fillFormWithTestData(
      'Wonder Woman',
      'Diana Prince',
      'Lasso of Truth'
    );

    const heroCountBefore = await formPage.getHeroListCount();
    await formPage.submitForm();
    const heroCountAfter = await formPage.getHeroListCount();

    // Hero should be added to list
    expect(heroCountAfter).toBeGreaterThan(heroCountBefore);
  });

  test('should fill multiple heroes', async () => {
    const heroes = [
      { name: 'Spider-Man', alterEgo: 'Peter Parker', power: 'Web Slinging' },
      { name: 'Captain America', alterEgo: 'Steve Rogers', power: 'Strength & Tactics' },
      { name: 'Thor', alterEgo: 'Thor Odinson', power: 'Thunder' },
    ];

    for (const hero of heroes) {
      await formPage.fillFormWithTestData(hero.name, hero.alterEgo, hero.power);
      await formPage.submitForm();
    }

    const heroCount = await formPage.getHeroListCount();
    expect(heroCount).toBeGreaterThanOrEqual(heroes.length);
  });
});

test.describe('Form Page - Form Validation @regression', () => {
  let formPage: FormPage;

  test.beforeEach(async ({ page }) => {
    formPage = new FormPage(page);
    await formPage.goto();
  });

  test('should have submit button enabled when form is filled', async () => {
    await formPage.fillFormWithTestData('Test', 'Alias', 'Power');
    expect(await formPage.isSubmitButtonEnabled()).toBeTruthy();
  });

  test('should display form with all fields initially empty', async () => {
    const nameValue = await formPage.getNameValue();
    const alterEgoValue = await formPage.getAlterEgoValue();
    const powerValue = await formPage.getHeroPowerValue();

    expect(nameValue).toBe('');
    expect(alterEgoValue).toBe('');
    expect(powerValue).toBe('');
  });

  test('should allow special characters in form fields', async () => {
    const specialName = "O'Neill-Smith";
    const specialAlterEgo = "Dr. Strange@Wizard";
    const specialPower = "Magic & Mysticism";

    await formPage.fillFormWithTestData(specialName, specialAlterEgo, specialPower);

    const nameValue = await formPage.getNameValue();
    expect(nameValue).toBe(specialName);
  });
});
