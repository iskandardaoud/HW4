
def my_steps(n):
    if not (1 <= n <= 25):
        raise ValueError("Input is out of bounds. Please provide an integer
between 1 and 25.")

    # Create a list to store the number of ways for each step
    ways = [0] * (n + 1)

    # There is only one way to climb the first step
    ways[1] = 1

    # There are two ways to climb the second step
    ways[2] = 2

    # Calculate the number of ways to climb the ladder for each step
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]

# Example usage:
# result = my_steps(2)
# print(result)  # This should output 2

# result = my_steps(3)
# print(result)  # This should output 3
