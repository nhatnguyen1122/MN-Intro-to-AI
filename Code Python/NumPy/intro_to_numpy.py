import numpy as np

arr = np.array([1, 2, 3, 4, 5]) # Using array

print(arr)

print("Version: ", np.__version__)

print("Type: ", type(arr))

arr1 = np.array((1, 2, 3, 4, 5)) # Using tuple

if type(arr) == type(arr1):
    print("Same type: 'ndarray'")