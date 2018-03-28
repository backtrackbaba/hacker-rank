import os
import sys

#
# Complete the solve function below.
#
def solve(a0, a1, a2, b0, b1, b2):

    resA = 0
    resB = 0

    if (a0 < b0):
        resB = resB + 1
    elif (b0 < a0):
        resA = resA +1

    if (a1 < b1):
        resB = resB + 1
    elif (b1 < a1):
        resA = resA +1

    if (a2 < b2):
        resB = resB + 1
    elif (b2 < a2):
        resA = resA +1

    return (resA, resB)

a0A1A2 = input().split()

a0 = int(a0A1A2[0])

a1 = int(a0A1A2[1])

a2 = int(a0A1A2[2])

b0B1B2 = input().split()

b0 = int(b0B1B2[0])

b1 = int(b0B1B2[1])

b2 = int(b0B1B2[2])

result = solve(a0, a1, a2, b0, b1, b2)

print (result)




