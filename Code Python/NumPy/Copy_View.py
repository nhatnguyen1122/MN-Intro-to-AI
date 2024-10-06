# Any changes made to the copy does NOT affect the original array and vice versa

# Any changes made to the view DO affect the original array and vice versa


import numpy as np

arr = np.array([1, 2, 3, 4, 5])

copy_arr = arr.copy()

copy_arr[2] = 69

print("Copy method: ")
print(arr)
print(copy_arr)


arr = np.array([1, 2, 3, 4, 5])

view_arr = arr.view()

view_arr[0] = 96
arr[3] = 24

print("View method: ")
print(arr)
print(view_arr)


# The "base" method will return None with the Copy
#                   and return the original array with View

print("\nBase for copy: ", copy_arr.base)
print("Base for view: ", view_arr.base)