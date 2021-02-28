from tkinter import *
import time


root = Tk()
root.title("Clock")



def timer():
    t = 30
    for i in range(0,t):
        second = t-1
        my_label.config(text="{}".format(second))
        my_label.after(1000,timer)


my_label = Label(root, text="", font="Helvetica 48")
my_label.grid(pady=20)

timer()

# my_label.after(1000, update)




root.mainloop()