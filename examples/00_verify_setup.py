"""
Verify Setup
This script verifies that Playwright is correctly installed and configured.
It doesn't require internet access.
"""

import sys


def verify_playwright():
    """Verify Playwright installation"""
    print("Checking Playwright installation...")
    
    try:
        import playwright
        print(f"✅ Playwright is installed")
    except ImportError:
        print("❌ Playwright is not installed")
        print("   Run: pip install -r requirements.txt")
        return False
    
    try:
        from playwright.sync_api import sync_playwright
        print("✅ Playwright sync API is available")
    except ImportError:
        print("❌ Could not import Playwright sync API")
        return False
    
    return True


def verify_browser():
    """Verify browser installation"""
    print("\nChecking browser installation...")
    
    try:
        from playwright.sync_api import sync_playwright
        
        with sync_playwright() as p:
            # Try to get browser executable path
            try:
                browser_type = p.chromium
                print("✅ Chrome/Chromium browser type is available")
                
                # Try to launch browser (will fail if not installed)
                try:
                    browser = browser_type.launch(headless=True)
                    browser.close()
                    print("✅ Chrome browser is installed and can be launched")
                    return True
                except Exception as e:
                    print(f"⚠️  Chrome browser is not installed or cannot be launched")
                    print(f"   Error: {str(e)[:100]}")
                    print("   Run: playwright install chrome")
                    return False
                    
            except Exception as e:
                print(f"❌ Error accessing browser: {e}")
                return False
                
    except Exception as e:
        print(f"❌ Error during browser check: {e}")
        return False


def verify_dependencies():
    """Verify system dependencies"""
    print("\nChecking system dependencies...")
    
    import os
    import subprocess
    
    # Check for required system libraries
    dependencies = [
        "libnss3",
        "libnspr4",
        "libatk1.0-0",
        "libatk-bridge2.0-0",
        "libcups2",
        "libdrm2",
        "libdbus-1-3",
        "libxkbcommon0",
        "libxcomposite1",
        "libxdamage1",
        "libxfixes3",
        "libxrandr2",
        "libgbm1",
        "libasound2"
    ]
    
    try:
        # Try to check if dpkg is available (Debian/Ubuntu systems)
        result = subprocess.run(
            ["dpkg", "-l"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        installed = result.stdout
        missing = []
        
        for dep in dependencies:
            if dep not in installed:
                missing.append(dep)
        
        if missing:
            print(f"⚠️  Some dependencies may be missing: {', '.join(missing[:3])}")
            print("   These are required for Chrome to run properly")
        else:
            print("✅ All required system dependencies appear to be installed")
            
    except Exception as e:
        print("⚠️  Could not verify system dependencies")
        print(f"   (This is normal on some systems)")
    
    return True


def main():
    """Run all verification checks"""
    print("=" * 60)
    print("Playwright Setup Verification")
    print("=" * 60)
    print()
    
    all_good = True
    
    # Check Playwright
    if not verify_playwright():
        all_good = False
    
    # Check browser
    if not verify_browser():
        all_good = False
    
    # Check dependencies
    verify_dependencies()
    
    print("\n" + "=" * 60)
    if all_good:
        print("✅ Setup verification complete - all checks passed!")
        print("\nYou can now run the example scripts:")
        print("  python examples/01_hello_world.py")
        print("  python examples/02_form_filling.py")
        print("  python examples/03_reading_data.py")
        print("  python examples/04_clicking_buttons.py")
        print("  python examples/05_complete_example.py")
    else:
        print("⚠️  Setup incomplete - please address the issues above")
        print("\nQuick fix:")
        print("  1. Install dependencies: pip install -r requirements.txt")
        print("  2. Install browsers: playwright install chrome")
    print("=" * 60)
    
    return 0 if all_good else 1


if __name__ == "__main__":
    sys.exit(main())
