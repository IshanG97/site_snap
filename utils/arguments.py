import argparse

DEFAULT_ARG = {
    '--browser': 'chrome',
    '--url': 'https://www.gsmarena.com/oneplus_13r-13548.php',  # Fixed URL format
    '--format': 'png',
    '--width': 1920,
    '--height': 1080,
    '--render_timer': 2,
    '--get_bin': False,
}

def parse_arguments():
    parser = argparse.ArgumentParser(description='SiteSnap')

    # Add arguments with short options
    parser.add_argument('-b', '--browser', default=DEFAULT_ARG['--browser'], help='Target browser name, default: %(default)s')
    parser.add_argument('-u', '--url', default=DEFAULT_ARG['--url'], help='URL of the website being screenshot, default: %(default)s')
    parser.add_argument('-f', '--format', default=DEFAULT_ARG['--format'], help='Format to save the screenshot (png, jpg, or pdf), default: %(default)s')
    parser.add_argument('-w', '--width', type=int, default=DEFAULT_ARG['--width'], help='Width of the viewport, default: %(default)s')
    parser.add_argument('-ht', '--height', type=int, default=DEFAULT_ARG['--height'], help='Height of the viewport, default: %(default)s')
    parser.add_argument('-t', '--render_timer', type=int, default=DEFAULT_ARG['--render_timer'], help='Timer wait in seconds for website to render, default: %(default)s')
    parser.add_argument('-g', '--get_bin', action='store_true', help='Get browser binary location, default: %(default)s')

    args = parser.parse_args()
    
    # Convert all string arguments to lowercase
    lowercase_args = vars(args)
    lowercase_args = {key: (value.lower() if isinstance(value, str) else value) for key, value in lowercase_args.items()}
    
    return argparse.Namespace(**lowercase_args)  # Convert back to Namespace
