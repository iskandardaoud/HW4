def cacti_number(func):
    def wrapper(plot):
        if not isinstance(plot, list) or not all(isinstance(row, list) for row in plot):
            raise TypeError("Input must be a 2-D array of 0s and 1s.")

        rows, cols = len(plot), len(plot[0])

        def is_valid(x, y):
            return 0 <= x < rows and 0 <= y < cols

        count = 0
        for x in range(rows):
            for y in range(cols):
                if plot[x][y] == 0:
                    can_plant_cactus = True

                    # Check for adjacent cacti in all eight directions (including diagonals)
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx == 0 and dy == 0:
                                continue
                            new_x, new_y = x + dx, y + dy
                            if is_valid(new_x, new_y) and plot[new_x][new_y] == 1:
                                can_plant_cactus = False
                                break

                    if can_plant_cactus:
                        count += 1

        return count

    return wrapper

# Example usage:

# Create a file named cacti.py and place the decorator code in it.

# In a separate file (e.g., test.py), you can use the decorator as follows:

# test.py
# from cacti import cacti_number

# Define the main function and apply the decorator
# def main():
#     plot = [[1, 0, 1, 0, 1],
#             [0, 0, 0, 0, 0],
#             [1, 0, 0, 0, 0]]
#     print(cacti_number(plot))

# Call the main function
# if __name__ == "__main__":
#     main()

