#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import Tk, Label, Button, PhotoImage, Canvas
import tkinter as tk
from PIL import ImageTk, Image


class GUI:
    def __init__(self, parent, *args, **kwargs):
        super(GUI, self).__init__(*args, **kwargs)
        # parents basic settings
        self.parent = parent
        self.parent.title("Mining ETH statistics!")
        self.parent.iconbitmap('eth_icon.ico')
        self.parent.geometry('600x530')

        # background settings
        self.img = ImageTk.PhotoImage(Image.open("eth_background.png"))
        self.my_canvas = Canvas(self.parent, width=600, height=530)
        self.my_canvas.pack(fill='both', expand=True)
        self.my_canvas.create_image(0, 0, image=self.img, anchor='nw')

        #  self.my_canvas.create_text(300, 100, text="welcome")
        # self.backgroud = Label(self.parent, image=self.img)
        # self.backgroud.pack(side="top", fill="both", expand=True)

    # self.label = Label(self.parent, text="This is our first GUI!")
    # self.label.place(x=205, y=25, anchor="center")

    # self.greet_button = Button(parent, text="Greet", command=self.greet)
    # self.greet_button.pack()

    # self.close_button = Button(parent, text="Close", command=parent.quit)
    # self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def resizer(self, e):
        """ Function allows stretching background during changing window size """

        global bg, resized_bg, new_bg
        bg = Image.open('eth_background.png')
        resized_bg = bg.resize((e.width, e.height), Image.ANTIALIAS)
        new_bg = ImageTk.PhotoImage(resized_bg)
        self.my_canvas.create_image(0, 0, image=new_bg, anchor='nw')


if __name__ == "__main__":
    root = Tk()
    gui = GUI(root)
    root.bind('<Configure>', gui.resizer)
    root.mainloop()
