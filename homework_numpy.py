import numpy
from array import array
from collections import deque
import time



max_num = 10**5

def speed_test(collection):
    start = time.perf_counter()
    for i in range(len(collection)):
        collection[i] += 1
    print(f"Время для {type(collection)}: {time.perf_counter() - start}")


speed_test(list(range(max_num)))
speed_test(numpy.array(list(range(max_num))))
speed_test(deque(range(max_num)))
speed_test(array('i', range(max_num)))
