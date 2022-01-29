from tkinter import *
from tkinter import messagebox
from storage import local_data_utilities
from windows import dashboard_window
from windows import registration_window
import tkinter


def validate_login(user_name, pass_word, root_window, log_window):
    if user_name.get() == '' and pass_word.get() == '':
        messagebox.showwarning('Empty Fields!', 'Enter a username and password to log in!')

    users = local_data_utilities.load_users()

    for user in users:
        if user.username == user_name.get():
            if user.password != pass_word.get():
                messagebox.showwarning('Wrong Password!', 'You have entered the wrong password, try again!')
            else:
                log_window.destroy()
                dashboard(root_window, user)
                break


def dashboard(root_window, logged_in_user):
    dashboard_window.dashboard_window(root_window, logged_in_user)


def login_window(root_window):
    log_window = tkinter.Toplevel(root_window)
    log_window.geometry('220x100')
    log_window.title('Login')

    Label(log_window, text='User Name').grid(row=0, column=0)
    Label(log_window, text='Password').grid(row=1, column=0)

    username = StringVar()
    password = StringVar()

    Entry(log_window, textvariable=username).grid(row=0, column=1)
    Entry(log_window, textvariable=password, show='*').grid(row=1, column=1)

    Button(log_window, text='Login', command=lambda: validate_login(username, password, root_window, log_window)).grid(
        row=4,
        column=0)
    Button(log_window, text='Register',
           command=lambda: registration_window.registration_window(root_window, log_window)).grid(row=4,
                                                                                                  column=1)

    def close():
        if messagebox.askokcancel('Quit', 'Do You Want To Quit?'):
            root_window.destroy()

    log_window.protocol('WM_DELETE_WINDOW', close)
