"""
Form Filling Example
This script demonstrates how to:
- Fill in text fields
- Select options from dropdowns
- Check checkboxes
- Click submit buttons
"""

from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        # Launch Chrome browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Navigate to a form example page
        print("Navigating to test form...")
        page.goto("https://www.w3schools.com/html/html_forms.asp")
        
        # Wait for page to load
        page.wait_for_load_state("networkidle")
        
        # Find and interact with form elements
        # Note: This is a demonstration - the actual form may vary
        print("Page loaded successfully")
        
        # Example: Fill in a text input (if exists)
        if page.locator('input[type="text"]').count() > 0:
            first_input = page.locator('input[type="text"]').first
            first_input.fill("John Doe")
            print("Filled text input with 'John Doe'")
        
        # Get page title to verify we're on the right page
        title = page.title()
        print(f"Page title: {title}")
        
        # Take a screenshot
        page.screenshot(path="form_filling.png")
        print("Screenshot saved as form_filling.png")
        
        # Close browser
        browser.close()
        print("Done!")


if __name__ == "__main__":
    main()
