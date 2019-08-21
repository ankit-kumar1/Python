#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
finalstr = ""
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

print(matrix)
for i in range(m):
    for j in range(n):
        finalstr = finalstr+matrix[j][i]

print(finalstr)
s = re.sub('(\w)\W+(\w)', r'\1 \2', finalstr)

print(s)

