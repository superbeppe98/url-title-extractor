# URL Title Extractor
URL Title Extractor is a Python program that extracts the titles of web pages from a file containing URLs. It uses the requests and BeautifulSoup libraries to extract the title, and then applies some text processing to remove the suffix "| eBay" and decode any HTML entities.

## Installation
To use URL Title Extractor, you need to have Python 3 installed on your system. The program also requires two dependencies, requests and BeautifulSoup, to be installed. You can install these dependencies by running the following command in your terminal or command prompt:
```shell
pip install -r requirements.txt
```

## Usage
To use URL Title Extractor, you need to provide a text file named "url.txt" that contains a list of URLs to extract the titles from. Once you have the file ready, you can run the program by navigating to the directory where the program is stored and running the following command:
```shell
$ python3 url_title_extractor.py

```
This will prompt you to enter the expiration date of the packaging in the format "dd-mm-yyyy". After entering the date, the program will display a table with the name, quantity, packaging, and purchase price of the products whose expiration date is later than the date you entered.

Here's an example output for the given sample:

```shell
Enter the expiration date of the packaging (format: dd-mm-yyyy): 01-01-2025
+----------------+------------+-----------------+----------------------+
| Nome Articolo  | Quantità   | Confezionamento | Prezzo di acquisto |
+================+============+=================+======================+
| 1111 | Test    | 9          | 01-01-2023      | 0.50                 |
+----------------+------------+-----------------+----------------------+
| 2222 | Test    | 1          | 01-01-2024      | 20.00                |
+----------------+------------+-----------------+----------------------+
| 3333 | Test    | 1          | 01-01-2024      | 34.50                |
+----------------+------------+-----------------+----------------------+
| 4444 | Test    | 2          | 01-01-2025      | 23.00                |
+----------------+------------+-----------------+----------------------+
```
This output shows the name, quantity, packaging, and purchase price of all the products whose expiration date is later than January 1, 2025.
