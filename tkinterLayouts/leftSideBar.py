import tkinter as tk
from tkinter import ttk


class sideMenu:
    def __init__(self, root):
        self.root = root

        leftMenuFrame = tk.Frame(self.root, bg='#1c2d60', width=200, height=600)
        leftMenuFrame.pack(side='left', fill='both')

        homeButton = ttk.Button(self.leftMenuFrame, text='Home')
        tablesButton = ttk.Button(self.leftMenuFrame, text='Table Management')
        menuButton = ttk.Button(self.leftMenuFrame, text='Menu')
        employeeButton = ttk.Button(self.leftMenuFrame, text='Employee Management')

        homeButton.pack(padx=10, pady=25, fill='both')
        tablesButton.pack(padx=10, pady=25, fill='both')
        menuButton.pack(padx=10, pady=25, fill='both')
        employeeButton.pack(padx=10, pady=25, fill='both')
