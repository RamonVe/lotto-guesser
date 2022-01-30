from tkinter import messagebox


def quit_confirmation(root_window, current_window):
    def close():
        if messagebox.askokcancel('Quit Lotto Guesser?', 'Do You Want To Quit?'):
            root_window.destroy()

    current_window.protocol('WM_DELETE_WINDOW', close)
