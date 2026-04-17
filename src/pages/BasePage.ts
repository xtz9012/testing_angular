import { Page, expect } from '@playwright/test';
import { config } from '../utils/config';

/**
 * Base Page Object Model class for all pages
 * Provides common methods for interacting with web elements
 */
export class BasePage {
  constructor(protected page: Page) {}

  /**
   * Navigate to a URL
   */
  async navigate(url: string): Promise<void> {
    await this.page.goto(url, { waitUntil: 'domcontentloaded' });
  }

  /**
   * Wait for element to be visible
   */
  async waitForElement(selector: string, timeout: number = config.elementWaitTimeout): Promise<void> {
    await this.page.waitForSelector(selector, { timeout });
  }

  /**
   * Click on element
   */
  async click(selector: string): Promise<void> {
    await this.page.locator(selector).click();
  }

  /**
   * Fill text input or select element
   */
  async fill(selector: string, text: string): Promise<void> {
    const element = this.page.locator(selector);
    const tagName = await element.evaluate((el) => el.tagName.toLowerCase());
    
    if (tagName === 'select') {
      await element.selectOption(text);
    } else {
      await element.fill(text);
    }
  }

  /**
   * Get text content of element
   */
  async getText(selector: string): Promise<string | null> {
    return await this.page.textContent(selector);
  }

  /**
   * Get attribute value of element
   */
  async getAttribute(selector: string, attribute: string): Promise<string | null> {
    return await this.page.getAttribute(selector, attribute);
  }

  /**
   * Check if element is visible
   */
  async isElementVisible(selector: string): Promise<boolean> {
    try {
      await this.page.waitForSelector(selector, { timeout: config.elementWaitTimeout });
      return true;
    } catch {
      return false;
    }
  }

  /**
   * Check if element is hidden
   */
  async isElementHidden(selector: string): Promise<boolean> {
    try {
      await this.page.waitForSelector(selector, { state: 'hidden', timeout: config.elementWaitTimeout });
      return true;
    } catch {
      return false;
    }
  }

  /**
   * Get all text content from elements matching selector
   */
  async getAllText(selector: string): Promise<string[]> {
    return await this.page.locator(selector).allTextContents();
  }

  /**
   * Select option from dropdown
   */
  async selectOption(selector: string, value: string): Promise<void> {
    await this.page.selectOption(selector, value);
  }

  /**
   * Check element is enabled
   */
  async isElementEnabled(selector: string): Promise<boolean> {
    return await this.page.locator(selector).isEnabled();
  }

  /**
   * Check element is disabled
   */
  async isElementDisabled(selector: string): Promise<boolean> {
    return !(await this.isElementEnabled(selector));
  }

  /**
   * Hover over element
   */
  async hover(selector: string): Promise<void> {
    await this.page.hover(selector);
  }

  /**
   * Get page title
   */
  async getPageTitle(): Promise<string> {
    return await this.page.title();
  }

  /**
   * Get current URL
   */
  async getCurrentUrl(): Promise<string> {
    return this.page.url();
  }

  /**
   * Wait for navigation
   */
  async waitForNavigation(): Promise<void> {
    await this.page.waitForNavigation({ timeout: config.navigationTimeout });
  }

  /**
   * Reload page
   */
  async reloadPage(): Promise<void> {
    await this.page.reload();
  }
}
