import tkinter as tk
from tkinter import ttk

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.title('Distance Converter')

metersValue = tk.StringVar()
feetValue = tk.StringVar(value='Feet Shown Here')


def calculateFeet(*args):
    try:
        meters = float(metersValue.get())
        feet = meters * 3.28084
        feetValue.set(f"{feet:.3f}")

    except ValueError:
        pass


root.columnconfigure(0, weight=1)  # centers the main content as the window is expanded

main = ttk.Frame(root, padding=(30, 15))
main.grid()

metersLabel = ttk.Label(main, text='Meters: ')
metersInput = ttk.Entry(main, width=10, textvariable=metersValue)
metersLabel.grid(column=0, row=0, sticky='W', padx=5, pady=5)
metersInput.grid(column=1, row=0, sticky='EW', padx=5, pady=5)

feetLabel = ttk.Label(main, text='Feet: ')
feetDisplay = ttk.Label(main, textvariable=feetValue)
feetLabel.grid(column=0, row=1, sticky='W', padx=5, pady=5)
feetDisplay.grid(column=1, row=1, sticky='EW', padx=5, pady=5)

calcButton = ttk.Button(main, text='Calculate', command=calculateFeet)
calcButton.grid(column=0, row=2, columnspan=2, sticky="EW", padx=5, pady=5)

root.mainloop()
