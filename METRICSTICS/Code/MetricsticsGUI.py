# lLibrary and class Imports
import tkinter as tk
from MetricsticsCalculation import *
from tkinter import filedialog
from Helper import *
import random
import matplotlib.pyplot as plt
class MetricsticsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("METRICSTICS")
        self.root.geometry("1400x1400")  
        self.data_label = tk.Label(self.root, text="Enter comma-separated data. For example: Enter numbers separated by commas like this: 1,2,3,4,5,6", font=("Arial", 12))     
        self.data_entry = tk.Entry(self.root, font=("Arial", 12))
        self.data_label.pack(pady=10)
        self.data_entry.pack(padx=10)
        #Frame to set the general buttons to right side of the screen
        self.general_button_frame = tk.Frame(self.root)
        self.general_button_frame.pack(side=tk.RIGHT)
        #Label for displaying the results
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14),wraplength=400)
        self.result_label.pack(pady=20)
        #Button for uploading file
        upload_btn = tk.Button(self.general_button_frame, text="Upload File", font=("Arial", 12), command=self.upload_file)
        upload_btn.configure(bg="blue", width=15, height=2)
        upload_btn.pack(side=tk.TOP, padx=10, pady=10)   
        #Button for Generating random dataset
        random_data_button = tk.Button(self.general_button_frame, text="Generate Random Data", font=("Arial", 12), command=self.generate_random_data)
        random_data_button.configure(bg="green", width=20, height=2)
        random_data_button.pack(side=tk.TOP, padx=10, pady=10)
        #Button for visualizing dataset
        visualize_button = tk.Button(self.general_button_frame, text="Visualize Data", font=("Arial", 12), command=self.visualize_data)
        visualize_button.configure(bg="orange", width=15, height=2)
        visualize_button.pack(side=tk.TOP, padx=10, pady=10)        
        #All statistics buttons With their respective methods.
        self.calculate_buttons = [
            ("Minimum", MetricsticsCalculation.get_min),
            ("Maximum", MetricsticsCalculation.get_max),
            ("Mean", MetricsticsCalculation.get_mean),
            ("Median", MetricsticsCalculation.get_median),
            ("Mode", MetricsticsCalculation.get_mode),
            ("MAD", MetricsticsCalculation.get_mad),
            ("Standard Deviation", MetricsticsCalculation.get_stddev)
        ]
        self.create_buttons()
        self.create_reset_button()  
        self.create_show_all_button()  
        self.save_button()
        self.logout_button()
        self.error_flag = False 
    #Function that display the data visualization      
    def visualize_data(self):
        data_input = self.data_entry.get()
        if not data_input:
            self.result_label.config(text="Please enter data.", fg="red")
            return
        if data_input.endswith(","):
            self.result_label.config(text="Error: Invalid input.", fg="red")
            return
        try:
            data = [float(x) for x in data_input.split(',')]  # Use float instead of int
            number = len(data)
            # Calculate required statistics
            min_value = MetricsticsCalculation.get_min(data, number)
            max_value = MetricsticsCalculation.get_max(data, number)
            mean_value = MetricsticsCalculation.get_mean(data, number)
            median_value = MetricsticsCalculation.get_median(data, number)
            mad=MetricsticsCalculation.get_mad(data,number)
            stdd=MetricsticsCalculation.get_stddev(data,number)
            # Create a bar chart
            labels = ['Minimum', 'Maximum', 'Mean', 'Median','MAD','Standard_deviation']
            values = [min_value, max_value, mean_value, median_value,mad,stdd]
            plt.bar(labels, values, color=['blue', 'red', 'green', 'purple','black','yellow'])
            plt.xlabel('Statistics')
            plt.ylabel('Values')
            plt.title('Visualization of Statistics')
            plt.show()
        except ValueError as e:
            self.result_label.config(text="Only Numbers are allowed.", fg="red")            
    #Function that creates individual buttons for individual METRICSTICS.
    def create_buttons(self):
        #Frame to set the individual METRICSTICS buttons to left side of the screen
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.LEFT,pady=10)
        # Loop Through the calculate_buttons to create buttons 
        for button_text, func in self.calculate_buttons:
            button = tk.Button(button_frame, text=button_text, font=("Arial", 12), command=lambda f=func: self.calculate_and_display(f))
            button.configure(bg="green", width=15, height=2)
            button.pack(side=tk.TOP, padx=10,pady=10)
    #Funtion to handle upload file
    def upload_file(self):
        file_path = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                file_content = file.read()
                self.data_entry.delete(0, tk.END)
                self.data_entry.insert(tk.END, file_content)
    #Function that that generates the random data
    def generate_random_data(self):
        rd = ','.join(map(str, [random.randint(1, 1000) for _ in range(3000)]))
        self.data_entry.delete(0, tk.END)
        self.data_entry.insert(tk.END, rd)
    #Reset Button
    def create_reset_button(self):
        reset_button = tk.Button(self.general_button_frame, text="Reset", font=("Arial", 12), command=self.reset_data_field)
        reset_button.configure(bg="green", width=15, height=2)
        reset_button.pack(side=tk.TOP, padx=10, pady=10)
    #Save Button
    def save_button(self):
        save_button = tk.Button(self.general_button_frame, text="save data", font=("Arial", 12), command=self.save)
        save_button.configure(bg="green", width=15, height=2)
        save_button.pack(side=tk.TOP, padx=10, pady=10)
    #Show All Statistics Button
    def create_show_all_button(self):
        show_all_button = tk.Button(self.general_button_frame, text="Show All Statistics", font=("Arial", 12), command=self.show_all_statistics)
        show_all_button.configure(bg="green", width=15, height=2)
        show_all_button.pack(side=tk.TOP, padx=10, pady=10)
    #Show Logout Button
    def logout_button(self):
        logout_button = tk.Button(self.general_button_frame, text="Exit", font=("Arial", 12), command=self.logout)
        logout_button.configure(bg="green", width=15, height=2)
        logout_button.pack(side=tk.TOP, padx=10, pady=10)
    #Show Reset Button
    def reset_data_field(self):
        self.result_label.config(text="")
        self.data_entry.delete(0, tk.END) 
    #Function to calculate the individual statistics  
    def calculate_and_display(self, func):
        data_input = self.data_entry.get()
        if not data_input:
            self.result_label.config(text="Please enter data.", fg="red")
            return
        if data_input.endswith(","):
            self.result_label.config(text="Error: Invalid input.", fg="red")
            return
        try:
            data = [float(x) for x in data_input.split(',')]  # Use float instead of int
            number = len(data)
            result = func(data,number)
            button_text = [button_text for button_text, f in self.calculate_buttons if f == func][0]
            self.result_label.config(text=f"{button_text}: {result}", fg="green")
        except ValueError as e:
            self.result_label.config(text="Only Numbers are allowed.", fg="red")
    #Function to show all the statistics
    def show_all_statistics(self):
        data_input = self.data_entry.get()
        if not data_input:
            self.result_label.config(text="Please enter data. It cannot be left blank.", fg="red")
            return
        if data_input.endswith(","):
            self.result_label.config(text="Error: Enter comma-separated data (1,2,3,4,5) ensuring it doesn't end with a comma.", fg="red")
            return
        try:
            data = [float(x) for x in data_input.split(',')]
            number = len(data)
            results = []
            for button_text, func in self.calculate_buttons:                
                result = func(data,number)
                results.append(f"{button_text}: {result}")

            self.result_label.config(text="\n".join(results), fg="green")
        except ValueError as e:
            self.result_label.config(text="Only comma-separated data is allowed(1,2,3,4,5))", fg="red")
    #Save The data in the txt file
    def save(self):
        data_input = self.data_entry.get()
        if not data_input:
            self.result_label.config(text="Please enter data.", fg="red")
            return
        if data_input.endswith(","):
            self.result_label.config(text="Error: Data cannot end with a comma.", fg="red")
            return
        try:
            data = [float(x) for x in data_input.split(',')]  # Use float instead of int
            number = len(data)
            results = []
            for button_text, func in self.calculate_buttons:
                result = func(data,number)
                results.append(f"{button_text}: {result}")
            try:
                file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

                if file_path:
                    with open(file_path, 'w') as file:
                        file.write(f"{results}")

                    return f"Statistics saved successfully to {file_path}."
                else:
                    return "Save operation cancelled."
            except Exception as e:
                return f"Error occurred while saving: {str(e)}"
            #self.result_label.config(text="\n".join(results), fg="green")

        except ValueError as e:
            self.result_label.config(text=f"Error: {str(e)}", fg="red")
    #Function to logout/exit. Which will close the the application.
    def logout(self):
        self.root.destroy()
