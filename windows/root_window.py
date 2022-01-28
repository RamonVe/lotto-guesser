import tkinter as tk

from windows import login_window


def initialize_ui():
    root_window = tk.Tk()

    # The root window is hidden
    root_window.withdraw()

    tk.Label(root_window, text='This is the root window.').pack()

    login_window.login_window(root_window)

    root_window.mainloop()
