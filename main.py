from tkinter import *
from subprocess import call
from tkinter import ttk , Tk
from tkinter import messagebox
import mysql.connector
import os
import appif
import time

#connecting to the database
db = mysql.connector.connect(host="localhost",
  user="root",
  password="",
  database="stock_db")
mycur = db.cursor()

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("login")
    root2.geometry("1080x620")
    root2.minsize(480, 360)
    global username_varify
    global password_varify
    username_varify = StringVar()
    password_varify = StringVar()
    root2.iconbitmap("DANE-STUDIO.ico")
    # redefinir le fond
    root2.config(background='#ffdeda')
    # creer une frame
    center_frame = Frame(root2, bg='#ffdeda')
    center_frame.pack(expand=YES)
    Label(center_frame, text="", font=("Times New Roman", 20), bg='#ffdeda').pack()
    Label(center_frame, text="Username :", font=("Times New Roman", 20), bg='#ffdeda').pack()
    Entry(center_frame, textvariable=username_varify,font=("Times New Roman", 20)).pack()
    Label(center_frame, text="", font=("Times New Roman", 20), bg='#ffdeda').pack()
    Label(center_frame, text="Password :",font=("Times New Roman", 20), bg='#ffdeda').pack()
    Entry(center_frame, textvariable=password_varify,font=("Times New Roman", 20), show="*").pack()
    Label(center_frame, text="", font=("Times New Roman", 20), bg='#ffdeda').pack()
    Button(center_frame, text="Log-In",font=("Times New Roman", 20), bg='#00c2cb',command=login_varify).pack(fill=X,pady=10)
    Label(center_frame, text="", font=("Times New Roman", 20), bg='#ffdeda')

def logg_destroy():
    logg.destroy()
    root2.destroy()

def logged():
    global logg
    appif.window
    logg.geometry("1080x620")
    logg.minsize(480, 360)
    Label(logg, text="Welcome {} ".format(username_varify.get()), fg="green", font="bold").pack()
    Label(logg, text="").pack()
    Button(logg, text="Log-Out", bg="grey", width=8, height=1, command=logg_destroy).pack()


def failed():
    messagebox.showerror("Error", "Invalid credentials...")


def login_varify():
    user_varify = username_varify.get()
    pas_varify = password_varify.get()
    sql = "select * from user where mail = %s and pwd = %s"
    mycur.execute(sql,[(user_varify),(pas_varify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()


def main_screen():
    global root
    root = Tk()
    root.title("Acceuil")
    root.geometry("1080x620")
    root.minsize(480, 360)
    root.iconbitmap("DANE-STUDIO.ico")
    # redefinir le fond

    root.config(background='#ffdeda')

    # creer une frame
    frame = Frame(root, bg='#ffdeda')
    frame.pack(expand=YES)

    # ajouter du texte
    title = Label(frame, text="Bienvenue sur StockConfig", font=("Times New Roman", 40), bg='#ffdeda')
    title.pack()
    # ajouter un bouton
    button = Button(frame, text="Acceder à votre espace", font=("Times New Roman", 20), bg='#ffdeda', fg='#00c2cb',command=login)
    button.pack()


main_screen()
root.mainloop()

