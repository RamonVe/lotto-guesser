from tkinter import *
from functools import partial


def validate_login(user_name, pass_word):
    print("username entered :", user_name.get())
    print("password entered :", pass_word.get())
    return


# window
login_window = Tk()
login_window.geometry('400x150')
login_window.title('Lotto Guesser')

# username label and text entry box
Label(login_window, text="User Name").grid(row=0, column=0)
username = StringVar()
Entry(login_window, textvariable=username).grid(row=0, column=1)

# password label and password entry box
Label(login_window, text="Password").grid(row=1, column=0)
password = StringVar()
Entry(login_window, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validate_login, username, password)

# login button
Button(login_window, text="Login", command=validateLogin).grid(row=4, column=0)

# registration button
Button(login_window, text="Register", command=validateLogin).grid(row=5, column=0)

login_window.mainloop()
