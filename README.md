# URL Title Extractor Ebay
URL Title Extractor Ebay is a Python program that extracts the titles of Ebay web pages from a file containing URLs. It uses the requests and BeautifulSoup libraries to extract the title, and then applies some text processing to remove the suffix "| eBay" and decode any HTML entities.

## Installation
To use URL Title Extractor Ebay, you need to have Python 3 installed on your system. The program also requires two dependencies, requests and BeautifulSoup, to be installed. You can install these dependencies by running the following command in your terminal or command prompt:
```shell
pip install -r requirements.txt
```

## Usage
To use URL Title Extractor Ebay, you need to provide a text file named "url.txt" that contains a list of URLs to extract the titles from. Once you have the file ready, you can run the program by navigating to the directory where the program is stored and running the following command:
```shell
$ python3 url_title_extractor.py

```
This will extract the titles from each URL in the file and output the results to a file named "output.txt". If there are any errors encountered during the extraction process, the program will output the URL with an "ERROR LINK" prefix to the output file.

After running the program, you can view the output file to see the extracted titles.
