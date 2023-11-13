class Mean:
    @staticmethod
    def calculate(data):
        if not data:
            raise ValueError("Data is empty")
        total = 0
        for x in data:
            total += x
        return total / len(data)