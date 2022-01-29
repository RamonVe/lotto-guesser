from tkinter import *
from tkinter import messagebox
from windows import dashboard_window
from windows import registration_window
import tkinter


def validate_login(user_name, pass_word, root_window, log_window):
    print('username entered :', user_name.get())
    print('password entered :', pass_word.get())
    log_window.destroy()
    dashboard(root_window)
    return


def dashboard(root_window):
    dashboard_window.dashboard_window(root_window)


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

    # Button(log_window, text='Return to root window.', command=lambda: change_window(
    #     log_window, root_window)).grid(row=6, column=0)

    def close():
        if messagebox.askokcancel('Quit', 'Do You Want To Quit?'):
            root_window.destroy()

    log_window.protocol('WM_DELETE_WINDOW', close)

# def change_window(log_window, root_window):
#     # remove the other window entirely
#     log_window.destroy()
#
#     # make root_window visible again
#     root_window.iconify()
#     root_window.deiconify()
