
def staircase(n):
    for i in range(n-1):
        print (" " * (n-i-2) , "#" * (i+1))
        
    print ("#" * n)

n = int(6)

staircase(n)
