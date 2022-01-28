# how to create simple GUI registration form.
# importing tkinter module for GUI application
import tkinter
from tkinter import *
from tkinter import messagebox


def registration_window(root_window, login_window):
    login_window.destroy()
    # Creating object 'root' of Tk()
    register_screen = tkinter.Toplevel(root_window)
    # Providing Geometry to the form
    register_screen.geometry('500x500')
    # Providing title to the form
    register_screen.title('Registration form')
    # this creates 'Label' widget for Registration Form and uses place() method.
    label_0 = Label(register_screen, text='Registration form', width=20, font=('bold', 20))
    # place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    label_0.place(x=90, y=60)
    # this creates 'Label' widget for Fullname and uses place() method.
    label_1 = Label(register_screen, text='FullName', width=20, font=('bold', 10))
    label_1.place(x=80, y=130)
    # this will accept the input string text from the user.
    entry_1 = Entry(register_screen)
    entry_1.place(x=240, y=130)
    # this creates 'Label' widget for Email and uses place() method.
    label_3 = Label(register_screen, text='Email', width=20, font=('bold', 10))
    label_3.place(x=68, y=180)
    entry_3 = Entry(register_screen)
    entry_3.place(x=240, y=180)
    # this creates 'Label' widget for Gender and uses place() method.
    label_4 = Label(register_screen, text='Gender', width=20, font=('bold', 10))
    label_4.place(x=70, y=230)
    # the variable 'var' mentioned here holds Integer Value, by default 0
    var = IntVar()
    # this creates 'Radio button' widget and uses place() method
    Radiobutton(register_screen, text='Male', padx=5, variable=var, value=1).place(x=235, y=230)
    Radiobutton(register_screen, text='Female', padx=20, variable=var, value=2).place(x=290, y=230)
    # this creates 'Label' widget for country and uses place() method.
    label_5 = Label(register_screen, text='Country', width=20, font=('bold', 10))
    label_5.place(x=70, y=280)
    # this creates list of countries available in the dropdown-list.
    list_of_country = ['India', 'US', 'UK', 'Germany', 'Austria']
    # the variable 'c' mentioned here holds String Value, by default '
    c = StringVar()
    droplist = OptionMenu(register_screen, c, *list_of_country)
    droplist.config(width=15)
    c.set('Select your Country')
    droplist.place(x=240, y=280)
    # this creates 'Label' widget for Language and uses place() method.
    label_6 = Label(register_screen, text='Language', width=20, font=('bold', 10))
    label_6.place(x=75, y=330)
    # the variable 'var1' mentioned here holds Integer Value, by default 0
    var1 = IntVar()
    # this creates Checkbutton widget and uses place() method.
    Checkbutton(register_screen, text='English', variable=var1).place(x=230, y=330)
    # the variable 'var2' mentioned here holds Integer Value, by default 0
    var2 = IntVar()
    Checkbutton(register_screen, text='German', variable=var2).place(x=290, y=330)
    # this creates button for submitting the details provides by the user
    Button(register_screen, text='Submit', width=20, bg='black', fg='white').place(x=180, y=380)

    def close():
        if messagebox.askokcancel('Quit', 'Do You Want To Quit?'):
            root_window.destroy()

    register_screen.protocol('WM_DELETE_WINDOW', close)
