from tkinter import *
from tkinter import ttk
from entities import user as u
from geomagnetic_data import geomagnetic_retrieval as gr
from windows.test_windows.practice_test import past_lottery_randomizer as plr
from windows.test_windows.practice_test import practice_test_session_results_window as psr
from windows.test_windows.test_timer import timer as t
from windows.window_utillities import lottery_color as lc
from windows.window_utillities import window_icon as wi
from windows.window_utillities import window_protocol as wp
import tkinter


def practice_session_item_guess(root_window, selected_lottery, user):
    input_window = tkinter.Toplevel(root_window)
    input_window.grid_columnconfigure(0, weight=1)
    input_window.grid_rowconfigure(0, weight=1)
    input_window.iconbitmap(wi.window_icon())
    user_first_name = u.User.first_name(user)
    input_window.title(user_first_name + "'s " + selected_lottery + ' Practice Test Ball/Item Guess')

    time_frame = LabelFrame(input_window, text='Timer', font="Times 12 bold")
    test_info_frame = LabelFrame(input_window)
    geomagnetic_frame = LabelFrame(input_window, text='Geomagnetic', font="Times 12 bold")
    input_frame = LabelFrame(input_window, text='What item is each ball?', font="Times 12 bold")

    timer = t.Timer(time_frame)
    timer.start()

    random_lottery = plr.random_lottery_details(selected_lottery)
    lottery_date = random_lottery[0:14]
    lottery_details = [selected_lottery, lottery_date]

    lotto_split = random_lottery.split(',', 2)
    second_lotto_split = lotto_split[1].split(' ', 2)
    winning_numbers = second_lotto_split[0]
    winning_number_list = winning_numbers.split('-')

    test_label = Label(test_info_frame,
                       text=selected_lottery + ' on ' + lottery_date, font="Times 12 bold")

    kp = gr.get_kp()
    bz = gr.get_bz()
    geomagnetic_label = Label(geomagnetic_frame, text='KP: ' + kp + ' BZ: ' + bz, font="Times 12 bold")

    first_input_label = Label(input_frame, text='Ball 1: ', background='white', font="Times 12 bold")
    second_input_label = Label(input_frame, text='Ball 2: ', background='white', font="Times 12 bold")
    third_input_label = Label(input_frame, text='Ball 3: ', background='white', font="Times 12 bold")
    fourth_input_label = Label(input_frame, text='Ball 4: ', background='white', font="Times 12 bold")
    fifth_input_label = Label(input_frame, text='Ball 5: ',
                              background=lc.color(selected_lottery), foreground=lc.text_color(selected_lottery),
                              font="Times 12 bold")

    item_list = open('storage/item_list', 'r').readlines()
    pure_items = []
    for item in item_list:
        pure_items.append(item.strip())

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

    first_entry = ttk.Combobox(input_frame, values=pure_items, textvariable=option_one, width=20, font="Times 12 bold")
    second_entry = ttk.Combobox(input_frame, values=pure_items, textvariable=option_two, width=20, font="Times 12 bold")
    third_entry = ttk.Combobox(input_frame, values=pure_items, textvariable=option_three, width=20,
                               font="Times 12 bold")
    fourth_entry = ttk.Combobox(input_frame, values=pure_items, textvariable=option_four, width=20,
                                font="Times 12 bold")
    fifth_entry = ttk.Combobox(input_frame, values=pure_items, textvariable=option_five, width=20, font="Times 12 bold")

    item_predictions = [option_one, option_two, option_three, option_four, option_five]

    submit_button = Button(input_frame, text='Submit',
                           command=lambda: submit(root_window, input_window, user, lottery_details, winning_number_list,
                                                  timer, item_predictions), font="Times 12 bold")

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

    first_input_label.grid(row=0, column=0, padx=5)
    second_input_label.grid(row=0, column=1, padx=5)
    third_input_label.grid(row=0, column=2, padx=5)
    fourth_input_label.grid(row=0, column=3, padx=5)
    fifth_input_label.grid(row=0, column=4, padx=5)

    first_entry.grid(row=1, column=0, padx=5)
    second_entry.grid(row=1, column=1, padx=5)
    third_entry.grid(row=1, column=2, padx=5)
    fourth_entry.grid(row=1, column=3, padx=5)
    fifth_entry.grid(row=1, column=4, padx=5)

    submit_button.grid(row=2, column=2, padx=20, pady=20)

    wp.quit_confirmation(root_window, input_window)


def submit(root_window, current_window, user, lottery_details, winning_number_list, timer, item_prediction):
    timer.stop()

    time = timer.time_as_string

    # Console debug output
    # print(winning_number_list)
    # print(time)
    #
    # for prediction in item_prediction:
    #     print(prediction.get())

    current_window.destroy()

    psr.session_results(root_window, user, lottery_details, winning_number_list, time, item_prediction)
