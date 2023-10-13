def merge_list(list1, list2):
    # Check if the input is valid lists
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Both inputs must be lists")

    # Merge the two unsorted lists and sort them
    merged = list1 + list2
    merged.sort()

    return merged

# Example usage:
# result = merge_list([1, 5, 52, 83], [2, 6, 7, 8])
# print(result)  # This should output [1, 2, 5, 6, 7, 8, 52, 83]

# result = merge_list([-8, 1, 2, 70, 71], [-20, -19, 68])
# print(result)  # This should output [-20, -19, -8, 1, 2, 68, 70, 71]
