'''

Given an array of integers, find the sum of its elements.

Function Description

Complete the simpleArraySum function described below to return the sum of all elements of the array.

simpleArraySum(integer: n, integer array: arr)

Parameters:

n: array size
ar: array of integers to sum

Returns: integer sum of all array elements



Sample Input 0

6
1 2 3 4 10 11
Sample Output 0

31

'''
#!/bin/python3

import os
import sys

def simpleArraySum(ar):
    #
    # Write your code here.
    add = 0
    for i in ar:
        add = add + i
    return add
    

ar_count = int(input())

print ("ar_count = ", ar_count )

ar = list(map(int, input().rstrip().split()))

print ("ar = ", ar)

result = simpleArraySum(ar)

print ("result = ", result)