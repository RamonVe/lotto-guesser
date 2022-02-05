from entities import user
from storage import local_data_utilities
from tkinter import *
from tkinter import messagebox
from windows import login_window
from windows.window_utillities import window_icon
from windows.window_utillities import window_protocol
import tkinter


def registration_window(root_window):
    register_window = tkinter.Toplevel(root_window)
    register_window.title('Register')
    register_window.iconbitmap(window_icon.window_icon())

    f_name_frame = LabelFrame(register_window)
    l_name_frame = LabelFrame(register_window)
    age_frame = LabelFrame(register_window)
    location_frame = LabelFrame(register_window)
    user_name_frame = LabelFrame(register_window)
    pass_word_frame = LabelFrame(register_window)
    button_frame = LabelFrame(register_window)

    f_name = StringVar()
    f_name_label = Label(f_name_frame, text='First Name', font="Times 12 bold", width=10)
    f_name_entry = Entry(f_name_frame, textvariable=f_name, width=20)

    l_name = StringVar()
    l_name_label = Label(l_name_frame, text='Last Name', font="Times 12 bold", width=10)
    l_name_entry = Entry(l_name_frame, textvariable=l_name, width=20)

    age = StringVar()
    age_label = Label(age_frame, text='Age', font="Times 12 bold", width=10)
    age_entry = Entry(age_frame, textvariable=age, width=20)

    location = StringVar()
    location_label = Label(location_frame, text='Location', font="Times 12 bold", width=10)
    location_entry = Entry(location_frame, textvariable=location, width=20)

    user_name = StringVar()
    user_name_label = Label(user_name_frame, text='User Name', font="Times 12 bold", width=10)
    user_name_entry = Entry(user_name_frame, textvariable=user_name, width=20)

    pass_word = StringVar()
    pass_word_label = Label(pass_word_frame, text='Password', font="Times 12 bold", width=10)
    pass_word_entry = Entry(pass_word_frame, textvariable=pass_word, width=20, show='*')

    submit_button = Button(button_frame, text='Submit', width=16,
                           command=lambda: register(root_window,
                                                    register_window,
                                                    f_name,
                                                    l_name,
                                                    age,
                                                    location,
                                                    user_name,
                                                    pass_word), font="Times 12 bold")

    return_button = Button(button_frame, text='Return To Login', width=16,
                           command=lambda: return_to_login(root_window, register_window), font="Times 12 bold")

    f_name_frame.pack(padx=5, pady=5)
    l_name_frame.pack(padx=5, pady=5)
    age_frame.pack(padx=5, pady=5)
    location_frame.pack(padx=5, pady=5)
    user_name_frame.pack(padx=5, pady=5)
    pass_word_frame.pack(padx=5, pady=5)
    button_frame.pack(padx=5, pady=5)

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

    window_protocol.quit_confirmation(root_window, register_window)


def register(root_window, register_window, f_name, l_name, age, location, user_name, pass_word):
    first_name_input = f_name.get()
    last_name_input = l_name.get()
    age_input = age.get()
    location_input = location.get()
    user_name_input = user_name.get()
    pass_word_input = pass_word.get()

    new_user = user.User(first_name=first_name_input,
                         last_name=last_name_input,
                         age=age_input,
                         location=location_input,
                         username=user_name_input,
                         password=pass_word_input)

    if first_name_input == '' or last_name_input == '' or age_input == '' or location_input == '' \
            or user_name_input == '' or pass_word_input == '':
        messagebox.showwarning('Empty Field!', 'A field has been left empty!')
        return

    users = local_data_utilities.load_users()

    for exiting_user in users:
        if exiting_user.username == user_name.get():
            messagebox.showwarning('Duplicate Username!', 'The username you entered has already been taken!')
            return

    local_data_utilities.save_user(new_user)
    messagebox.showinfo('Success!', user_name_input + ' has been successfully registered!')

    register_window.destroy()
    login_window.login_window(root_window)


def return_to_login(root_window, register_window):
    register_window.destroy()
    login_window.login_window(root_window)
