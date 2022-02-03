from entities import user as u
from tkinter import *
from windows.test_windows.future_test import future_test_home_window as fth
from windows.test_windows.practice_test import practice_test_home_window as pth
from windows.window_utillities import window_icon as wi
from windows.window_utillities import window_protocol as wp
import tkinter


def dashboard_window(root_window, user):
    dash_window = tkinter.Toplevel(root_window)
    dash_window.geometry('450x200')
    first_name = u.User.first_name(user)
    dash_window.title(first_name + "'s Dashboard")
    dash_window.iconbitmap(wi.window_icon())

    Button(dash_window, text='Start A Practice Test', width=20,
           command=lambda: practice_test(root_window, dash_window, user)).grid(row=0, column=0)
    Label(dash_window, text='', width=20).grid(row=0, column=1)
    Button(dash_window, text='Start A Future Test', width=20,
           command=lambda: future_test(root_window, dash_window, user)).grid(row=0, column=2)

    wp.quit_confirmation(root_window, dash_window)


def practice_test(root_window, dash_window, user):
    dash_window.destroy()
    pth.practice_test_window(root_window, user)


def future_test(root_window, dash_window, user):
    dash_window.destroy()
    fth.future_test_window(root_window, user)
