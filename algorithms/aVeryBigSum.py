'''
Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

Function Description

Complete the function aVeryBigSum described below to return the sum of all elements of the array.
'''

def aVeryBigSum(n, ar):
    sum = 0
    for i in ar:
        sum = sum + i
    return sum

n = int(input())

ar = list(map(int, input().rstrip().split()))

result = aVeryBigSum(n, ar)

print (result)