from datetime import datetime
from tkinter import *
from tkcalendar import Calendar
from windows.test_windows.future_test import future_test_home_window as fth
from windows.test_windows.future_test import future_test_number_input_window as ftn
from windows.window_utillities import window_icon as wi
from windows.window_utillities import window_protocol as wp
import tkinter


def input_date(root_window, selected_lottery, user):
    input_window = tkinter.Toplevel(root_window)
    input_window.geometry('400x400')
    input_window.iconbitmap(wi.window_icon())
    input_window.title('Future ' + selected_lottery + ' Date Selection')

    instruction_label = Label(input_window,
                              text='Select a future date for ' + selected_lottery + '\n' + days(selected_lottery))

    instruction_label.pack(pady=20)

    date = StringVar()
    calendar = Calendar(input_window, textvariable=date, selectmode='day', mindate=datetime.now())

    calendar.pack(pady=10)

    Button(input_window, text='Submit',
           command=lambda: submit(root_window, input_window, selected_lottery, date.get(), user)).pack(pady=10)

    Button(input_window, text='Return To Lottery Selection',
           command=lambda: lottery_selection(root_window, input_window, user)).pack(pady=5)

    wp.quit_confirmation(root_window, input_window)


def days(selected_lottery):
    if selected_lottery == 'Powerball':
        return 'The Powerball is only drawn on Monday, Wednesday and Saturday'

    elif selected_lottery == 'Mega Millions':
        return 'The Mega Millions is only drawn on Tuesday and Friday'

    elif selected_lottery == 'Lotto America':
        return 'The Lotto America is only drawn on Wednesday and Saturday'

    elif selected_lottery == 'Cash 4 Life':
        return 'The Cash 4 Life is drawn everyday.'

    else:
        return 'The TN Cash is only drawn on Monday, Wednesday and Friday'


def submit(root_window, input_window, selected_lottery, selected_date, user):
    print(selected_date)

    input_window.destroy()

    ftn.future_session_number_input(root_window, selected_lottery, selected_date, user)


def lottery_selection(root_window, input_window, user):
    input_window.destroy()

    fth.future_test_window(root_window, user)
