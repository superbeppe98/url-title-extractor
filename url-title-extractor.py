import os
import requests
from bs4 import BeautifulSoup

# Specify the paths for input and output files
input_path = "input.txt"
output_path = "output.txt"

# Create input file if it doesn't exist
if not os.path.exists(input_path):
    with open(input_path, "w") as f:
        pass

# Clear the contents of the output file
with open(output_path, "w"):
    pass

# Initialize counters
total_count = 0
extract_count = 0

# Loop over the lines in the input file
with open(input_path, "r") as f:
    for line in f:
        total_count += 1
        url = line.strip()

        # Add 'https://' if the URL doesn't have a scheme
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error if the request fails
            soup = BeautifulSoup(response.text, 'html.parser')
            title_tag = soup.find('title')

            if title_tag:
                title = title_tag.get_text()
            else:
                raise Exception("Title tag not found")

        except Exception as e:
            with open(output_path, "a") as f_out:
                f_out.write(f"ERROR EXTRACT TITLE: {url} - {str(e)}\n")
            extract_count += 1
            continue

        with open(output_path, "a") as f_out:
            f_out.write(title + "\n")

# Print a summary of the results
print(f"Total URLs processed: {total_count}")
print(f"Extract errors encountered: {extract_count}")
