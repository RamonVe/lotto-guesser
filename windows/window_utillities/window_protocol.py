from tkinter import messagebox as m


# This function prevents a user from accidentally closing a window by pressing the close button by asking for
# confirmation.
def quit_confirmation(root_window, current_window):
    def close():
        if m.askokcancel('Quit Lotto Guesser?',
                         'Do you want to close the program?' + '\n' + 'Any unsaved progress will be lost.'):
            root_window.destroy()

    current_window.protocol('WM_DELETE_WINDOW', close)
