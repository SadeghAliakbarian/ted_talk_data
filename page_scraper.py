
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

print urls


# crawling each talk
for url in urls:
    # details
    source = requests.get("https://" + url).text
    soup = BeautifulSoup(source, 'lxml')
    # url, title, view, location, data, summary, tags, speaker, speaker occupation, speaker introduction

    # transcript
    source = requests.get("https://" + url + '/transcript').text
    soup = BeautifulSoup(source, 'lxml')
    # transcript in multiple languages

    # further reading
    source = requests.get("https://" + url + '/reading-list').text
    soup = BeautifulSoup(source, 'lxml')
    # list of books

    # discussion
    source = requests.get("https://" + url + '/discussion').text
    soup = BeautifulSoup(source, 'lxml')
    # comments

