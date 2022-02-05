from tkinter import *
from windows import dashboard_window as dw
from windows.test_windows.future_test import future_test_date_input_window as fti
from windows.window_utillities import window_icon as wi
from windows.window_utillities import window_protocol as wp
import tkinter


def future_test_window(root_window, user):
    future_window = tkinter.Toplevel(root_window)
    future_window.geometry('320x150')
    future_window.title('Future Test')
    future_window.iconbitmap(wi.window_icon())

    test_label = Label(future_window, text='Select a lottery to predict.')

    power_ball_button = Button(future_window, text='Powerball',
                               command=lambda: power_ball(root_window, future_window, user))

    empty_space_one = Label(future_window, text='')

    mega_millions_button = Button(future_window, text='Mega Millions',
                                  command=lambda: mega_millions(root_window, future_window, user))
    lotto_america_button = Button(future_window, text='Lotto America',
                                  command=lambda: lotto_america(root_window, future_window, user))

    empty_space_two = Label(future_window, text='')

    cash_four_life_button = Button(future_window, text='Cash 4 Life',
                                   command=lambda: cash_four_life(root_window, future_window, user))
    tn_cash_button = Button(future_window, text='TN Cash',
                            command=lambda: tn_cash(root_window, future_window, user))

    dashboard_button = Button(future_window, text='Return To Dashboard',
                              command=lambda: dash_board(root_window, future_window, user))

    test_label.grid(row=0, column=1)
    power_ball_button.grid(row=1, column=0)
    empty_space_one.grid(row=2, column=0)
    mega_millions_button.grid(row=3, column=0)
    lotto_america_button.grid(row=1, column=2)
    empty_space_two.grid(row=2, column=3)
    cash_four_life_button.grid(row=3, column=2)
    tn_cash_button.grid(row=4, column=1)
    dashboard_button.grid(row=5, column=1)

    wp.quit_confirmation(root_window, future_window)


def power_ball(root_window, future_window, user):
    date_input(root_window, future_window, 'Powerball', user)


def mega_millions(root_window, future_window, user):
    date_input(root_window, future_window, 'Mega Millions', user)


def lotto_america(root_window, future_window, user):
    date_input(root_window, future_window, 'Lotto America', user)


def cash_four_life(root_window, future_window, user):
    date_input(root_window, future_window, 'Cash 4 Life', user)


def tn_cash(root_window, future_window, user):
    date_input(root_window, future_window, 'TN Cash', user)


def date_input(root_window, future_window, selected_lottery, user):
    future_window.destroy()
    fti.input_date(root_window, selected_lottery, user)


def dash_board(root_window, future_window, user):
    future_window.destroy()
    dw.dashboard_window(root_window, user)