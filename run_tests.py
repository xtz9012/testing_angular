#!/usr/bin/env python3
import subprocess
import sys
import os
import platform
import webbrowser
from pathlib import Path


def run_command(cmd, description=""):
    """Run a command and handle errors gracefully."""
    if description:
        print(f"\n{'='*50}")
        print(f"{description}")
        print(f"{'='*50}")
    
    try:
        result = subprocess.run(cmd, shell=True, check=False)
        return result.returncode == 0
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    """Main test runner."""
    print("\n" + "="*60)
    print("E2E Test Suite - Quick Runner")
    print("="*60)
    
    # Check if virtual environment exists
    venv_path = Path(".venv")
    if not venv_path.exists():
        print("\nVirtual environment not found!")
        print("Run './setup.sh' first to set up the environment")
        sys.exit(1)
    
    # Activate venv command based on OS
    if platform.system() == "Windows":
        activate_venv = ".venv\\Scripts\\activate.bat &&"
    else:
        activate_venv = "source .venv/bin/activate &&"
    
    # Clean old results
    print("\nCleaning up old test results...")
    run_command("rm -rf allure-results allure-report 2>/dev/null", "")
    
    # Run tests
    print("\nRunning pytest with Allure reporting...")
    test_passed = run_command(
        f"{activate_venv} pytest tests/ -v --alluredir=allure-results",
        "Test Execution"
    )
    
    if test_passed:
        print("\nAll tests passed!")
    else:
        print("\nSome tests may have failed - check output above")
    
    # Open Allure report
    print("\nGenerating Allure report...")
    report_opened = run_command(
        f"{activate_venv} allure serve allure-results --clean",
        "Opening Allure Report"
    )
    
    if not report_opened:
        print("\nCould not open Allure report automatically")
        print("Try: allure serve allure-results")
        print("Results are in: ./allure-results/")
    
    print("\n" + "="*60)
    print("Test run completed!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
