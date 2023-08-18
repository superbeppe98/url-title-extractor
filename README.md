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

Run the url_title_extractor.py script:

```shell
python3 url_title_extractor.py
```

The script will connect to your InvenTree server using the provided credentials and fetch the part data. It will then sort the parts by their IPN and save the links to an input file named output.txt.

After the script has finished running, you can view the output.txt file to see the extracted links.

Please ensure that you have the correct access permissions to the InvenTree server and comply with the usage policies of the server.

Note: The script assumes that the Part class has been appropriately imported from the inventree module and that the link attribute exists for each part in the server's data.