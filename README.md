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

### Output all URLs to a CSV

```
python3 crawl.py crawl "http://example.com" --output
``` 
Using the `--output` flag will print all the links in the terminal and create crawl.csv in the root

### Limit to only onsite URLs

```
python3 crawl.py crawl "http://example.com" --onsite
``` 
Using the `--onsite` will ignore any URLs which do NOT contain the crawl URL, in this case if the link does not contain `http://example.com` the script will skip over this index.

### Chaining Options 
```
python3 crawl.py crawl "http://example.com" --output-onsite
``` 
Optional flags can be chained, seperated by a single hyphen. The options string must begin with 2 hyphens.