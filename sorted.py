def reverse_sort_dictionary(input_dict):
    # Sort the dictionary in reverse order by names
    sorted_items = sorted(input_dict.items(), key=lambda item: item[0], reverse=True)

    # Extract the name and phone number from each tuple
    result = [(name, data[0]) for name, data in sorted_items]

    return result

# Example usage:
# input_dict = {'Tom': (5464512, 24), 'Sara': (5446987, 32), 'Mary': (1557896, 20)}
# result = reverse_sort_dictionary(input_dict)
# print(result)  # This should output [('Tom', 5464512), ('Sara', 5446987), ('Mary', 1557896)]
