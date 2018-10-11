from bs4 import BeautifulSoup
import csv
import requests
from datetime import datetime
import time
from tkinter import *
import tkinter as tk
import mytk


def WriteCSV(csvName):
    if os.path.exists(csvName):
        with open(csvName, 'w',newline='') as fp:
            a = csv.writer(fp,delimiter=',')
            data=['Paragraph','Link','DateTime']
            a.writerows(data)

def scrape(className,urlName,csvName,tagType):    
    f = csv.writer(open(csvName, 'w'))
    f.writerow(['Name', 'Link', 'Date'])
    pages = []
    pages.append(urlName)
    for item in pages:
        page = requests.get(item)
        soup = BeautifulSoup(page.text, 'html.parser')
    artist_name_list = soup.find(class_=className)
    artist_name_list_items = artist_name_list.find_all(tagType)

    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        links = 'https://web.archive.org' + artist_name.get('href')
        now = datetime.now()
        f.writerow([names, links, now])
