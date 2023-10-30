import tkinter as tk

class Metricstics:
    def __init__(self, data):
        self.data = data

    def minimum(self):
        if not self.data:
            raise ValueError("Data is empty")
        min_value = self.data[0]
        for x in self.data:
            if x < min_value:
                min_value = x
        return min_value

    def maximum(self):
        if not self.data:
            raise ValueError("Data is empty")
        max_value = self.data[0]
        for x in self.data:
            if x > max_value:
                max_value = x
        return max_value

    def mode(self):
        if not self.data:
            raise ValueError("Data is empty")
        counts = {}
        max_count = 0
        mode = []

        for x in self.data:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1

            if counts[x] > max_count:
                max_count = counts[x]

        for key, value in counts.items():
            if value == max_count:
                mode.append(key)

        return mode

    def median(self):
        if not self.data:
            raise ValueError("Data is empty")
        sorted_data = self.data[:]
        n = len(sorted_data)
        sorted_data.sort()

        if n % 2 == 0:
            middle1 = sorted_data[n // 2 - 1]
            middle2 = sorted_data[n // 2]
            return (middle1 + middle2) / 2
        else:
            return sorted_data[n // 2]

    def mean(self):
        if not self.data:
            raise ValueError("Data is empty")
        total = 0
        for x in self.data:
            total += x
        return total / len(self.data)

    def mad(self):
        if not self.data:
            raise ValueError("Data is empty")
        mean = self.mean()
        total_deviation = 0
        for x in self.data:
            total_deviation += abs(x - mean)
        return total_deviation / len(self.data)

    def standard_deviation(self):
        if not self.data:
            raise ValueError("Data is empty")
        mean = self.mean()
        total_squared_deviation = 0
        for x in self.data:
            total_squared_deviation += (x - mean) ** 2
        return (total_squared_deviation / len(self.data)) ** 0.5

class MetricsticsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("METRICSTICS")

        self.data_label = tk.Label(self.root, text="Enter comma-separated data:")
        self.data_entry = tk.Entry(self.root)
        self.data_label.pack()
        self.data_entry.pack()

        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_stats)
        self.calculate_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.error_flag = False

    def calculate_stats(self):
        try:
            data_input = self.data_entry.get()
            if not data_input and not self.error_flag:
                self.result_label.config(text="Please enter data.")
                self.error_flag = True
                return
            elif not data_input and self.error_flag:
                self.error_flag = False
                return

            data = [int(x) for x in data_input.split(',')]
            metricstics = Metricstics(data)

            result = f"Minimum: {metricstics.minimum()}\n" \
                     f"Maximum: {metricstics.maximum()}\n" \
                     f"Mode: {metricstics.mode()}\n" \
                     f"Median: {metricstics.median()}\n" \
                     f"Mean: {metricstics.mean()}\n" \
                     f"Mean Absolute Deviation (MAD): {metricstics.mad()}\n" \
                     f"Standard Deviation: {metricstics.standard_deviation()}"

            self.result_label.config(text=result)
        except ValueError as e:
            self.result_label.config(text=f"Error: {str(e)}")
            self.error_flag = True

def main():
    root = tk.Tk()
    app = MetricsticsGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
