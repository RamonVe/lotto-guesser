from tkinter import *
from entities import user as u
from windows.test_windows.item_randomizer import item_randomizer as ir
from windows.window_utillities import lottery_color as lc
from windows.window_utillities import window_icon as wi
from windows.window_utillities import window_protocol as wp
import tkinter


def session_results(root_window, user, lottery_details, time, lotto_guess_input):
    results_window = tkinter.Toplevel(root_window)
    results_window.geometry('918x250')
    results_window.title('Practice Test Results')
    results_window.iconbitmap(wi.window_icon())

    user_first_name = u.User.first_name(user)

    time_frame = LabelFrame(results_window, text='Total Time')
    test_info_frame = LabelFrame(results_window)
    geomagnetic_frame = LabelFrame(results_window, text='Geomagnetic')
    input_frame = LabelFrame(results_window, text=user_first_name + "'s " + 'guess.')
    results_frame = LabelFrame(results_window, text='Results!')

    time_frame.grid(row=0, column=0, padx=20)
    test_info_frame.grid(row=0, column=1, padx=20)
    geomagnetic_frame.grid(row=0, column=2, padx=20)
    input_frame.grid(row=1, column=1, padx=20, pady=50)
    results_frame.grid(row=2, column=1, padx=20, pady=50)

    time_label = Label(time_frame, text=time)
    time_label.pack()

    lottery_name = lottery_details[0]
    lottery_date = lottery_details[1]

    test_label = Label(test_info_frame,
                       text='The winning numbers for ' + lottery_name + ' on ' + lottery_date)
    test_label.pack()

    geomagnetic_label = Label(geomagnetic_frame, text='Geomagnetic')
    geomagnetic_label.pack()

    ball_one = lotto_guess_input[0]
    ball_two = lotto_guess_input[1]
    ball_three = lotto_guess_input[2]
    ball_four = lotto_guess_input[3]
    ball_five = lotto_guess_input[4]

    ball_item_results = ir.random_items()

    item_one_result = ball_item_results[0]
    item_two_result = ball_item_results[1]
    item_three_result = ball_item_results[2]
    item_four_result = ball_item_results[3]
    item_five_result = ball_item_results[4]

    first_input_label = Label(input_frame, text='Ball 1: ' + ball_one + '/' + item_one_result)
    second_input_label = Label(input_frame, text='Ball 2: ' + ball_two + '/' + item_two_result)
    third_input_label = Label(input_frame, text='Ball 3: ' + ball_three + '/' + item_three_result)
    fourth_input_label = Label(input_frame, text='Ball 4: ' + ball_four + '/' + item_four_result)
    fifth_input_label = Label(input_frame, text='Ball 5: ' + ball_five + '/' + item_five_result,
                              background=lc.color(lottery_name), foreground=lc.text_color(lottery_name))

    first_input_label.grid(row=0, column=0)
    second_input_label.grid(row=0, column=1)
    third_input_label.grid(row=0, column=2)
    fourth_input_label.grid(row=0, column=3)
    fifth_input_label.grid(row=0, column=4)

    number_results = lottery_details[2]
    split_number_results = number_results.split('-')

    number_one_result = split_number_results[0]
    number_two_result = split_number_results[1]
    number_three_result = split_number_results[2]
    number_four_result = split_number_results[3]
    number_five_result = split_number_results[4]

    first_results_label = Label(results_frame, text='Ball 1: ' + number_one_result,
                                background=result_background(ball_one, number_one_result))
    second_results_label = Label(results_frame, text='Ball 2: ' + number_two_result,
                                 background=result_background(ball_two, number_two_result))
    third_results_label = Label(results_frame, text='Ball 3: ' + number_three_result,
                                background=result_background(ball_three, number_three_result))
    fourth_results_label = Label(results_frame, text='Ball 4: ' + number_four_result,
                                 background=result_background(ball_four, number_four_result))
    fifth_results_label = Label(results_frame, text='Ball 5: ' + number_five_result,
                                background=result_background(ball_five, number_five_result))

    first_results_label.grid(row=1, column=0, padx=5)
    second_results_label.grid(row=1, column=1, padx=5)
    third_results_label.grid(row=1, column=2, padx=5)
    fourth_results_label.grid(row=1, column=3, padx=5)
    fifth_results_label.grid(row=1, column=4, padx=5)

    wp.quit_confirmation(root_window, results_window)


def result_background(user_input, correct_number):
    if user_input == correct_number:
        return 'green'
    else:
        return 'red'
