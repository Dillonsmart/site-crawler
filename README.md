# Site Crawler
Site crawler is a python script which parses a html document and returns all the links within the page. 

## Installation

Clone or download the zip for this repo. You must have Python 3 installed on your machine for this script to work.

### Installing Beautiful Soup

```
sudo apt-get install python3-bs4
```
or
```
pip install beautifulsoup4
```

## Usage

Run the script to print all links on the webpage to the terminal

```
python3 crawl.py crawl "http://example.com"
```

Print all links to a csv 

```
python3 crawl.py crawl "http://example.com" --output
``` 
This will print all the links in the terminal and create crawl.csv in the root