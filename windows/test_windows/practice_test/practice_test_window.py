from tkinter import *
from windows.test_windows.practice_test import practice_test_session_input_window
from windows.window_utillities import window_protocol
import tkinter


def practice_test_window(root_window, logged_in_user):
    p_test_window = tkinter.Toplevel(root_window)
    p_test_window.geometry('320x150')
    p_test_window.title('Practice Test')

    test_label = Label(p_test_window, text='Select a lottery to practice.')

    power_ball_button = Button(p_test_window, text='Powerball',
                               command=lambda: power_ball(root_window, p_test_window, logged_in_user))

    empty_space_one = Label(p_test_window, text='')

    mega_millions_button = Button(p_test_window, text='Mega Millions',
                                  command=lambda: mega_millions(root_window, p_test_window, logged_in_user))
    lotto_america_button = Button(p_test_window, text='Lotto America',
                                  command=lambda: lotto_america(root_window, p_test_window, logged_in_user))

    empty_space_two = Label(p_test_window, text='')

    cash_four_life_button = Button(p_test_window, text='Cash 4 Life',
                                   command=lambda: cash_four_life(root_window, p_test_window, logged_in_user))
    tn_cash_button = Button(p_test_window, text='TN Cash',
                            command=lambda: tn_cash(root_window, p_test_window, logged_in_user))

    dashboard_button = Button(p_test_window, text='Return To Dashboard')

    test_label.grid(row=0, column=1)
    power_ball_button.grid(row=1, column=0)
    empty_space_one.grid(row=2, column=0)
    mega_millions_button.grid(row=3, column=0)
    lotto_america_button.grid(row=1, column=2)
    empty_space_two.grid(row=2, column=3)
    cash_four_life_button.grid(row=3, column=2)
    tn_cash_button.grid(row=4, column=1)
    dashboard_button.grid(row=5, column=1)

    window_protocol.quit_confirmation(root_window, p_test_window)


def power_ball(root_window, p_test_window, logged_in_user):
    practice_test_input(root_window, p_test_window, 'Powerball', logged_in_user)


def mega_millions(root_window, p_test_window, logged_in_user):
    practice_test_input(root_window, p_test_window, 'Mega Millions', logged_in_user)


def lotto_america(root_window, p_test_window, logged_in_user):
    practice_test_input(root_window, p_test_window, 'Lotto America', logged_in_user)


def cash_four_life(root_window, p_test_window, logged_in_user):
    practice_test_input(root_window, p_test_window, 'Cash 4 Life', logged_in_user)


def tn_cash(root_window, p_test_window, logged_in_user):
    practice_test_input(root_window, p_test_window, 'TN Cash', logged_in_user)


def practice_test_input(root_window, p_test_window, selected_lottery, logged_in_user):
    p_test_window.destroy()
    practice_test_session_input_window.practice_test_session_input_window(root_window, selected_lottery, logged_in_user)