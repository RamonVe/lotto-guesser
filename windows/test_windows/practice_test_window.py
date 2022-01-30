from tkinter import *
from windows.window_utillities import window_protocol
import tkinter


def practice_test_window(root_window, logged_in_user):
    p_test_window = tkinter.Toplevel(root_window)
    p_test_window.geometry('320x150')
    p_test_window.title('Practice Test')

    test_label = Label(p_test_window, text='Select a lottery to practice.')
    power_ball_button = Button(p_test_window, text='Powerball')
    empty_space_one = Label(p_test_window, text='', )
    mega_millions_button = Button(p_test_window, text='Mega Millions')
    lotto_america_button = Button(p_test_window, text='Lotto America')
    empty_space_two = Label(p_test_window, text='')
    cash_four_life_button = Button(p_test_window, text='Cash 4 Life')
    tn_cash_button = Button(p_test_window, text='TN Cash')
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
