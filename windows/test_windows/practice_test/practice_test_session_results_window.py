from tkinter import *
from entities import user as u
from windows import dashboard_window as dw
from windows.test_windows.item_randomizer import item_randomizer as ir
from windows.window_utillities import lottery_color as lc
from windows.window_utillities import window_icon as wi
from windows.window_utillities import window_protocol as wp
import tkinter


def session_results(root_window, user, lottery_details, winning_numbers, time, item_guess_input):
    results_window = tkinter.Toplevel(root_window)
    results_window.geometry('930x500')
    results_window.title('Practice Test Results')
    results_window.iconbitmap(wi.window_icon())

    user_first_name = u.User.first_name(user)

    time_frame = LabelFrame(results_window, text='Total Time')
    test_info_frame = LabelFrame(results_window)
    geomagnetic_frame = LabelFrame(results_window, text='Geomagnetic')
    input_frame = LabelFrame(results_window, text=user_first_name + "'s " + 'guess.')
    results_frame = LabelFrame(results_window, text='Results!')
    pairing_frame = LabelFrame(results_window, text='All Pairings')

    time_frame.grid(row=0, column=0, padx=20)
    test_info_frame.grid(row=0, column=1, padx=20)
    geomagnetic_frame.grid(row=0, column=2, padx=20)
    input_frame.grid(row=1, column=1, padx=20, pady=50)
    results_frame.grid(row=2, column=1, padx=20, pady=50)
    pairing_frame.grid_remove()

    time_label = Label(time_frame, text=time, background='white')
    time_label.pack()

    lottery_name = lottery_details[0]
    lottery_date = lottery_details[1]

    test_label = Label(test_info_frame,
                       text='The winning numbers for ' + lottery_name + ' on ' + lottery_date, background='white')
    test_label.pack()

    geomagnetic_label = Label(geomagnetic_frame, text='Geomagnetic', background='white')
    geomagnetic_label.pack()

    guess_one = item_guess_input[0].get()
    guess_two = item_guess_input[1].get()
    guess_three = item_guess_input[2].get()
    guess_four = item_guess_input[3].get()
    guess_five = item_guess_input[4].get()

    number_one = winning_numbers[0]
    number_two = winning_numbers[1]
    number_three = winning_numbers[2]
    number_four = winning_numbers[3]
    number_five = winning_numbers[4]

    first_input_label = Label(input_frame, text='Ball 1: ' + number_one + '/' + guess_one, background='white')
    second_input_label = Label(input_frame, text='Ball 2: ' + number_two + '/' + guess_two, background='white')
    third_input_label = Label(input_frame, text='Ball 3: ' + number_three + '/' + guess_three, background='white')
    fourth_input_label = Label(input_frame, text='Ball 4: ' + number_four + '/' + guess_four, background='white')
    fifth_input_label = Label(input_frame, text='Ball 5: ' + number_five + '/' + guess_five,
                              background=lc.color(lottery_name),
                              foreground=lc.text_color(lottery_name))

    first_input_label.grid(row=0, column=0)
    second_input_label.grid(row=0, column=1)
    third_input_label.grid(row=0, column=2)
    fourth_input_label.grid(row=0, column=3)
    fifth_input_label.grid(row=0, column=4)

    random_number_item_pair = ir.random_pair()

    correct_items = correct_item_list(random_number_item_pair, winning_numbers)
    correct_item_one = correct_items[0]
    correct_item_two = correct_items[1]
    correct_item_three = correct_items[2]
    correct_item_four = correct_items[3]
    correct_item_five = correct_items[4]

    first_results_label = Label(results_frame, text='Ball 1: ' + number_one + '/' + correct_item_one,
                                background='white')
    second_results_label = Label(results_frame, text='Ball 2: ' + number_two + '/' + correct_item_two,
                                 background='white')
    third_results_label = Label(results_frame, text='Ball 3: ' + number_three + '/' + correct_item_three,
                                background='white')
    fourth_results_label = Label(results_frame, text='Ball 4: ' + number_four + '/' + correct_item_four,
                                 background='white')
    fifth_results_label = Label(results_frame, text='Ball 5: ' + number_five + '/' + correct_item_five,
                                background='white')

    color_results_label = Label(results_frame, width=10, background=result_background(guess_two, correct_item_two))
    second_color_results_label = Label(results_frame, width=10,
                                       background=result_background(guess_two, correct_item_two))
    third_color_results_label = Label(results_frame, width=10,
                                      background=result_background(guess_three, correct_item_three))
    fourth_color_results_label = Label(results_frame, width=10,
                                       background=result_background(guess_four, correct_item_four))
    fifth_color_results_label = Label(results_frame, width=10, background=result_background(guess_five, number_five))

    dash_button = Button(results_window, text='Return to Dashboard',
                         command=lambda: dash_board(root_window, results_window, user))

    show_results = Button(results_window, text='Show ball/item pairings?',
                          command=lambda: show_pairings(results_window, pairing_frame, show_results))
    dash_button.grid(row=3, column=1, padx=5)
    show_results.grid(row=4, column=1, padx=5)

    keys = list(random_number_item_pair.keys())
    values = list(random_number_item_pair.values())

    pairings_text = Text(pairing_frame)
    pairing = "\n".join("{} : {}".format(x, y) for x, y in zip(keys, values))
    pairings_text.insert(tkinter.END, pairing)
    pairings_text.grid(row=0, column=0)

    first_results_label.grid(row=1, column=0, padx=5)
    second_results_label.grid(row=1, column=1, padx=5)
    third_results_label.grid(row=1, column=2, padx=5)
    fourth_results_label.grid(row=1, column=3, padx=5)
    fifth_results_label.grid(row=1, column=4, padx=5)
    color_results_label.grid(row=2, column=0, padx=5)
    second_color_results_label.grid(row=2, column=1, padx=5)
    third_color_results_label.grid(row=2, column=2, padx=5)
    fourth_color_results_label.grid(row=2, column=3, padx=5)
    fifth_color_results_label.grid(row=2, column=4, padx=5)

    scrollbar = Scrollbar(pairing_frame, orient=VERTICAL)
    pairings_text.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=pairings_text.yview())
    scrollbar.grid(row=0, column=2, sticky=NS)

    wp.quit_confirmation(root_window, results_window)


def correct_item_list(random_number_item_pair, winning_numbers):
    correct_items = []
    keys = list(random_number_item_pair.keys())

    for n in winning_numbers:
        for key in keys:
            if n == key:
                correct_items.append(random_number_item_pair.get(key))

    return correct_items


def result_background(user_input, correct_item):
    if user_input == correct_item:
        return 'green'
    else:
        return 'red'


def show_pairings(results_window, pairing_frame, show_results):
    show_results.grid_remove()
    results_window.geometry('930x902')
    pairing_frame.grid(row=4, column=1, padx=20, pady=50)
    return


def dash_board(root_window, current_window, logged_in_user):
    current_window.destroy()
    dw.dashboard_window(root_window, logged_in_user)
