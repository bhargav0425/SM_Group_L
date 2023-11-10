class Mode:
    @staticmethod
    def calculate(data):
        if not data:
            raise ValueError("Data is empty")
        counts = {}
        max_count = 0
        mode = []

        for x in data:
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