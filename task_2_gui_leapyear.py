import tkinter as tk


class LeapYearGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x300")
        self.root.title("Leap year finder")
        self.lbl_header = tk.Label(self.root, text="Leap years between given interval", font=("Ariel", 16))
        self.lbl_header.pack(padx=10, pady=10)

        self.frm_entry = tk.Frame(self.root)

        # self.vcmd = (self.root.register(self.validate), '%P')
        self.entry1 = tk.Entry(self.frm_entry, width=4, font=("Ariel", 20))
        self.lbl_dash = tk.Label(self.frm_entry, text="\N{EN DASH}", font=("Ariel", 20))
        self.entry2 = tk.Entry(self.frm_entry, width=4, font=("Ariel", 20))
        self.btn1 = tk.Button(self.frm_entry, text="Find leap years", font=("Ariel", 14), command=self.find_leap)
        self.entry1.grid(row=0, column=0, sticky=tk.E, padx=5)
        self.lbl_dash.grid(row=0, column=1, sticky=tk.E, padx=5)
        self.entry2.grid(row=0, column=2, sticky=tk.W, padx=5)
        self.btn1.grid(row=0, column=3, sticky=tk.W, padx=5)

        self.frm_entry.pack()

        self.lbl_result = tk.Label(self.root, text=f"Results:\n", font=("Ariel", 12))
        # self.lbl_result.pack(padx=5, pady=5, side="left",
        #                      text=) # TODO: sugaut rezultatą ir jį parodyt kaip label
        self.root.mainloop()

    def validate(self):
        if len(self.entry1.get()) > 4 and len(self.entry2.get()) > 4:
            return False
        elif not self.entry1.get().isdigit() and not self.entry2.get().isdigit():
            return False
        return True

    def find_leap(self):
        result = []
        year1 = int(self.entry1.get())
        year2 = int(self.entry2.get())
        for year in range(year1, year2 + 1):
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                result.append(year)
        return result

    def show_result(self):



LeapYearGUI()
