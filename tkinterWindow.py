import tkinter as tk
from tkinter import ttk
import restaurantInfo
import time

root = tk.Tk()
root.title('Restaurant POS Main Window')
root.config(background="#FFFFFF")
root.geometry("900x700")

topBar = ttk.Label(root, text=time.ctime(), background='#000000', foreground='#ffffff')
topBar.pack(side='top', fill='both')

bottomBar = ttk.Label(root, text='Restaurant Software - made by McLean Turner',
                      background='#000000', foreground='#ffffff')
bottomBar.pack(side='bottom', fill='both')


#  SIDE BAR MENU DISPLAY
leftMenuFrame = tk.Frame(root, bg='#1c2d60', width=200, height=600)
leftMenuFrame.pack(side='left', fill='both')
rightFrame = ttk.Frame(root)
rightFrame.pack()

homeButton = ttk.Button(leftMenuFrame, text='Home')
tablesButton = ttk.Button(leftMenuFrame, text='Table Management')
menuButton = ttk.Button(leftMenuFrame, text='Menu', command=rightFrame.tkraise())
employeeButton = ttk.Button(leftMenuFrame, text='Employee Management')

homeButton.pack(padx=10, pady=25, fill='both')
tablesButton.pack(padx=10, pady=25, fill='both')
menuButton.pack(padx=10, pady=25, fill='both')
employeeButton.pack(padx=10, pady=25, fill='both')



#  MENU FRAME DISPLAY
s = ttk.Style()
s.configure('my.TButton', font=('serif', 15))
total = 0
totalLabel = tk.StringVar(value=f'Total: ${total:.2f}')


availableItems = restaurantInfo.readRestaurantInfo('availableItems.csv')
itemList = availableItems[0]
priceList = availableItems[1]
categoryList = availableItems[2]
COLUMNS = 3
total = 0
label = tk.Label(rightFrame, textvariable=totalLabel, foreground='#000000')
label.grid(row=5, column=1, padx=5, pady=5)

for i, item in enumerate(itemList):
    lbl = ttk.Button(rightFrame, text=item, style='my.TButton')
    row, column = divmod(i, COLUMNS)
    lbl.grid(row=row, column=column, sticky='news', ipadx=25, ipady=25)

root.mainloop()
