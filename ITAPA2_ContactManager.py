# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 15:35:55 2022

@author: 9zwvq8p64
"""

#https://itsourcecode.com/free-projects/python-projects/contact-management-system-project-in-python-with-source-code/

from tkinter import *
import sqlite3
import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

#Developed by L. Gumede

root = Tk()
root.title("Contact List")
root.geometry("700x400+0+0")
root.resizable(0, 0)
root.config(bg="dark gray")

#Declaring variables for contact details
# VARIABLES
f_name = StringVar()
l_name = StringVar()
age = StringVar()
address = StringVar()
contact = StringVar()
gender = StringVar()


# METHODS
def Exit():
    wayOut = tkinter.messagebox.askyesno("Contact Management System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return

def Reset():
    f_name.set("")
    l_name.set("")
    gender.set("")
    age.set("")
    address.set("")
    contact.set("")
    
#Method creates the database connection
def Database():
    conn = sqlite3.connect("ContactManager.db")
    cursor = conn.cursor()
    #Creating the table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `contact_details` (id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT)")
    cursor.execute("SELECT * FROM `contact_details` ORDER BY `last_name` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

#Method contains query functions for inserting data into the table
#Handles input validation to insure all fields contain data
def Submit():
    if f_name.get() == "" or l_name.get() == "" or gender.get() == "" or age.get() == "" or address.get() == "" or contact.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("ContactManager.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO `contact_details` (first_name, last_name, gender, age, address, contact) VALUES(?, ?, ?, ?, ?, ?)", (str(f_name.get()), str(l_name.get()), str(gender.get()), int(age.get()), str(address.get()),
            int(contact.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `contact_details` ORDER BY `last_name` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        f_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        address.set("")
        contact.set("")
        

#Method contains query functions for updating the data in the table
#Handles input validation to insure all fields contain data
def Update():
    if gender.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("ContactManager.db")
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE `contact_details` SET `first_name` = ?, `last_name` = ?, `gender` =?, `age` = ?,  `address` = ?, `contact` = ?  WHERE `id` = ?",
            (str(f_name.get()),  str(l_name.get()), str(gender.get()), int(age.get()), str(address.get()),
            str(contact.get()), int(id)))
        conn.commit()
        cursor.execute("SELECT * FROM `contact_details` ORDER BY `last_name` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        f_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        address.set("")
        contact.set("")
        

#Double clicking on a row opens the Update window
#Update window is a frame for updating the data in the selected row
#Frame contains interface functions with data in the text boxes
#Update button updates the data in the table
def UpdateContactWindow(event):
    global id, UpdateWindow
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    id = selecteditem[0]
    f_name.set("")
    l_name.set("")
    gender.set("")
    age.set("")
    address.set("")
    contact.set("")
    

    f_name.set(selecteditem[1])
    l_name.set(selecteditem[2])

    age.set(selecteditem[4])
    address.set(selecteditem[5])
    contact.set(selecteditem[6])
    

    UpdateWindow = Toplevel()
    UpdateWindow.title("Contact Details")
    UpdateWindow.geometry("500x520+0+0")
    UpdateWindow.config(bg="dark gray")
    UpdateWindow.resizable(0, 0)
    if 'NewWindow' in globals():
        NewWindow.destroy()

    # FRAMES
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=gender, value="Male", font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=gender, value="Female", font=('arial', 14)).pack(side=LEFT)
    
    # LABELS
    lbl_title = Label(FormTitle, text="Updating Contacts", bd=12, relief=GROOVE, fg="White", bg="green",
                      font=("Calibri", 14, "bold"), pady=3)
    lbl_title.pack(fill=X)
    lbl_FirstName = Label(ContactForm, text="First Name", font=('arial', 14), bd=5)
    lbl_FirstName.grid(row=0, sticky=W)

    lbl_LastName = Label(ContactForm, text="Last Name", font=('arial', 14), bd=5)
    lbl_LastName.grid(row=1, sticky=W)

    lbl_Gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_Gender.grid(row=2, sticky=W)

    lbl_Age = Label(ContactForm, text="Age", font=('arial', 14), bd=5)
    lbl_Age.grid(row=3, sticky=W)

    lbl_Address = Label(ContactForm, text="Address", font=('arial', 14), bd=5)
    lbl_Address.grid(row=4, sticky=W)

    lbl_Contact = Label(ContactForm, text="Contact", font=('arial', 14), bd=5)
    lbl_Contact.grid(row=5, sticky=W)

    

    # TEXT ENTRY
    FirstName = Entry(ContactForm, textvariable=f_name, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    FirstName.grid(row=0, column=1)

    LastName = Entry(ContactForm, textvariable=l_name, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    LastName.grid(row=1, column=1)

    RadioGroup.grid(row=2, column=1)

    Age = Entry(ContactForm, textvariable=age, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    Age.grid(row=3, column=1)

    Address = Entry(ContactForm, textvariable=address, font=('arial', 14, 'bold'), bd=10, width=20,
                        justify='left')
    Address.grid(row=4, column=1)

    Contact = Entry(ContactForm, textvariable=contact, font=('arial', 14, 'bold'), bd=10, width=20,
                        justify='left')
    Contact.grid(row=5, column=1)

   
    # ==================BUTTONS==============================
    ButtonUpdateContact = Button(ContactForm, text='Update', bd=10, font=('arial', 12, 'bold'), relief="ridge", fg="white",
                              bg="green", command=Update)
    ButtonUpdateContact.grid(row=9, columnspan=2, pady=10)


#Method for deleting an entry from the database
#Select a row so it can be deleted
#Deletes a row of data from the table
def Delete():
    if not tree.selection():
        result = tkMessageBox.showwarning('', 'Please Select in the Table First!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are You Sure You Want To Delete This Record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = sqlite3.connect("ContactManager.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `contact_details` WHERE `id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

#Creates the frame for adding a new entry in the contact manager
#Allows you to save the new entry to the database
def AddNewContact():
    global NewWindow
    f_name.set("")
    l_name.set("")
    gender.set("")
    age.set("")
    address.set("")
    contact.set("")
    
    NewWindow = Toplevel()
    NewWindow.title("Contact Details")
    NewWindow.resizable(0, 0)
    NewWindow.geometry("500x520+0+0")
    NewWindow.config(bg="dark gray")
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()

    # ===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=gender, value="Male", font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=gender, value="Female", font=('arial', 14)).pack(side=LEFT)
    
    # ===================LABELS==============================
    lbl_title = Label(FormTitle, text="Adding New Contacts",  bd=12, relief=GROOVE, fg="White", bg="green",
                      font=("Calibri", 14, "bold"), pady=3)
    lbl_title.pack(fill=X)
    lbl_FirstName = Label(ContactForm, text="First Name", font=('arial', 14), bd=5)
    lbl_FirstName.grid(row=0, sticky=W)

    lbl_LastName = Label(ContactForm, text="Last Name", font=('arial', 14), bd=5)
    lbl_LastName.grid(row=1, sticky=W)

    lbl_Gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_Gender.grid(row=2, sticky=W)

    lbl_Age = Label(ContactForm, text="Age", font=('arial', 14), bd=5)
    lbl_Age.grid(row=3, sticky=W)

    lbl_Address = Label(ContactForm, text="Address", font=('arial', 14), bd=5)
    lbl_Address.grid(row=4, sticky=W)

    lbl_Contact = Label(ContactForm, text="Contact", font=('arial', 14), bd=5)
    lbl_Contact.grid(row=5, sticky=W)

    

    # ===================ENTRY===============================
    FirstName = Entry(ContactForm, textvariable=f_name, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    FirstName.grid(row=0, column=1)

    LastName = Entry(ContactForm, textvariable=l_name, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    LastName.grid(row=1, column=1)

    RadioGroup.grid(row=2, column=1)

    Age = Entry(ContactForm, textvariable=age, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    Age.grid(row=3, column=1)

    Address = Entry(ContactForm, textvariable=address, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    Address.grid(row=4, column=1)

    Contact = Entry(ContactForm, textvariable=contact, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    Contact.grid(row=5, column=1)

    

    # ==================BUTTONS==============================
    ButtonAddContact = Button(ContactForm, text='Save',  bd=10, font=('arial', 12, 'bold'), relief="ridge", fg="white",
                   bg="green", command=Submit)
    ButtonAddContact.grid(row=9, columnspan=2, pady=10)

#Create layout for frame
# ============================FRAMES======================================
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=500, bg="dark gray")
Mid.pack(side=BOTTOM)
f1 = Frame(root, width=6, height=8, bd=8, bg="dark gray")
f1.pack(side=BOTTOM)
flb = Frame(f1, width=6, height=8, bd=8, bg="green")
flb.pack(side=BOTTOM)
MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370, bg="dark gray")
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)

# LABELS
lbl_title = Label(Top,  text="Contact Management System", bd=12, relief=GROOVE, fg="White", bg="green",
                      font=("Calibri", 36, "bold"), pady=3)
lbl_title.pack(fill=X)


# BUTTONS
ButtonAdd = Button(flb, text='Add New Contact',  bd=8, font=('arial', 12, 'bold'), relief="groove", fg="black",
                   bg="dark gray", command=AddNewContact).grid(row=0, column=0, ipadx=20, padx=30)

ButtonDelete = Button(flb, text='Delete', bd=8, font=('arial', 12, 'bold'), relief="groove",  command=Delete,
                  fg="black", bg="dark gray").grid(row=0, column=1, ipadx=20)

ButtonExit = Button(flb, text='Exit System', bd=8, font=('arial', 12, 'bold'), relief="groove",  command=Exit,
                 fg="black", bg="dark gray").grid(row=0, column=2, ipadx=20, padx=30)

# TABLES
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Id", "First Name", "Last Name", "Gender", "Age", "Address", "Contact"),
                    height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Id', text="Id", anchor=W)
tree.heading('First Name', text="First Name", anchor=W)
tree.heading('Last Name', text="Last Name", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Age', text="Age", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.heading('Contact', text="Contact", anchor=W)

tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=100)
tree.column('#4', stretch=NO, minwidth=0, width=70)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.column('#6', stretch=NO, minwidth=0, width=100)
tree.column('#7', stretch=NO, minwidth=0, width=80)

tree.pack()
tree.bind('<Double-Button-1>', UpdateContactWindow)

# ============================INITIALIZATION==============================
if __name__ == '__main__':
    Database()
    root.mainloop()

