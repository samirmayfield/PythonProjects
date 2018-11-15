from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re
import csv
import my_tkinter
import os
 

def scrape(url_name, csv_name):
    # a queue of urls to be crawled
    new_urls = deque([url_name])
    # process urls one by one until we exhaust the queue
    while len(new_urls):


        # a set of urls that we have already crawled
        processed_urls = set()

        # a set of crawled emails
        

        # move next url from the queue to the set of processed urls
        url = new_urls.popleft()
        processed_urls.add(url)

        # extract base url to resolve relative links
        parts = urlsplit(url)
        base_url = "{0.scheme}://{0.netloc}".format(parts)
        path = url[:url.rfind('/')+1] if '/' in parts.path else url

        # get url's content
        if os.path.exists(csv_name):
            f = csv.writer(open(csv_name, 'a'))
            f.writerow([url])
        # else write new file name along with colum names for data
        else:
            f = csv.writer(open(csv_name, 'w'))
            f.writerow(["Links"])
            f.writerow([url])

        print("Processing %s" % url)
        try:
            response = requests.get(url)
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            # ignore pages with errors
            continue
     
        # extract all email addresses and add them into the resulting set
        # create a beutiful soup for the html document
        soup = BeautifulSoup(response.text)
##        new_emails = soup.find_all("[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I)
##        set(new_emails).update(new_emails, 'a')
        # write emails to csv file, must create index.csv at path location

     
        # find and process all the anchors in the document
        for anchor in soup.find_all("a"):
            # extract link url from the anchor
            link = anchor.attrs["href"] if "href" in anchor.attrs else ''
            # resolve relative links
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
            # add the new url to the queue if it was not enqueued nor processed yet
            if not link in new_urls and not link in processed_urls:
                new_urls.append(link)

