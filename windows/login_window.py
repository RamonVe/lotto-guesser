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
    log_window.title('Login')
    log_window.iconbitmap(wi.window_icon())

    user_frame = LabelFrame(log_window)
    pass_frame = LabelFrame(log_window)
    button_frame = LabelFrame(log_window)

    username = StringVar()
    user_label = Label(user_frame, text='User Name:', font="Times 12 bold")
    user_entry = Entry(user_frame, textvariable=username)

    password = StringVar()
    pass_label = Label(pass_frame, text='Password:', font="Times 12 bold")
    pass_entry = Entry(pass_frame, textvariable=password, show='*')

    login_button = Button(button_frame, text='Login',
                          command=lambda: validate_login(username, password, root_window, log_window),
                          font="Times 12 bold")
    register_button = Button(button_frame, text='Register',
                             command=lambda: rw.registration_window(root_window, log_window), font="Times 12 bold")

    user_frame.pack(padx=5, pady=5)
    pass_frame.pack(padx=5, pady=5)
    button_frame.pack(padx=5, pady=5)

    user_label.grid(row=0, column=0)
    user_entry.grid(row=0, column=1)
    pass_label.grid(row=1, column=0)
    pass_entry.grid(row=1, column=1)
    login_button.grid(row=2, column=0)
    register_button.grid(row=2, column=1)

    wp.quit_confirmation(root_window, log_window)


def validate_login(username, password, root_window, log_window):
    user_name = username.get()
    pass_word = password.get()

    users = ldu.load_users()

    for user in users:
        if user.username == user_name:
            if user.password != pass_word:
                m.showwarning('Wrong Password!', 'You have entered the wrong password, try again!')
            else:
                log_window.destroy()
                dashboard(root_window, user)
                break
        else:
            if user_name == '' and pass_word == '':
                m.showwarning('Empty Fields!', 'Enter a username and password to log in!')
            else:
                m.showwarning('No user found!', 'No user with that username found, try again!')
                break


def dashboard(root_window, logged_in_user):
    dw.dashboard_window(root_window, logged_in_user)
