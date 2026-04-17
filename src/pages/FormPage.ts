import { Page } from '@playwright/test';
import { BasePage } from './BasePage';
import { config } from '../utils/config';

/**
 * Page Object for Form / Hero Form Page
 */
export class FormPage extends BasePage {
  // Selectors for form elements
  private readonly formTitle = 'h1, .form-title';
  private readonly nameInput = 'input[name="name"], input[placeholder*="Name"], #name';
  private readonly alterEgoInput = 'input[name="alterEgo"], input[placeholder*="Alter"], #alterEgo';
  private readonly heroPowerInput = 'input[name="heroPower"], input[placeholder*="Power"], #power';
  private readonly submitButton = 'button[type="submit"]';
  private readonly resetButton = 'button[type="reset"], button:has-text("New Hero")';
  private readonly formContainer = 'form, .form-container, [role="form"]';
  private readonly heroList = 'ul, .heroes, [role="list"]';

  constructor(page: Page) {
    super(page);
  }

  /**
   * Navigate to form page
   */
  async goto(): Promise<void> {
    await this.navigate(`${config.baseUrl}${config.formUrl}`);
  }

  /**
   * Check if form page is loaded
   */
  async isFormPageLoaded(): Promise<boolean> {
    return await this.isElementVisible(this.formContainer);
  }

  /**
   * Get form title
   */
  async getFormTitle(): Promise<string | null> {
    return await this.getText(this.formTitle);
  }

  /**
   * Fill name field
   */
  async fillName(name: string): Promise<void> {
    await this.fill(this.nameInput, name);
  }

  /**
   * Fill alter ego field
   */
  async fillAlterEgo(alterEgo: string): Promise<void> {
    await this.fill(this.alterEgoInput, alterEgo);
  }

  /**
   * Fill hero power field
   */
  async fillHeroPower(power: string): Promise<void> {
    await this.fill(this.heroPowerInput, power);
  }

  /**
   * Get name field value
   */
  async getNameValue(): Promise<string | null> {
    return await this.page.inputValue(this.nameInput);
  }

  /**
   * Get alter ego field value
   */
  async getAlterEgoValue(): Promise<string | null> {
    return await this.page.inputValue(this.alterEgoInput);
  }

  /**
   * Get hero power field value
   */
  async getHeroPowerValue(): Promise<string | null> {
    return await this.page.inputValue(this.heroPowerInput);
  }

  /**
   * Submit the form
   */
  async submitForm(): Promise<void> {
    await this.click(this.submitButton);
    // Wait for hero list to update after submission
    await this.page.locator(`${this.heroList} li, ${this.heroList} > *`).first().waitFor({ state: 'attached', timeout: config.defaultTimeout });
  }

  /**
   * Reset the form
   */
  async resetForm(): Promise<void> {
    await this.click(this.resetButton);
  }

  /**
   * Check if submit button is enabled
   */
  async isSubmitButtonEnabled(): Promise<boolean> {
    return await this.isElementEnabled(this.submitButton);
  }

  /**
   * Check if submit button is disabled
   */
  async isSubmitButtonDisabled(): Promise<boolean> {
    return await this.isElementDisabled(this.submitButton);
  }

  /**
   * Fill entire form with test data
   */
  async fillFormWithTestData(name: string, alterEgo: string, power: string): Promise<void> {
    await this.fillName(name);
    await this.fillAlterEgo(alterEgo);
    await this.fillHeroPower(power);
  }

  /**
   * Get hero list items count
   */
  async getHeroListCount(): Promise<number> {
    const count = await this.page.locator(`${this.heroList} li, ${this.heroList} > *`).count();
    return count;
  }

  /**
   * Get hero name from list
   */
  async getHeroNameFromList(index: number): Promise<string | null> {
    const items = this.page.locator(`${this.heroList} li, ${this.heroList} > *`);
    if (index < await items.count()) {
      return await items.nth(index).textContent();
    }
    return null;
  }
}
