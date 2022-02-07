from entities import user as u
from storage import local_data_utilities as ldu
from tkinter import *
from tkinter import messagebox as m
from windows import login_window as lw
from windows.window_utillities import window_icon as wi
from windows.window_utillities import window_protocol as wp
import tkinter as tk


# This function creates a registration window on top of the root window.
def registration_window(root_window):

    # Window details are set.
    register_window = tk.Toplevel(root_window)
    register_window.title('Register')
    register_window.iconbitmap(wi.window_icon())

    # Frames to hold widgets are created.
    f_name_frame = LabelFrame(register_window)
    l_name_frame = LabelFrame(register_window)
    age_frame = LabelFrame(register_window)
    location_frame = LabelFrame(register_window)
    user_name_frame = LabelFrame(register_window)
    pass_word_frame = LabelFrame(register_window)
    button_frame = LabelFrame(register_window)

    # First name var, label, and input are created.
    f_name = StringVar()
    f_name_label = Label(f_name_frame, text='First Name', font="Times 12 bold", width=10)
    f_name_entry = Entry(f_name_frame, textvariable=f_name, width=20)

    # Last name var, label, and input are created.
    l_name = StringVar()
    l_name_label = Label(l_name_frame, text='Last Name', font="Times 12 bold", width=10)
    l_name_entry = Entry(l_name_frame, textvariable=l_name, width=20)

    # Age var, label, and input are created.
    age = StringVar()
    age_label = Label(age_frame, text='Age', font="Times 12 bold", width=10)
    age_entry = Entry(age_frame, textvariable=age, width=20)

    # Location var, label, and input are created.
    location = StringVar()
    location_label = Label(location_frame, text='Location', font="Times 12 bold", width=10)
    location_entry = Entry(location_frame, textvariable=location, width=20)

    # Username var, label, and input are created.
    user_name = StringVar()
    user_name_label = Label(user_name_frame, text='User Name', font="Times 12 bold", width=10)
    user_name_entry = Entry(user_name_frame, textvariable=user_name, width=20)

    # Password var, label, and input are created.
    pass_word = StringVar()
    pass_word_label = Label(pass_word_frame, text='Password', font="Times 12 bold", width=10)
    pass_word_entry = Entry(pass_word_frame, textvariable=pass_word, width=20, show='*')

    # Submit button is created and calls the register function to register a new user.
    submit_button = Button(button_frame, text='Submit', width=16,
                           command=lambda: register(root_window,
                                                    register_window,
                                                    f_name,
                                                    l_name,
                                                    age,
                                                    location,
                                                    user_name,
                                                    pass_word), font="Times 12 bold")

    # Return button is created and calls the return to login window function.
    return_button = Button(button_frame, text='Return To Login', width=16,
                           command=lambda: return_to_login(root_window, register_window), font="Times 12 bold")

    # Frames are packed onto the register window.
    f_name_frame.pack(padx=5, pady=5)
    l_name_frame.pack(padx=5, pady=5)
    age_frame.pack(padx=5, pady=5)
    location_frame.pack(padx=5, pady=5)
    user_name_frame.pack(padx=5, pady=5)
    pass_word_frame.pack(padx=5, pady=5)
    button_frame.pack(padx=5, pady=5)

    # Widgets are placed into each frame using grid layout.
    f_name_label.grid(row=0, column=0)
    f_name_entry.grid(row=0, column=1)
    l_name_label.grid(row=0, column=0)
    l_name_entry.grid(row=0, column=1)
    age_label.grid(row=0, column=0)
    age_entry.grid(row=0, column=1)
    location_label.grid(row=0, column=0)
    location_entry.grid(row=0, column=1)
    user_name_label.grid(row=0, column=0)
    user_name_entry.grid(row=0, column=1)
    pass_word_label.grid(row=0, column=0)
    pass_word_entry.grid(row=0, column=1)
    submit_button.grid(row=0, column=0)
    return_button.grid(row=0, column=1)

    # This function prevents a user from accidentally closing the application when the close button is pressed.
    wp.quit_confirmation(root_window, register_window)


# This function registers a new user.
def register(root_window, register_window, f_name, l_name, age, location, user_name, pass_word):

    # Each input needs to be retrieved.
    first_name_input = f_name.get()
    last_name_input = l_name.get()
    age_input = age.get()
    location_input = location.get()
    user_name_input = user_name.get()
    pass_word_input = pass_word.get()

    # A new user object is created and its properties are set to the input.
    new_user = u.User(first_name=first_name_input,
                      last_name=last_name_input,
                      age=age_input,
                      location=location_input,
                      username=user_name_input,
                      password=pass_word_input)

    # This checks and displays a warning when an input is left empty.
    if first_name_input == '' or last_name_input == '' or age_input == '' or location_input == '' \
            or user_name_input == '' or pass_word_input == '':
        m.showwarning('Empty Field!', 'A field has been left empty!')
        return

    # User list is retrieved to add a new user to it.
    users = ldu.load_users()

    # This prevents two users from having the same username.
    for exiting_user in users:
        if exiting_user.username == user_name_input:
            m.showwarning('Duplicate Username!', 'The username you entered has already been taken!')
            return

    # The new user is saved.
    ldu.save_user(new_user)
    m.showinfo('Success!', user_name_input + ' has been successfully registered!')

    # Return to login window function called.
    return_to_login(root_window, register_window)


# The registration window is destroyed and a login window is placed on top of the root window.
def return_to_login(root_window, register_window):
    register_window.destroy()
    lw.login_window(root_window)
