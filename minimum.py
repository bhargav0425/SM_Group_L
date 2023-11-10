class Minimum:
    @staticmethod
    def calculate(data):
        if not data:
            raise ValueError("Data is empty")
        min_value = data[0]
        for x in data:
            if x < min_value:
                min_value = x
        return min_value