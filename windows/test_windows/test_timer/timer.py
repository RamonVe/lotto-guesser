from tkinter import *


class Timer:

    def __init__(self, parent):
        self.count = 0
        self.time_as_string = ''
        self.parent = parent
        self.time = StringVar()
        self.time.set("00:00:00")
        self.label = Label(self.parent, textvariable=self.time, font="Times 8 bold", bg="white")
        self.label.pack()

    def reset(self):
        self.count = 0
        self.time.set('00:00:00')

    def start(self):
        self.count = 0
        self.timer()

    def stop(self):
        self.count = 1

    def timer(self):
        if self.count == 0:
            self.time_as_string = str(self.time.get())
            hour, minute, second = map(int, self.time_as_string.split(":"))
            hour = int(hour)
            minute = int(minute)
            second = int(second)
            if second < 59:
                second += 1
            elif second == 59:
                second = 0
                if minute < 59:
                    minute += 1
                elif minute == 59:
                    minute = 0
                    hour += 1
            if hour < 10:
                hour = str(0) + str(hour)
            else:
                hour = str(hour)
            if minute < 10:
                minute = str(0) + str(minute)
            else:
                minute = str(minute)
            if second < 10:
                second = str(0) + str(second)
            else:
                second = str(second)
            self.time_as_string = hour + ":" + minute + ":" + second
            self.time.set(self.time_as_string)
            if self.count == 0:
                self.parent.after(1000, self.timer)
