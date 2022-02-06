from entities import user as u
from tkinter import *
from windows.window_utillities import lottery_color as lc
from windows.window_utillities import window_icon as wi
from windows.window_utillities import window_protocol as wp
import tkinter


def future_update_number_input(root_window, user, future_test):
    future_test_dict = eval(future_test)

    time = future_test_dict.get('time')

    lottery_name_list = future_test_dict.get('lottery_name')
    lottery_name = lottery_name_list[0]

    lottery_date_list = future_test_dict.get('lottery_date')
    lottery_date = lottery_date_list[0]

    item_guesses = future_test_dict.get('item_guesses')
    item_guess_list = item_guesses[0]

    number_item_pair = future_test_dict.get('number_item_pair')

    input_window = tkinter.Toplevel(root_window)
    input_window.grid_columnconfigure(0, weight=1)
    input_window.grid_rowconfigure(0, weight=1)
    input_window.iconbitmap(wi.window_icon())
    user_first_name = u.User.first_name(user)
    input_window.title(user_first_name + "'s " + lottery_name + ' Ball Number Guess')

    time_frame = LabelFrame(input_window, text='Timer', font='Times 12 bold')
    test_info_frame = LabelFrame(input_window)
    geomagnetic_frame = LabelFrame(input_window, text='Geomagnetic', font='Times 12 bold')
    input_frame = LabelFrame(input_window, text='What number was drawn for each ball?', font='Times 12 bold')

    timer_label = Label(time_frame, text=time, background='white', font='Times 12 bold')

    test_label = Label(test_info_frame,
                       text=lottery_name + ' prediction' + ' for ' + lottery_date, font="Times 12 bold")

    geomagnetic_label = Label(geomagnetic_frame, text='Geomagnetic', font="Times 12 bold")

    first_input_label = Label(input_frame, text='Ball 1: ', background='white', font='Times 12 bold')
    second_input_label = Label(input_frame, text='Ball 2: ', background='white', font='Times 12 bold')
    third_input_label = Label(input_frame, text='Ball 3: ', background='white', font='Times 12 bold')
    fourth_input_label = Label(input_frame, text='Ball 4: ', background='white', font='Times 12 bold')
    fifth_input_label = Label(input_frame, text='Ball 5: ',
                              background=lc.color(lottery_name), foreground=lc.text_color(lottery_name),
                              font='Times 12 bold')

    number_one = StringVar()
    number_two = StringVar()
    number_three = StringVar()
    number_four = StringVar()
    number_five = StringVar()

    first_number_entry = Entry(input_frame, textvariable=number_one)
    second_number_entry = Entry(input_frame, textvariable=number_two)
    third_number_entry = Entry(input_frame, textvariable=number_three)
    fourth_number_entry = Entry(input_frame, textvariable=number_four)
    fifth_number_entry = Entry(input_frame, textvariable=number_five)

    correct_numbers = [number_one, number_two, number_three, number_four, number_five]

    submit_button = Button(input_frame, text='Submit',
                           command=lambda: submit(root_window, input_window, user, time, lottery_name, lottery_date,
                                                  item_guess_list, number_item_pair, correct_numbers))

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

    timer_label.pack()
    test_label.pack()
    geomagnetic_label.pack()

    first_input_label.grid(row=0, column=0, padx=5, pady=5)
    second_input_label.grid(row=0, column=1, padx=5, pady=5)
    third_input_label.grid(row=0, column=2, padx=5, pady=5)
    fourth_input_label.grid(row=0, column=3, padx=5, pady=5)
    fifth_input_label.grid(row=0, column=4, padx=5, pady=5)

    first_number_entry.grid(row=2, column=0, padx=5, pady=5)
    second_number_entry.grid(row=2, column=1, padx=5, pady=5)
    third_number_entry.grid(row=2, column=2, padx=5, pady=5)
    fourth_number_entry.grid(row=2, column=3, padx=5, pady=5)
    fifth_number_entry.grid(row=2, column=4, padx=5, pady=5)

    submit_button.grid(row=3, column=2, padx=20, pady=20)

    wp.quit_confirmation(root_window, input_window)


def submit(root_window, current_window, user, time, lottery_name, lottery_date, item_guesses, number_item_pair,
           correct_numbers):

    print(time)
    print(lottery_name)
    print(lottery_date)
    print(item_guesses)
    print(number_item_pair)
    for number in correct_numbers:
        print(number.get())

    # current_window.destroy()

    return
