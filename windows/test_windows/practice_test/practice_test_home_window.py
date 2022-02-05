from tkinter import *
from windows import dashboard_window as dw
from windows.test_windows.practice_test import practice_test_input_window as pti
from windows.window_utillities import window_icon as wi
from windows.window_utillities import window_protocol as wp
import tkinter


def practice_test_window(root_window, user):
    practice_window = tkinter.Toplevel(root_window)
    practice_window.title('Practice Test')
    practice_window.iconbitmap(wi.window_icon())

    test_label = Label(practice_window, text='Select a lottery to practice.', font="Times 12 bold")

    power_ball_button = Button(practice_window, text='Powerball',
                               command=lambda: power_ball(root_window, practice_window, user), font="Times 12 bold")

    mega_millions_button = Button(practice_window, text='Mega Millions',
                                  command=lambda: mega_millions(root_window, practice_window, user),
                                  font="Times 12 bold")
    lotto_america_button = Button(practice_window, text='Lotto America',
                                  command=lambda: lotto_america(root_window, practice_window, user),
                                  font="Times 12 bold")

    cash_four_life_button = Button(practice_window, text='Cash 4 Life',
                                   command=lambda: cash_four_life(root_window, practice_window, user),
                                   font="Times 12 bold")
    tn_cash_button = Button(practice_window, text='TN Cash',
                            command=lambda: tn_cash(root_window, practice_window, user), font="Times 12 bold")

    dashboard_button = Button(practice_window, text='Return To Dashboard',
                              command=lambda: dash_board(root_window, practice_window, user), font="Times 12 bold")

    test_label.grid(row=0, column=1, pady=10, padx=10)
    power_ball_button.grid(row=1, column=0, pady=10, padx=10)
    mega_millions_button.grid(row=2, column=0, pady=10, padx=10)
    lotto_america_button.grid(row=1, column=2, pady=10, padx=10)
    cash_four_life_button.grid(row=2, column=2, pady=10, padx=10)
    tn_cash_button.grid(row=3, column=1, pady=10, padx=10)
    dashboard_button.grid(row=4, column=1, pady=10, padx=10)

    wp.quit_confirmation(root_window, practice_window)


def power_ball(root_window, practice_window, user):
    practice_test_input(root_window, practice_window, 'Powerball', user)


def mega_millions(root_window, practice_window, user):
    practice_test_input(root_window, practice_window, 'Mega Millions', user)


def lotto_america(root_window, practice_window, user):
    practice_test_input(root_window, practice_window, 'Lotto America', user)


def cash_four_life(root_window, practice_window, user):
    practice_test_input(root_window, practice_window, 'Cash 4 Life', user)


def tn_cash(root_window, practice_window, user):
    practice_test_input(root_window, practice_window, 'TN Cash', user)


def practice_test_input(root_window, practice_window, selected_lottery, user):
    practice_window.destroy()
    pti.practice_session_item_guess(root_window, selected_lottery, user)


def dash_board(root_window, practice_window, user):
    practice_window.destroy()
    dw.dashboard_window(root_window, user)
