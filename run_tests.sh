#!/bin/bash

# E2E Test Suite - Run Tests & Generate Allure Report
# This script runs all tests and automatically opens the Allure report

set -e  # Exit on error

echo "=========================================="
echo "E2E Test Suite - Running Tests"
echo "=========================================="
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Virtual environment not found"
    echo "Please run './setup.sh' first"
    exit 1
fi

# Activate virtual environment
source .venv/bin/activate

# Clean up old Allure results
echo "Cleaning up old test results..."
rm -rf allure-results/
rm -rf allure-report/
echo "Old test artifacts removed"

echo ""
echo "Running pytest tests with Allure reporting..."
echo ""

# Run tests with Allure reporting
if pytest tests/ -v --alluredir=allure-results; then
    echo ""
    echo "All tests passed!"
else
    echo ""
    echo "Some tests failed - check output above"
    echo "Generating report anyway..."
fi

echo ""
echo "Generating Allure report..."

# Generate and open Allure report
if command -v allure &> /dev/null; then
    allure serve allure-results --clean
else
    echo "Allure CLI not found, but results are in ./allure-results/"
    echo "Install allure via: brew install allure (macOS) or apt-get install allure (Linux)"
fi

echo ""
echo "=========================================="
echo "Test run completed!"
echo "=========================================="
