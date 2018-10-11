from bs4 import BeautifulSoup
import csv
import requests
from tkinter import *
import tkinter as tk
import scrape

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Scraping Application')
        self.master.config(bg="lightgray")

        self.varURLName = StringVar()
        self.varClassName = StringVar()
        self.varCSVName = StringVar()
        self.varTAGType = StringVar()

        self.lblURLName = tk.Label(self.master,text='URL: ', font=("Helvetica", 18), fg='black', bg='lightgray')
        self.lblURLName.grid(row=0,column=0, padx=(30,0), pady=(30,0))

        self.lblClassName = tk.Label(self.master,text='Class: ', font=("Helvetica", 18), fg='black', bg='lightgray')
        self.lblClassName.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        self.lblTAGType = tk.Label(self.master,text='Tag:', font=("Helvetica", 18), fg='black', bg='lightgray')
        self.lblTAGType.grid(row=2, column=0, padx=(30,0), pady=(30,0))

        self.lblCSVName = tk.Label(self.master,text='CSV(ex. data.csv): ', font=("Helvetica", 18), fg='black', bg='lightgray')
        self.lblCSVName.grid(row=3, column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay = tk.Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=4, column=1,padx=(30,0), pady=(30,0))        

        self.txtURLName = tk.Entry(self.master,text=self.varURLName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtURLName.grid(row=0, column=1,padx=(30,0), pady=(30,0))

        self.txtClassName = tk.Entry(self.master,text=self.varClassName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtClassName.grid(row=1, column=1,padx=(30,0), pady=(30,0))

        self.txtTAGType = tk.Entry(self.master,text=self.varTAGType, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtTAGType.grid(row=2, column=1,padx=(30,0), pady=(30,0))
        
        self.txtCSVName = tk.Entry(self.master,text=self.varCSVName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtCSVName.grid(row=3, column=1,padx=(30,0), pady=(30,0))
        
        self.btnExport = tk.Button(self.master,text="Export", width=10, height=2, command=self.export)
        self.btnExport.grid(row=4, column=1,padx=(0,90), pady=(30,0), sticky=NE)
    
    def export(self):
        urlName = self.varURLName.get()
        className = self.varClassName.get()
        csvName = self.varCSVName.get()
        tagType = self.varTAGType.get()
        scrape.WriteCSV(csvName)
        scrape.scrape(className,urlName,csvName,tagType)

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
