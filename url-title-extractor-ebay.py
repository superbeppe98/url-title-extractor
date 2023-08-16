import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from html import unescape
import re
from inventree.api import InvenTreeAPI
from inventree.part import Part

# Load environment variables from .env file
load_dotenv()

# Specify the paths for input and output files
input_path = "url.txt"
output_path = "output.txt"

# Clear the contents of the input and output files
with open(input_path, "w"):
    pass
with open(output_path, "w"):
    pass

# Create an instance of the Inventree API
SERVER_ADDRESS = os.environ.get('INVENTREE_SERVER_ADDRESS')
MY_USERNAME = os.environ.get('INVENTREE_USERNAME')
MY_PASSWORD = os.environ.get('INVENTREE_PASSWORD')
api = InvenTreeAPI(SERVER_ADDRESS, username=MY_USERNAME,
                   password=MY_PASSWORD, timeout=3600)

try:
    # Request the list of parts through the API
    parts = Part.list(api)

    # Order the list of parts by IPN
    parts.sort(key=lambda x: x.IPN)

    # Write part links to the input file or empty lines if link is missing
    with open(input_path, 'a') as f:
        for part in parts:
            f.write(part.link + '\n' if part.link else '\n')
except Exception as e:
    print("An error occurred:", str(e))

# Initialize counters
total_count = 0
error_count = 0
extract_count = 0

# Loop over the lines in the input file
with open(input_path, "r") as f:
    for line in f:
        total_count += 1
        url = line.strip()

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('title').get_text()
        except Exception:
            with open(output_path, "a") as f_out:
                f_out.write(f"ERROR EXTRACT TITLE: {url}\n")
            extract_count += 1
            continue

        decoded_string = unescape(title)

        decoded_string = re.sub(r'\s*\|\s*eBay\s*$', '', decoded_string)

        if decoded_string == "Pagina errore":
            with open(output_path, "a") as f_out:
                f_out.write(f"ERROR LINK: {url}\n")
            error_count += 1
            continue

        with open(output_path, "a") as f_out:
            f_out.write(decoded_string + "\n")

# Print a summary of the results
print(f"Total URLs processed: {total_count}")
print(f"Errors encountered: {error_count}")
print(f"Extract encountered: {extract_count}")
