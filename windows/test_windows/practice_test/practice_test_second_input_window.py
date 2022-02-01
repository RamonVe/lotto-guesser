import tkinter
from tkinter import *
from entities import user as u
from windows.test_windows.practice_test import practice_test_session_results_window as psr
from windows.window_utillities import lottery_color as lc
from windows.window_utillities import window_protocol as wp


def practice_session_item_guess(root_window, user, lottery_details, time, lotto_guess_input):
    input_window = tkinter.Toplevel(root_window)
    input_window.geometry('918x250')
    user_first_name = u.User.first_name(user)
    lottery_name = lottery_details[0]
    input_window.title(user_first_name + "'s " + lottery_name + ' Ball Item Guess')

    time_frame = LabelFrame(input_window, text='Total Time')
    test_info_frame = LabelFrame(input_window)
    geomagnetic_frame = LabelFrame(input_window, text='Geomagnetic')
    input_frame = LabelFrame(input_window, text='What object is each ball?')

    time_frame.grid(row=0, column=0, padx=20)
    test_info_frame.grid(row=0, column=1, padx=20)
    geomagnetic_frame.grid(row=0, column=2, padx=20)
    input_frame.grid(row=1, column=1, padx=20, pady=50)

    time_label = Label(time_frame, text=time)
    time_label.pack()

    lottery_name = lottery_details[0]
    lottery_date = lottery_details[1]

    test_label = Label(test_info_frame,
                       text='What were the winning numbers for the ' + lottery_name + ' on ' + lottery_date + '?')
    test_label.pack()

    geomagnetic_label = Label(geomagnetic_frame, text='Geomagnetic')
    geomagnetic_label.pack()

    ball_one = lotto_guess_input[0]
    ball_two = lotto_guess_input[1]
    ball_three = lotto_guess_input[2]
    ball_four = lotto_guess_input[3]
    ball_five = lotto_guess_input[4]

    first_input_label = Label(input_frame, text='Ball 1: ' + ball_one)
    second_input_label = Label(input_frame, text='Ball 2: ' + ball_two)
    third_input_label = Label(input_frame, text='Ball 3: ' + ball_three)
    fourth_input_label = Label(input_frame, text='Ball 4: ' + ball_four)
    fifth_input_label = Label(input_frame, text='Ball 5: ' + ball_five)

    option_one = StringVar()
    option_two = StringVar()
    option_three = StringVar()
    option_four = StringVar()
    option_five = StringVar()
    options = ['item', 'taste', 'smell', 'sound', 'color']

    first_entry = OptionMenu(input_frame, option_one, *options)
    first_entry.config(width=6, background='white')
    second_entry = OptionMenu(input_frame, option_two, *options)
    second_entry.config(width=6, background='white')
    third_entry = OptionMenu(input_frame, option_three, *options)
    third_entry.config(width=6, background='white')
    fourth_entry = OptionMenu(input_frame, option_four, *options)
    fourth_entry.config(width=6, background='white')
    fifth_entry = OptionMenu(input_frame, option_five, *options)
    fifth_entry.config(width=6, background=lc.color(lottery_name))

    submit_button = Button(input_frame, text='Submit',
                           command=lambda: submit(root_window, input_window, user, lottery_details, time,
                                                  lotto_guess_input, options))

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


def submit(root_window, current_window, user, lottery_details, time, guesses, options):

    # Console debug output
    print(time)
    for guess in guesses:
        print(guess)

    current_window.destroy()

    psr.results(root_window, user, lottery_details, time, guesses, options)
