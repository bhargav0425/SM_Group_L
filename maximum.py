class Maximum:
    @staticmethod
    def calculate(data):
        if not data:
            raise ValueError("Data is empty")
        max_value = data[0]
        for x in data:
            if x > max_value:
                max_value = x
        return max_value