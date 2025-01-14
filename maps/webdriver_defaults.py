import selenium.webdriver as webdriver

# Define a dictionary to map driver and options to workloads
WEBDRIVER_DEFAULTS = {
    'chrome': {
        'driver': webdriver.Chrome,
        'options': webdriver.ChromeOptions,
    },
    'chrome-canary': {
        'driver': webdriver.Chrome,
        'options': webdriver.ChromeOptions,
    },
    'chromium': {
        'driver': webdriver.Chrome,
        'options': webdriver.ChromeOptions
    },
    'safari': {
        'driver': webdriver.Safari,
        'options': webdriver.SafariOptions
    },
    'firefox': {
        'driver': webdriver.Firefox,
        'options': webdriver.FirefoxOptions
    },
    'edge': {
        'driver': webdriver.Edge,
        'options': webdriver.EdgeOptions
    }
    # Add more options and their corresponding drivers as needed
}