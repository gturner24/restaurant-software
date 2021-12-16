import tkinter as tk
from tkinter import ttk
from restaurantSoftware import restaurantInfo


class menuFrame:
    def __init__(self, frame):
        self.frame = frame



    def initiateWindow(self):
        s = ttk.Style()
        s.configure('my.TButton', font=('serif', 15))

        totalLabel = tk.StringVar(value=f'Total: ${0:.2f}')

        availableItems = restaurantInfo.readRestaurantInfo('availableItems.csv')
        itemList = availableItems[0]
        priceList = availableItems[1]
        categoryList = availableItems[2]
        COLUMNS = 3
        total = 0
        label = tk.Label(self.frame, textvariable=totalLabel, foreground='#000000')
        label.grid(row=5, column=1, padx=5, pady=5)

        for i, item in enumerate(itemList):
            lbl = ttk.Button(self.frame, text=item, style='my.TButton')
            row, column = divmod(i, COLUMNS)
            lbl.grid(row=row, column=column, sticky='news', ipadx=25, ipady=25)