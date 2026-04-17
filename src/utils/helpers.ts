import { Page } from '@playwright/test';
import { config } from './config';

/**
 * Navigate to a specific URL
 */
export async function navigateTo(page: Page, path: string): Promise<void> {
  await page.goto(`${config.baseUrl}${path}`);
  await page.waitForLoadState('networkidle');
}

/**
 * Navigate to form page
 */
export async function navigateToForm(page: Page): Promise<void> {
  await navigateTo(page, config.formUrl);
}

/**
 * Navigate to stepper page
 */
export async function navigateToStepper(page: Page): Promise<void> {
  await navigateTo(page, config.stepperUrl);
}

/**
 * Navigate to welcome page
 */
export async function navigateToWelcome(page: Page): Promise<void> {
  await navigateTo(page, config.welcomeUrl);
}

/**
 * Wait for element to be visible with custom timeout
 */
export async function waitForElement(
  page: Page,
  selector: string,
  timeout: number = config.elementWaitTimeout
): Promise<void> {
  await page.waitForSelector(selector, { timeout });
}

/**
 * Check if element exists
 */
export async function isElementVisible(page: Page, selector: string): Promise<boolean> {
  try {
    await page.waitForSelector(selector, { timeout: 1000 });
    return true;
  } catch {
    return false;
  }
}

/**
 * Get element text content
 */
export async function getElementText(page: Page, selector: string): Promise<string | null> {
  return await page.textContent(selector);
}

/**
 * Get element attribute value
 */
export async function getElementAttribute(
  page: Page,
  selector: string,
  attribute: string
): Promise<string | null> {
  return await page.getAttribute(selector, attribute);
}

/**
 * Fill input field
 */
export async function fillInput(
  page: Page,
  selector: string,
  value: string
): Promise<void> {
  await page.fill(selector, value);
}

/**
 * Click element
 */
export async function clickElement(page: Page, selector: string): Promise<void> {
  await page.click(selector);
}

/**
 * Take screenshot for debugging
 */
export async function takeScreenshot(page: Page, name: string): Promise<void> {
  await page.screenshot({ path: `./screenshots/${name}.png` });
}
