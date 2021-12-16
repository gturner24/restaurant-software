import tkinter as tk
from tkinter import ttk
from programSkelekton import mainWindow
from menuFrame import menuFrame


if __name__ == '__main__':
    x = mainWindow()
    y = menuFrame(x.rightFrame)
    y.initiateWindow()
    x.startWindow()

