#!/bin/bash

# Setup script for Playwright with Chrome
# This script should be run inside the dev container

set -e

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Installing Playwright browsers (Chrome)..."
playwright install chrome

echo ""
echo "✅ Setup complete!"
echo ""
echo "You can now run the examples:"
echo "  python examples/01_hello_world.py"
echo "  python examples/02_form_filling.py"
echo "  python examples/03_reading_data.py"
echo "  python examples/04_clicking_buttons.py"
