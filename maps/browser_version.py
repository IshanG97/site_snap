BROWSER_VERSION = {
    'macos': {
        'safari': "defaults read /Applications/Safari.app/Contents/Info CFBundleShortVersionString",
        'chrome': "/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome --version",
        'firefox': "/Applications/Firefox.app/Contents/MacOS/firefox --version",
        'edge': "/Applications/Microsoft\\ Edge.app/Contents/MacOS/Microsoft\\ Edge --version",
        'opera': "/Applications/Opera.app/Contents/MacOS/Opera --version",
    },
    'windows': {
        'chrome': "\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\" --version",
        'firefox': "\"C:\\Program Files\\Mozilla Firefox\\firefox.exe\" --version",
        'edge': "\"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe\" --version",
        'opera': "\"C:\\Program Files\\Opera\\launcher.exe\" --version",
        'internet_explorer': "\"C:\\Program Files\\internet explorer\\iexplore.exe\" --version",
    },
    'linux': {
        'chrome': "/usr/bin/google-chrome --version",
        'firefox': "/usr/bin/firefox --version",
        'opera': "/usr/bin/opera --version",
    }
}
