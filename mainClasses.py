import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from restaurantSoftware import restaurantInfo
from clock import clock

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


class restaurantSoftware(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Restaurant Software POS")
        self.frames = dict()

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky='EW')

        self.sideNavMenu = sideNavMenu(container, self, width=200, height=600)
        self.sideNavMenu.grid(row=0, column=0)

        style = ttk.Style()

        for frameClass in (homeFrame, tableManagementFrame, menuFrame, employeeManagementFrame):
            frame = frameClass(container, self)
            self.frames[frameClass] = frame
            style.configure(f'{frame}.TFrame', background='black')
            frame.grid(row=0, column=1, sticky='NESW')


        self.show_frame(homeFrame)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


class sideNavMenu(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        homeButton = ttk.Button(self, text='Home', command=lambda: controller.show_frame(homeFrame))
        tablesButton = ttk.Button(self, text='Table Management', command=lambda: controller.show_frame(tableManagementFrame))
        menuButton = ttk.Button(self, text='Menu', command=lambda: controller.show_frame(menuFrame))
        employeeButton = ttk.Button(self, text='Employee Management', command=lambda: controller.show_frame(employeeManagementFrame))

        homeButton.pack(padx=10, pady=25, fill='both')
        tablesButton.pack(padx=10, pady=25, fill='both')
        menuButton.pack(padx=10, pady=25, fill='both', )
        employeeButton.pack(padx=10, pady=25, fill='both')


class homeFrame(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        clockFrame = clock(self)
        clockFrame.grid()


class tableManagementFrame(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)


class menuFrame(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        self.tableTotal = tk.DoubleVar(value=0.0)
        self.total = 0

        tableNumber = 12
        tableList = []
        for table in range(0, tableNumber):
            tableList.append(table + 1)

        self.availableItems = restaurantInfo.readRestaurantInfo('availableItems.csv')
        self.itemList = self.availableItems[0]
        self.priceList = self.availableItems[1]
        self.categoryList = self.availableItems[2]

        tableLabel = ttk.Label(self, text='Table Number: ', font=('Segoe UI', 16))
        tableLabel.grid(row=0, column=0)

        self.selectedTable = tk.StringVar()
        tableSelector = ttk.Combobox(self, textvariable=self.selectedTable, width=50, font=('Segoe UI', 16))
        tableSelector['values'] = tableList
        tableSelector['state'] = 'readonly'
        tableSelector.current(0)
        tableSelector.bind('<<ComboboxSelected>>', self.showListbox)
        tableSelector.grid(row=0, column=1, columnspan=2, padx=15, pady=15)


        COLUMNS = 3

        for i, item in enumerate(self.itemList):
            lbl = ttk.Button(self, text=item, style='my.TButton', command=lambda item=self.itemList[i]: [self.updateReceipt(item), self.showListbox('')])
            row, column = divmod(i, COLUMNS)
            lbl.grid(row=row + 1, column=column, sticky='news', ipadx=25, ipady=25)

        self.tableInfoFrame = ttk.Frame(self)
        self.tableInfoFrame.grid(row=1, column=3, padx=15, pady=15, rowspan=5)

        self.receiptItems = []
        self.receiptPrices = []
        self.receiptItemsDICT = {}
        self.receiptPricesDICT = {}

        for table in range(tableNumber):
            self.receiptItemsDICT[table + 1] = []
            self.receiptPricesDICT[table + 1] = []

        self.selectedReceiptItem = tk.StringVar()
        self.receiptBox = tk.Listbox(self.tableInfoFrame, listvariable=self.selectedReceiptItem)
        self.receiptBox.pack()

        totalLabel = ttk.Label(self.tableInfoFrame, textvariable=self.tableTotal)
        totalLabel.pack()
        resetTotalButton = ttk.Button(self.tableInfoFrame, text='Reset Receipt', command=self.resetReceipt)
        resetTotalButton.pack()

        deleteSelectedItemButton = ttk.Button(self.tableInfoFrame, text='Delete Selected Item', command=self.deleteSelectedItem)
        deleteSelectedItemButton.pack()



    def updateReceipt(self, item):
        self.receiptItemsDICT[int(self.selectedTable.get())].append(item)

        self.receiptPricesDICT[int(self.selectedTable.get())].clear()  # this dictionary must be cleared because it iterates through another dictionary

        for item in self.receiptItemsDICT[int(self.selectedTable.get())]:
            if item in self.itemList:
                self.receiptPricesDICT[int(self.selectedTable.get())].append(self.priceList[self.itemList.index(item)])


    def resetReceipt(self):
        self.receiptPricesDICT[int(self.selectedTable.get())].clear()  # resets the receipt prices for the specified table
        self.receiptItemsDICT[int(self.selectedTable.get())].clear()   # resets the receipt items for the specified table
        self.tableTotal.set(round(sum(self.receiptPricesDICT[int(self.selectedTable.get())]), 2))

        self.receiptBox.delete(0, 'end')
        for item in self.receiptItemsDICT[int(self.selectedTable.get())]:
            self.receiptBox.insert(0, item)
        self.tableTotal.set(round(sum(self.receiptPricesDICT[int(self.selectedTable.get())]), 2))

    def deleteSelectedItem(self):
        items = self.receiptBox.curselection()
        for item in items:
            menuItem = self.receiptBox.get(item)
        self.receiptItemsDICT[int(self.selectedTable.get())].remove(menuItem)

        for i, thing in enumerate(self.itemList):
            if thing == menuItem:
                price = self.priceList[i]
                self.receiptPricesDICT[int(self.selectedTable.get())].remove(price)

        self.receiptBox.delete(0, 'end')
        for item in self.receiptItemsDICT[int(self.selectedTable.get())]:
            self.receiptBox.insert(0, item)
        self.tableTotal.set(round(sum(self.receiptPricesDICT[int(self.selectedTable.get())]), 2))


    def showListbox(self, event):
        self.receiptBox.delete(0, 'end')
        for item in self.receiptItemsDICT[int(self.selectedTable.get())]:
            self.receiptBox.insert(0, item)
        self.tableTotal.set(sum(self.receiptPricesDICT[int(self.selectedTable.get())]))


class employeeManagementFrame(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)


root = restaurantSoftware()

font.nametofont("TkDefaultFont").configure(size=15)

root.columnconfigure(0, weight=1)  # centers the main content as the window is expanded
root.mainloop()
