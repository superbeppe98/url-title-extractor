#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from html import unescape
import re

# Specify the path to the file containing URLs
path = "url.txt"

# Specify the output file name
output_file = "output.txt"

# Clear the contents of the output file
with open(output_file, "w") as f:
    f.write("")

# Initialize error count and total count to 0
error_count = 0
total_count = 0

# Loop over the lines in the file specified by path
with open(path, "r") as f:
    for line in f:
        total_count += 1
        url = line.strip()

        # Extract the title from the URL using requests and BeautifulSoup
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('title').get_text()
        except:
            with open(output_file, "a") as f:
                f.write(f"ERROR LINK: {url}\n")
            error_count += 1
            continue

        # Decode the title using unescape
        decoded_string = unescape(title)

        # Remove the "| eBay" suffix using regex
        decoded_string = re.sub(r'\s*\|\s*eBay\s*$', '', decoded_string)

        # Check if the decoded string is "Page Error", indicating an error
        if decoded_string == "Page Error":
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
