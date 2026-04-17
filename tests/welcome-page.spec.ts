import { test, expect } from '@playwright/test';
import { WelcomePage } from '../src/pages/WelcomePage';

test.describe('Welcome Page - Smoke Tests @smoke', () => {
  let welcomePage: WelcomePage;

  test.beforeEach(async ({ page }) => {
    welcomePage = new WelcomePage(page);
    await welcomePage.goto();
  });

  test('should load welcome page successfully', async ({ page }) => {
    expect(await welcomePage.isPageLoaded()).toBeTruthy();
  });

  test('should display page title', async () => {
    const title = await welcomePage.getPageTitle();
    expect(title).toBeTruthy();
  });

  test('should have navigation links to other pages', async () => {
    expect(await welcomePage.areNavigationLinksPresent()).toBeTruthy();
  });

  test('should display navigation with Form and Stepper links', async () => {
    const links = await welcomePage.getNavigationLinks();
    const linkTexts = links.join(' ').toLowerCase();
    expect(linkTexts).toContain('form');
    expect(linkTexts).toContain('stepper');
  });
});

test.describe('Welcome Page Navigation @regression', () => {
  let welcomePage: WelcomePage;

  test.beforeEach(async ({ page }) => {
    welcomePage = new WelcomePage(page);
    await welcomePage.goto();
  });

  test('should navigate to form page when form link clicked', async ({ page }) => {
    await welcomePage.navigateToForm();
    expect(page.url()).toContain('form');
  });

  test('should navigate to stepper page when stepper link clicked', async ({ page }) => {
    await welcomePage.navigateToStepper();
    expect(page.url()).toContain('stepper');
  });
});
