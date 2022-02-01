from entities import user as u
from tkinter import *
from windows.test_windows.practice_test import practice_test_second_input_window as psi
from windows.test_windows.practice_test import past_lottery_randomizer as plr
from windows.test_windows.test_timer import timer as t
from windows.window_utillities import window_protocol as wp
import tkinter


def practice_input_window(root_window, lottery, user):
    input_window = tkinter.Toplevel(root_window)
    input_window.geometry('918x300')
    first_name = u.User.first_name(user)
    input_window.title(first_name + "'s " + lottery + ' Practice Test Session')

    timer_frame = LabelFrame(input_window, text='Timer')
    info_frame = LabelFrame(input_window)
    geomagnetic_frame = LabelFrame(input_window, text='Geomagnetic')
    input_frame = LabelFrame(input_window, text='Input')

    timer_frame.grid(row=0, column=0, padx=20)
    info_frame.grid(row=0, column=1, padx=20)
    geomagnetic_frame.grid(row=0, column=2, padx=20)
    input_frame.grid(row=1, column=1, padx=20, pady=50)

    timer = t.Timer(timer_frame)
    timer.start()

    random_details = plr.random_lottery_details(lottery)
    random_date = random_details[0:14]
    lotto_split = random_details.split(',', 2)
    second_lotto_split = lotto_split[1].split(' ', 2)
    winning_numbers = second_lotto_split[0]
    lottery_details = [lottery, random_date, winning_numbers]

    test_label = Label(info_frame,
                       text='What were the winning numbers for the ' + lottery + ' on ' + random_date + '?')
    test_label.pack()

    geomagnetic_label = Label(geomagnetic_frame, text='Geomagnetic')
    geomagnetic_label.pack()

    first_input_label = Label(input_frame, text='Ball 1:')
    second_input_label = Label(input_frame, text='Ball 2:')
    third_input_label = Label(input_frame, text='Ball 3:')
    fourth_input_label = Label(input_frame, text='Ball 4:')
    fifth_input_label = Label(input_frame, text='Ball 5:')

    first_guess = IntVar()
    second_guess = IntVar()
    third_guess = IntVar()
    fourth_guess = IntVar()
    fifth_guess = IntVar()

    user_input = [first_guess, second_guess, third_guess, fourth_guess, fifth_guess]

    first_entry = Entry(input_frame, textvariable=first_guess)
    second_entry = Entry(input_frame, textvariable=second_guess)
    third_entry = Entry(input_frame, textvariable=third_guess)
    fourth_entry = Entry(input_frame, textvariable=fourth_guess)
    fifth_entry = Entry(input_frame, textvariable=fifth_guess, background='red')

    submit_button = Button(input_frame, text='Submit',
                           command=lambda: submit(root_window, input_window, user, lottery_details, timer,
                                                  user_input))

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


def submit(root_window, current_window, logged_in_user, lottery_details, timer, lotto_guess_input):
    timer.stop()

    time = timer.time

    # Console debug output
    print(timer.time_as_string)
    for each_input in lotto_guess_input:
        print(each_input.get())

    print(lottery_details)

    current_window.destroy()

    psi.practice_test_session_item_guess_window(root_window, logged_in_user, lottery_details, time, lotto_guess_input)
