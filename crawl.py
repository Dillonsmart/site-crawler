#!/usr/bin/python3
import sys
import os
import io
import requests
from bs4 import BeautifulSoup

# Config
output_path = "crawl.csv"
output_csv = False
onsite_only = False
timeout = 5

# Set the request headers
headers = requests.utils.default_headers()
headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

def crawl( url ) : 
    
    # Download the html
    html = requests.get(url, headers, timeout = timeout)
    
    # Parse and prettify the html 
    soup = BeautifulSoup(html.content, 'html.parser')
    soup.prettify()
    
    links = get_anchors( soup )

    # Print each link to the console 
    for link in links :             

        # If link must be an onsite link
        if(onsite_only and url not in link and url ) :
            continue
        
        # If output True, write new line to CSV
        if( output_csv ) :
            write_to_csv( link )

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

# write to csv
def write_to_csv(line):
    f = open(output_path,'a')
    f.write(line + '\n')
    f.close()             

if __name__ == '__main__':
    if("output" in sys.argv[3]):
        output_csv=True

    if("onsite" in sys.argv[3]):
        onsite_only=True

    globals()[sys.argv[1]](sys.argv[2])