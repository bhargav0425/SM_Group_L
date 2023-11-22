from Helper import *
class MetricsticsCalculation:
    # Static method to calculate the minimum value in the given data
    @staticmethod
    def get_min(data,number):
            if not data:
                raise ValueError("Please enter comma separated values in order to calculate statistics")
            minimum_value = data[0]
            for value in data:
                if value < minimum_value:
                    minimum_value = value
            return minimum_value
    # Static method to calculate the max value in the given data
    @staticmethod
    def get_max(data,number):
            if not data:
                raise ValueError("Please enter comma separated values in order to calculate statistics")
            maximum_value = data[0]
            for value in data:
                if value > maximum_value:
                    maximum_value = value
            return maximum_value
    # Static method to calculate the mean value in the given data
    @staticmethod
    def get_mean(data,count):
            if not data:
                raise ValueError("Please enter comma separated values in order to calculate statistics")

            total = 0
            for value in data:
                total += value

            return total / count
    # Static method to calculate the mad value in the given data
    @staticmethod
    def get_mad(data,n):
            if not data:
                raise ValueError("Please Enter comma separated values in order to calculate statistics")

            # mean calculation of the given data set.
            mean = MetricsticsCalculation.get_mean(data,n) 
            # Calculate the total absolute deviation 
            total_deviation = 0
            for x in data:
                diff = x - mean
                total_deviation += diff if diff >= 0 else -diff

            mad = total_deviation / n
            return mad
    # Static method to calculate the median value in the given data
    @staticmethod
    def get_median(data,number):
            if not data:
                raise ValueError("Please enter comma separated values in order to calculate statistics")
            
            # Sorting using Bubble Sort
            data =   Helper.merge_sort(data)

            # Calculate the median based on the sorted data set.
            if number % 2 == 0:
                middle1 = data[number // 2 - 1]
                middle2 = data[number // 2]
                return (middle1 + middle2) / 2
            else:
                return data[number // 2]       
    
    # Static method to calculate the mode value in the given data
    @staticmethod
    def get_mode(data,n):
            if not data:
                raise ValueError("Please enter comma separated values in order to calculate statistics")

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

            for key in counts:
                value = counts[key]
                if value == max_count:
                    if not mode:
                        mode = [key]
                    else:
                        mode = mode + [key]

            return mode
    
    # Static method to calculate the standard deviation value in the given data
    @staticmethod
    def get_stddev(data,n):
            if not data:
                raise ValueError("Please enter comma separated values in order to calculate statistics")

            mean = MetricsticsCalculation.get_mean(data,n)
            total_squared_deviation = 0

            for value in data:
                total_squared_deviation += (value - mean) ** 2

            return (total_squared_deviation / n) ** 0.5
