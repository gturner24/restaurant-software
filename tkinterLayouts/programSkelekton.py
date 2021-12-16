import tkinter as tk
from tkinter import ttk
import leftSideBar
import time
from menuFrame import menuFrame


class mainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Restaurant POS Main Window')
        self.root.config(background="#FFFFFF")
        self.root.geometry("900x700")

        self.topBar = ttk.Label(self.root, text=time.ctime(), background='#000000', foreground='#ffffff')
        self.topBar.pack(side='top', fill='both')
        self.sideBar = leftSideBar.sideMenu(self.root)

        self.bottomBar = ttk.Label(self.root, text='Restaurant Software - made by McLean Turner',
                                   background='#000000', foreground='#ffffff')
        self.bottomBar.pack(side='bottom', fill='both')

        self.rightFrame = ttk.Frame(self.root)
        self.rightFrame.pack()



    def startWindow(self):
        self.root.mainloop()


    def displayMenu(self):
        self.menuFrame = menuFrame(self.rightFrame)
