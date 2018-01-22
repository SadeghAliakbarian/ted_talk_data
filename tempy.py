
from bs4 import BeautifulSoup
import requests
import time

# reading all urls to crawl
urls = []
with open('output/ted_urls.csv', 'r') as f:
    for line in f:
        url = line.split(',')[-1].split('\n')[0]
        if url != 'url':
            urls.append(url)


URL = urls[0]

source = requests.get("https://" + URL).text
soup = BeautifulSoup(source, 'lxml')


