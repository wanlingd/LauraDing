#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'segment' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER_ARRAY arr
#

def segment(x, arr):
    # Write your code here
    result = 0
    print("result",result)
    for i in range(len(arr)-x):
        # seg = arr[i:i+x]
        # minima = min(seg)
        # if minima > result:
        #     result = minima
        length = x-1
        compare = arr[i]
        if length > 0:
            compare = arr[i]
            print("first compare",compare)
            if arr[i+1] < compare:
                compare = arr[i+1]
                print("if compare",compare)
            length -= 1
            print("result",result)
        if compare > result:
            result = compare
            print("result",result)

    return result


print(segment(1, [2,3,2,1]))