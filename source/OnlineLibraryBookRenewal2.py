import mysql.connector
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from datetime import datetime
from tkinter import Tk, Frame, Entry, Label, messagebox, Button, Radiobutton, PhotoImage

fonts = ('Times New Roman', 20, 'bold')

class Login:
    def __init__(self, root):
        self.root = root
        self.login_frame = Frame(self.root, width = 900, height = 650, bg = 'dark turquoise')
        self.login_frame.place(x = 0, y = 0)
        #create account
        self.create_button = Button(self.login_frame, text = 'CREATE', bg = 'white', fg = 'steel blue', command = self.create, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1', width = 10)
        self.create_button.place(x = 360, y = 420)
        #image 
        #self.im = ImageTk.PhotoImage(Image.open("..//assets//studentlogo.png"))
        #self.img_label = Label(self.login_frame, image = self.im)
        #self.img_label.place(x = 240 ,y = 90)
        #label for reg.no
        self.reg_no_label = Label(self.login_frame, text = 'Admission Number', font = fonts, bg = 'dark turquoise', fg = 'navy', width =40)
        self.reg_no_label.place(x = 50, y = 225)
        self.reg_no_entry = Entry(self.login_frame, width  = 13, font = fonts, bg = 'white')
        self.reg_no_entry.place(x = 490, y = 225)
        #label for password
        self.passw_label = Label(self.login_frame, text = 'Password', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.passw_label.place(x = 250, y = 275)
        self.passw_entry = Entry(self.login_frame, width  = 13, font = fonts, bg = 'white', show = '*')
        self.passw_entry.place(x = 490, y = 275)
        #label for button
        self.login_btn = Button(self.login_frame, text = 'LOGIN', bg = 'white', fg = 'steel blue', command = self.check, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.login_btn.place(x = 390, y = 350)
        #label for back_button
        self.submit_btn = Button(self.login_frame, text = 'BACK', bg = 'white', fg = 'steel blue', command = self.back,  cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.submit_btn.place(x = 20, y = 20)

    def back(self):
        self.login_frame.destroy()
        backnav = Welcome(root)

    #checking valid student
    def check(self):
        self.regno = self.reg_no_entry.get()        
        self.password = self.passw_entry.get()

        command = f"SELECT * FROM StudentDetails WHERE StudentId = '{self.regno}' AND password = '{self.password}'"
        cursor.execute(command)
        result = cursor.fetchone()
        if result:
            messagebox.showinfo('WELCOME','WELCOME ' + self.regno)
            self.login_frame.destroy()
            req = BookDetail(root,self.regno)
        else:
            messagebox.showerror('INVALID CREDENTIALS','CHECK YOUR CREDENTIALS')


    def create(self):
        self.login_frame.destroy()
        createstudent = Create(self.root)

class BookDetail:
    def __init__(self,root,regno):
        self.root = root
        self.regno = regno
        self.Bookdetails = Frame(self.root, width = 900, height = 650, bg = 'goldenrod')
        self.Bookdetails.place(x = 0, y = 0)
        self.detbutton = Button(self.Bookdetails, text = 'Previous Requests', font = fonts, bg = 'white', fg = 'steel blue', cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.detbutton.place(x = 320, y = 200)
        self.detlabel2 = Button(self.Bookdetails, text = 'Present Book details', font = fonts, bg = 'white', fg = 'steel blue', cursor = 'hand2', activebackground = 'Rosy Brown1',command=self.detail)
        self.detlabel2.place(x = 320, y = 350)
        self.back_btn = Button(self.Bookdetails, text = 'BACK', bg = 'white', fg = 'steel blue', command = self.back, cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.back_btn.place(x = 20, y = 20)

    def back(self):
        self.Bookdetails.destroy()
        backnav = Login(root,self.regno)

    def detail(self):
        self.Bookdetails.destroy()
        det = Detail(root,self.regno)

class Detail:
    def __init__(self, root, regno):
        self.root = root
        self.regno = regno
        self.query = f"SELECT * FROM bookdetails WHERE StudentId = '{self.regno}'"
        cursor.execute(self.query)
        self.result = cursor.fetchall()
        style = ttk.Style()
        #style.configure('self.Detail_frame' , background='dark turquoise')
        
        self.Detail_frame = tk.Frame(self.root, width=900, height=650)
        #self.Detail_frame.config(background = 'dark turquoise')
        self.Detail_frame.pack(fill=tk.BOTH, expand=True)
        self.root.geometry('900x650+350+100')
        self.root.resizable(False, False)
        style.configure('Treeview', background='dark turquoise', foreground='navy', font=('Times New Roman', 15, 'bold'))
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
        self.submit_btn = Button(self.Detail_frame, text = 'Apply for Renew', bg = 'white', fg = 'steel blue', command = self.renew, cursor = 'hand2', activebackground = 'Rosy Brown1',font = fonts)
        self.submit_btn.place(x = 400, y = 200)
        self.back_btn = Button(self.Detail_frame, text = 'BACK', bg = 'white', fg = 'steel blue', command = self.back, cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'))
        self.back_btn.place(x = 200, y = 200)

    def back(self):
        self.Detail_frame.destroy()
        backnav = Bookdetail(root, self.regno)
    def renew(self):
        self.book_no_label = Label(self.Detail_frame, text = 'Book Id', font = fonts, fg = 'navy', width =40)
        self.book_no_label.place(x = 50, y = 400)
        self.book_no_entry = Entry(self.Detail_frame, width  = 13, font = fonts, bg = 'white')
        self.book_no_entry.place(x = 490, y = 400)
        self.submit_btn = Button(self.Detail_frame, text = 'Submit', bg = 'white', fg = 'steel blue', cursor = 'hand2', activebackground = 'Rosy Brown1',font = fonts, command = self.success)
        self.submit_btn.place(x = 400, y = 550)
        
    def success(self):
        self.bid = self.book_no_entry.get()
        self.query = f"SELECT * FROM Bookdetails WHERE BookId LIKE '{self.bid}'"
        cursor.execute(self.query)
        self.result = cursor.fetchone()
        if self.result:
            r = messagebox.askquestion("Alert","Confirm Renewal")
            if r == 'yes':
                self.query1 =f"insert into RenewalDetails values('{self.result[0]}','{self.result[1]}','{self.result[2]}','{self.result[3]}','{self.result[4]}')"
                cursor.execute(self.query1)
                conn.commit()
                messagebox.showinfo("Success","Successfully submitted")
        else:
            messagebox.showerror("Error","Invalid BOOk ID")




class Create:
    def __init__(self, root):
        self.root = root
        self.root.title('Create a login')
        self.create_frame = Frame(root, width = 900, height = 650, bg = 'dark turquoise')
        self.create_frame.place(x = 0, y = 0)
        #label for reg. no
        self.reg_no_label = Label(self.create_frame, text = 'Admission Number', font = fonts, bg = 'dark turquoise', fg = 'navy', width =40)
        self.reg_no_label.place(x = 50, y = 225)
        self.reg_no_entry = Entry(self.create_frame, width  = 13, font = fonts, bg = 'white')
        self.reg_no_entry.place(x = 490, y = 225)
        #label for password
        self.passw_label = Label(self.create_frame, text = 'Password', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.passw_label.place(x = 250, y = 275)
        self.passw_entry = Entry(self.create_frame, width  = 13, font = fonts, bg = 'white', show = '*')
        self.passw_entry.place(x = 490, y = 275)
        self.enter_button = Button(self.create_frame, text = 'SUBMIT', bg = 'white', fg = 'steel blue',  font = fonts, command = self.save, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.enter_button.place(x = 390, y = 350)
        #label for back_button
        self.submit_btn = Button(self.create_frame, text = 'BACK', bg = 'white', fg = 'steel blue', command = self.back, cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.submit_btn.place(x = 20, y = 20)

    def back(self):
        self.create_frame.destroy()
        backnav = Login(root)


    def save(self):
        
        self.regno = self.reg_no_entry.get()
        self.password = self.passw_entry.get()
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
        self.lib_frame = Frame(self.root, width = 900, height = 650, bg = 'dark turquoise')
        self.lib_frame.place(x = 0, y = 0)
        #label for reg.no
        self.LID_label = Label(self.lib_frame, text = 'ID', font = fonts, bg = 'dark turquoise', fg = 'navy', width =40)
        self.LID_label.place(x = 50, y = 225)
        self.LID_entry = Entry(self.lib_frame, width  = 13, font = fonts, bg = 'white')
        self.LID_entry.place(x = 490, y = 225)
        #label for password
        self.passw_label = Label(self.lib_frame, text = 'Password', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.passw_label.place(x = 250, y = 275)
        self.passw_entry = Entry(self.lib_frame, width  = 13, font = fonts, bg = 'white', show = '*')
        self.passw_entry.place(x = 490, y = 275)
        #label for button
        self.login_btn = Button(self.lib_frame, text = 'LOGIN', bg = 'white', fg = 'steel blue', font = fonts, command = self.check, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.login_btn.place(x = 390, y = 350)
        #label for back_button
        self.submit_btn = Button(self.lib_frame, text = 'BACK', bg = 'white', fg = 'steel blue', command = self.back,  cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
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
        self.Req_details_frame = Frame(self.root, width = 900, height = 650, bg = 'dark turquoise')
        self.Req_details_frame.place(x = 0, y = 0)
        #label for button
        self.UpdateDetails_btn = Button(self.Req_details_frame, text = 'Upload Book Details', bg = 'white', fg = 'steel blue',command = self.upload,  font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.UpdateDetails_btn.place(x = 320, y = 200)
        #label for button
        self.Req_btn = Button(self.Req_details_frame, text = 'Show Renewal Requests', bg = 'white', fg = 'steel blue', font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.Req_btn.place(x = 300, y = 350)
        #label for back_button
        self.back_btn = Button(self.Req_details_frame, text = 'BACK', bg = 'white', fg = 'steel blue', command = self.back,  cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.back_btn.place(x = 20, y = 20)

    def back(self):
        self.Req_details_frame.destroy()
        backnav = librarianlog(root)
    
    def upload(self):
        self.Req_details_frame.destroy()
        details = UploadDetails(root)
    
class UploadDetails:
    def __init__(self,root):
        self.root = root
        self.Upload_details_frame = Frame(self.root, width = 900, height = 650, bg = 'dark turquoise')
        self.Upload_details_frame.place(x = 0, y = 0)
        #label for reg.no
        self.SID_label = Label(self.Upload_details_frame, text = 'Student Admission Number', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 20)
        self.SID_label.place(x = 150, y = 100)
        self.SID_entry = Entry(self.Upload_details_frame, width  = 13, font = fonts, bg = 'white')
        self.SID_entry.place(x = 485, y = 100)

        self.Bid_label = Label(self.Upload_details_frame, text = 'Book Id', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.Bid_label.place(x = 300, y = 150)
        self.Bid_entry = Entry(self.Upload_details_frame, width  = 13, font = fonts, bg = 'white')
        self.Bid_entry.place(x = 485, y = 150)

        self.BName_label = Label(self.Upload_details_frame, text = 'Book Name', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.BName_label.place(x = 300, y = 200)
        self.BName_entry = Entry(self.Upload_details_frame, width  = 13, font = fonts, bg = 'white')
        self.BName_entry.place(x = 485, y = 200)

        self.Idate_label = Label(self.Upload_details_frame, text = 'Issued Date', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.Idate_label.place(x = 300, y = 250)
        self.Idate_entry = Entry(self.Upload_details_frame, width  = 13, font = fonts, bg = 'white')
        self.Idate_entry.place(x = 485, y = 250)

        self.Ddate_label = Label(self.Upload_details_frame, text = 'Due Date', font = fonts, bg = 'dark turquoise', fg = 'navy', width = 10)
        self.Ddate_label.place(x = 300, y = 300)
        self.Ddate_entry = Entry(self.Upload_details_frame, width  = 13, font = fonts, bg = 'white')
        self.Ddate_entry.place(x = 485, y = 300)
        #label for button
        self.upload_btn = Button(self.Upload_details_frame, text = 'UPLOAD', bg = 'white', fg = 'steel blue', font = fonts,  command = self.upload, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.upload_btn.place(x = 390, y = 400)
        #label for back_button
        self.submit_btn = Button(self.Upload_details_frame, text = 'BACK', bg = 'white', fg = 'steel blue', command = self.back,  cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
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
        messagebox.showinfo('SUCCESS', 'Successfully Uploaded')
        


class Welcome:
    def __init__(self, root):
        self.root = root
        self.Welcomeframe = Frame(self.root, width = 900, height = 650, bg = 'dark turquoise')
        self.Welcomeframe.place(x = 0, y = 0)

        self.im = ImageTk.PhotoImage(Image.open("..//assets//BOOKS.jpeg"))
        self.img_label = Label(self.Welcomeframe, image = self.im)
        self.img_label.place(x = 50 ,y = 200, width= 400)

        self.Wellabel = Label(self.Welcomeframe, text = 'ONLINE LIBRARY BOOK', font = fonts, bg = 'dark turquoise', fg = 'navy')
        self.Wellabel.place(x = 590, y = 150)
        self.Wellabel2 = Label(self.Welcomeframe, text = 'RENEWAL !!!', font = fonts, bg = 'dark turquoise', fg = 'navy')
        self.Wellabel2.place(x = 615, y = 200)

        self.Stud_login_btn = Button(self.Welcomeframe, text = 'Student', bg = 'white', fg = 'steel blue', command = self.studlogin, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.Stud_login_btn.place(x = 630, y = 390)

        self.Admin_login_btn = Button(self.Welcomeframe, text = 'Librarian', bg = 'white', fg = 'steel blue', command = self.librarianlogin, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.Admin_login_btn.place(x = 620, y = 300)

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
cursor.execute('create table if not exists BookDetails(BookId varchar(5) PRIMARY KEY, BookName CHAR(50), IssuedDate DATE, DueDate DATE,StudentId varchar(15))')
cursor.execute("create table if not exists RenewalDetails(BookId varchar(15) PRIMARY KEY, BookName CHAR(50),IssuedDate DATE,DueDate DATE,StudentId varchar(15))")

if __name__ == "__main__":
    root = Tk()
    root.title('BookRenewal')
    root.geometry('900x650+350+100')
    welcome = Welcome(root)
    root.resizable(False, False)
    #root.iconphoto(True, PhotoImage(file="..//assets//DESKSLOT.png"))
    root.mainloop()
