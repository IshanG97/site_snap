# Define a dictionary to map the workloads to their url and elements
OS_NAMES = {
    'darwin': 'macos',
    'win32' : 'windows',
    'linux': 'linux'
    }

OS_COMMANDS = {
    'macos': "open -a '%s' '%s'",
    'windows': "\"%s\" %s",
    'linux': "%s %s",
}