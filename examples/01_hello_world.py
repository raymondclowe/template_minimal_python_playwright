"""
Basic Hello World Example
This script demonstrates the most basic Playwright usage:
- Launching a browser
- Navigating to a page
- Taking a screenshot
"""

from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        # Launch Chrome browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Navigate to a website
        print("Navigating to example.com...")
        page.goto("https://example.com")
        
        # Get the page title
        title = page.title()
        print(f"Page title: {title}")
        
        # Get the main heading text
        heading = page.locator("h1").text_content()
        print(f"Main heading: {heading}")
        
        # Take a screenshot
        page.screenshot(path="hello_world.png")
        print("Screenshot saved as hello_world.png")
        
        # Close browser
        browser.close()
        print("Done!")


if __name__ == "__main__":
    main()
