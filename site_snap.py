from webdriver_defaults import WEBDRIVER_DEFAULTS
from browser_path import BROWSER_PATH
from PIL import Image
import os
import time
from arguments import parse_arguments
import utils

def parse_screenshot(img_format,output_path,temp_screenshot):
    # Convert to desired format
    if img_format in ["jpg", "jpeg", "png"]:
        img = Image.open(temp_screenshot)
        if img_format == "jpg":
            output_path = output_path.replace(".png", ".jpg")
            img = img.convert("RGB")
        img.save(output_path, img_format)
    elif img_format == "pdf":
        img = Image.open(temp_screenshot)
        pdf_path = output_path.replace(".png", ".pdf")
        img.convert("RGB").save(pdf_path, "PDF", resolution=100.0)

    print(f"Screenshot saved in {output_path}")

def screeshot_website(args):
    # Lowercase the os and browser for quality of life
    host_os = utils.detect_os()
    if not host_os: return
    #args.browser = args.browser.lower()
    if not utils.setup_os(host_os): return
    if not utils.setup_browser(host_os, args.browser): return
    
    driver = utils.setup_webdriver(host_os, args.browser, args.get_bin, args.width, args.height)

    try:
        print(f'Started SiteSnap, args: {args}')

        # Open the URL
        driver.get(args.url)
        time.sleep(args.render_timer)  # Allow time for the page to fully render

        # Save screenshot as PNG
        temp_screenshot="temp_screenshot.png"
        
        driver.save_screenshot(temp_screenshot)

        parse_screenshot(args.format, args.output_path,temp_screenshot)
        
    
    finally:
        if os.path.exists(temp_screenshot):
            os.remove(temp_screenshot)
       
        driver.quit()
    
        #browser_version = utils.get_browser_version(host_os,args.browser)
        browser_version = driver.capabilities['browserVersion']
        print(f'SiteSnap completed successfully, args: {args}')

if __name__ == "__main__":
    args = parse_arguments()
    print(args.browser)
    screeshot_website(args)