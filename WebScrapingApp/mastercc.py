import os
import sys
import numpy as np
from bs4 import BeautifulSoup
import django
import csv
import time
import requests
from datetime import datetime
from tkinter import *
import tkinter as tk
import mytk



###############################################################################################################################################################################
##
## ##numpy array attributes##
##
### Example of numpy arrays : Each array has attributes ndim
### (the number of dimensions), shape (the size of each dimension),
### and size (the total size of the array)
##
##
##a = np.array([1, 2, 3, 4, 5]) #1 dimensional array
##b = np.array([[1,2],[3,4], [5,6]]) #2 dimensional array
##c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]]) #3 dimensional array
##print(a)
##print(b)
##print(c)
##
### Convert numpy array to list
##
##a_list = a.tolist()
##print(a_list)
##
### parse index of list to var
##index0 = a_list[0]
##print(index0)
#############################################################################################################################################################################
##
#### Export to CSV file
##with open('index.csv', 'a') as csv_file:    
##    writer = csv.writer(csv_file)
####    writer.writerow([names, datetime.now()])
##
##
##
##
############################################################################################################################################################################
##
##
##    
##
##
### set f variable to opening the index.csv file and preparing to write
##f = csv.writer(open('index.csv', 'w'))
### opens index.csv then writes three row names
##f.writerow(['Name', 'Link', 'Hello'])
### set pages object equal to empty list
##pages = []
### itterating - using method str() to place a string between 1 and 5 into url as i which then appends all links to pages
##for i in range(1, 5):
##    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
##    pages.append(url)
##
### for every item (url) within pages set a get request to each item to page then pass page.text which is get request
### for all the pages text content through the beautifulsoup() method which will parse them into soup using specified "html.parser" argument
##for item in pages:
##    page = requests.get(item)
##    soup = BeautifulSoup(page.text, 'html.parser')
### set last_links variable to execute soup variable we just made using its property find  to locate specified class AlphaNav
##    last_links = soup.find(class_='AlphaNav')
### use decompose method to shave off the bottom links of the returned link values from AlphaNav
##    last_links.decompose()
### do the same thing from above except search in BodyText class and set all info within that class along with html tags to artist_name_list
##    artist_name_list = soup.find(class_='BodyText')
### now locate only tags with the a reference for action links and store these into artist_name_list_items
##    artist_name_list_items = artist_name_list.find_all('a')
### set each item in artist_name_list_items to artist_name then set the content listings to names
### concatinate the first half of url that is static with the specified link grabbed for the individual artist reference page to create
### a list of all page links and write them in order from the rows created initially to csv file
##    for artist_name in artist_name_list_items:
##        names = artist_name.contents[0]
##        links = 'https://web.archive.org' + artist_name.get('href')
##
##        f.writerow([names, links, "Hi"])
##
##################################################################################################################################################


###############################################################################################################################################################
#### tkinter visual UI for scraping application
##class ParentWindow(Frame):
##    def __init__ (self, master):
##        Frame.__init__ (self)
##
##        self.master = master
##        self.master.resizable(width=False, height=False)
##        self.master.geometry('{}x{}'.format(700, 400))
##        self.master.title('Scraping Application')
##        self.master.config(bg="lightgray")
##
##        self.varURLName = StringVar()
##        self.varClassName = StringVar()
##        self.varCSVName = StringVar()
##
##        self.lblURLName = tk.Label(self.master,text='URL: ', font=("Helvetica", 18), fg='black', bg='lightgray')
##        self.lblURLName.grid(row=0,column=0, padx=(30,0), pady=(30,0))
##
##        self.lblClassName = tk.Label(self.master,text='Class: ', font=("Helvetica", 18), fg='black', bg='lightgray')
##        self.lblClassName.grid(row=1, column=0, padx=(30,0), pady=(30,0))
##
##        self.lblCSVName = tk.Label(self.master,text='CSV(ex. index.csv): ', font=("Helvetica", 18), fg='black', bg='lightgray')
##        self.lblCSVName.grid(row=2, column=0, padx=(30,0), pady=(30,0))
##
##        self.lblDisplay = tk.Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray')
##        self.lblDisplay.grid(row=3, column=1,padx=(30,0), pady=(30,0))
##        
##
##        self.txtURLName = tk.Entry(self.master,text=self.varURLName, font=("Helvetica", 16), fg='black', bg='lightblue')
##        self.txtURLName.grid(row=0, column=1,padx=(30,0), pady=(30,0))
##
##        self.txtClassName = tk.Entry(self.master,text=self.varClassName, font=("Helvetica", 16), fg='black', bg='lightblue')
##        self.txtClassName.grid(row=1, column=1,padx=(30,0), pady=(30,0))
##
##        self.txtCSVName = tk.Entry(self.master,text=self.varCSVName, font=("Helvetica", 16), fg='black', bg='lightblue')
##        self.txtCSVName.grid(row=2, column=1,padx=(30,0), pady=(30,0))
##        
##        self.btnExport = tk.Button(self.master,text="Export", width=10, height=2, command=self.export)
##        self.btnExport.grid(row=3, column=1,padx=(0,90), pady=(30,0), sticky=NE)
##        
##    
##
##    def export(self):
##        urlName = self.varURLName.get()
##        className = self.varClassName.get()
##        csvName = self.varCSVName.get()
##        WriteCSV(self)
##    def WriteCSV(self):
##        with open(csvName, 'w',newline='') as fp:
##            a = csv.writer(fp,delimeter=',')
##            data=['Paragraph','Link']
##            a.writerows(data)    
##    
##    
##
##
####def cancel(self):
####    self.master.destroy()
##
##
##if __name__ == "__main__":
##    root = Tk()
##    App = ParentWindow(root)
##    root.mainloop()

##################################################################################################################################################

## scrape for application


###Create new CSV file function###


##def WriteCSV(self):
##    with open(csvName, 'w',newline='') as fp:
##        a = csv.writer(fp,delimiter=',')
##        data=['Paragraph','Link']
##        a.writerows(data)
# set f variable to opening the index.csv file and preparing to write        
f = csv.writer(open(csvName, 'w'))
# opens index.csv then writes three row names
f.writerow(['Name', 'Link', 'Hello'])
# set pages object equal to empty list
pages = []
# itterating - using method str() to place a string between 1 and 5 into url as i which then appends all links to pages
for i in range(1, 5):
    url = urlName
    pages.append(url)

# for every item (url) within pages set a get request to each item to page then pass page.text which is get request
# for all the pages text content through the beautifulsoup() method which will parse them into soup using specified "html.parser" argument
for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
# set last_links variable to execute soup variable we just made using its property find  to locate specified class AlphaNav
    last_links = soup.find(class_='AlphaNav')
# use decompose method to shave off the bottom links of the returned link values from AlphaNav
    last_links.decompose()
# do the same thing from above except search in BodyText class and set all info within that class along with html tags to artist_name_list
    artist_name_list = soup.find(class_='BodyText')
# now locate only tags with the a reference for action links and store these into artist_name_list_items
    artist_name_list_items = artist_name_list.find_all('a')
# set each item in artist_name_list_items to artist_name then set the content listings to names
# concatinate the first half of url that is static with the specified link grabbed for the individual artist reference page to create
# a list of all page links and write them in order from the rows created initially to csv file
    for artist_name in artist_name_list_items:
        names = artist_name.contents[0]
        links = 'https://web.archive.org' + artist_name.get('href')

        f.writerow([names, links, "Hi"])







