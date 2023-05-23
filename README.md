# Site Crawler
Site crawler is a python script which parses a html document and returns all the links within the page. 

Links can be filtered to only onsite links, and outputted to a CSV.

## Requirements
- Python 3.9.6
- OpenSSL 1.1
- Beautiful Soup 4
- Requests Library

## Usage
Run the script to print all links on the webpage to the terminal

```
python3 crawl.py crawl "https://example.com"
```

### Output all URLs to a CSV

```
python3 crawl.py crawl "https://example.com" --output
``` 
Using the `--output` flag will print all the links in the terminal and create crawl.csv in the root

### Limit to only onsite URLs

```
python3 crawl.py crawl "https://example.com" --onsite
``` 
Using the `--onsite` will ignore any URLs which do NOT contain the crawl URL, in this case if the link does not contain `http://example.com` the script will skip over this index.

### Chaining Options 
```
python3 crawl.py crawl "https://example.com" --output-onsite
``` 
Optional flags can be chained, seperated by a single hyphen. The options string must begin with 2 hyphens.