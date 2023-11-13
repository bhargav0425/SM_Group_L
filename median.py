class Median:
    @staticmethod
    def calculate(data):
        if not data:
            raise ValueError("Data is empty")
        sorted_data = data[:]
        n = len(sorted_data)
        sorted_data.sort()
        if n % 2 == 0:
            middle1 = sorted_data[n // 2 - 1]
            middle2 = sorted_data[n // 2]
            return (middle1 + middle2) / 2
        else:
            return sorted_data[n // 2]