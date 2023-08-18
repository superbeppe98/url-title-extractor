# URL Title Extractor
URL Title Extractor is a Python program that extracts the titles of web pages from a file containing URLs. It uses the requests and BeautifulSoup libraries to extract the title and decode any HTML entities.

## Installation
To use URL Title Extractor, you need to have Python 3 installed on your system. The program also requires two dependencies, requests and BeautifulSoup, to be installed. You can install these dependencies by running the following command in your terminal or command prompt:
```shell
pip install -r requirements.txt
```

## Usage
Run the url-title-extractor.py script:

```shell
python3 url-title-extractor.py
```

The script will connect to the provided URLs, extract the titles of the web pages, and save them to an output file named output.txt.

Once the script completes, you can view the output.txt file to see the extracted titles and any error messages.

Note: If the script encounters errors while extracting titles, it will log these errors in the output.txt file.