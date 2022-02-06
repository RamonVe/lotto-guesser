from entities import user as u
from tkinter import *
from tkinter import ttk
from windows.future_test_updates import future_test_update_input_window as ftu
from windows.test_windows.future_test import future_test_home_window as fth
from windows.test_windows.practice_test import practice_test_home_window as pth
from windows.window_utillities import window_icon as wi
from windows.window_utillities import window_protocol as wp
import re
import tkinter


def dashboard_window(root_window, user):
    dash_window = tkinter.Toplevel(root_window)
    first_name = u.User.first_name(user)
    dash_window.title(first_name + "'s Dashboard")
    dash_window.iconbitmap(wi.window_icon())

    parent_frame = LabelFrame(dash_window)
    practice_frame = LabelFrame(parent_frame)
    future_frame = LabelFrame(parent_frame)
    saved_tests_frame = LabelFrame(dash_window)

    practice_button = Button(practice_frame, text='Start A Practice Test', width=20,
                             command=lambda: practice_test(root_window, dash_window, user), font='Times 12 bold')

    future_button = Button(future_frame, text='Start A Future Test', width=20,
                           command=lambda: future_test(root_window, dash_window, user), font='Times 12 bold')

    saved_tests_label = Label(saved_tests_frame, text='Select a saved future test to update.',
                              font='Times 12 bold')

    selected_future_test = StringVar()
    saved_tests_dropdown = ttk.Combobox(saved_tests_frame, values=get_saved_future_tests(user),
                                        textvariable=selected_future_test,
                                        font='Times 12 bold')

    update_button = Button(saved_tests_frame, text='Update', font='Times 12 bold',
                           command=lambda: submit(root_window, dash_window, user,
                                                  selected_future_test.get()))

    parent_frame.pack()
    practice_frame.pack(side='left', padx=10)
    future_frame.pack(side='right', padx=10)
    saved_tests_frame.pack(pady=20)

    practice_button.pack()
    future_button.pack()
    saved_tests_label.pack()
    saved_tests_dropdown.pack()
    update_button.pack()

    wp.quit_confirmation(root_window, dash_window)


def practice_test(root_window, dash_window, user):
    dash_window.destroy()
    pth.practice_test_window(root_window, user)


def future_test(root_window, dash_window, user):
    dash_window.destroy()
    fth.future_test_window(root_window, user)


def get_saved_future_tests(user):
    f = open('storage/future_tests/' + user.username + '_future_test_storage.txt', 'r')
    saved_tests = f.readlines()

    saved_tests_dropdown_options = []
    for tests in saved_tests:
        split = tests.split(',')
        lottery_info = split[4]
        lottery_date = split[5]
        lotto_name = re.findall('"([^"]*)"', lottery_info)
        lotto_date = re.findall('"([^"]*)"', lottery_date)
        saved_tests_dropdown_options.append(lotto_name[1] + ': ' + lotto_date[1])

    return saved_tests_dropdown_options


def prepare_future_test(user, selected_future_test):
    selected_test = selected_future_test.split(': ')

    f = open('storage/future_tests/' + user.username + '_future_test_storage.txt', 'r')
    saved_tests = f.readlines()

    for test in saved_tests:
        split_test = test.split(',')
        lottery_info = split_test[4]
        lottery_date = split_test[5]

        lotto_name = re.findall('"([^"]*)"', lottery_info)
        lotto_date = re.findall('"([^"]*)"', lottery_date)

        test_details = [lotto_name[1], lotto_date[1]]

        if selected_test == test_details:
            return test


def submit(root_window, current_window, user, selected_future_test):
    prepared_future_test = prepare_future_test(user, selected_future_test)

    current_window.destroy()

    ftu.future_update_number_input(root_window, user, prepared_future_test)
