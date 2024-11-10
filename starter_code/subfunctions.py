import numpy as np

def piecewise_max(array1, array2):
    # Ensure both arrays are of the same size
    if len(array1) != len(array2):
        raise ValueError("Arrays must be of the same size")
    
    # Create an empty result list
    result = []
    
    # Iterate through both arrays and get piecewise max
    for a, b in zip(array1, array2):
        result.append(max(a, b))
    
    return result

def arr_sum_keep_zeroes(*arrays):
    array_lengths = [len(array) for array in arrays]
    if len(set(array_lengths)) != 1:
        raise ValueError("All arrays must be of the same length")
    
    # Create a result list to store the piecewise sum for each index
    result = []
    
    # Iterate through the elements of the arrays
    for i in range(len(arrays[0])):  # We use the length of the first array
        # Check if any element at index i is zero across all arrays
        if any(array[i] == 0 for array in arrays):
            result.append(0)
        else:
            result.append(sum(array[i] for array in arrays))
    
    return result
