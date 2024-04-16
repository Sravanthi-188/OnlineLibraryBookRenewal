import mysql.connector
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from datetime import datetime
import re
from tkinter import Tk, Frame, Entry, Label, messagebox, Button, Radiobutton, PhotoImage
from tkcalendar import DateEntry
fonts = ('Times New Roman', 20, 'bold')

class Login:
    def __init__(self, root):
        self.root = root
        self.login_frame = Frame(self.root, width = 900, height = 650, bg = '#BDFCC9')
        self.login_frame.place(x = 0, y = 0)
        self.stulabel = Label(self.login_frame, text = 'STUDENT LOGIN PAGE', font = ('Times New Roman', 25, 'bold'), bg = '#BDFCC9', fg = 'navy')
        self.stulabel.place(x = 250, y = 100)
        self.reg_no_label = Label(self.login_frame, text = 'Admission Number', font = fonts, bg = '#BDFCC9', fg = 'navy', width =40)
        self.reg_no_label.place(x = 50, y = 225)
        self.reg_no_entry = Entry(self.login_frame, width  = 13, font = fonts, bg = 'white')
        self.reg_no_entry.place(x = 490, y = 225)
        #label for password
        self.passw_label = Label(self.login_frame, text = 'Password', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 10)
        self.passw_label.place(x = 250, y = 275)
        self.passw_entry = Entry(self.login_frame, width  = 13, font = fonts, bg = 'white', show = '*')
        self.passw_entry.place(x = 490, y = 275)
        #label for button
        self.login_btn = Button(self.login_frame, text = 'LOGIN', bg = '#54FF9F', fg = 'navy', command = self.check, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.login_btn.place(x = 390, y = 350)
        #create account
        self.create_button = Button(self.login_frame, text = 'SIGNUP', bg = '#54FF9F', fg = 'navy', command = self.create, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1', width = 10)
        self.create_button.place(x = 360, y = 420)
        self.forgot_btn = Button(self.login_frame, text = 'forgot password?', bg = '#54FF9F', fg = 'navy', command = self.forgot, font = ('Times New Roman', 10, 'bold'), width=15, height=1, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.forgot_btn.place(x = 490, y = 320)
        #label for back_button
        self.submit_btn = Button(self.login_frame, text = 'BACK', bg = '#54FF9F', fg = 'navy', command = self.back,  cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.submit_btn.place(x = 20, y = 20)

    def back(self):
        self.login_frame.destroy()
        backnav = Welcome(root)
    def forgot(self):
        self.login_frame.destroy()
        backnav = Forgot(root)
    #checking valid student
    def check(self):
        self.regno = self.reg_no_entry.get()        
        self.password = self.passw_entry.get()
        if self.regno and self.password:
            command = f"SELECT * FROM StudentDetails WHERE StudentId = '{self.regno}' AND password = '{self.password}'"
            cursor.execute(command)
            result = cursor.fetchone()
            if result:
                messagebox.showinfo('WELCOME','WELCOME ' + self.regno)
                self.login_frame.destroy()
                req = BookDetail(root, self.regno)
            else:
                messagebox.showerror('NO ACCOUNT','CREATE NEW ACCOUNT')
        else:
            messagebox.showerror('INVALID CREDENTIALS','CHECK YOUR CREDENTIALS')

    def create(self):
        self.login_frame.destroy()
        createstudent = Create(self.root)
class Forgot:
    def __init__(self,root):
        self.root = root
        self.forgot_frame = Frame(self.root, width = 900, height = 650, bg = '#BDFCC9')
        self.forgot_frame.place(x = 0, y = 0)
        self.regno_label = Label(self.forgot_frame, text = 'Admission Number', font = fonts, bg = '#BDFCC9', fg = 'navy', width =40)
        self.regno_label.place(x = 50, y = 175)
        self.regno_entry = Entry(self.forgot_frame, width  = 13, font = fonts, bg = 'white')
        self.regno_entry.place(x = 490, y = 175)
        self.sub_btn = Button(self.forgot_frame, text = 'SUBMIT', bg = '#54FF9F', fg = 'navy', command = self.valid, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.sub_btn.place(x = 390, y = 390)
        self.back_btn = Button(self.forgot_frame, text = 'BACK', bg = '#54FF9F', fg = 'navy', command = self.back,  cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.back_btn.place(x = 20, y = 20)


    def valid(self):
        self.regno = self.regno_entry.get()
        command = f"SELECT * FROM StudentDetails WHERE StudentId = '{self.regno}'"
        cursor.execute(command)
        result = cursor.fetchone()
        if result:
            self.passw_label = Label(self.forgot_frame, text = 'New Password', font = fonts, bg = '#BDFCC9', fg = 'navy', width =40)
            self.passw_label.place(x = 50, y = 225)
            self.passw_entry = Entry(self.forgot_frame, width  = 13, font = fonts, bg = 'white', show='*')
            self.passw_entry.place(x = 490, y = 225)
            #label for password
            self.cpassw_label = Label(self.forgot_frame, text = 'Confirm Password', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 20)
            self.cpassw_label.place(x = 160, y = 275)
            self.cpassw_entry = Entry(self.forgot_frame, width  = 13, font = fonts, bg = 'white', show = '*')
            self.cpassw_entry.place(x = 490, y = 275)
            self.login_btn = Button(self.forgot_frame, text = 'SUBMIT', bg = '#54FF9F', fg = 'navy', command = self.confirm, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
            self.login_btn.place(x = 390, y = 390)
        else:
            messagebox.showerror('ERROR','No account found!')
    
    def confirm(self):
        self.passw = self.passw_entry.get()
        self.cpassw = self.cpassw_entry.get()
        if self.passw:
            if self.passw == self.cpassw:
                messagebox.showinfo("success",'Successfully updated')
                self.query = f"UPDATE StudentDetails SET password = '{self.passw}' WHERE StudentId = '{self.regno}'"
                cursor.execute(self.query)
                conn.commit()
                self.forgot_frame.destroy()
                backnav = Forgot(root)
            else:
                messagebox.showerror('ERROR','Re-Enter confirm password')
        else:
            messagebox.showerror('ERROR','Invalid Password')
    
    def back(self):
        self.forgot_frame.destroy()
        backnav = Login(root)

class BookDetail:
    def __init__(self,root, regno):
        self.root = root
        self.regno = regno
        self.Bookdetails = Frame(self.root, width = 900, height = 650, bg = '#BDFCC9')
        self.Bookdetails.place(x = 0, y = 0)
        self.detbutton = Button(self.Bookdetails, text = 'Previous Requests', font = fonts, bg = '#54FF9F', fg = 'navy', cursor = 'hand2', activebackground = 'Rosy Brown1',command=self.req_books)
        self.detbutton.place(x = 320, y = 200)
        self.detlabel2 = Button(self.Bookdetails, text = 'Present Book details', font = fonts, bg = '#54FF9F', command = self.details, fg = 'navy', cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.detlabel2.place(x = 320, y = 350)
        self.back_btn = Button(self.Bookdetails, text = 'BACK', bg = '#54FF9F', fg = 'navy', command = self.back, cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.back_btn.place(x = 20, y = 20)
    def back(self):
        self.Bookdetails.destroy()
        backnav = Login(root)

    def details(self):
        self.Bookdetails.destroy()
        det = Detail(root, self.regno)
    def req_books(self):
        self.Bookdetails.destroy()
        req = Requestedbooks(root,self.regno)

class Requestedbooks:
    def __init__(self,root, regno):
        self.root = root
        self.regno = regno
        self.query = f"SELECT * FROM renewed WHERE StudentId ='{self.regno}'"
        cursor.execute(self.query)
        self.result = cursor.fetchall()
        style = ttk.Style()
        #style.configure('self.Detail_frame' , background='#BDFCC9')
        
        self.Requested_frame = tk.Frame(self.root, width=900, height=650)
        #self.Detail_frame.config(background = '#BDFCC9')
        self.Requested_frame.pack(fill=tk.BOTH, expand=True)
        self.root.geometry('900x650+350+100')
        self.root.resizable(False, False)
        style.configure('Treeview', background='#BDFCC9', foreground='navy', font=('Times New Roman', 15, 'bold'))
        # Create a Treeview widget to hold the seat grid
        self.tree = ttk.Treeview(self.Requested_frame, columns=('BookId', 'BookName', 'Fine'), show='headings')
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('BookId', width=150, anchor='center')
        self.tree.column('BookName', width=150, anchor='center')
        self.tree.column('Fine', width=150, anchor='center')
        self.tree.heading('BookId', text='BookId')
        self.tree.heading('BookName', text='BookName')
        self.tree.heading('Fine', text='Fine')
        self.tree.pack(fill=tk.BOTH, expand=True)
        # Insert data into the Treeview widget
        for row in self.result: 
            self.tree.insert('', 'end', values=row)
    
        self.back_btn = Button(self.Requested_frame, text = 'BACK', bg = '#54FF9F', fg = 'navy', command = self.back, cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 20, 'bold'))
        self.back_btn.place(x = 400, y = 500)

    def back(self):
        self.Requested_frame.destroy()
        backFrame = BookDetail(root,self.regno)

class Detail:
    def __init__(self, root, regno):
        self.root = root
        self.regno = regno
        self.query = f"SELECT * FROM bookdetails WHERE StudentId = '{self.regno}'"
        cursor.execute(self.query)
        self.result = cursor.fetchall()
        style = ttk.Style()
        #style.configure('self.Detail_frame' , background='#BDFCC9')
        
        self.Detail_frame = tk.Frame(self.root, width=900, height=650)
        self.Detail_frame.config(background = '#BDFCC9')
        self.Detail_frame.pack(fill=tk.BOTH, expand=True)
        self.root.geometry('900x650+350+100')
        self.root.resizable(False, False)
        style.configure('Treeview', background='#BDFCC9', foreground='navy', font=('Times New Roman', 15, 'bold'))
        # Create a Treeview widget to hold the seat grid
        self.tree = ttk.Treeview(self.Detail_frame, columns=('BookId', 'BookName', 'IssuedDate', 'DueDate'), show='headings')
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('BookId', width=200, anchor='center')
        self.tree.column('BookName', width=200, anchor='center')
        self.tree.column('IssuedDate', width=200, anchor='center')
        self.tree.column('DueDate', width=200, anchor='center')
        self.tree.heading('BookId', text='BookId')
        self.tree.heading('BookName', text='BookName')
        self.tree.heading('IssuedDate', text='IssuedData')
        self.tree.heading('DueDate', text='DueDate')
        self.tree.pack(fill=tk.BOTH, expand=True)
        # Insert data into the Treeview widget
        for row in self.result: 
            self.tree.insert('', 'end', values=row)
        #label for back_button
        self.submit_btn = Button(self.Detail_frame, text = 'Apply for Renew', bg = '#54FF9F', fg = 'navy', command = self.renew, cursor = 'hand2', activebackground = 'Rosy Brown1',font = fonts)
        self.submit_btn.place(x = 400, y = 200)
        self.back_btn = Button(self.Detail_frame, text = 'BACK', bg = '#54FF9F', fg = 'navy', command = self.back, cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 20, 'bold'))
        self.back_btn.place(x = 200, y = 200)

    def back(self):
        self.Detail_frame.destroy()
        backnav = BookDetail(root, self.regno)

    def renew(self):
        self.book_no_label = Label(self.Detail_frame, text = 'Book Id', font = fonts, fg = 'navy',bg = 'white', width =40)
        self.book_no_label.place(x = 50, y = 400)
        self.book_no_entry = Entry(self.Detail_frame, width  = 13, font = fonts, bg = 'white')
        self.book_no_entry.place(x = 490, y = 400)
        self.submit_btn = Button(self.Detail_frame, text = 'Submit', bg = '#54FF9F', fg = 'navy', cursor = 'hand2', activebackground = 'Rosy Brown1',font = fonts, command = self.success)
        self.submit_btn.place(x = 400, y = 550)
        
    def success(self):
        self.bid = self.book_no_entry.get()
        self.query2 = f"SELECT * FROM RenewalDetails WHERE BookId LIKE '{self.bid}'"
        cursor.execute(self.query2)
        self.result = cursor.fetchone()
        if self.result:
            messagebox.showerror("Error","This Book has already applied for Renewal")
        else:
            self.query = f"SELECT * FROM Bookdetails WHERE BookId LIKE '{self.bid}'"
            cursor.execute(self.query)
            self.result = cursor.fetchone()
            if self.result:
                r = messagebox.askquestion("Alert","Apply for Renewal")
                if r == 'yes':
                    self.query1 =f"insert into RenewalDetails values('{self.result[0]}','{self.result[1]}','{self.result[2]}','{self.result[3]}','{self.result[4]}')"
                    cursor.execute(self.query1)
                    conn.commit()
                    messagebox.showinfo("Success","Successfully submitted")
                    self.Detail_frame.destroy()
                    revisit = Detail(root, self.regno)
            else:
                messagebox.showerror("Error","Invalid BOOk ID")

class Create:
    def __init__(self, root):
        self.root = root
        self.root.title('Create a login')
        self.create_frame = Frame(root, width = 900, height = 650, bg = '#BDFCC9')
        self.create_frame.place(x = 0, y = 0)
        #label for reg. no
        self.reg_no_label = Label(self.create_frame, text = 'Admission Number', font = fonts, bg = '#BDFCC9', fg = 'navy', width =40)
        self.reg_no_label.place(x = 50, y = 225)
        self.reg_no_entry = Entry(self.create_frame, width  = 13, font = fonts, bg = 'white')
        self.reg_no_entry.place(x = 490, y = 225)
        #label for password
        self.passw_label = Label(self.create_frame, text = 'Password', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 10)
        self.passw_label.place(x = 250, y = 275)
        self.passw_entry = Entry(self.create_frame, width  = 13, font = fonts, bg = 'white', show = '*')
        self.passw_entry.place(x = 490, y = 275)
        self.enter_button = Button(self.create_frame, text = 'SUBMIT', bg = '#54FF9F', fg = 'navy',  font = fonts, command = self.save, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.enter_button.place(x = 390, y = 350)
        #label for back_button
        self.submit_btn = Button(self.create_frame, text = 'BACK', bg = '#54FF9F', fg = 'navy', command = self.back, cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.submit_btn.place(x = 20, y = 20)

    def back(self):
        self.create_frame.destroy()
        backnav = Login(root)


    def save(self):
        self.regno = self.reg_no_entry.get()
        self.password = self.passw_entry.get()
        self.queryv = f"SELECT * FROM StudentDetails WHERE StudentId = '{self.regno}'"
        cursor.execute(self.queryv)
        self.result = cursor.fetchone()
        if self.result:
            messagebox.showerror("ERROR",'YOU ALREADY HAVE AN ACCOUNT')
        else:
            if self.regno and self.password:
                self.query = f"insert into StudentDetails values('{self.regno}','{self.password}')"
                cursor.execute(self.query)
                conn.commit()
                messagebox.showinfo('SUCCESS', 'Successfully created the account')
                self.create_frame.destroy()
                login = Login(root)
            else:
                messagebox.showerror("Error", "Enter Valid Credentials !")

class librarianlog:
    def __init__(self, root):
        self.root = root
        self.lib_frame = Frame(self.root, width = 900, height = 650, bg = '#BDFCC9')
        self.lib_frame.place(x = 0, y = 0)
        self.liblabel = Label(self.lib_frame, text = 'LIBRARIAN LOGIN PAGE', font = ('Times New Roman', 25, 'bold'), bg = '#BDFCC9', fg = 'navy')
        self.liblabel.place(x = 250, y = 100)
        # self.liblabel1 = Label(self.lib_frame, text = 'RENEWAL !!!',font = ('Times New Roman', 35, 'bold'), bg = '#BDFCC9', fg = 'navy')
        # self.liblebel1.place(x = 295, y = 100)
        #label for reg.no
        self.LID_label = Label(self.lib_frame, text = 'Librarian ID', font = fonts, bg = '#BDFCC9', fg = 'navy', width =40)
        self.LID_label.place(x = 30, y = 225)
        self.LID_entry = Entry(self.lib_frame, width  = 13, font = fonts, bg = 'white')
        self.LID_entry.place(x = 490, y = 225)
        #label for password
        self.passw_label = Label(self.lib_frame, text = 'Password', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 10)
        self.passw_label.place(x = 250, y = 275)
        self.passw_entry = Entry(self.lib_frame, width  = 13, font = fonts, bg = 'white', show = '*')
        self.passw_entry.place(x = 490, y = 275)
        #label for button
        self.login_btn = Button(self.lib_frame, text = 'LOGIN', bg = '#54FF9F', fg = 'navy', font = fonts, command = self.check, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.login_btn.place(x = 390, y = 350)
        #label for back_button
        self.submit_btn = Button(self.lib_frame, text = 'BACK', bg = '#54FF9F', fg = 'navy', command = self.back,  cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.submit_btn.place(x = 20, y = 20)

    def back(self):
        self.lib_frame.destroy()
        backnav = Welcome(root)
    
    def check(self):
        self.LId = self.LID_entry.get()        
        self.password = self.passw_entry.get()

        command = f"SELECT * FROM Librarian WHERE LId = '{self.LId}' AND password = '{self.password}'"
        cursor.execute(command)
        result = cursor.fetchone()
        if result:
            messagebox.showinfo('WELCOME','WELCOME ' + self.LId)
            self.lib_frame.destroy()
            next = Req_Details(root)
        else:
            messagebox.showinfo('INVALID','INVALID CREDENTIALS')

class Req_Details:
    def __init__(self, root):
        self.root = root
        self.Req_details_frame = Frame(self.root, width = 900, height = 650, bg = '#BDFCC9')
        self.Req_details_frame.place(x = 0, y = 0)
        #label for button
        self.UpdateDetails_btn = Button(self.Req_details_frame, text = 'Upload Book Details', bg = '#54FF9F', fg = 'navy',command = self.upload,  font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.UpdateDetails_btn.place(x = 120, y = 200)
        #label for button
        self.UpdateDetails_btn = Button(self.Req_details_frame, text = 'Delete Book Details', bg = '#54FF9F', fg = 'navy',command = self.delete,  font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.UpdateDetails_btn.place(x = 520, y = 200)
        #label for button
        self.Req_btn = Button(self.Req_details_frame, text = 'Show Renewal Requests', bg = '#54FF9F', fg = 'navy',command = self.view, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.Req_btn.place(x = 300, y = 350)
        #label for back_button
        self.back_btn = Button(self.Req_details_frame, text = 'BACK', bg = '#54FF9F', fg = 'navy', command = self.back,  cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.back_btn.place(x = 20, y = 20)

    def back(self):
        self.Req_details_frame.destroy()
        backnav = librarianlog(root)
    
    def upload(self):
        self.Req_details_frame.destroy()
        details = UploadDetails(root)
    
    def view(self):
        self.Req_details_frame.destroy()
        req = ViewRequests(root)

    def delete(self):
        self.Req_details_frame.destroy()
        next = DeleteBookDetails(root)

class DeleteBookDetails:
    def __init__(self, root):
        self.root = root
        self.delete_frame = Frame(self.root, width = 900, height = 650, bg = '#BDFCC9')
        self.delete_frame.place(x = 0, y = 0)
        self.delete_label = Label(self.delete_frame, text = 'Enter Book Id :', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 20)
        self.delete_label.place(x = 200, y = 50)
        self.delete_entry = Entry(self.delete_frame, width  = 13, font = fonts, bg = 'white')
        self.delete_entry.place(x = 500, y = 50)
        self.submit_btn = Button(self.delete_frame, text = 'SUBMIT', bg = '#54FF9F', fg = 'navy', command = self.details,  cursor = 'hand2', activebackground = 'Rosy Brown1',font = fonts)
        self.submit_btn.place(x = 250, y = 100)
        self.back_btn = Button(self.delete_frame, text = 'BACK', bg = '#54FF9F', fg = 'navy', command = self.back,  cursor = 'hand2', activebackground = 'Rosy Brown1',font = fonts)
        self.back_btn.place(x = 450, y = 100)

    def back(self):
        self.delete_frame.destroy()
        backnav = Req_Details(root)

    def details(self):
        self.bid = self.delete_entry.get()
        self.query = f"SELECT * FROM BookDetails WHERE BookId LIKE '{self.bid}'"
        cursor.execute(self.query)
        self.result = cursor.fetchone()
        if self.result:
            self.Bid_label = Label(self.delete_frame, text = 'Book Id :', font = fonts, bg = '#BDFCC9', fg = 'navy', width =30)
            self.Bid_label.place(x = 100, y = 200)
            self.Bid_label_text = Label(self.delete_frame, text = self.result[0], font = fonts, bg = '#BDFCC9', fg = 'navy', width =5)
            self.Bid_label_text.place(x = 450, y = 200)
            
            self.BName_label = Label(self.delete_frame, text = 'Book Name :', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 10)
            self.BName_label.place(x = 250, y = 250)
            self.BName_label_text = Label(self.delete_frame, text = self.result[1], font = fonts, bg = '#BDFCC9', fg = 'navy', width = 5)
            self.BName_label_text.place(x = 450, y = 250)

            self.Idate_label = Label(self.delete_frame, text = 'IssuedDate :', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 10)
            self.Idate_label.place(x = 310, y = 300)
            self.Idate_label_text = Label(self.delete_frame, text = self.result[2], font = fonts, bg = '#BDFCC9', fg = 'navy', width = 10)
            self.Idate_label_text.place(x = 510, y = 300)

            self.Ddate_label = Label(self.delete_frame, text = 'DueDate :', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 10)
            self.Ddate_label.place(x = 310, y = 350)
            self.Ddate_label_text = Label(self.delete_frame, text = self.result[3], font = fonts, bg = '#BDFCC9', fg = 'navy', width = 15)
            self.Ddate_label_text.place(x = 450, y = 350)

            self.Sid_label = Label(self.delete_frame, text = 'Student Id :', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 10)
            self.Sid_label.place(x = 300, y = 400)
            self.Sid_label_text = Label(self.delete_frame, text = self.result[4], font = fonts, bg = '#BDFCC9', fg = 'navy', width = 15)
            self.Sid_label_text.place(x = 450, y = 400)  

            self.delete_btn = Button(self.delete_frame, text = 'DELETE', bg = '#54FF9F', fg = 'navy', command = self.deletebook,  cursor = 'hand2', activebackground = 'Rosy Brown1',font = fonts)
            self.delete_btn.place(x = 400, y = 450)
        else:
            messagebox.showerror('ERROR','NO BOOK FOUND')

    def deletebook(self):
        r = messagebox.askquestion("Alert!",'Do you want to delete book?')
        if r=='yes':
            self.querydel = f"DELETE FROM BookDetails WHERE BookId LIKE '{self.bid}'"
            cursor.execute(self.querydel)
            conn.commit()
            messagebox.showinfo("SUCCESS",'Successfully deleted')
            self.delete_frame.destroy()
            revisit = DeleteBookDetails(root)
    
class ViewRequests:
    def __init__(self, root):
        self.root = root
        self.query = f"SELECT * FROM RenewalDetails"
        cursor.execute(self.query)
        self.result = cursor.fetchall()
        style = ttk.Style()
        self.Requests_frame = tk.Frame(self.root, width=900, height=650)
        self.Requests_frame.pack(fill=tk.BOTH, expand=True)
        self.root.geometry('900x650+350+100')
        self.root.resizable(False, False)
        style.configure('Treeview', background='#BDFCC9', foreground='navy', font=('Times New Roman', 15, 'bold'))
        # Create a Treeview widget to hold the seat grid
        self.tree = ttk.Treeview(self.Requests_frame, columns=('BookId', 'BookName', 'IssuedDate', 'DueDate', 'StudentId'), show='headings')
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('BookId', width=150, anchor='center')
        self.tree.column('BookName', width=150, anchor='center')
        self.tree.column('IssuedDate', width=150, anchor='center')
        self.tree.column('DueDate', width=150, anchor='center')
        self.tree.column('StudentId', width=150, anchor='center')
        self.tree.heading('BookId', text='BookId')
        self.tree.heading('BookName', text='BookName')
        self.tree.heading('IssuedDate', text='IssuedData')
        self.tree.heading('DueDate', text='DueDate')
        self.tree.heading('StudentId', text='StudentId')
        self.tree.pack(fill=tk.BOTH, expand=True)
        # Insert data into the Treeview widget
        for row in self.result: 
            self.tree.insert('', 'end', values=row)
        #label for back_button
        self.submit_btn = Button(self.Requests_frame, text = 'RENEW', bg = '#54FF9F', fg = 'navy', command = self.renew, cursor = 'hand2', activebackground = 'Rosy Brown1',font = fonts)
        self.submit_btn.place(x = 420, y = 200)
        self.back_btn = Button(self.Requests_frame, text = 'BACK', bg = '#54FF9F', fg = 'navy', command = self.back, cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 20, 'bold'))
        self.back_btn.place(x = 280, y = 200)

    def back(self):
        self.Requests_frame.destroy()
        backnav = Req_Details(root)
    
    def renew(self):
        self.book_no_label = Label(self.Requests_frame, text = 'Book Id', font = fonts, fg = 'navy',bg = 'white', width =40)
        self.book_no_label.place(x = 50, y = 400)
        self.book_no_entry = Entry(self.Requests_frame, width  = 13, font = fonts, bg = 'white')
        self.book_no_entry.place(x = 490, y = 400)
        self.submit_btn = Button(self.Requests_frame, text = 'Submit', bg = '#54FF9F', fg = 'navy',command = self.details, cursor = 'hand2', activebackground = 'Rosy Brown1',font = fonts)
        self.submit_btn.place(x = 400, y = 550)
    
    def details(self):
        self.bid = self.book_no_entry.get()
        self.queryf = f"SELECT * FROM RenewalDetails WHERE BookId = '{self.bid}'"
        cursor.execute(self.queryf)
        self.resultf = cursor.fetchone()
        if self.resultf:
            self.Requests_frame.destroy()
            next = Fine(root,self.bid)
        else:
            messagebox.showerror("ERROR",'INVALID BOOKID')

class Fine:
    def __init__(self,root, bid):
        self.root = root
        self.bid = bid
        self.query = f"SELECT * FROM RenewalDetails WHERE BookId LIKE '{self.bid}'"
        cursor.execute(self.query)
        self.result = cursor.fetchone()
        self.fine_frame = Frame(self.root, width = 900, height = 650, bg = '#BDFCC9')
        self.fine_frame.place(x = 0, y = 0)

        self.head_label = Label(self.fine_frame, text = 'Book Details', font = ('Times New Roman', 30, 'bold'), bg = '#BDFCC9', fg = 'navy', width =30)
        self.head_label.place(x = 70, y = 40)

        self.Bid_label = Label(self.fine_frame, text = 'Book Id :', font = fonts, bg = '#BDFCC9', fg = 'navy', width =30)
        self.Bid_label.place(x = 50, y = 100)
        self.Bid_label_text = Label(self.fine_frame, text = self.result[0], font = fonts, bg = '#BDFCC9', fg = 'navy', width =5)
        self.Bid_label_text.place(x = 450, y = 100)
        
        self.BName_label = Label(self.fine_frame, text = 'Book Name :', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 10)
        self.BName_label.place(x = 250, y = 150)
        self.BName_label_text = Label(self.fine_frame, text = self.result[1], font = fonts, bg = '#BDFCC9', fg = 'navy', width = 5)
        self.BName_label_text.place(x = 450, y = 150)

        self.Idate_label = Label(self.fine_frame, text = 'IssuedDate :', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 10)
        self.Idate_label.place(x = 210, y = 200)
        self.Idate_label_text = Label(self.fine_frame, text = self.result[2], font = fonts, bg = '#BDFCC9', fg = 'navy', width = 10)
        self.Idate_label_text.place(x = 410, y = 200)

        self.Ddate_label = Label(self.fine_frame, text = 'DueDate :', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 10)
        self.Ddate_label.place(x = 210, y = 250)
        self.Ddate_label_text = Label(self.fine_frame, text = self.result[3], font = fonts, bg = '#BDFCC9', fg = 'navy', width = 15)
        self.Ddate_label_text.place(x = 350, y = 250)

        self.Sid_label = Label(self.fine_frame, text = 'Student Id :', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 10)
        self.Sid_label.place(x = 200, y = 300)
        self.Sid_label_text = Label(self.fine_frame, text = self.result[4], font = fonts, bg = '#BDFCC9', fg = 'navy', width = 15)
        self.Sid_label_text.place(x = 350, y = 300)
        
        self.newduedate_label = Label(self.fine_frame, text = 'Enter updated due date :', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 20)
        self.newduedate_label.place(x = 190, y = 350)
        self.newduedate_entry = DateEntry(self.fine_frame, width  = 13, font = fonts, bg = 'white', date_pattern = 'yyyy-mm-dd')
        self.newduedate_entry.place(x = 490, y = 350)

        self.completed_btn = Button(self.fine_frame, text = 'BOOK RENEWED', bg = '#54FF9F', fg = 'navy', command = self.prompt,  cursor = 'hand2', activebackground = 'Rosy Brown1',font = fonts)
        self.completed_btn.place(x = 100, y = 400)

        self.back_btn = Button(self.fine_frame, text = 'BACK', bg = '#54FF9F', fg = 'navy', command = self.back,  cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.back_btn.place(x = 20, y = 20)

    def applyFine(self):
        self.applyfine_label = Label(self.fine_frame, text = 'Enter fine :', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 20)
        self.applyfine_label.place(x = 210, y = 500)
        self.applyfine_entry = Entry(self.fine_frame, width  = 13, font = fonts, bg = 'white')
        self.applyfine_entry.place(x = 490, y = 500)
        self.applyfine_label = Label(self.fine_frame, text = 'Enter 0 if no fine', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 20)
        self.applyfine_label.place(x = 525, y = 500)
        self.submit_btn = Button(self.fine_frame, text = 'SUBMIT', bg = '#54FF9F', fg = 'navy', command = self.submit,  cursor = 'hand2', activebackground = 'Rosy Brown1',font = fonts)
        self.submit_btn.place(x = 230, y = 550)
    
    def back(self):
        self.fine_frame.destroy()
        backnav = ViewRequests(root)

    def submit(self):
        self.fine = self.applyfine_entry.get()
        if self.fine:
            self.queryi = f"INSERT INTO Renewed VALUES('{self.result[0]}','{self.result[1]}','{self.fine}','{self.result[4]}')"
            cursor.execute(self.queryi)
            conn.commit()
            messagebox.showinfo("SUCCESS",'successfully applied')
            self.fine_frame.destroy()
            backnav = ViewRequests(root)
        else:
            messagebox.showerror("ERROR",'INVALID FINE')
        

    def prompt(self):
        self.newduedate = self.newduedate_entry.get()
        if self.newduedate:
            messagebox.showinfo("success",'Successfully renewed book')
            self.query = f"UPDATE BookDetails SET IssuedDate = '{self.result[3]}' WHERE BookId LIKE '{self.result[0]}'"
            cursor.execute(self.query)
            self.queryx = f"UPDATE BookDetails SET DueDate = '{self.newduedate}' WHERE BookId LIKE '{self.result[0]}'"
            cursor.execute(self.queryx)
            self.queryd = f"DELETE FROM RenewalDetails WHERE BookId = '{self.result[0]}'"
            cursor.execute(self.queryd)
            conn.commit()
        
            self.apply_fine_btn = Button(self.fine_frame, text = 'APPLY FINE', bg = 'white', fg = 'navy', command = self.applyFine, cursor = 'hand2', activebackground = 'Rosy Brown1',font = fonts)
            self.apply_fine_btn.place(x = 600, y = 400)


        else:
            messagebox.showerror("ERROR",'Invalid new due date')
    
class UploadDetails:
    def __init__(self,root):
        self.root = root
        self.Upload_details_frame = Frame(self.root, width = 900, height = 650, bg = '#BDFCC9')
        self.Upload_details_frame.place(x = 0, y = 0)

        self.SID_label = Label(self.Upload_details_frame, text = 'Student Admission Number', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 20)
        self.SID_label.place(x = 150, y = 100)
        self.SID_entry = Entry(self.Upload_details_frame, width  = 13, font = fonts, bg = 'white')
        self.SID_entry.place(x = 485, y = 100)

        self.Bid_label = Label(self.Upload_details_frame, text = 'Book Id', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 10)
        self.Bid_label.place(x = 300, y = 150)
        self.Bid_entry = Entry(self.Upload_details_frame, width  = 13, font = fonts, bg = 'white')
        self.Bid_entry.place(x = 485, y = 150)

        self.BName_label = Label(self.Upload_details_frame, text = 'Book Name', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 10)
        self.BName_label.place(x = 300, y = 200)
        self.BName_entry = Entry(self.Upload_details_frame, width  = 13, font = fonts, bg = 'white')
        self.BName_entry.place(x = 485, y = 200)

        self.Idate_label = Label(self.Upload_details_frame, text = 'Issued Date', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 10)
        self.Idate_label.place(x = 300, y = 250)
        self.Idate_entry = DateEntry(self.Upload_details_frame, width  = 13, font = fonts, bg = 'white', date_pattern = 'yyyy-mm-dd')
        self.Idate_entry.place(x = 485, y = 250)

        self.Ddate_label = Label(self.Upload_details_frame, text = 'Due Date', font = fonts, bg = '#BDFCC9', fg = 'navy', width = 10)
        self.Ddate_label.place(x = 300, y = 300)
        self.Ddate_entry = DateEntry(self.Upload_details_frame, width  = 13, font = fonts, bg = 'white', date_pattern = 'yyyy-mm-dd')
        self.Ddate_entry.place(x = 485, y = 300)

        #label for button
        self.upload_btn = Button(self.Upload_details_frame, text = 'UPLOAD', bg = '#54FF9F', fg = 'navy', font = fonts,  command = self.validate, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.upload_btn.place(x = 390, y = 400)
        #label for back_button
        self.submit_btn = Button(self.Upload_details_frame, text = 'BACK', bg = '#54FF9F', fg = 'navy', command = self.back,  cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.submit_btn.place(x = 20, y = 20)

    def back(self):
        self.Upload_details_frame.destroy()
        backnav = Req_Details(root)

    def upload(self):
        self.sid = self.SID_entry.get()
        self.bid = self.Bid_entry.get()
        self.bname = self.BName_entry.get()
        self.issue = self.Idate_entry.get()
        self.due = self.Ddate_entry.get()
        self.query = f"insert into BookDetails values('{self.bid}','{self.bname}','{self.issue}','{self.due}','{self.sid}')"
        cursor.execute(self.query)
        conn.commit()

    def validate(self):
        self.sid = self.SID_entry.get()
        self.bid = self.Bid_entry.get()
        self.bname = self.BName_entry.get()
        self.issue = self.Idate_entry.get()
        self.due = self.Ddate_entry.get()
        sid_pattern = r'^[a-zA-Z0-9]{10}$'
        bid_pattern = r'^[0-9]{5}$'
        bname_pattern = r'^[a-zA-Z\s]{3,30}$'
        issue_pattern = r'^\d{4}-\d{2}-\d{2}$'
        due_pattern = r'^\d{4}-\d{2}-\d{2}$'

        if not re.match(sid_pattern, self.sid):
            messagebox.showerror('Invalid',"Invalid Student ID")
        if not re.match(bid_pattern, self.bid):
            messagebox.showerror('Invalid',"Invalid Book ID")
        if not re.match(bname_pattern, self.bname):
            messagebox.showerror('Inavlid',"Invalid Book Name")
        if not re.match(issue_pattern, self.issue):
            messagebox.showerror('Invalid',"Invalid Issue Date")
        if not re.match(due_pattern, self.due):
            messagebox.showerror('Invalid',"Invalid Due Date")
        if re.match(sid_pattern, self.sid) and re.match(bid_pattern, self.bid) and re.match(bname_pattern, self.bname) and re.match(issue_pattern, self.issue) and re.match(due_pattern, self.due):
            upl = self.upload()
            messagebox.showinfo('SUCCESS', 'SUCCESSFULLY UPLOADED')
            self.Upload_details_frame.destroy()
            revisit = UploadDetails(root)
        
class Welcome:
    def __init__(self, root):
        self.root = root
        self.Welcomeframe = Frame(self.root, width = 900, height = 650, bg = '#BDFCC9')
        self.Welcomeframe.place(x = 0, y = 0)

        self.im = ImageTk.PhotoImage(Image.open("..//assets//BOOKS.png"))
        self.img_label = Label(self.Welcomeframe, image = self.im)
        self.img_label.place(x = 50 ,y = 200, width= 400)

        self.Wellabel = Label(self.Welcomeframe, text = 'ONLINE LIBRARY BOOK', font = ('Times New Roman', 35, 'bold'), bg = '#BDFCC9', fg = 'navy')
        self.Wellabel.place(x = 150, y = 50)
        self.Wellabel2 = Label(self.Welcomeframe, text = 'RENEWAL !!!',font = ('Times New Roman', 35, 'bold'), bg = '#BDFCC9', fg = 'navy')
        self.Wellabel2.place(x = 295, y = 100)

        self.Stud_login_btn = Button(self.Welcomeframe, text = 'Student', bg = '#54FF9F', fg = 'navy', command = self.studlogin, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.Stud_login_btn.place(x = 630, y = 350)

        self.Admin_login_btn = Button(self.Welcomeframe, text = 'Librarian', bg = '#54FF9F', fg = 'navy', command = self.librarianlogin, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.Admin_login_btn.place(x = 620, y = 260)
        
    def studlogin(self):
        self.Welcomeframe.destroy()
        loginstud = Login(root)

    def librarianlogin(self):
        self.Welcomeframe.destroy()
        loginad = librarianlog(root)

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = "BookRenewal",
    auth_plugin = 'mysql_native_password'
)
cursor = conn.cursor()
cursor.execute('create database if not exists BookRenewal')
cursor.execute('use BookRenewal')
cursor.execute("create table if not exists Librarian(LId varchar(15) PRIMARY KEY,  password varchar(15))")
cursor.execute('create table if not exists StudentDetails(StudentId varchar(15) PRIMARY KEY, password varchar(15))')
cursor.execute('create table if not exists BookDetails(BookId varchar(5) PRIMARY KEY, BookName CHAR(50), IssuedDate DATE, DueDate DATE, StudentId varchar(15))')
cursor.execute("create table if not exists RenewalDetails(BookId varchar(15) PRIMARY KEY, BookName CHAR(50),IssuedDate DATE,DueDate DATE,StudentId varchar(15))")
cursor.execute("create table if not exists Renewed(BookId varchar(15) PRIMARY KEY, BookName CHAR(50), Fine INT ,StudentId varchar(15))")


if __name__ == "__main__":
    root = Tk()
    root.title('BookRenewal')
    root.geometry('900x650+350+100')
    welcome = Welcome(root)
    root.resizable(False,False)
    root.iconphoto(True, PhotoImage(file="..//assets//books.png"))
    # bg = PhotoImage(file="..//assets//books.png")
    root.mainloop()
