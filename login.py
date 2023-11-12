import tkinter as tk
from mad import MAD
from maximum import Maximum
from mean import Mean
from median import Median
from minimum import Minimum
from mode import Mode
from standard_dev import StandardDeviation
from main import MetricsticsGUI
class LoginGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x200")
        self.username_label = tk.Label(self.root, text="Username:", font=("Arial", 12))
        self.username_entry = tk.Entry(self.root, font=("Arial", 12))
        self.password_label = tk.Label(self.root, text="Password:", font=("Arial", 12))
        self.password_entry = tk.Entry(self.root, font=("Arial", 12))  # To hide the password input
        self.login_button = tk.Button(self.root, text="Login", font=("Arial", 12), command=self.login)

        self.username_label.pack(pady=10)
        self.username_entry.pack(pady=10)
        self.password_label.pack(pady=10)
        self.password_entry.pack(pady=10)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # You can customize this logic to validate the username and password
        if username == "1" and password == "1":
            self.root.destroy()  # Close the login window
            root = tk.Tk()
            app = MetricsticsGUI(root)
            root.mainloop()
        else:
            # Show an error message or take appropriate action for invalid login
            pass

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


def main():
    root = tk.Tk()
    login_app = LoginGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()