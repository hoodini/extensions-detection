# extensions-detection
This repository contains a Python script that scans a user's local machine to find installed extensions on Google Chrome and Microsoft Edge browsers. It outputs the findings in both the console, in a structured tabular format, and a CSV file.

# Browser Extension Scanner
This Python script scans the local machine to find installed extensions on Google Chrome and Microsoft Edge browsers. It prints a list of all installed extensions and their corresponding browser(s) in the console as well as saving this data to a CSV file.

# Requirements
To run this script, you need to have Python installed on your machine. The script has been tested with Python 3.8 and newer versions. You also need to have the tabulate Python package installed. You can install it using pip:

pip install tabulate
Usage
To run the script, navigate to the directory containing the script in a terminal and run:

python extension_scanner.py
Output
The script prints a table to the console that lists all installed extensions with the corresponding browser(s). It also writes this data to a CSV file named extensions.csv in the same directory. The table and the CSV file have the following format:

Extension|Browser
-------------------------------
Extension Name 1	chrome, edge
Extension Name 2	chrome
Extension Name 3	edge

Errors while reading the manifest.json file of an extension and entries with localization placeholders in the extension name are filtered out from the output.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
