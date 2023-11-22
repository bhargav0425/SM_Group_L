class Helper:
    #merge sort implementation to sort the data 
    @staticmethod
    def merge_sort(data):
            if len(data) <= 1:
                return data

            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            left_half = Helper.merge_sort(left_half)
            right_half = Helper.merge_sort(right_half)

            return Helper.merge(left_half, right_half)

    @staticmethod 
    def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result

