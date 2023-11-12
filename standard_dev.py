from mean import Mean
class StandardDeviation:
    @staticmethod
    def calculate(data):
        if not data:
            raise ValueError("Data is empty")
        mean = Mean.calculate(data)
        total_squared_deviation = 0
        for x in data:
            total_squared_deviation += (x - mean) ** 2
        return (total_squared_deviation / len(data)) ** 0.5