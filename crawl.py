#!/usr/bin/python3
import sys
import os
import io
import requests
from bs4 import BeautifulSoup

# Set the request headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

def crawl( url ) : 
    
    # Download the html
    html = requests.get(url, headers)
    
    # Parse and prettify the html 
    soup = BeautifulSoup(html.content, 'html.parser')
    soup.prettify()
    
    links = get_anchors( soup )

    # Print each link to the console 
    for link in links : 
        print( link )

# Download the webpage
def download_html( url ) :
    return requests.get(url, headers)

# Get all anchor elements from the webpage
def get_anchors( soup ) : 

    page_anchors = []

    for link in soup.find_all('a'):

        # Check if the anchor element has a href attribute 
        if link.get('href') == None:
            continue

        # Store the href attribute value in the variable so we can use it  
        new_anchor = link.get('href')
        new_anchor = new_anchor.split('?')
        page_anchors.append(new_anchor[0])

    return page_anchors    

if __name__ == '__main__':
    globals()[sys.argv[1]](sys.argv[2])