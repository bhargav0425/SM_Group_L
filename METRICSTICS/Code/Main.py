# import necessary libraries
import tkinter as tk

from MetricsticsGUI import *

class Main:
   
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        screen_width = root.winfo_screenwidth()
        self.root.geometry('1024x768')
        username_label = tk.Label(self.root, text="Username(admin):", font=("Arial", 12))
        username_label.pack(pady=10)

        password_label = tk.Label(self.root, text="Password(admin):", font=("Arial", 12))
        password_label.pack(pady=10)
        
        self.username_entry = tk.Entry(self.root, font=("Arial", 12))
        self.username_entry.pack(pady=10)
        
        self.password_entry = tk.Entry(self.root, font=("Arial", 12))
        self.password_entry.pack(pady=10)
        
        login_button = tk.Button(self.root, text="Login", font=("Arial", 12), command=self.login)
        login_button.pack(pady=20)

        self.login_label = tk.Label(self.root, text="", font=("Arial", 14),wraplength=400)
        self.login_label.pack(pady=20)



    # login functionality
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin":
            self.root.destroy()  
            root = tk.Tk()
            app = MetricsticsGUI(root)
            root.mainloop()
        else:
            self.login_label.config(text="Please Check your Id and Password", fg="red")
            pass
# Main window of the Application
def main():
    root = tk.Tk()
    login_app = Main(root)
    root.mainloop()

if __name__ == "__main__":
    main()

