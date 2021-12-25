from time import strftime
from tkinter import Label
from tkinter import ttk


# ======= Configuring window =========
class clock(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(*args, **kwargs)  # =======Background of the clock=====

        self.clock_label = Label(container, bg="black", fg="white", font=("Segoe UI", 30, "bold"), relief="flat")
        self.clock_label.place(x=20, y=20)
        self.update_label()


    def update_label(self):
        """
        This function will update the clock

        every 80 milliseconds
        """
        current_time = strftime("%H: %M: %S\n %m/%d/%Y ")
        self.clock_label.configure(text=current_time)
        self.clock_label.after(80, self.update_label)
        self.clock_label.pack(anchor="center")



# ==============The end by github.com/kalebu ==========
