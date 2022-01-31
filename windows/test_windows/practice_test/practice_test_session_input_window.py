from entities import user
from tkinter import *
from windows.test_windows.test_timer import timer
from windows.window_utillities import window_protocol
import tkinter


def practice_test_session_input_window(root_window, selected_lottery, logged_in_user):
    p_test_session_input_window = tkinter.Toplevel(root_window)
    p_test_session_input_window.geometry('918x300')
    p_test_session_input_window.title(
        user.User.first_name(logged_in_user) + "'s " + selected_lottery + ' Practice Test Session')

    timer_frame = LabelFrame(p_test_session_input_window, text='Timer')
    test_info_frame = LabelFrame(p_test_session_input_window)
    geomagnetic_frame = LabelFrame(p_test_session_input_window, text='Geomagnetic')
    input_frame = LabelFrame(p_test_session_input_window, text='Input')

    timer_frame.grid(row=0, column=0, padx=20)
    test_info_frame.grid(row=0, column=1, padx=20)
    geomagnetic_frame.grid(row=0, column=2, padx=20)
    input_frame.grid(row=1, column=1, padx=20, pady=50)

    timer_label = timer.Timer(timer_frame)
    timer_label.start()

    test_label = Label(test_info_frame,
                       text='What are the winning numbers for the ' + selected_lottery + ' on 1/29/2022?')
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

    guesses = [fifth_guess, second_guess, third_guess, fourth_guess, fifth_guess]

    first_entry = Entry(input_frame, textvariable=first_guess)
    second_entry = Entry(input_frame, textvariable=second_guess)
    third_entry = Entry(input_frame, textvariable=third_guess)
    fourth_entry = Entry(input_frame, textvariable=fourth_guess)
    fifth_entry = Entry(input_frame, textvariable=fifth_guess, background='red')

    submit_button = Button(input_frame, text='Submit', command=lambda: submit(timer_label, guesses))

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

    window_protocol.quit_confirmation(root_window, p_test_session_input_window)


def submit(timer_label, guesses):
    timer_label.stop()
    print(timer_label.time_as_string)
    for guess in guesses:
        print(guess.get())
