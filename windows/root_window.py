from windows import login_window as lw
from windows.window_utillities import window_icon as wi
import tkinter as tk


# This function initializes the ui by creating a window which acts as the root window for all other windows to be
# placed on top off.
def initialize_ui():
    # A root window is created using the Tkinter library.
    root_window = tk.Tk()

    # The root window is hidden and all other windows will be placed on top the root window.
    root_window.withdraw()

    # The root window is given an icon.
    root_window.iconbitmap(wi.window_icon())

    # The login window is created and placed on top of the root window.
    lw.login_window(root_window)

    # This function essentially starts the program.
    root_window.mainloop()
