from entities import user
from tkinter import *
from windows.test_windows import practice_test_window
from windows.window_utillities import window_protocol
import tkinter


def dashboard_window(root_window, logged_in_user):
    dash_window = tkinter.Toplevel(root_window)

    dash_window.geometry('450x200')

    dash_window.title(user.User.first_name(logged_in_user) + "'s Dashboard")

    Button(dash_window, text='Start A Practice Test', width=20,
           command=lambda: practice_test(root_window, dash_window, logged_in_user)).grid(row=0, column=0)
    Label(dash_window, text='', width=20).grid(row=0, column=1)
    Button(dash_window, text='Start A Future Test', width=20).grid(row=0, column=2)

    window_protocol.quit_confirmation(root_window, dash_window)


def practice_test(root_window, dash_window, logged_in_user):
    dash_window.destroy()
    practice_test_window.practice_test_window(root_window, logged_in_user)
