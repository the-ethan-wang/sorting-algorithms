"""
MAIN.PY
all the algorithms
"""

import math
import random
import numpy as np
import time

def check_sorted(array: list):
    sorted_right = True
    highest = array[0] - 1
    for item in array:
        if sorted_right == False:
            pass
        else:
            if item < highest:
                sorted_right = False
            highest = item
    return sorted_right

def miracle_sort(array: list):
    # PRAY
    return array

def bogo_sort(array: list):
    while not check_sorted(array):
        random.shuffle(array)
        print("failed with", str(array))
    return array


print('using bogosort')

print(bogo_sort([0,1,2,3,4,5,56,67,7,95,69,85,94,3245,356,27]))