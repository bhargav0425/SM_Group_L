# import tkinter as tk
# from mad import MAD
# from maximum import Maximum
# from mean import Mean
# from median import Median
# from minimum import Minimum
# from mode import Mode
# from standard_dev import StandardDeviation


# class MetricsticsGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("METRICSTICS")
#         self.root.geometry("400x400")  # Set initial window size
#         self.data_label = tk.Label(self.root, text="Enter comma-separated data:", font=("Arial", 12))
#         self.data_entry = tk.Entry(self.root, font=("Arial", 12))
#         self.data_label.pack(pady=10)
#         self.data_entry.pack(pady=10)

#         self.calculate_buttons = [
#             ("Minimum", Minimum.calculate),
#             ("Maximum", Maximum.calculate),
#             ("Mean", Mean.calculate),
#             ("Median", Median.calculate),
#             ("Mode", Mode.calculate),
#             ("MAD", MAD.calculate),
#             ("Standard Deviation", StandardDeviation.calculate)
#         ]

#         self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
#         self.result_label.pack(pady=20)

#         self.create_buttons()
#         self.error_flag = False

#     def create_buttons(self):
#         for button_text, func in self.calculate_buttons:
#             button = tk.Button(self.root, text=button_text, font=("Arial", 12), command=lambda f=func: self.calculate_and_display(f))
#             button.pack(pady=5, padx=10, ipadx=10)

#     def calculate_and_display(self, func):
#         data_input = self.data_entry.get()
#         if not data_input:
#             self.result_label.config(text="Please enter data.", fg="red")
#             return
#         if data_input.endswith(","):
#             self.result_label.config(text="Error: Data cannot end with a comma.", fg="red")
#             return
#         try:
#             data = [int(x) for x in data_input.split(',')]
#             result = func(data)
#             self.result_label.config(text=f"{func.__name__}: {result}", fg="green")
#         except ValueError as e:
#             self.result_label.config(text=f"Error: {str(e)}", fg="red")

import tkinter as tk
from mad import MAD
from maximum import Maximum
from mean import Mean
from median import Median
from minimum import Minimum
from mode import Mode
from standard_dev import StandardDeviation

class MetricsticsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("METRICSTICS")
        self.root.geometry("400x400")  # Set initial window size
        self.data_label = tk.Label(self.root, text="Enter comma-separated data:", font=("Arial", 12))
        self.data_entry = tk.Entry(self.root, font=("Arial", 12))
        self.data_label.pack(pady=10)
        self.data_entry.pack(pady=10)

        self.calculate_buttons = [
            ("Minimum", Minimum.calculate),
            ("Maximum", Maximum.calculate),
            ("Mean", Mean.calculate),
            ("Median", Median.calculate),
            ("Mode", Mode.calculate),
            ("MAD", MAD.calculate),
            ("Standard Deviation", StandardDeviation.calculate)
        ]

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

        self.create_buttons()
        self.create_reset_button()  # Add a reset button

        self.error_flag = False

    def create_buttons(self):
        for button_text, func in self.calculate_buttons:
            button = tk.Button(self.root, text=button_text, font=("Arial", 12), command=lambda f=func: self.calculate_and_display(f))
            button.pack(pady=5, padx=10, ipadx=10)

    def create_reset_button(self):
        reset_button = tk.Button(self.root, text="Reset", font=("Arial", 12), command=self.reset_data_field)
        reset_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    def reset_data_field(self):
        self.data_entry.delete(0, tk.END)  # Clear the data field

    def calculate_and_display(self, func):
        data_input = self.data_entry.get()
        if not data_input:
            self.result_label.config(text="Please enter data.", fg="red")
            return
        if data_input.endswith(","):
            self.result_label.config(text="Error: Data cannot end with a comma.", fg="red")
            return
        try:
            data = [int(x) for x in data_input.split(',')]
            result = func(data)
            self.result_label.config(text=f"{func.__name__}: {result}", fg="green")
        except ValueError as e:
            self.result_label.config(text=f"Error: {str(e)}", fg="red")

#





