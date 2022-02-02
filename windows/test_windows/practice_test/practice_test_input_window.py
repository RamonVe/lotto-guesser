from tkinter import *
from entities import user as u
from windows.test_windows.practice_test import past_lottery_randomizer as plr
from windows.test_windows.practice_test import practice_test_session_results_window as psr
from windows.test_windows.test_timer import timer as t
from windows.window_utillities import lottery_color as lc
from windows.window_utillities import window_icon as wi
from windows.window_utillities import window_protocol as wp
import tkinter


def practice_session_item_guess(root_window, lottery, user):
    input_window = tkinter.Toplevel(root_window)
    input_window.geometry('918x250')
    input_window.iconbitmap(wi.window_icon())
    user_first_name = u.User.first_name(user)
    input_window.title(user_first_name + "'s " + lottery + ' Practice Test Ball/Item Guess')

    time_frame = LabelFrame(input_window, text='Timer')
    test_info_frame = LabelFrame(input_window)
    geomagnetic_frame = LabelFrame(input_window, text='Geomagnetic')
    input_frame = LabelFrame(input_window, text='What object is each ball?')

    time_frame.grid(row=0, column=0, padx=20)
    test_info_frame.grid(row=0, column=1, padx=20)
    geomagnetic_frame.grid(row=0, column=2, padx=20)
    input_frame.grid(row=1, column=1, padx=20, pady=50)

    timer = t.Timer(time_frame)
    timer.start()

    random_lottery = plr.random_lottery_details(lottery)
    lottery_date = random_lottery[0:14]
    lotto_split = random_lottery.split(',', 2)
    second_lotto_split = lotto_split[1].split(' ', 2)
    winning_numbers = second_lotto_split[0]
    lottery_details = [lottery, lottery_date, winning_numbers]
    split_lottery = winning_numbers.split('-')

    print(split_lottery)

    test_label = Label(test_info_frame,
                       text='What were the winning numbers for the ' + lottery + ' on ' + lottery_date + '?')
    test_label.pack()

    geomagnetic_label = Label(geomagnetic_frame, text='Geomagnetic')
    geomagnetic_label.pack()

    first_input_label = Label(input_frame, text='Ball 1: ' + split_lottery[0])
    second_input_label = Label(input_frame, text='Ball 2: ' + split_lottery[1])
    third_input_label = Label(input_frame, text='Ball 3: ' + split_lottery[2])
    fourth_input_label = Label(input_frame, text='Ball 4: ' + split_lottery[3])
    fifth_input_label = Label(input_frame, text='Ball 5: ' + split_lottery[4])

    option_one = StringVar()
    option_two = StringVar()
    option_three = StringVar()
    option_four = StringVar()
    option_five = StringVar()
    options = ['item', 'taste', 'smell', 'sound', 'color']
    item_predictions = [option_one, option_two, option_three, option_four, option_five]

    first_entry = OptionMenu(input_frame, option_one, *options)
    first_entry.config(width=6, background='white')
    second_entry = OptionMenu(input_frame, option_two, *options)
    second_entry.config(width=6, background='white')
    third_entry = OptionMenu(input_frame, option_three, *options)
    third_entry.config(width=6, background='white')
    fourth_entry = OptionMenu(input_frame, option_four, *options)
    fourth_entry.config(width=6, background='white')
    fifth_entry = OptionMenu(input_frame, option_five, *options)
    fifth_entry.config(width=6, background=lc.color(lottery))

    submit_button = Button(input_frame, text='Submit',
                           command=lambda: submit(root_window, input_window, user, lottery_details, timer,
                                                  item_predictions))

    first_input_label.grid(row=0, column=0)
    second_input_label.grid(row=0, column=1)
    third_input_label.grid(row=0, column=2)
    fourth_input_label.grid(row=0, column=3)
    fifth_input_label.grid(row=0, column=4)

    first_entry.grid(row=1, column=0, padx=5)
    second_entry.grid(row=1, column=1, padx=5)
    third_entry.grid(row=1, column=2, padx=5)
    fourth_entry.grid(row=1, column=3, padx=5)
    fifth_entry.grid(row=1, column=4, padx=5)

    submit_button.grid(row=2, column=2, padx=20, pady=20)

    wp.quit_confirmation(root_window, input_window)


def submit(root_window, current_window, user, lottery_details, timer, item_prediction):
    timer.stop()

    time = timer.time_as_string

    # Console debug output
    print(time)
    for prediction in item_prediction:
        print(prediction)

    current_window.destroy()

    psr.session_results(root_window, user, lottery_details, time, item_prediction)
