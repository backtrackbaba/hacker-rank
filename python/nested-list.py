'''

Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, N, the number of students. 
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

Constraints

2 <= N <=5

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.


[(3.0, 'sai'), (3.0, 'sagar'), (10.0, 'jogesh'), (2.0, 'nishant'), (15.0, 'kalpesh')]
[[3.0, 'sai'], [3.0, 'sagar'], [10.0, 'jogesh'], [2.0, 'nishant'], [15.0, 'kalpesh']]
'''
# lis = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     tup = [score, name]
#     lis.append(tup)
    
# sor = sorted(lis)
# print (lis)
# # print(sor[-2][1])
# # print(sor[-1][1])

def getKey(item):
    return item[0]
l = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
print(sorted(l, key=getKey)[1:2][0][0])
print(sorted(l, key=getKey)[2:3][0][0])