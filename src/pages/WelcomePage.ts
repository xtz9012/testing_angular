import { Page } from '@playwright/test';
import { BasePage } from './BasePage';
import { config } from '../utils/config';

/**
 * Page Object for Welcome Page
 */
export class WelcomePage extends BasePage {
  // Selectors
  private readonly pageTitle = 'h1, h2';
  private readonly formLinkSelector = 'a[href*="form"]';
  private readonly stepperLinkSelector = 'a[href*="stepper"]';
  private readonly navLinks = 'nav a, [role="navigation"] a';

  constructor(page: Page) {
    super(page);
  }

  /**
   * Navigate to welcome page
   */
  async goto(): Promise<void> {
    await this.navigate(`${config.baseUrl}${config.welcomeUrl}`);
  }

  /**
   * Check if welcome page is loaded
   */
  async isPageLoaded(): Promise<boolean> {
    return await this.isElementVisible(this.pageTitle);
  }

  /**
   * Get page title/heading
   */
  async getPageTitle(): Promise<string | null> {
    return await this.getText(this.pageTitle);
  }

  /**
   * Navigate to form page
   */
  async navigateToForm(): Promise<void> {
    await this.click(this.formLinkSelector);
    await this.page.waitForLoadState('domcontentloaded');
  }

  /**
   * Navigate to stepper page
   */
  async navigateToStepper(): Promise<void> {
    await this.click(this.stepperLinkSelector);
    await this.page.waitForLoadState('domcontentloaded');
  }

  /**
   * Verify navigation links are present
   */
  async areNavigationLinksPresent(): Promise<boolean> {
    const count = await this.page.locator(this.navLinks).count();
    return count >= 2; // At least Form and Stepper links
  }

  /**
   * Get all navigation link texts
   */
  async getNavigationLinks(): Promise<string[]> {
    return await this.getAllText(this.navLinks);
  }
}
