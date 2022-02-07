from tkinter import *
from windows import dashboard_window as dw
from windows.test_windows.future_test import future_test_date_input_window as fti
from windows.window_utillities import window_icon as wi
from windows.window_utillities import window_protocol as wp
import tkinter as tk


# This function creates a future test lottery selection window.
def future_test_window(root_window, user):
    future_window = tk.Toplevel(root_window)
    future_window.title('Future Test')
    future_window.iconbitmap(wi.window_icon())

    test_label = Label(future_window, text='Select a lottery to predict.', font="Times 12 bold")

    power_ball_button = Button(future_window, text='Powerball',
                               command=lambda: power_ball(root_window, future_window, user), font="Times 12 bold")

    mega_millions_button = Button(future_window, text='Mega Millions',
                                  command=lambda: mega_millions(root_window, future_window, user),
                                  font="Times 12 bold")
    lotto_america_button = Button(future_window, text='Lotto America',
                                  command=lambda: lotto_america(root_window, future_window, user),
                                  font="Times 12 bold")

    cash_four_life_button = Button(future_window, text='Cash 4 Life',
                                   command=lambda: cash_four_life(root_window, future_window, user),
                                   font="Times 12 bold")
    tn_cash_button = Button(future_window, text='TN Cash',
                            command=lambda: tn_cash(root_window, future_window, user), font="Times 12 bold")

    dashboard_button = Button(future_window, text='Return To Dashboard',
                              command=lambda: dash_board(root_window, future_window, user), font="Times 12 bold")

    test_label.grid(row=0, column=1, pady=10, padx=10)
    power_ball_button.grid(row=1, column=0, pady=10, padx=10)
    mega_millions_button.grid(row=2, column=0, pady=10, padx=10)
    lotto_america_button.grid(row=1, column=2, pady=10, padx=10)
    cash_four_life_button.grid(row=2, column=2, pady=10, padx=10)
    tn_cash_button.grid(row=3, column=1, pady=10, padx=10)
    dashboard_button.grid(row=4, column=1, pady=10, padx=10)

    wp.quit_confirmation(root_window, future_window)


# This function selects powerball for the future test session.
def power_ball(root_window, future_window, user):
    date_input(root_window, future_window, 'Powerball', user)


# This function selects mega millions for the future test session.
def mega_millions(root_window, future_window, user):
    date_input(root_window, future_window, 'Mega Millions', user)


# This function selects lotto america for the future test session.
def lotto_america(root_window, future_window, user):
    date_input(root_window, future_window, 'Lotto America', user)


# This function selects cash 4 life for the future test session.
def cash_four_life(root_window, future_window, user):
    date_input(root_window, future_window, 'Cash 4 Life', user)


# This function selects tn cash for the future test session.
def tn_cash(root_window, future_window, user):
    date_input(root_window, future_window, 'TN Cash', user)


# This function passes the selected lottery and launches the date selection window.
def date_input(root_window, future_window, selected_lottery, user):
    future_window.destroy()
    fti.input_date(root_window, selected_lottery, user)


# This function returns to the dashboard.
def dash_board(root_window, future_window, user):
    future_window.destroy()
    dw.dashboard_window(root_window, user)
