import { Page } from '@playwright/test';
import { BasePage } from './BasePage';
import { config } from '../utils/config';

/**
 * Page Object for Stepper Page
 */
export class StepperPage extends BasePage {
  // Selectors for stepper elements
  private readonly stepperContainer = '[role="tablist"], .stepper, .mat-stepper';
  private readonly stepLabel = '.mat-step-label, [role="tab"]';
  private readonly nameInput = 'input[aria-label*="name"], input[placeholder*="Name"], #name';
  private readonly addressInput = 'textarea[aria-label*="address"], input[aria-label*="address"], textarea, #address';
  private readonly nextButton = 'button:has-text("Next"), button[aria-label*="Next"]';
  private readonly previousButton = 'button:has-text("Previous"), button:has-text("Back")';
  private readonly doneButton = 'button:has-text("Done"), button[aria-label*="Done"]';
  private readonly finishButton = 'button:has-text("Finish")';
  private readonly stepContent = '.mat-step-content, [role="tabpanel"]';

  constructor(page: Page) {
    super(page);
  }

  /**
   * Navigate to stepper page
   */
  async goto(): Promise<void> {
    await this.navigate(`${config.baseUrl}${config.stepperUrl}`);
  }

  /**
   * Check if stepper page is loaded
   */
  async isStepperPageLoaded(): Promise<boolean> {
    return await this.isElementVisible(this.stepperContainer);
  }

  /**
   * Get number of steps
   */
  async getStepCount(): Promise<number> {
    return await this.page.locator(this.stepLabel).count();
  }

  /**
   * Get current step label
   */
  async getCurrentStepLabel(): Promise<string | null> {
    // Find the active step
    const activeStep = this.page.locator(`${this.stepLabel}[aria-selected="true"], ${this.stepLabel}.active`);
    return await activeStep.textContent();
  }

  /**
   * Fill name on first step
   */
  async fillName(name: string): Promise<void> {
    await this.fill(this.nameInput, name);
  }

  /**
   * Get name field value
   */
  async getNameValue(): Promise<string | null> {
    return await this.page.inputValue(this.nameInput);
  }

  /**
   * Fill address on second step
   */
  async fillAddress(address: string): Promise<void> {
    await this.fill(this.addressInput, address);
  }

  /**
   * Get address field value
   */
  async getAddressValue(): Promise<string | null> {
    try {
      return await this.page.inputValue(this.addressInput);
    } catch {
      return await this.getText(this.addressInput);
    }
  }

  /**
   * Click next button to go to next step
   */
  async clickNext(): Promise<void> {
    await this.click(this.nextButton);
    await this.page.waitForLoadState('domcontentloaded');
  }

  /**
   * Click previous button to go to previous step
   */
  async clickPrevious(): Promise<void> {
    // Try previous first, then back button
    try {
      await this.click(this.previousButton);
    } catch {
      // Button might not exist on first step
    }
    await this.page.waitForLoadState('domcontentloaded');
  }

  /**
   * Click done button (usually on last step)
   */
  async clickDone(): Promise<void> {
    const isDone = await this.isElementVisible(this.doneButton);
    if (isDone) {
      await this.click(this.doneButton);
      await this.page.waitForLoadState('domcontentloaded');
    }
  }

  /**
   * Click finish button
   */
  async clickFinish(): Promise<void> {
    await this.click(this.finishButton);
    await this.page.waitForLoadState('domcontentloaded');
  }

  /**
   * Complete entire stepper flow
   */
  async completeStepperFlow(name: string, address: string): Promise<void> {
    // Step 1: Name
    await this.fillName(name);
    await this.clickNext();

    // Step 2: Address
    await this.fillAddress(address);
    await this.clickNext();

    // Final step: Done
    await this.clickDone();
  }

  /**
   * Check if next button is enabled
   */
  async isNextButtonEnabled(): Promise<boolean> {
    return await this.isElementEnabled(this.nextButton);
  }

  /**
   * Check if previous button is visible
   */
  async isPreviousButtonVisible(): Promise<boolean> {
    return await this.isElementVisible(this.previousButton);
  }

  /**
   * Check if step is completed
   */
  async isStepCompleted(stepIndex: number): Promise<boolean> {
    const step = this.page.locator(`${this.stepLabel}`).nth(stepIndex);
    const ariaCompleted = await step.getAttribute('aria-completed');
    return ariaCompleted === 'true';
  }

  /**
   * Navigate to specific step
   */
  async goToStep(stepIndex: number): Promise<void> {
    const step = this.page.locator(`${this.stepLabel}`).nth(stepIndex);
    await step.click();
    await this.page.waitForLoadState('domcontentloaded');
  }
}
