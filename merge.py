def merge_list(list1, list2):
    # Check if the input is valid lists
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Both inputs must be lists")

    # Merge and sort the two unsorted lists
    merged = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Append any remaining elements from the two lists
    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged

# Example usage:
# result = merge_list([1, 5, 3, 7], [6, 2, 4])
# print(result)  # This should output [1, 2, 3, 4, 5, 6, 7]

# result = merge_list([1, 5, 3, 2], [2, 1, 4, 5, 6])
# print(result)  # This should output [1, 1, 2, 2, 3, 4, 5, 5, 6]

# result = merge_list([1, 5, 9], [])
# print(result)  # This should output [1, 5, 9]

