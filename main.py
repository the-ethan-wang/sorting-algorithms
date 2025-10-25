import math
import random
import numpy as np
import time

stopwatch = None

def reset_timer():
    global stopwatch
    stopwatch = time.time()

def check_timer():
    global stopwatch
    if stopwatch is None:
        print("Stopwatch has not been started.")
        return
    elapsed = time.time() - stopwatch
    print(f"Time elapsed: {elapsed:.2f} seconds.")
    return elapsed

def check_sorted(array: list):
    # ill make this a bit better later but im not bothered rn
    sorted = True
    highest = array[0] - 1
    for item in array:
        if sorted == False:
            pass
        else:
            if item < highest:
                sorted = False
            highest = item
    return sorted

def miracle_sort(array: list, info=True, logging=False, limit=3600, wait=30):
    if info:
        print("Using miracle sort to sort array {}".format(str(array)))
    if check_sorted(array):
        print("it was alr sorted")
        return
    
    start = time.time()
    while time.time() - start < limit:
        if logging and check_sorted(array): print("IT WORKED") 
        elif logging: print("uh oh no miracle occured, waiting {} seconds".format(wait))
        time.sleep(wait)
    if not check_sorted(array):
        print("Aw shucks it timed out... {} seconds have passed without a miracle.".format(limit))
    return array

def bogo_sort(array: list, info=True, logging=False):
    if info:
        print("Using bogosort to sort array {}.".format(str(array)))
    if check_sorted(array):
            print("it was alr sorted")
            return
    
    if logging:
        while not check_sorted(array):
            random.shuffle(array)
            print("failed with", str(array))
    else:
        while not check_sorted(array):
            random.shuffle(array)
    return array


reset_timer()
bogo_sort([0,1,2,5,-9,7,1])
check_timer()
reset_timer()
miracle_sort([0,1,2,5,-9,7,1], logging=True)
check_timer()