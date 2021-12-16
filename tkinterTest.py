import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


def greet():
    print(f'Hello, {userName.get() or "World"}!')


root = tk.Tk()
root.title("Greeting App")

root.columnconfigure(0, weight=1)

inputFrame = ttk.Frame(root, padding=(20, 10, 20, 0))
inputFrame.grid(row=0, column=0, sticky='EW')

userName = tk.StringVar()

nameLabel = ttk.Label(inputFrame, text="Name: ")
nameLabel.grid(row=0, column=0, padx=(0, 10))
nameEntry = ttk.Entry(inputFrame, width=15, textvariable=userName)
nameEntry.grid(row=0, column=1)
nameEntry.focus()

buttonFrame = ttk.Frame(root, padding=(20, 10, 20, 0))
buttonFrame.grid(row=1, column=0, sticky='EW')
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)

greetButton = ttk.Button(buttonFrame, text="Greet", command=greet)
greetButton.grid(row=0, column=0, sticky='EW')
quitButton = ttk.Button(buttonFrame, text="Quit", command=root.destroy)
quitButton.grid(row=0, column=1, sticky='EW')

frame3 = ttk.Frame(root)
frame3.grid(row=2, column=0, sticky='EW')
frame3.grid_columnconfigure(0, weight=1)
frame3.grid_rowconfigure(0, weight=1)

text = tk.Text(frame3, height=8)
text.grid(row=0, column=0, sticky='EW')
text.insert("1.0", "Please enter a comment...")

textScroll = ttk.Scrollbar(frame3, orient="vertical", command=text.yview)
textScroll.grid(row=0, column=1, sticky="NS")
text["yscrollcommand"] = textScroll.set

checkButton = ttk.Checkbutton(frame3, text='Click Me')
checkButton.grid(row=1, column=0)
checkButton['state'] = 'normal'

frame4 = ttk.Frame(root)
frame4.grid(row=3, column=0, sticky="EW")

selectedWeekday = tk.StringVar()
weekday = ttk.Combobox(frame4, textvariable=selectedWeekday)
weekday['values'] = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
weekday.set('Enter the weekday...')
weekday['state'] = 'readonly'
weekday.pack()


def handleSelection(event):
    print('Today is', selectedWeekday.get())
    print("But we're going to change it to Friday")
    selectedWeekday.set('Friday')
    print(weekday.current())


listBoxFrame = ttk.Frame(root)
listBoxFrame.grid(row=4, column=0, sticky='EW')
weekday.bind("<<ComboboxSelected>>", handleSelection)
print(selectedWeekday, 'was selected.')

languages = ['C', 'Go', 'JavaScript', 'Perl', 'Python', 'Rust', 'C++', 'HTML5', 'Linux']
langVar = tk.StringVar(value=languages)
langsSelect = tk.Listbox(listBoxFrame, listvariable=langVar, height=6)
langsSelect['selectmode'] = 'extended'  # browse
langsSelect.pack(side='left')

listBoxScroll = ttk.Scrollbar(listBoxFrame, orient="vertical", command=langsSelect.yview)
listBoxScroll.pack(side='left', fill='y')
langsSelect["yscrollcommand"] = listBoxScroll.set


def handleSelectionChange(event):
    selectedIndices = langsSelect.curselection()
    for item in selectedIndices:
        print(langsSelect.get(item))


langsSelect.bind('<<ListboxSelect>>', handleSelectionChange)


initialValue = tk.IntVar(value=20)
spinBox = ttk.Spinbox(
    frame4,
    from_=0,
    to=30,
    textvariable=initialValue,
    wrap=False
)
spinBox.pack()


def handleScaleChange(event):
    print(scale.get())

currentValue = tk.DoubleVar()

scale = ttk.Scale(frame4, orient='horizontal', from_=0, to=10, command=handleScaleChange, variable=currentValue)
scale.pack(fill='x')

scale['state'] = 'normal'  # disabled


root.mainloop()
