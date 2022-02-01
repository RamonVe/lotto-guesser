from tkinter import *
from tkinter import messagebox as m
from storage import local_data_utilities as ldu
from windows import dashboard_window as dw
from windows import registration_window as rw
from windows.window_utillities import window_icon as wi
from windows.window_utillities import window_protocol as wp
import tkinter


def login_window(root_window):
    log_window = tkinter.Toplevel(root_window)
    log_window.geometry('220x100')
    log_window.title('Login')
    log_window.iconbitmap(wi.window_icon())

    user_label = Label(log_window, text='User Name')
    pass_label = Label(log_window, text='Password')

    username = StringVar()
    password = StringVar()

    user_entry = Entry(log_window, textvariable=username)
    pass_entry = Entry(log_window, textvariable=password, show='*')

    login_button = Button(log_window, text='Login',
                          command=lambda: validate_login(username, password, root_window, log_window))
    register_button = Button(log_window, text='Register',
                             command=lambda: rw.registration_window(root_window, log_window))

    user_label.grid(row=0, column=0)
    pass_label.grid(row=1, column=0)
    user_entry.grid(row=0, column=1)
    pass_entry.grid(row=1, column=1)
    login_button.grid(row=4, column=0)
    register_button.grid(row=4, column=1)

    wp.quit_confirmation(root_window, log_window)


def validate_login(username, password, root_window, log_window):
    user_name = username.get()
    pass_word = password.get()
    if user_name == '' and pass_word == '':
        m.showwarning('Empty Fields!', 'Enter a username and password to log in!')

    users = ldu.load_users()

    for user in users:
        if user.username == user_name:
            if user.password != pass_word:
                m.showwarning('Wrong Password!', 'You have entered the wrong password, try again!')
            else:
                log_window.destroy()
                dashboard(root_window, user)
                break


def dashboard(root_window, logged_in_user):
    dw.dashboard_window(root_window, logged_in_user)
