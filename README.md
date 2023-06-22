# Browser Extension Data Extractor (for Windows, if using other OS the paths should be modified accordingly)

This Python script collects data on all installed extensions in Chrome and Edge browsers for a given user on a machine. The script specifically extracts the following data:

- Extension ID
- Extension Name
- Version
- Author
- Default Title
- Browser (Chrome or Edge)

The script outputs this data in two formats:

1. A CSV file named `extensions.csv` saved in the same directory as the script.
2. A printed tabular output in the console.

## Requirements

- Python 3.6 or higher
- [tabulate](https://pypi.org/project/tabulate/)

## Installation

1. Clone this repository to your local machine.
2. Install the necessary Python packages by running `pip install -r requirements.txt` in your terminal.

## Usage

1. Navigate to the repository directory in your terminal.
2. Run the script by typing `python extensions.py`.
3. Check the generated `extensions.csv` file in the same directory, or observe the tabular output in your console.

## Disclaimer

This script is created for demonstration and educational purposes. It doesn't collect or send any data elsewhere. Please use responsibly and ensure you have necessary permissions to run this on any machine.
