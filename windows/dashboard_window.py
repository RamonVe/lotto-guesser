import tkinter
from entities import user
from tkinter import *
from tkinter import messagebox


def dashboard_window(root_window, logged_in_user):

    dash_window = tkinter.Toplevel(root_window)

    dash_window.geometry('500x500')

    dash_window.title(user.User.first_name(logged_in_user) + "'s Dashboard")

    def close():
        if messagebox.askokcancel('Quit', 'Do You Want To Quit?'):
            root_window.destroy()

    dash_window.protocol('WM_DELETE_WINDOW', close)
