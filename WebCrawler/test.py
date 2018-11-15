from selenium import webdriver
import requests; import re
from lxml.html import fromstring
from urllib.parse import urljoin

main_url = [
'http://advanta.in/',
'http://warnaengineeringworks.com/',
'http://unifrostindia.com/',
'http://www.superrefrigerations.com/',
'http://www.westernequipments.com/',
]

def search_item(driver,url):
    driver.get(url)
    tree = fromstring(driver.page_source)
    for item in tree.xpath("//a/@href"):
        if "contact us" in item.lower() or "about us" in item.lower() or "contact" in item.lower() or "about" in item.lower():
            get_item(urljoin(url,item))
            break

def get_item(link):
    response = requests.get(link).text
    try:
        email = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',response)[0]
    except: pass
    if email:
        print(link,email)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    try:
        for link in main_url:
            search_item(driver,link)
    finally:
        driver.quit()
