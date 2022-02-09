import tkinter as tk
from tkinter import *
from tkinter import ttk

from entities import user as u
from windows.future_test_updates import future_test_update_input_window as ftu
from windows.test_windows.future_test import future_test_home_window as fth
from windows.test_windows.practice_test import practice_test_home_window as pth
from windows.window_utillities import window_icon as wi
from windows.window_utillities import window_protocol as wp


# This function creates a dashboard window for a user after log in.
def dashboard_window(root_window, user):
    # Window details are set.
    dash_window = tk.Toplevel(root_window)
    first_name = u.User.first_name(user)
    dash_window.title(first_name + "'s Dashboard")
    dash_window.iconbitmap(wi.window_icon())

    # Frames to hold widgets are created.
    parent_frame = LabelFrame(dash_window)
    practice_frame = LabelFrame(parent_frame)
    future_frame = LabelFrame(parent_frame)
    saved_tests_frame = LabelFrame(dash_window)

    # Buttons are created and have the functionality to start either a practice test or future test.
    practice_button = Button(practice_frame, text='Start A Practice Test', width=20,
                             command=lambda: practice_test(root_window, dash_window, user), font='Times 12 bold')
    future_button = Button(future_frame, text='Start A Future Test', width=20,
                           command=lambda: future_test(root_window, dash_window, user), font='Times 12 bold')

    # Label is created.
    saved_tests_label = Label(saved_tests_frame, text='Select a saved future test to update.',
                              font='Times 12 bold')

    # Variable to hold selected saved future test from dropdown.
    selected_future_test = StringVar()

    # Using ttk library a dropdown is created and has a lambda function to get all saved future tests for a user.
    saved_tests_dropdown = ttk.Combobox(saved_tests_frame, values=get_saved_future_tests(user),
                                        textvariable=selected_future_test,
                                        font='Times 12 bold')

    # This button has a lambda function to allow a user to update a saved future test.
    update_button = Button(saved_tests_frame, text='Update', font='Times 12 bold',
                           command=lambda: submit(root_window, dash_window, user,
                                                  selected_future_test.get()))

    # Frames are packed into the dashboard window.
    parent_frame.pack()
    practice_frame.pack(side='left', padx=10)
    future_frame.pack(side='right', padx=10)
    saved_tests_frame.pack(pady=20)

    # Widgets are packed into their frames.
    practice_button.pack()
    future_button.pack()
    saved_tests_label.pack()
    saved_tests_dropdown.pack()
    update_button.pack()

    # This function prevents a user from accidentally closing the application when the close button is pressed.
    wp.quit_confirmation(root_window, dash_window)


# This function opens up a practice test window and closes the dashboard window.
def practice_test(root_window, dash_window, user):
    dash_window.destroy()
    pth.practice_test_window(root_window, user)


# This function opens up a future test window and closes the dashboard window.
def future_test(root_window, dash_window, user):
    dash_window.destroy()
    fth.future_test_window(root_window, user)


# This function retrieves all the saved future tests for a user.
def get_saved_future_tests(user):
    # File is found via its location and username.
    f = open('storage/future_tests/' + user.username + '_future_test_storage.txt', 'r')

    # The open file is converted into a list of saved future tests.
    saved_tests = f.readlines()

    # Empty list to hold the options of saved future tests is created.
    saved_tests_dropdown_options = []

    # For loop to iterate through all the saved test.
    for test in saved_tests:
        saved_test_dict = eval(test)

        lottery_name_list = saved_test_dict.get('lottery_name')
        lottery_name = lottery_name_list[0]
        lottery_date_list = saved_test_dict.get('lottery_date')
        lottery_date = lottery_date_list[0]

        # Using a saved future test's details and regex, each saved future test is turned into simple string to be used
        # as an option for the saved future test dropdown
        saved_tests_dropdown_options.append(lottery_name + ': ' + lottery_date)

    return saved_tests_dropdown_options


# This function uses the selected future test from the dropdown input and is compared with all the saved future tests
# and returns the matching future test to be updated.
def prepare_future_test(user, selected_future_test):
    selected_test = selected_future_test.split(': ')

    f = open('storage/future_tests/' + user.username + '_future_test_storage.txt', 'r')
    saved_tests = f.readlines()

    for test in saved_tests:
        saved_test_dict = eval(test)

        lottery_name_list = saved_test_dict.get('lottery_name')
        lottery_name = lottery_name_list[0]
        lottery_date_list = saved_test_dict.get('lottery_date')
        lottery_date = lottery_date_list[0]

        test_details = [lottery_name, lottery_date]

        if selected_test == test_details:
            return test


# This function calls prepare_future_test to pass the selected future test to be updated in the future update number
# input.
def submit(root_window, current_window, user, selected_future_test):
    prepared_future_test = prepare_future_test(user, selected_future_test)

    current_window.destroy()

    ftu.future_update_number_input(root_window, user, prepared_future_test)
