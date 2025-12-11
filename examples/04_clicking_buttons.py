"""
Clicking Buttons and Waiting Example
This script demonstrates how to:
- Click buttons and links
- Wait for navigation
- Wait for elements to appear
- Handle dynamic content
"""

from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        # Launch Chrome browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Navigate to example.com
        print("Navigating to example.com...")
        page.goto("https://example.com")
        
        # Wait for page to load
        page.wait_for_load_state("networkidle")
        print("Page loaded")
        
        # Get initial page title
        initial_title = page.title()
        print(f"Initial page title: {initial_title}")
        
        # Find and click a link (if available)
        links = page.locator("a")
        if links.count() > 0:
            link_text = links.first.text_content()
            link_href = links.first.get_attribute("href")
            print(f"\nClicking link: '{link_text}' -> {link_href}")
            
            # Click the link
            links.first.click()
            
            # Wait for navigation to complete
            page.wait_for_load_state("networkidle")
            
            # Get new page title
            new_title = page.title()
            print(f"New page title: {new_title}")
            print(f"Current URL: {page.url}")
            
            # Take a screenshot of the new page
            page.screenshot(path="after_click.png")
            print("Screenshot saved as after_click.png")
            
            # Go back to previous page
            print("\nGoing back...")
            page.go_back()
            page.wait_for_load_state("networkidle")
            
            back_title = page.title()
            print(f"Back to: {back_title}")
        else:
            print("No clickable links found on the page")
            page.screenshot(path="clicking_buttons.png")
            print("Screenshot saved as clicking_buttons.png")
        
        # Close browser
        browser.close()
        print("Done!")


if __name__ == "__main__":
    main()
