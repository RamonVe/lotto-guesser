from windows.window_utillities import window_icon
import tkinter

from windows import login_window


def initialize_ui():
    root_window = tkinter.Tk()

    # The root window is hidden
    root_window.withdraw()

    root_window.iconbitmap(window_icon.window_icon())

    tkinter.Label(root_window, text='This is the root window.').pack()

    login_window.login_window(root_window)

    root_window.mainloop()
