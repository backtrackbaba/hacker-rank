import copy
arr = [1,2,3,4,5]
temp = copy.copy(arr)
add = []

def a():
    temp = copy.copy(arr)
    for i in range(len(arr)):
        temp.pop(i)
        add.append(sum(temp))
        temp = copy.copy(arr)


    #print ("Last waala temp = ", temp)
    return (min(add), max(add))

result = a()

print (result[0], result[1])
