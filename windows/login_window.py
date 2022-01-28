import tkinter
from tkinter import *
from tkinter import messagebox

from windows import registration_window


def validate_login(user_name, pass_word):
    print('username entered :', user_name.get())
    print('password entered :', pass_word.get())
    return


def login_window(root_window):
    # window
    login_window_instance = tkinter.Toplevel(root_window)
    login_window_instance.geometry('400x150')
    login_window_instance.title('Lotto Guesser')
    # username label and text entry box
    Label(login_window_instance, text='User Name').grid(row=0, column=0)
    username = StringVar()
    Entry(login_window_instance, textvariable=username).grid(row=0, column=1)
    # password label and password entry box
    Label(login_window_instance, text='Password').grid(row=1, column=0)
    password = StringVar()
    Entry(login_window_instance, textvariable=password, show='*').grid(row=1, column=1)
    # login button
    Button(login_window_instance, text='Login', command=lambda: validate_login(username, password)).grid(row=4,
                                                                                                         column=0)
    # registration button
    Button(login_window_instance, text='Register',
           command=lambda: registration_window.registration_window(root_window, login_window_instance)).grid(row=5,
                                                                                                             column=0)

    Button(login_window_instance, text='Return to root window.', command=lambda: change_window(
        login_window_instance, root_window)).grid(row=6, column=0)

    def close():
        if messagebox.askokcancel('Quit', 'Do You Want To Quit?'):
            root_window.destroy()

    login_window_instance.protocol('WM_DELETE_WINDOW', close)


def change_window(login_window_instance, root_window):
    # remove the other window entirely
    login_window_instance.destroy()

    # make root_window visible again
    root_window.iconify()
    root_window.deiconify()
