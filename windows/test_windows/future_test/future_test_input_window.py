from entities import future_test as fu
from entities import user as u
from geomagnetic_data import geomagnetic_retrieval as gr
from storage import local_data_utilities as ldu
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from windows import dashboard_window as dw
from windows.test_windows.item_randomizer import item_randomizer as ir
from windows.test_windows.test_timer import timer as t
from windows.window_utillities import lottery_color as lc
from windows.window_utillities import window_icon as wi
from windows.window_utillities import window_protocol as wp
import tkinter as tk


# This function creates a future test input window.
def future_session_input(root_window, selected_lottery, selected_date, user):
    input_window = tk.Toplevel(root_window)
    input_window.grid_columnconfigure(0, weight=1)
    input_window.grid_rowconfigure(0, weight=1)
    input_window.iconbitmap(wi.window_icon())
    user_first_name = u.User.first_name(user)
    input_window.title(user_first_name + "'s " + selected_lottery + ' Ball Number Guess')

    time_frame = LabelFrame(input_window, text='Timer', font='Times 12 bold')
    test_info_frame = LabelFrame(input_window)
    geomagnetic_frame = LabelFrame(input_window, text='Geomagnetic', font='Times 12 bold')
    input_frame = LabelFrame(input_window, text='What item is each ball?', font='Times 12 bold')

    timer = t.Timer(time_frame)
    timer.start()

    test_label = Label(test_info_frame,
                       text=selected_lottery + ' prediction' + ' for ' + selected_date, font="Times 12 bold")

    kp = gr.get_kp()
    bz = gr.get_bz()
    geomagnetic_label = Label(geomagnetic_frame, text='KP: ' + kp + ' BZ: ' + bz, font="Times 12 bold")

    first_input_label = Label(input_frame, text='Ball 1: ', background='white', font='Times 12 bold')
    second_input_label = Label(input_frame, text='Ball 2: ', background='white', font='Times 12 bold')
    third_input_label = Label(input_frame, text='Ball 3: ', background='white', font='Times 12 bold')
    fourth_input_label = Label(input_frame, text='Ball 4: ', background='white', font='Times 12 bold')
    fifth_input_label = Label(input_frame, text='Ball 5: ',
                              background=lc.color(selected_lottery), foreground=lc.text_color(selected_lottery),
                              font='Times 12 bold')

    option_one = StringVar()
    option_two = StringVar()
    option_three = StringVar()
    option_four = StringVar()
    option_five = StringVar()

    option_one.set('Select an item.')
    option_two.set('Select an item.')
    option_three.set('Select an item.')
    option_four.set('Select an item.')
    option_five.set('Select an item.')

    item_list = open('storage/item_list', 'r').readlines()
    pure_items = []
    for item in item_list:
        pure_items.append(item.strip())

    first_item_entry = ttk.Combobox(input_frame, values=pure_items, textvariable=option_one)
    second_item_entry = ttk.Combobox(input_frame, values=pure_items, textvariable=option_two)
    third_item_entry = ttk.Combobox(input_frame, values=pure_items, textvariable=option_three)
    fourth_item_entry = ttk.Combobox(input_frame, values=pure_items, textvariable=option_four)
    fifth_item_entry = ttk.Combobox(input_frame, values=pure_items, textvariable=option_five)

    item_guess = [option_one, option_two, option_three, option_four, option_five]

    submit_button = Button(input_frame, text='Save Future Test',
                           command=lambda: submit(root_window, input_window, selected_lottery, selected_date, user,
                                                  timer, item_guess))

    time_frame.grid(row=0, column=0, padx=20, sticky=NW)
    time_frame.grid_rowconfigure(0, weight=1)
    time_frame.grid_columnconfigure(0, weight=1)

    test_info_frame.grid(row=0, column=1, padx=20, sticky=N)
    test_info_frame.grid_rowconfigure(0, weight=1)
    test_info_frame.grid_columnconfigure(1, weight=1)

    geomagnetic_frame.grid(row=0, column=2, padx=20, sticky=NE)
    geomagnetic_frame.grid_rowconfigure(0, weight=1)
    geomagnetic_frame.grid_columnconfigure(2, weight=1)

    input_frame.grid(row=1, column=1, padx=20, pady=20, sticky=S)
    input_frame.grid_rowconfigure(1, weight=1)
    input_frame.grid_columnconfigure(1, weight=1)

    timer.label.pack()
    test_label.pack()
    geomagnetic_label.pack()

    first_input_label.grid(row=0, column=0, padx=5, pady=5)
    second_input_label.grid(row=0, column=1, padx=5, pady=5)
    third_input_label.grid(row=0, column=2, padx=5, pady=5)
    fourth_input_label.grid(row=0, column=3, padx=5, pady=5)
    fifth_input_label.grid(row=0, column=4, padx=5, pady=5)

    first_item_entry.grid(row=2, column=0, padx=5, pady=5)
    second_item_entry.grid(row=2, column=1, padx=5, pady=5)
    third_item_entry.grid(row=2, column=2, padx=5, pady=5)
    fourth_item_entry.grid(row=2, column=3, padx=5, pady=5)
    fifth_item_entry.grid(row=2, column=4, padx=5, pady=5)

    submit_button.grid(row=3, column=2, padx=20, pady=20)

    wp.quit_confirmation(root_window, input_window)


# This function passes all the data from the input window and saves the data as an object in a text file list.
def submit(root_window, current_window, selected_lottery, selected_date, user, timer, item_guess):
    timer.stop()

    time = timer.time_as_string

    serializable_item_guess = []
    for item in item_guess:
        serializable_item_guess.append(item.get())

    random_number_item_pair = ir.random_pair()

    future_test = fu.FutureTest(user, time, selected_lottery, selected_date, serializable_item_guess,
                                random_number_item_pair)

    ldu.save_future_test(user, future_test)

    messagebox.showinfo('Success!', selected_lottery + ' for ' + selected_date + ' has been saved!')

    current_window.destroy()

    dw.dashboard_window(root_window, user)
