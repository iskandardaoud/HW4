def merge_list(list1, list2):
    # Check if the input is valid lists
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Both inputs must be lists")

    # Function to merge and sort two lists
    def merge_and_sort(left, right):
        sorted_list = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        
        return sorted_list

    # Merge and sort the two unsorted lists
    sorted_result = merge_and_sort(list1, list2)

    return sorted_result

# Example usage:
# result = merge_list([1, 5, 3, 7], [6, 2, 4])
# print(result)  # This should output [1, 2, 3, 4, 5, 6, 7]

# result = merge_list([1, 5, 3, 2], [2, 1, 4, 5, 6])
# print(result)  # This should output [1, 1, 2, 2, 3, 4, 5, 5, 6]

# result = merge_list([1, 5, 9], [])
# print(result)  # This should output [1, 5, 9]

