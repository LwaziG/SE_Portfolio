# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 12:52:22 2022

@author: 9zwvq8p64
"""

#Codemy Database App
from tkinter import *
#from PIL import ImageTK, Image
import sqlite3
#import mysql.connector

#Developed by L. Gumede
root = Tk()
root.title('Fault Management')

f_name= StringVar()
l_name= StringVar()
gender= StringVar()
contact= StringVar()
apartment= StringVar()
report_date= StringVar()
unit= StringVar()
fault= StringVar()

#Databases

#Create a database or connect to one
conn = sqlite3.connect('FaultManagement.db')



#Create cursor
c = conn.cursor()

#Create table
c.execute("""CREATE TABLE IF NOT EXISTS faultList (
    first_name text,
    last_name text,
    gender text,
    contact text,
    apartment text,
    report_date text,
    unit text,
    fault text
    )""")

#Create Submit Function for Database
def submit():
    global SubmitWindow
    
    if f_name.get() == "" or l_name.get() == "" or gender.get() == "" or contact.get() == "" or apartment.get() == "" or report_date.get() == "" or unit.get() == "" or fault.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        
        #Create a database or connect to one
        conn = sqlite3.connect('FaultManagement.db')
        
        #Create cursor
        c = conn.cursor()
        
        #Insert Into Table
        
        c.execute("INSERT INTO faultList VALUES (:first_name, :last_name, :gender, :contact, :apartment, :report_date, :unit, :fault)",
                {
                    'first_name': f_name.get(),
                    'last_name': l_name.get(),
                    'gender': gender.get(),
                    'contact': contact.get(),
                    'apartment': apartment.get(),
                    'report_date': report_date.get(),
                    'unit': unit.get(),
                    'fault': fault.get()
                })
        
        #Commit Changes
        conn.commit()
        
        #Close Connection
        conn.close()
        
        #Clear the Text Boxes
        f_name.delete(0, END)
        l_name.delete(0, END)
        gender.delete(0, END)
        contact.delete(0, END)
        apartment.delete(0, END)
        report_date.delete(0, END)
        unit.delete(0, END)
        fault.delete(0, END)
    
#Create a Query Function
def query():
    #Create a database or connect to one
    conn = sqlite3.connect('FaultManagement.db')
    #conn = mysql.connector.connect(host = "127.0.0.1", user = "root", password = "")
    #Create cursor
    c = conn.cursor()
    #myCursor = conn.cursor()
    
    
    #Query the database
    c.execute("SELECT * FROM faultList")
    records = c.fetchall()
    print(records)
    
    #Loop through results
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"
        
    query_label = Label(root, text = print_records)
    query_label.grid(row = 8, column = 0, columnspan = 2)
     
    #Commit Changes
    conn.commit()
    
    #Close Connection
    conn.close()


#Create Text Boxes
f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20)
l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1)
contact = Entry(root, width = 30)
contact.grid(row = 2, column = 1)
apartment = Entry(root, width = 30)
apartment.grid(row = 3, column = 1)
report_date = Entry(root, width = 30)
report_date.grid(row = 4, column = 1)
unit = Entry(root, width = 30)
unit.grid(row = 5, column = 1)


Male = Radiobutton(root, text="Male", variable=gender, value="Male", font=('arial', 14))
Female = Radiobutton(root, text="Female", variable=gender, value="Female", font=('arial', 14))


#RadioGroup.grid(row=6, column=1)
Male.grid(row = 6, column = 1)
Female.grid(row = 6, column = 2)
fault = Entry(root, width = 30)
fault.grid(row = 7, column = 1)

#Create Text Box Labels
f_name_label = Label(root, text = "First Name:")
f_name_label.grid(row = 0, column = 0)
l_name_label = Label(root, text = "Last Name:")
l_name_label.grid(row = 1, column = 0)
contact_label = Label(root, text = "Contact:")
contact_label.grid(row = 2, column = 0)
apartment_label = Label(root, text = "Apartment:")
apartment_label.grid(row = 3, column = 0)
report_date_label = Label(root, text = "Report Date:")
report_date_label.grid(row = 4, column = 0)
unit_label = Label(root, text = "Unit:")
unit_label.grid(row = 5, column = 0)
gender_label = Label(root, text = "Gender:")
gender_label.grid(row = 6, column = 0)
fault_label = Label(root, text = "Fault:")
fault_label.grid(row = 7, column = 0)

#Create Submit Button
submit_btn = Button(root, text = "Submit Now", command = submit)
submit_btn.grid(row = 9, column = 1, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

#Create a Query Button
query_btn = Button(root, text = "List Fault", command = query)
query_btn.grid(row = 10, column = 1, columnspan = 2, pady = 10, padx = 10, ipadx = 137)

#Commit changes
conn.commit()

#Close Connection
conn.close()
root.mainloop()

