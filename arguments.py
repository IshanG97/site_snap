import argparse

DEFAULT_ARG = {
    '--browser' : 'chrome', 
    '--url':'www.google.com',
    '--output_path':'screenshots',
    '--format':'png',
    '--render_timer' : 2,
    '--skip_save':False,
    '--get_bin' : False,
}

def parse_arguments():
    parser = argparse.ArgumentParser(description='SiteSnap')

    # Add arguments with short options
    parser.add_argument('-b', '--browser', default=DEFAULT_ARG['--browser'], help='Target browser name, default: %(default)s')
    parser.add_argument('-u', '--url', default=DEFAULT_ARG['--url'], help='URL of the website being screenshot, default: %(default)s')
    parser.add_argument('-o', '--output_path', default=DEFAULT_ARG['--output_path'], help='Path to save the screenshot, default: %(default)s')
    parser.add_argument('-f', '--format', default=DEFAULT_ARG['--format'], help='Format to save the screenshot (png, jpg, or pdf), default: %(default)s')
    parser.add_argument('-w', '--width', default=DEFAULT_ARG['--width'], help='Width of the viewport, default: %(default)s')
    parser.add_argument('-h', '--height', default=DEFAULT_ARG['--height'], help='Height of the viewport, default: %(default)s')
    parser.add_argument('-t', '--render_timer', type=int, default=DEFAULT_ARG['--render_timer'], help='Timer wait in seconds for website to render, default: %(default)s')
    parser.add_argument('-s', '--skip_save', action='store_true', default=DEFAULT_ARG['--skip_save'], help='Skip saving images, default: %(default)s')
    parser.add_argument('-g', '--get_bin', action='store_true', help='Get browser binary location, default: %(default)s')

    return parser.parse_args()
