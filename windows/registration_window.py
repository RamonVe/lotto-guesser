from entities import user
from storage import local_data_utilities
from tkinter import *
from tkinter import messagebox
from windows import login_window
import tkinter


def registration_window(root_window, log_window):
    log_window.destroy()

    register_window = tkinter.Toplevel(root_window)
    register_window.geometry('230x180')
    register_window.title('Register')

    f_name_label = Label(register_window, text='First Name')
    l_name_label = Label(register_window, text='Last Name')
    age_label = Label(register_window, text='Age')
    location_label = Label(register_window, text='Location')
    user_name_label = Label(register_window, text='User Name')
    pass_word_label = Label(register_window, text='Password')

    f_name = StringVar()
    l_name = StringVar()
    age = StringVar()
    location = StringVar()
    user_name = StringVar()
    pass_word = StringVar()

    f_name_entry = Entry(register_window, textvariable=f_name)
    l_name_entry = Entry(register_window, textvariable=l_name)
    age_entry = Entry(register_window, textvariable=age)
    location_entry = Entry(register_window, textvariable=location)
    user_name_entry = Entry(register_window, textvariable=user_name)
    pass_word_entry = Entry(register_window, textvariable=pass_word)

    f_name_label.grid(row=0, column=0)
    l_name_label.grid(row=1, column=0)
    age_label.grid(row=2, column=0)
    location_label.grid(row=3, column=0)
    user_name_label.grid(row=4, column=0)
    pass_word_label.grid(row=5, column=0)

    f_name_entry.grid(row=0, column=1)
    l_name_entry.grid(row=1, column=1)
    age_entry.grid(row=2, column=1)
    location_entry.grid(row=3, column=1)
    user_name_entry.grid(row=4, column=1)
    pass_word_entry.grid(row=5, column=1)

    Button(register_window, text='Submit', width=16, bg='black', fg='white',
           command=lambda: register(root_window,
                                    register_window,
                                    f_name,
                                    l_name,
                                    age,
                                    location,
                                    user_name,
                                    pass_word)).grid(row=6, column=1)

    def close():
        if messagebox.askokcancel('Quit', 'Do You Want To Quit?'):
            root_window.destroy()

    register_window.protocol('WM_DELETE_WINDOW', close)


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

    if first_name_input == '' or last_name_input == '' or age_input == '' or location_input == ''\
            or user_name_input == '' or pass_word_input == '':
        messagebox.showwarning('Empty Field', 'A field has been left empty!')
        return

    users = local_data_utilities.load_users()

    for exiting_user in users:
        if exiting_user.username == user_name.get():
            messagebox.showwarning('Duplicate Username.', 'The username you entered has already been taken!')
            return

    local_data_utilities.save_user(new_user)
    messagebox.showinfo('Success', user_name_input + ' has been successfully registered')

    register_window.destroy()
    login_window.login_window(root_window)
