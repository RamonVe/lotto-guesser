from entities import user as u
from tkinter import *
from windows.test_windows.test_timer import timer as t
from windows.window_utillities import lottery_color as lc
from windows.window_utillities import window_icon as wi
from windows.window_utillities import window_protocol as wp

import tkinter


def future_session_number_input(root_window, selected_lottery, selected_date, user):
    input_window = tkinter.Toplevel(root_window)
    input_window.grid_columnconfigure(0, weight=1)
    input_window.grid_rowconfigure(0, weight=1)
    input_window.iconbitmap(wi.window_icon())
    user_first_name = u.User.first_name(user)
    input_window.title(user_first_name + "'s " + selected_lottery + ' Ball Number Guess')

    time_frame = LabelFrame(input_window, text='Timer')
    test_info_frame = LabelFrame(input_window)
    geomagnetic_frame = LabelFrame(input_window, text='Geomagnetic')
    input_frame = LabelFrame(input_window, text='What number is each ball?')

    timer = t.Timer(time_frame)
    timer.start()

    test_label = Label(test_info_frame,
                       text='What will be the winning numbers for the ' + selected_lottery + ' on ' +
                            selected_date + '?', font="Times 12 bold")

    geomagnetic_label = Label(geomagnetic_frame, text='Geomagnetic', font="Times 12 bold")

    first_input_label = Label(input_frame, text='Ball 1: ', background='white',
                              font="Times 10 bold")
    second_input_label = Label(input_frame, text='Ball 2: ', background='white',
                               font="Times 10 bold")
    third_input_label = Label(input_frame, text='Ball 3: ', background='white',
                              font="Times 10 bold")
    fourth_input_label = Label(input_frame, text='Ball 4: ', background='white',
                               font="Times 10 bold")
    fifth_input_label = Label(input_frame, text='Ball 5: ',
                              background=lc.color(selected_lottery), foreground=lc.text_color(selected_lottery),
                              font="Times 10 bold")

    first_guess = StringVar()
    second_guess = StringVar()
    third_guess = StringVar()
    fourth_guess = StringVar()
    fifth_guess = StringVar()

    first_entry = Entry(input_frame, textvariable=first_guess)
    second_entry = Entry(input_frame, textvariable=second_guess)
    third_entry = Entry(input_frame, textvariable=third_guess)
    fourth_entry = Entry(input_frame, textvariable=fourth_guess)
    fifth_entry = Entry(input_frame, textvariable=fifth_guess)

    number_guess = [first_guess, second_guess, third_guess, fourth_guess, fifth_guess]

    submit_button = Button(input_frame, text='Submit',
                           command=lambda: submit(root_window, input_window, selected_lottery, selected_date, user,
                                                  timer, number_guess))

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


def submit(root_window, current_window, selected_lottery, selected_date, user, timer, number_guess):
    timer.stop()

    time = timer.time_as_string

    print(selected_lottery)
    print(selected_date)
    print(time)

    for number in number_guess:
        print(number.get())

    # current_window.destroy()
