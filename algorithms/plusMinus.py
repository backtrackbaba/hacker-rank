def plusMinus(arr):
    neg = 0
    pos = 0
    zero = 0


    for i in range(n):
        
        if (int(arr[i]) < 0) :
            neg = neg + 1
        elif int((arr[i]) > 0):
            pos = pos + 1
        else:
            zero = zero + 1
    
    pos =  ('%.6f' % (pos/n))
    neg =  ('%.6f' % (neg/n))
    zero =  ('%.6f' % (zero/n))
    return ( pos,neg, zero)


n = 6

arr = [-4, 3, -9, 0, 4, 1  ]

result = plusMinus(arr)

print (result[0])
print (result[1])
print (result[2])
