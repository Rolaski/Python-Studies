import numpy as np


def create_squared_array():
    first_row = np.array([2, 3, 4, 5, 6])

    # Create an empty 5x5 array
    array_2d = np.empty((5, 5), dtype=int)

    # Fill the first row of the array
    array_2d[0] = first_row

    # Fill the rest of the array with squares of numbers from the first row
    for i in range(1, 5):
        array_2d[i] = first_row ** 2
        first_row = first_row ** 2  # Square each element in the first row for the next iteration

    return array_2d


# Test the function
result_array = create_squared_array()
print("Resulting 5x5 array:")
print(result_array)
