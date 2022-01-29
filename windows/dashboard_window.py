import tkinter
from tkinter import *
from tkinter import messagebox


def dashboard_window(root_window):

    dash_window = tkinter.Toplevel(root_window)

    dash_window.geometry('500x500')

    dash_window.title('Dashboard')

    def close():
        if messagebox.askokcancel('Quit', 'Do You Want To Quit?'):
            root_window.destroy()

    dash_window.protocol('WM_DELETE_WINDOW', close)
