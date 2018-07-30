'''
Task 
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.
'''

N = 24

if N % 2 == 1:
    print("Weird")

elif N >=2 and N <= 5 and N % 2 == 0:
    print ("Not Weird")

elif N >=6 and N <= 20 and N % 2 == 0:
    print("Weird")

elif N % 2 == 0 and N > 20:
    print("Not Weird")