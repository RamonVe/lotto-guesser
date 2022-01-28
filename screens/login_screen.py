import tkinter
from tkinter import *
from tkinter import messagebox

from screens import registration_screen


def validate_login(user_name, pass_word):
    print("username entered :", user_name.get())
    print("password entered :", pass_word.get())
    return


def login_screen(root_window):
    # window
    login_window = tkinter.Toplevel(root_window)
    login_window.geometry('400x150')
    login_window.title('Lotto Guesser')
    # username label and text entry box
    Label(login_window, text="User Name").grid(row=0, column=0)
    username = StringVar()
    Entry(login_window, textvariable=username).grid(row=0, column=1)
    # password label and password entry box
    Label(login_window, text="Password").grid(row=1, column=0)
    password = StringVar()
    Entry(login_window, textvariable=password, show='*').grid(row=1, column=1)
    # login button
    Button(login_window, text="Login", command=lambda: validate_login(username, password)).grid(row=4, column=0)
    # registration button
    Button(login_window, text="Register",
           command=lambda: registration_screen.registration_screen(root_window, login_window)).grid(row=5, column=0)

    Button(login_window, text="Return to root window.", command=lambda: change_window(
        login_window, root_window)).grid(row=6, column=0)

    def close():
        if messagebox.askokcancel("Quit", "Do You Want To Quit?"):
            root_window.destroy()

    login_window.protocol("WM_DELETE_WINDOW", close)


def change_window(login_window, root_window):
    # remove the other window entirely
    login_window.destroy()

    # make root_window visible again
    root_window.iconify()
    root_window.deiconify()
