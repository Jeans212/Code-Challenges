#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    c = 0           #sum points for a
    d = 0           #sum points for b
    e = []          #list of their result
    if a[0] > b[0]:
        c += 1
    elif a[0] < b[0]:
        d += 1
    else:
        c += 0
        d += 0

    if a[1] > b[1]:
        c += 1
    elif a[1] < b[1]:
        d += 1
    else:
        c += 0
        d += 0

    if a[2] > b[2]:
        c += 1
    elif a[2] < b[2]:
        d += 1
    else:
        c += 0
        d += 0

    e.append(c)
    e.append(d)
    return e  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
