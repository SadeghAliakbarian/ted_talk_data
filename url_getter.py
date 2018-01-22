
from bs4 import BeautifulSoup
import requests
import time


# crawler function
def crawler(page):

        talks = []

        grid_url_format = "https://www.ted.com/talks?page=" + str(page)
        source = requests.get(grid_url_format).text
        soup = BeautifulSoup(source, 'lxml')
        for item in soup.find_all('div', class_='media__message'):
            url = 'https://www.ted.com' + item.find('a', class_='ga-link')['href']
            speaker = item.find('h4', class_='h12 talk-link__speaker').text
            title = item.find('a', class_='ga-link').text.strip()
            date = item.find('span', class_='meta__val').text.strip()

            talks.append({'url': url, 'speaker': speaker, 'title': title, 'date': date})

        return talks


# getting talk urls
TED = {}
for page in range(1, 75):
        time.sleep(1)
        talks = crawler(page)
        time.sleep(2)
        TED[page] = talks
        print ("Done for page {}".format(page))


# filling missing urls/pages
for key, value in TED.items():
        if len(value) == 0:
                time.sleep(1)
                talks = crawler(page)
                TED[key] = talks
                print ("Done for page {} with len {}".format(key, len(talks)))


# writing the output
with open('output/ted_urls_rich.csv', 'w') as f:
        f.write('id,url,speaker,title,date\n')
        for key, value in TED.items():
                for item in value:
                        print value
                        print '\n\n'
                        f.write(str(key) + ',' +
                                        item['url'] + ',' +
                                        item['speaker'].encode('utf-8').strip() + ',' +
                                        item['title'].encode('utf-8').strip() + ',' +
                                        item['date'].encode('utf-8').strip() + '\n')

