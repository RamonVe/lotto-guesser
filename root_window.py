import tkinter as tk

from screens import login_screen


def initialize_ui():
    root_window = tk.Tk()

    # The root window is hidden
    root_window.withdraw()

    tk.Label(root_window, text="This is the root window.").pack()

    login_screen.login_screen(root_window)

    root_window.mainloop()
