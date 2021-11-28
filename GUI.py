#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *

from PIL import Image, ImageTk
from src import *


class GUI(Frame):
    def __init__(self, parent_frame, *args, **kwargs) -> None:
        super(GUI, self).__init__(*args, **kwargs)
        # the miner from which we want to get statistics
        self.miner = Miner(miner_address, miner_cost)
        self.save_data = SaveData(miner_address)

        self.parent_frame = parent_frame  # parent's settings
        self.parent_frame.geometry("1100x880")
        self.parent_frame.iconbitmap('eth_icon.ico')
        self.parent_frame.title("ETH mining statistics!")

        self.image = Image.open("eth_background.png")
        # background settings
        self.img_copy = self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        self.make_widgets()  # pack labels + buttons

    def make_widgets(self) -> None:
        """ Funtion creates buttons and labels and place it on root """

        # labels
        self.label_daily_eth = Label(self.parent_frame, text="Daily mined:  ", width=35, bg="light salmon",
                                     font=("Helvetica", 14))
        self.label_todays_eth_price = Label(self.parent_frame,
                                            text="Today's ETH price:  " + str(self.miner.price_eth) + " $",
                                            width=35, font=("Helvetica", 14))
        self.label_current_hashrate = Label(self.parent_frame,
                                            text="Current hashrate [Mh/s]:  " + str(self.miner.get_current_hashrate()),
                                            width=35, font=("Helvetica", 14))
        self.label_unpaid_eth = Label(self.parent_frame, text="Unpaid:  ", width=35, bg="sky blue",
                                      font=("Helvetica", 14))
        self.label_sum_of_payouts = Label(self.parent_frame, text="Sum of payouts:  ", bg="gold", width=35,
                                          font=("Helvetica", 14))
        self.label_days_to_next_payouts = Label(self.parent_frame,
                                                text="Days to next payout:  " + str(self.miner.days_to_next_payout()),
                                                width=35, font=("Helvetica", 14))
        self.label_eth_usd_pln_daily = Label(self.parent_frame,
                                             text=str(self.miner.get_daily_eth()) + " ETH | " + str(
                                                 round((self.miner.get_daily_eth() * self.miner.price_eth),
                                                       2)) + " USD | " + str(
                                                 round((
                                                         self.miner.get_daily_eth() * self.miner.price_eth * self.miner.price_pln_as_usd),
                                                     2)) + "PLN",
                                             width=35, bg="light salmon", font=("Helvetica", 14))
        self.label_eth_usd_pln_unpaid = Label(self.parent_frame,
                                              text=str(self.miner.get_unpaid_eth()) + " ETH | " + str(
                                                  round((self.miner.get_unpaid_eth() * self.miner.price_eth),
                                                        2)) + " USD | " + str(
                                                  round((
                                                          self.miner.get_unpaid_eth() * self.miner.price_eth * self.miner.price_pln_as_usd),
                                                      2)) + "PLN",
                                              width=35, bg="sky blue", font=("Helvetica", 14))
        self.label_eth_usd_pln_sum_payouts = Label(self.parent_frame,
                                                   text=str(self.miner.get_sum_payouts()) + " ETH | " + str(
                                                       round((self.miner.get_sum_payouts() * self.miner.price_eth),
                                                             2)) + " USD | " + str(
                                                       round((
                                                               self.miner.get_sum_payouts() * self.miner.price_eth * self.miner.price_pln_as_usd),
                                                           2)) + "PLN",
                                                   width=35, bg="gold", font=("Helvetica", 14))
        self.label_return_investment = Label(self.parent_frame,
                                                   text= f"Return on investment: {self.miner.get_percentage_of_return_on_investment()}%",
                                                   width=35, bg="green", font=("Helvetica", 14))
        # placing labels
        self.label_todays_eth_price.place(relx=0.5, rely=0.05, anchor=CENTER)
        self.label_current_hashrate.place(relx=0.5, rely=0.09, anchor=CENTER)
        self.label_daily_eth.place(relx=0.5, rely=0.13, anchor=CENTER)
        self.label_eth_usd_pln_daily.place(relx=0.5, rely=0.17, anchor=CENTER)

        self.label_unpaid_eth.place(relx=0.5, rely=0.21, anchor=CENTER)
        self.label_eth_usd_pln_unpaid.place(relx=0.5, rely=0.25, anchor=CENTER)

        self.label_sum_of_payouts.place(relx=0.5, rely=0.29, anchor=CENTER)
        self.label_eth_usd_pln_sum_payouts.place(relx=0.5, rely=0.33, anchor=CENTER)
        self.label_days_to_next_payouts.place(relx=0.5, rely=0.37, anchor=CENTER)
        self.label_return_investment.place(relx=0.5, rely=0.41, anchor=CENTER)

        # buttons
        self.quit_button = Button(self, text='Quit', command=self.quit)
        self.save_excel_button = Button(self, text="Save today's data to excel",
                                        command=self._save_data_to_excel_button_clicked, width=20,
                                        font=("Helvetica", 11))
        # placing buttons
        self.save_excel_button.place(relx=0.5, rely=0.9, anchor=CENTER)
        self.quit_button.place(relx=0.8, rely=0.9, anchor=CENTER)

    def _resize_image(self, event) -> None:
        """ Resize image on every window size change """

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)

    def _save_data_to_excel_button_clicked(self) -> None:
        """
        Function is called when clicking on button - save today's data to excel
        - saves today's data
        - place label with communicat that data is saved
        - make save data button disabled
        :return: None
        """
        self.save_data.save_todays_data_to_xlsx()  # save data to excel
        self.label_data_saved = Label(self, text="Today's data saved to excel file! :)", width=25,
                                      font=("Helvetica", 10))
        self.label_data_saved.place(relx=0.5, rely=0.85, anchor=CENTER)  # show communicat that data is saved
        self.save_excel_button['state'] = DISABLED  # make button disable
