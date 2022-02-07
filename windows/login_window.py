from tkinter import *
from tkinter import messagebox as m
from storage import local_data_utilities as ldu
from windows import dashboard_window as dw
from windows import registration_window as rw
from windows.window_utillities import window_icon as wi
from windows.window_utillities import window_protocol as wp
import tkinter as tk


# This function creates a login window on top of the root window.
def login_window(root_window):
    # Here the login window is placed on top of the root window.
    log_window = tk.Toplevel(root_window)

    # The title of the window is set.
    log_window.title('Login')

    # The icon of the window is set.
    log_window.iconbitmap(wi.window_icon())

    # Frames are created to hold widgets.
    user_frame = LabelFrame(log_window)
    pass_frame = LabelFrame(log_window)
    button_frame = LabelFrame(log_window)

    # Username variable is created to hold user input.
    username = StringVar()

    # Two widgets are created, a label and entry widget for username.
    user_label = Label(user_frame, text='User Name:', font="Times 12 bold", width=10)
    user_entry = Entry(user_frame, textvariable=username, width=20)

    # Password variable is created to hold user input.
    password = StringVar()

    # Two widgets are created, a label and entry widget for password.
    pass_label = Label(pass_frame, text='Password:', font="Times 12 bold", width=10)
    pass_entry = Entry(pass_frame, textvariable=password, show='*', width=20)

    # Login button is created, the command variable uses a lambda function so that the function that the button calls
    # can pass data from the login window to the function being called.
    login_button = Button(button_frame, text='Login',
                          command=lambda: validate_login(username, password, root_window, log_window),
                          font="Times 12 bold", width=10)

    # Register button is created, also uses a lambda function.
    register_button = Button(button_frame, text='Register', font="Times 12 bold",
                             command=lambda: registration(root_window, log_window), width=10)

    # The frames that will hold the widgets are packed into the login window.
    # When using .pack() the frames are stacked on top of each other.
    user_frame.pack(padx=5, pady=5)
    pass_frame.pack(padx=5, pady=5)
    button_frame.pack(padx=5, pady=5)

    # The widgets are all placed into their parent frames using .grid()
    # .grid() is used so that widgets can be placed inside a frame but specifying the location of each widget.
    user_label.grid(row=0, column=0)
    user_entry.grid(row=0, column=1)
    pass_label.grid(row=0, column=0)
    pass_entry.grid(row=0, column=1)
    login_button.grid(row=0, column=0)
    register_button.grid(row=0, column=1)

    # This function prevents a user from accidentally closing the application when the close button is pressed.
    wp.quit_confirmation(root_window, log_window)


# This function validates a user's entered username and password to log in.
def validate_login(username, password, root_window, log_window):

    # Variables to store input are created.
    user_name = username.get()
    pass_word = password.get()

    # A list of users is loaded.
    users = ldu.load_users()

    # This for loop iterates through all users to validate user input to log in.
    for user in users:

        # First we check if an entered username matches with any usernames from the loaded user list.
        if user.username == user_name:

            # Next we check if the entered password matches the saved password of a user whose username matches
            # the input.
            if user.password != pass_word:
                m.showwarning('Wrong Password!', 'You have entered the wrong password, try again!')
            else:

                # If both entered username and password match a user's username and password from the user list
                # The login window is destroyed and a dashboard window is placed on top of the root window.
                log_window.destroy()
                dashboard(root_window, user)
                break
        else:

            # Warning box is displayed if input is empty.
            if user_name == '' and pass_word == '':
                m.showwarning('Empty Fields!', 'Enter a username and password to log in!')
            else:

                # Warning box is displayed if a username does not match any of the usernames of the user list.
                m.showwarning('No user found!', 'No user with that username found, try again!')
                break


# This function creates a registration window by destroying the login window and calling a function to create a
# registration window on top of the root window.
def registration(root_window, log_window):
    log_window.destroy()
    rw.registration_window(root_window)


# This function creates a dashboard window after successful login.
def dashboard(root_window, logged_in_user):
    dw.dashboard_window(root_window, logged_in_user)
