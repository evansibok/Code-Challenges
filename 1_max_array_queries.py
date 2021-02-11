# NOT SOLVED

import math
import os
import random
import re
import sys


#
# Complete the 'maxArrayQueries' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

# n = number of zeros in the first array
# queries[i] = int1(start), int2(end), int3(k)
"""
queries[
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100],
]
"""
# queries[0] -> [1, 2, 100] -> start, end, k
# queries[1] -> [2, 5, 100] -> start, end, k
# queries[2] -> [3, 4, 100] -> start, end, k

# First update -> [100, 100, 0, 0, 0]
# Second update -> [100, 200, 100, 100, 100]
# Third update -> [100, 200, 200, 200, 100]
# Highest value is 200 -> return it


def maxArrayQueries(n, queries):
    # Write your code here
    # test_list = [0] * n

    # grab the start, end and k values for each queries
    # for k, v in enumerate(queries):
    #     start = queries[k][0]
    #     end = queries[k][1]
    #     k = queries[k][2]

    # Move through the list
    # range(start, stop, step)
    # For each movement through the list
    # target each start index and end index
    # using the queries start and end values
    # Increment the values of each index using the k value
    # At the end of each interation
    # Sort the values in order of highest to lowest and grab the first element
    # return the first value, as it will be the highest
    # for i in range(len(test_list)):
    #     print(test_list[i+1])
    #     test_list[i] += 100
    pass
