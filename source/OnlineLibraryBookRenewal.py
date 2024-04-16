import mysql.connector
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from datetime import datetime
from tkinter import Tk, Frame, Entry, Label, messagebox, Button, Radiobutton, PhotoImage
# from tkcalendar import Calendar

fonts = ('Times New Roman', 20, 'bold')

class Login:
    def __init__(self, root):
        self.root = root
        self.login_frame = Frame(self.root, width = 900, height = 650, bg = 'goldenrod')
        self.login_frame.place(x = 0, y = 0)
        #create account
        self.create_button = Button(self.login_frame, text = 'CREATE', bg = 'white', fg = 'steel blue', command = self.create, font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1', width = 10)
        self.create_button.place(x = 360, y = 420)
        #image 
        #self.im = ImageTk.PhotoImage(Image.open("..//assets//studentlogo.png"))
        #self.img_label = Label(self.login_frame, image = self.im)
        #self.img_label.place(x = 240 ,y = 90)
        #label for reg.no
        self.reg_no_label = Label(self.login_frame, text = 'Admission Number', font = fonts, bg = 'goldenrod', fg = 'navy', width =40)
        self.reg_no_label.place(x = 50, y = 225)
        self.reg_no_entry = Entry(self.login_frame, width  = 13, font = fonts, bg = 'white')
        self.reg_no_entry.place(x = 490, y = 225)
        #label for password
        self.passw_label = Label(self.login_frame, text = 'Password', font = fonts, bg = 'goldenrod', fg = 'navy', width = 10)
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
class BookDetail:
    def __init__(self,root):
        self.root = root
        self.Bookdetails = Frame(self.root, width = 900, height = 650, bg = 'goldenrod')
        self.Bookdetails.place(x = 0, y = 0)
        self.detbutton = Button(self.Bookdetails, text = 'Previous Requests', font = fonts, bg = 'white', fg = 'steel blue', cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.detbutton.place(x = 320, y = 200)
        self.detlabel2 = Button(self.Bookdetails, text = 'Present Book details', font = fonts, bg = 'white', fg = 'steel blue', cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.detlabel2.place(x = 320, y = 350)
        self.back_btn = Button(self.Bookdetails, text = 'BACK', bg = 'white', fg = 'steel blue', command = self.back, cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.back_btn.place(x = 20, y = 20)
    def back(self):
        self.Bookdetails.destroy()
        backnav = Login(root)
    #checking valid student
    def check(self):
        self.regno = self.reg_no_entry.get()        
        self.password = self.passw_entry.get()
        self.login_frame.destroy()
        book = BookDetail(root)
        # command = f"SELECT * FROM StudentDetails WHERE StudentId = '{self.regno}' AND password = '{self.password}'"
        # cursor.execute(command)
        # result = cursor.fetchone()
        # if result:
        #     messagebox.showinfo('WELCOME','WELCOME ' + self.regno)
        #     self.login_frame.destroy()
        # else:
        #     messagebox.showerror('INVALID CREDENTIALS','CHECK YOUR CREDENTIALS')


    def create(self):
        self.login_frame.destroy()
        createstudent = Create(root)

class Create:
    def __init__(self, root):
        self.root = root
        self.root.title('Create a login')
        self.create_frame = Frame(root, width = 900, height = 650, bg = 'goldenrod')
        self.create_frame.place(x = 0, y = 0)
        #label for reg. no
        self.reg_no_label = Label(self.create_frame, text = 'Admission Number', font = fonts, bg = 'goldenrod', fg = 'navy', width =40)
        self.reg_no_label.place(x = 50, y = 225)
        self.reg_no_entry = Entry(self.create_frame, width  = 13, font = fonts, bg = 'white')
        self.reg_no_entry.place(x = 490, y = 225)
        #label for password
        self.passw_label = Label(self.create_frame, text = 'Password', font = fonts, bg = 'goldenrod', fg = 'navy', width = 10)
        self.passw_label.place(x = 250, y = 275)
        self.passw_entry = Entry(self.create_frame, width  = 13, font = fonts, bg = 'white', show = '*')
        self.passw_entry.place(x = 490, y = 275)
        self.enter_button = Button(self.create_frame, text = 'SUBMIT', bg = 'white', fg = 'steel blue',  font = fonts, cursor = 'hand2', activebackground = 'Rosy Brown1')
        self.enter_button.place(x = 390, y = 350)
        #label for back_button
        self.submit_btn = Button(self.create_frame, text = 'BACK', bg = 'white', fg = 'steel blue', command = self.back, cursor = 'hand2', activebackground = 'Rosy Brown1',font = ('Times New Roman', 10, 'bold'), width=5, height=1)
        self.submit_btn.place(x = 20, y = 20)

    def back(self):
        self.create_frame.destroy()
        backnav = Login(root)


    '''def save(self):
        
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
            messagebox.showerror("Error", "Enter Valid Credentials !")'''


class librarianlog:
    pass

class Welcome:
    def __init__(self, root):
        self.root = root
        self.Welcomeframe = Frame(self.root, width = 900, height = 650, bg = 'goldenrod')
        self.Welcomeframe.place(x = 0, y = 0)

        self.im = ImageTk.PhotoImage(Image.open("..//assets//BOOKS.jpeg"))
        self.img_label = Label(self.Welcomeframe, image = self.im)
        self.img_label.place(x = 50 ,y = 200, width= 400)

        self.Wellabel = Label(self.Welcomeframe, text = 'ONLINE BOOK', font = fonts, bg = 'goldenrod', fg = 'navy')
        self.Wellabel.place(x = 590, y = 150)
        self.Wellabel2 = Label(self.Welcomeframe, text = 'RENEWAL !!', font = fonts, bg = 'goldenrod', fg = 'navy')
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
   # auth_plugin = 'mysql_native_password'
)
cursor = conn.cursor()
cursor.execute('create database if not exists BookRenewal')
cursor.execute('use BookRenewal')
cursor.execute("create table if not exists Librarian(LId varchar(15) PRIMARY KEY,  password varchar(15))")
cursor.execute('create table if not exists StudentDetails(StudentId varchar(15) PRIMARY KEY, password varchar(15))')
if __name__ == "__main__":
    root = Tk()
    root.title('Bookrenewal')
    root.geometry('900x650+350+100')
    welcome = Welcome(root)
    root.resizable(False, False)
    #root.iconphoto(True, PhotoImage(file="..//assets//DESKSLOT.png"))
    root.mainloop()
