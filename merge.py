def merge_list(list1, list2):
    # Check if the input is valid lists
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Both inputs must be lists")

    # Function to merge two lists and sort them
    def merge_sort(left, right):
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    # Merge and sort the two unsorted lists
    sorted_result = merge_sort(list1, list2)

    return sorted_result

# Example usage:
# result = merge_list([1, 5, 3, 7], [6, 2, 4])
# print(result)  # This should output [1, 2, 3, 4, 5, 6, 7]

# result = merge_list([1, 5, 3, 2], [2, 1, 4, 5, 6])
# print(result)  # This should output [1, 1, 2, 2, 3, 4, 5, 5, 6]

# result = merge_list([1, 5, 9], [])
# print(result)  # This should output [1, 5, 9]
