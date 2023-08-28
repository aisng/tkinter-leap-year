import tkinter as tk


class LeapYearGUI:
    def __init__(self):
        self.lbl_result = None
        self.root = tk.Tk()
        self.root.geometry("460x500")
        self.root.resizable(0, 0)
        self.root.title("Leap year finder")
        self.lbl_header = tk.Label(
            self.root, text="Leap years between given interval", font=("Ariel", 16)
        )
        self.lbl_header.pack(padx=10, pady=10)

        self.entry_frame = tk.Frame(self.root)

        self.date_entry1 = tk.Entry(self.entry_frame, width=4, font=("Ariel", 20))
        self.dash_between_date_entries = tk.Label(
            self.entry_frame, text="\N{EN DASH}", font=("Ariel", 20)
        )
        self.date_entry_2 = tk.Entry(self.entry_frame, width=4, font=("Ariel", 20))
        self.submit_btn = tk.Button(
            self.entry_frame,
            text="Find leap years",
            font=("Ariel", 14),
            command=self.find_leap_and_show_result,
        )
        self.date_entry1.grid(row=0, column=0, sticky=tk.E, padx=5)
        self.dash_between_date_entries.grid(row=0, column=1, padx=5)
        self.date_entry_2.grid(row=0, column=2, padx=5)
        self.submit_btn.grid(row=0, column=3, padx=5)
        self.entry_frame.pack(side=tk.TOP)

        self.result_frame = tk.Frame(self.root)
        self.result_label = tk.Label(
            self.result_frame, text="Result will be displayed here", font=("Ariel", 14)
        )
        self.result_label.pack()
        self.result_frame.pack(side=tk.BOTTOM, expand=True)
        self.root.mainloop()

    def validate(self):
        if len(self.date_entry1.get()) > 4 and len(self.date_entry_2.get()) > 4:
            return False
        elif (
            not self.date_entry1.get().isdigit()
            and not self.date_entry_2.get().isdigit()
        ):
            return False
        return True

    def find_leap_and_show_result(self):
        result = []
        year1 = int(self.date_entry1.get())
        year2 = int(self.date_entry_2.get())
        for year in range(year1, year2 + 1):
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                result.append(year)

        self.result_label["text"] = f"Found {len(result)} results"
        self.result_listbox = tk.Listbox(
            self.result_frame, font=("Ariel", 14), height=10, width=12
        )
        self.result_listbox_scrollbar = tk.Scrollbar(self.result_frame)

        self.result_listbox_scrollbar.config(command=self.result_listbox.yview)
        self.result_listbox.config(yscrollcommand=self.result_listbox_scrollbar.set)
        self.result_listbox.insert(tk.END, *result)
        self.result_listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_listbox.pack(side=tk.LEFT, padx=5, pady=5)


LeapYearGUI()
