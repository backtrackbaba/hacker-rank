'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

Function Description

Complete the diagonalDifference function described below to calculate the absolute difference between diagonal sums.
'''

n = 4

a = [[11, 2, 4, 1], [4, 5, 6, 2], [10, 8, -12, 3], [1,2,3,4]]

for i in range(n):
    print (a[i])

left = 0
right = 0

for i in range (n):
    left = left + (a[i][i])
    print ("No ", i , a[i][abs(i-2)])

print ("Left = ", left)


print ("\n \n")


for i in range (n):
    #print (abs(i-n+1))
    right = right + (a[i][abs(i-n+1)])
    print ("No ", i, (a[i][abs(i-n+1)]))

#print (left)
print ("Right = ", right)
diff = abs(left - right)
print (diff)