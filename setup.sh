#!/bin/bash

# E2E Test Suite Setup Script
# This script sets up Python virtual environment and installs all dependencies

set -e  # Exit on error

echo "=========================================="
echo "E2E Test Suite - Environment Setup"
echo "=========================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "Python $PYTHON_VERSION detected"
echo ""

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    echo "Virtual environment created"
else
    echo "Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip --quiet

# Install requirements
if [ -f "python_requirements.txt" ]; then
    echo "Installing dependencies from python_requirements.txt..."
    pip install -r python_requirements.txt --quiet
    echo "Dependencies installed"
else
    echo "Error: python_requirements.txt not found"
    exit 1
fi

# Install Playwright browsers
echo ""
echo "Installing Playwright browsers..."
playwright install firefox --quiet
echo "Playwright browsers installed"

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo ""
    echo "Creating .env file with default configuration..."
    cat > .env << EOF
BASE_URL=https://angular-qa-recruitment-app.netlify.app/
HEADLESS=true
EOF
    echo ".env file created"
else
    echo ".env file already exists"
fi

echo ""
echo "=========================================="
echo "Setup completed successfully!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. To run tests:        ./run_tests.sh"
echo "2. Or manually:         source .venv/bin/activate && pytest tests/ -v"
echo ""
