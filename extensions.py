import os
import json
import collections
import csv
from tabulate import tabulate

def get_extension_name(extension_folder):
    manifest_file = os.path.join(extension_folder, 'manifest.json')
    try:
        with open(manifest_file, 'r') as file:
            data = json.load(file)
            return data.get('name', 'Name not found in manifest.json')
    except:
        return 'Error reading manifest.json'

def get_browser_extensions(browser):
    if browser.lower() == 'chrome':
        path = os.path.expanduser('~') + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\"
    elif browser.lower() == 'edge':
        path = os.path.expanduser('~') + "\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Extensions\\"
    else:
        return []

    if not os.path.exists(path):
        return []

    extensions = {}
    for folder_name in os.listdir(path):
        extension_path = os.path.join(path, folder_name)
        latest_version = sorted(os.listdir(extension_path))[-1]
        extension_folder = os.path.join(extension_path, latest_version)
        extension_name = get_extension_name(extension_folder)
        if "__MSG_" in extension_name:
            extension_name = "Localization placeholder detected. Human-readable name not available."
        extensions[folder_name] = extension_name

    return extensions

browsers = ['chrome', 'edge']

extension_data = collections.defaultdict(list)

for browser in browsers:
    extensions = get_browser_extensions(browser)
    for extension, name in extensions.items():
        extension_data[name].append(browser)

# Filter out entries with errors or localization placeholders
filtered_extension_data = {
    name: browsers 
    for name, browsers in extension_data.items() 
    if name != "Error reading manifest.json" and 
       name != "Localization placeholder detected. Human-readable name not available."
}

with open('extensions.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Extension', 'Browser'])
    for extension, browsers in filtered_extension_data.items():
        writer.writerow([extension, ', '.join(browsers)])

# Tabulate data for console output
table_data = [[extension, ', '.join(browsers)] for extension, browsers in filtered_extension_data.items()]
print(tabulate(table_data, headers=['Extension', 'Browser']))
