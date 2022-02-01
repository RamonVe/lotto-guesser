from tkinter import *
from windows import dashboard_window as dw
from windows.test_windows.practice_test import practice_test_input_window as pti
from windows.window_utillities import window_icon
from windows.window_utillities import window_protocol
import tkinter


def practice_test_window(root_window, user):
    practice_window = tkinter.Toplevel(root_window)
    practice_window.geometry('320x150')
    practice_window.title('Practice Test')
    practice_window.iconbitmap(window_icon.window_icon())

    test_label = Label(practice_window, text='Select a lottery to practice.')

    power_ball_button = Button(practice_window, text='Powerball',
                               command=lambda: power_ball(root_window, practice_window, user))

    empty_space_one = Label(practice_window, text='')

    mega_millions_button = Button(practice_window, text='Mega Millions',
                                  command=lambda: mega_millions(root_window, practice_window, user))
    lotto_america_button = Button(practice_window, text='Lotto America',
                                  command=lambda: lotto_america(root_window, practice_window, user))

    empty_space_two = Label(practice_window, text='')

    cash_four_life_button = Button(practice_window, text='Cash 4 Life',
                                   command=lambda: cash_four_life(root_window, practice_window, user))
    tn_cash_button = Button(practice_window, text='TN Cash',
                            command=lambda: tn_cash(root_window, practice_window, user))

    dashboard_button = Button(practice_window, text='Return To Dashboard',
                              command=lambda: dash_board(root_window, practice_window, user))

    test_label.grid(row=0, column=1)
    power_ball_button.grid(row=1, column=0)
    empty_space_one.grid(row=2, column=0)
    mega_millions_button.grid(row=3, column=0)
    lotto_america_button.grid(row=1, column=2)
    empty_space_two.grid(row=2, column=3)
    cash_four_life_button.grid(row=3, column=2)
    tn_cash_button.grid(row=4, column=1)
    dashboard_button.grid(row=5, column=1)

    window_protocol.quit_confirmation(root_window, practice_window)


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
    pti.practice_input_window(root_window, selected_lottery, user)


def dash_board(root_window, practice_window, user):
    practice_window.destroy()
    dw.dashboard_window(root_window, user)
