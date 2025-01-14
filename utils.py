from os_defaults import OS_NAMES
from browser_path import BROWSER_PATH
from webdriver_defaults import WEBDRIVER_DEFAULTS
from browser_version import BROWSER_VERSION
import sys
import subprocess

def detect_os():
    host_os = OS_NAMES[sys.platform]
    if host_os:
        print(f"Detected OS: {host_os}")
        return host_os
    else:
        print(f"Could not detect OS!")
        return False

def setup_os(host_os):
    if host_os in BROWSER_PATH:
        print("OS supports automation")
        return True
    else:
        print("Unsupported OS!")
        return False
    
def setup_browser(host_os, browser):
    if browser in BROWSER_PATH[host_os]:
        print("Browser supports automation")
        return True
    else:
        print("Unsupported browser!")
        return False

def find_browser_bin(host_os, browser):
    browser_path = BROWSER_PATH[host_os][browser]
    if browser_path:
        print(f"Browser bin: {browser_path}")
        return True
    else:
        print(f"Cannot find browser bin for {browser}")
        return False
    
def get_browser_version(os_type, browser):
    command = BROWSER_VERSION[os_type][browser]
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Error obtaining browser version: {e}")
        return None
    
def setup_webdriver(host_os, browser, get_bin,width,height):
    # To do: check and enable remote automation for safari on macOS
    options = WEBDRIVER_DEFAULTS[browser]['options']()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument(f"--window-size={width},{height}")
    options.add_argument("--hide-scrollbars")
    
    if get_bin:
        # Modify browser_path if you want to temporarily change the browser bin path, or do this in browser_defaults.py
        browser_path = BROWSER_PATH[host_os][browser]
        print(f"Browser bin path: {browser_path}")
        options.binary_location = browser_path
        # Code to work with the browser path
    else:
        # Handle the absence of the key
        print("Browser bin path not specified")
        browser_path = None  # or some default path
    return WEBDRIVER_DEFAULTS[browser]['driver'](options=options)