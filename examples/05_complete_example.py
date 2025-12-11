"""
Complete Example - Combining All Concepts
This script demonstrates a complete workflow:
- Navigation
- Form filling
- Reading data
- Clicking and waiting
- Error handling
"""

from playwright.sync_api import sync_playwright, TimeoutError
import sys


def scrape_wikipedia_python():
    """Example: Scrape Python programming language page from Wikipedia"""
    
    with sync_playwright() as p:
        try:
            # Launch browser
            print("🚀 Launching Chrome browser...")
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                viewport={'width': 1920, 'height': 1080},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            )
            page = context.new_page()
            
            # Navigate to Wikipedia
            print("📄 Navigating to Wikipedia...")
            page.goto("https://www.wikipedia.org", wait_until="networkidle")
            
            # Search for "Python programming"
            print("🔍 Searching for 'Python programming'...")
            search_input = page.locator("#searchInput")
            search_input.fill("Python programming")
            search_input.press("Enter")
            
            # Wait for results page
            page.wait_for_load_state("networkidle")
            print(f"✅ Arrived at: {page.url}")
            
            # Extract information
            print("\n📊 Extracting information...")
            
            # Get page title
            title = page.title()
            print(f"Title: {title}")
            
            # Get the first paragraph
            first_paragraph = page.locator("#mw-content-text p").first
            if first_paragraph.count() > 0:
                paragraph_text = first_paragraph.text_content()
                print(f"\nFirst paragraph:\n{paragraph_text[:200]}...")
            
            # Get infobox data (if available)
            infobox = page.locator(".infobox")
            if infobox.count() > 0:
                print("\n📋 Infobox data found:")
                rows = infobox.locator("tr")
                count = min(5, rows.count())  # First 5 rows
                for i in range(count):
                    row = rows.nth(i)
                    text = row.text_content()
                    if text.strip():
                        print(f"  - {text.strip()[:80]}")
            
            # Click on "History" link if available
            print("\n🔗 Looking for navigation links...")
            toc = page.locator("#toc")
            if toc.count() > 0:
                toc_links = toc.locator("a")
                print(f"Found {toc_links.count()} table of contents links")
            
            # Take screenshots
            print("\n📸 Taking screenshots...")
            page.screenshot(path="wikipedia_full.png", full_page=True)
            print("✅ Full page screenshot saved: wikipedia_full.png")
            
            # Get all external links
            external_links = page.locator("a[href^='http']").all()
            print(f"\n🌐 Found {len(external_links)} external links")
            
            # Example: Navigate to a section
            history_link = page.locator("a:has-text('History')").first
            if history_link.count() > 0:
                print("\n📖 Navigating to History section...")
                history_link.click()
                page.wait_for_load_state("networkidle")
                
                # Take another screenshot
                page.screenshot(path="wikipedia_history.png")
                print("✅ Screenshot saved: wikipedia_history.png")
            
            # Close browser
            browser.close()
            print("\n✨ Complete! All operations finished successfully.")
            
        except TimeoutError as e:
            print(f"❌ Timeout error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Error occurred: {e}")
            sys.exit(1)


def main():
    """Run the complete example"""
    print("=" * 60)
    print("Complete Playwright Example - Wikipedia Scraping")
    print("=" * 60)
    print()
    
    scrape_wikipedia_python()


if __name__ == "__main__":
    main()
