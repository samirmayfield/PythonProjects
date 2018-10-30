from tkinter import *
import tkinter as tk
import webcrawl

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(600, 300))
        self.master.title('Email Extraction Scraper')
        self.master.config(bg="lightgreen")

        self.var_url_name = StringVar()
        self.var_csv_name = StringVar()

        self.lbl_url_name = tk.Label(self.master,text='URL: ', font=("Helvetica", 16), fg='black', bg='lightgreen')
        self.lbl_url_name.grid(row=0,column=0, padx=(30,0), pady=(30,0))

        self.lbl_csv_name = tk.Label(self.master,text='CSV(ex. data.csv): ', font=("Helvetica", 16), fg='black', bg='lightgreen')
        self.lbl_csv_name.grid(row=5, column=0, padx=(30,0), pady=(30,0))

        self.lbl_display = tk.Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgreen')
        self.lbl_display.grid(row=6, column=1,padx=(30,0), pady=(30,0))        

        self.txt_url_name = tk.Entry(self.master,text=self.var_url_name, font=("Helvetica", 16), fg='black', bg='white')
        self.txt_url_name.grid(row=0, column=1,padx=(30,0), pady=(30,0))
        
        self.txt_csv_name = tk.Entry(self.master,text=self.var_csv_name, font=("Helvetica", 16), fg='black', bg='white')
        self.txt_csv_name.grid(row=5, column=1,padx=(30,0), pady=(30,0))
        
        self.btn_export = tk.Button(self.master,text="Extract Emails", width=10, height=2, command=self.export)
        self.btn_export.grid(row=6, column=1,padx=(0,90), pady=(30,0), sticky=NE)
    
    def export(self):
        url_name = self.var_url_name.get()
        csv_name = self.var_csv_name.get()
        webcrawl.scrape(url_name,csv_name)

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()


