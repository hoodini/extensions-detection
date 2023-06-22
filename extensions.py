import os
import json
import collections
import csv
import socket
from tabulate import tabulate

def get_localized_string(extension_folder, placeholder):
    key = placeholder[6:-2]
    locale_file = os.path.join(extension_folder, '_locales', 'en', 'messages.json')
    try:
        with open(locale_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data.get(key, {}).get('message', 'Localized string not found')
    except Exception as e:
        print(f"Error reading localization file: {e}")
        return 'Error reading localization file'

def get_extension_name_and_version(extension_folder):
    manifest_file = os.path.join(extension_folder, 'manifest.json')
    try:
        with open(manifest_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            name = data.get('name', 'Localization placeholder detected. Human-readable name not available.')
            version = data.get('version', 'Version not found in manifest.json')
            author = data.get('author', 'Author not found in manifest.json')
            default_title = data.get('browser_action', {}).get('default_title', 'Title not found in manifest.json')
            if "__MSG_" in name:
                name = get_localized_string(extension_folder, name)
            if "__MSG_" in default_title:
                default_title = get_localized_string(extension_folder, default_title)
            return name, version, author, default_title
    except Exception as e:
        print(f"Error reading manifest.json: {e}")
        return 'Error reading manifest.json', '', '', ''

def get_browser_extensions(browser):
    if browser.lower() == 'chrome':
        path = os.path.expanduser('~') + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\"
    elif browser.lower() == 'edge':
        path = os.path.expanduser('~') + "\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Extensions\\"
    else:
        return {}

    if not os.path.exists(path):
        return {}

    extensions = {}
    for folder_name in os.listdir(path):
        extension_path = os.path.join(path, folder_name)
        latest_version = sorted(os.listdir(extension_path))[-1]
        extension_folder = os.path.join(extension_path, latest_version)
        extension_name, extension_version, author, default_title = get_extension_name_and_version(extension_folder)
        extensions[folder_name] = [extension_name, extension_version, author, default_title]

    return extensions

browsers = ['chrome', 'edge']

extension_data = collections.defaultdict(list)

for browser in browsers:
    extensions = get_browser_extensions(browser)
    for extension_id, details in extensions.items():
        extension_data[extension_id].append(details + [browser])

username = os.getlogin()
hostname = socket.gethostname()

with open('extensions.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Username', 'Hostname', 'Extension ID', 'Extension', 'Version', 'Author', 'Title', 'Browser'])
    for extension_id, details_list in extension_data.items():
        for details in details_list:
            extension_name, extension_version, author, default_title, browser = details
            writer.writerow([username, hostname, extension_id, extension_name, extension_version, author, default_title, browser])

# Tabulate data for console output
table_data = [[username, hostname, extension_id, extension_name, version, author, default_title, browser] for extension_id, details_list in extension_data.items() for extension_name, version, author, default_title, browser in details_list]
print(tabulate(table_data, headers=['Username', 'Hostname', 'Extension ID', 'Extension', 'Version', 'Author', 'Title', 'Browser']))
