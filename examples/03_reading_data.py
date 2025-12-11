"""
Reading Data Example
This script demonstrates how to:
- Extract text from elements
- Get attributes from elements
- Query multiple elements
- Extract structured data
"""

from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        # Launch Chrome browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Navigate to a page with structured content
        print("Navigating to example.com...")
        page.goto("https://example.com")
        
        # Wait for page to load
        page.wait_for_load_state("networkidle")
        
        # Read the page title
        title = page.title()
        print(f"\nPage Title: {title}")
        
        # Read the main heading
        heading = page.locator("h1").text_content()
        print(f"Main Heading: {heading}")
        
        # Read all paragraph texts
        paragraphs = page.locator("p").all_text_contents()
        print(f"\nFound {len(paragraphs)} paragraph(s):")
        for i, para in enumerate(paragraphs, 1):
            print(f"  {i}. {para.strip()}")
        
        # Get all links on the page
        links = page.locator("a").all()
        print(f"\nFound {len(links)} link(s):")
        for link in links:
            href = link.get_attribute("href")
            text = link.text_content()
            print(f"  - {text}: {href}")
        
        # Get meta information
        if page.locator('meta[name="viewport"]').count() > 0:
            viewport = page.locator('meta[name="viewport"]').get_attribute("content")
            print(f"\nViewport meta: {viewport}")
        
        # Take a screenshot
        page.screenshot(path="reading_data.png")
        print("\nScreenshot saved as reading_data.png")
        
        # Close browser
        browser.close()
        print("Done!")


if __name__ == "__main__":
    main()
