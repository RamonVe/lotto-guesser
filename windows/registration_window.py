from entities import user
from storage import local_data_utillities
from tkinter import *
from tkinter import messagebox
import tkinter


def registration_window(root_window, login_window):
    login_window.destroy()

    register_window = tkinter.Toplevel(root_window)
    register_window.geometry('210x180')
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
           command=lambda: register(f_name,
                                    l_name,
                                    age,
                                    location,
                                    user_name,
                                    pass_word)).grid(row=6, column=1)

    def close():
        if messagebox.askokcancel('Quit', 'Do You Want To Quit?'):
            root_window.destroy()

    register_window.protocol('WM_DELETE_WINDOW', close)


def register(f_name, l_name, age, location, user_name, pass_word):
    new_user = user.User(first_name=f_name.get(),
                         last_name=l_name.get(),
                         age=age.get(),
                         location=location.get(),
                         username=user_name.get(),
                         password=pass_word.get())

    local_data_utillities.save_object(new_user)
