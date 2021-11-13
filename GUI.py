#!/usr/bin/python
# -*- coding: utf-8 -*-
# Use Tkinter for python 2, tkinter for python 3
from tkinter import Tk, Label, Button, PhotoImage
import tkinter as tk
from PIL import ImageTk, Image


class GUI:
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent

        self.parent.geometry('600x530')

        self.img = ImageTk.PhotoImage(Image.open("eth_background.png"))

        self.backgroud = Label(self.parent, image=self.img)
        self.backgroud.pack(side="top", fill="both", expand=True)

       #self.label = Label(self.parent, text="This is our first GUI!")
        #self.label.place(x=205, y=25, anchor="center")

        self.greet_button = Button(parent, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(parent, text="Close", command=parent.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")


if __name__ == "__main__":
    # from tkinter import *
    # from PIL import ImageTk, Image

    # root = Tk()

    # canv = Canvas(root, width=800, height=800, bg='white')
    # canv.grid(row=2, column=3)

    # img = ImageTk.PhotoImage(Image.open("eth_background.png"))  # PIL solution
    # canv.create_image(200, 200, anchor=NW, image=img)

    # mainloop()
    root = Tk()
    gui = GUI(root)
    root.mainloop()
