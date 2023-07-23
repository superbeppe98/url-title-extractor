#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from html import unescape
import re
import time
from inventree.api import InvenTreeAPI
from inventree.part import Part
from inventree.stock import StockItem

# Load environment variables from .env file
load_dotenv()

# Specify the path to the file containing URLs
path = "url.txt"

# Specify the output file name
output_file = "output.txt"

# Create the file if it doesn't exist
if not os.path.exists(path):
    with open(path, "w") as f:
        pass

# Clear the contents of the  input and output files
with open(path, "w") as f:
    pass
with open(output_file, "w") as f:
    pass

# Create an instance of the Inventree API
SERVER_ADDRESS = os.environ.get('INVENTREE_SERVER_ADDRESS')
MY_USERNAME = os.environ.get('INVENTREE_USERNAME')
MY_PASSWORD = os.environ.get('INVENTREE_PASSWORD')
api = InvenTreeAPI(SERVER_ADDRESS, username=MY_USERNAME,
                   password=MY_PASSWORD, timeout=3600)

# Request the input file thought api request with all parts
parts = Part.list(api)

# Order the list of parts by IPN
parts.sort(key=lambda x: x.IPN)

# Append all parts in the input file if the link is not empty, otherwise make the link ""
with open(path, 'a') as f:
    for part in parts:
        if part.link:
            f.write(part.link + '\n')
        else:
            f.write('\n')

# Initialize error count and total count to 0
total_count = 0
error_count = 0
extract_count = 0

# Loop over the lines in the file specified by path
with open(path, "r") as f:
    for line in f:
        total_count += 1
        url = line.strip()

        # Extract the title from the URL using requests and BeautifulSoup
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            #title = soup.find('title').get_text()
            # displaying the title
            for title in soup.find_all('title'):
                print(title.get_text())
        except:
            with open(output_file, "a") as f:
                f.write(f"ERROR EXTRACT TITLE: {url}\n")
            extract_count += 1
            continue

        # Decode the title using unescape
        decoded_string = unescape(title.get_text())

        # Remove the "| eBay" suffix using regex
        decoded_string = re.sub(r'\s*\|\s*eBay\s*$', '', decoded_string)

        # Check if the decoded string is "Page Error", indicating an error
        if decoded_string == "Pagina errore":
            with open(output_file, "a") as f:
                f.write(f"ERROR LINK: {url}\n")
            error_count += 1
            continue

        # If no error, append the decoded string to the output file
        with open(output_file, "a") as f:
            f.write(decoded_string + "\n")

# Print a summary of the results
print(f"Total URLs processed: {total_count}")
print(f"Errors encountered: {error_count}")
print(f"Extract encountered: {extract_count}")
