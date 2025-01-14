from PIL import Image
import os
import time
from utils.arguments import parse_arguments
import utils.setup as setup

def save_screenshot(img_format, output_path, temp_screenshot):
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    # Convert to desired format
    if img_format in ["jpg", "jpeg", "png"]:
        img = Image.open(temp_screenshot)
        if img_format == "jpg":
            output_path = output_path.replace(".png", ".jpg")
            img = img.convert("RGB")
        print(output_path)
        img.save(output_path)
    elif img_format == "pdf":
        img = Image.open(temp_screenshot)
        pdf_path = output_path.replace(".png", ".pdf")
        img.convert("RGB").save(pdf_path, "PDF", resolution=100.0)

    print(f"Screenshot saved in {output_path}")

def screeshot_website(args):
    host_os = setup.detect_os()
    if not host_os: return
    if not setup.setup_os(host_os): return
    if not setup.setup_browser(host_os, args.browser): return
    
    driver = setup.setup_webdriver(host_os, args.browser, args.get_bin, args.width, args.height)

    try:
        print(f'Started SiteSnap, args: {args}')

        # Open the URL
        driver.get(args.url)
        time.sleep(args.render_timer)  # Allow time for the page to fully render

        # Setup browser before taking a screenshot
        setup.bypass_cookie_popup(driver)
        driver.set_window_size(args.width, driver.execute_script("return document.body.scrollHeight"))

        # Save temp screenshot as PNG
        temp_screenshot="temp_screenshot.png"
        driver.save_screenshot(temp_screenshot)
        
        # Build the output path
        browser_version = driver.capabilities['browserVersion']
        #browser_version = utils.get_browser_version(host_os,args.browser)
        screenshots_path = "screenshots"
        output_path = f'{screenshots_path}/{args.browser}_{browser_version}.{args.format}'

        # Parse the captured screenshot and save into the output path
        save_screenshot(img_format=args.format, output_path=output_path,temp_screenshot=temp_screenshot)
    
    finally:
        if os.path.exists(temp_screenshot):
            os.remove(temp_screenshot)
       
        driver.quit()
        
        print(f'SiteSnap completed successfully, args: {args}')

if __name__ == "__main__":
    args = parse_arguments()
    print(args.browser)
    screeshot_website(args)