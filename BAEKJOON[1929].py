#1929

import math
M,N = map(int,input().split())

A = [False,False]+[True]*(N-1)

for i in range(2,math.ceil(math.sqrt(N))+1):
    if A[i] == True:
        j = i**2
        while j<N+1:
            A[j]=False
            j = j+i

for i in range(M,N+1):
    if A[i] == True:
        print(i)