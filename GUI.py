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
        self.my_canvas.create_image(0, 0, image=self.img, anchor='nw')
        self.my_canvas.pack(fill='both', expand=True)

        # hpw to add text - ( ADD IT ALSO INTO RESIZER!!!)
        self.my_canvas.create_text(300, 100, text="FOO")
        # how to add button:
        self.greet_button = Button(parent, text="Greet", command=self.greet)
        self.button_window = self.my_canvas.create_window(10, 10, anchor="nw", window=self.greet_button)
        # how to add button:
        self.close_button = Button(parent, text="Close", command=parent.quit)
        self.close_window = self.my_canvas.create_window(100, 100, anchor="nw", window=self.close_button)

    def greet(self):
        print("Greetings!")

    def resizer(self, e):
        """ Function allows stretching background during changing window size """

        global bg, resized_bg, new_bg
        bg = Image.open('eth_background.png')
        resized_bg = bg.resize((e.width, e.height), Image.ANTIALIAS)
        new_bg = ImageTk.PhotoImage(resized_bg)
        self.my_canvas.create_image(0, 0, image=new_bg, anchor='nw')
        self.my_canvas.create_text(300, 100, text="FOO")


if __name__ == "__main__":
    root = Tk()
    gui = GUI(root)
    root.bind('<Configure>', gui.resizer)
    root.mainloop()
