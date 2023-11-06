from mean import Mean
class MAD:
    @staticmethod
    def calculate(data):
        if not data:
            raise ValueError("Data is empty")
        mean = Mean.calculate(data)
        total_deviation = 0
        for x in data:
            total_deviation += abs(x - mean)
        return total_deviation / len(data)