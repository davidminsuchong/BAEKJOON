#9020

import math

C = []
T = int(input())
for i in range(T):
    C.append(int(input()))
N = max(C)

A = [False,False]+[True]*(N-1)
B = []

for i in range(2,math.ceil(math.sqrt(N))+1):
    if A[i] == True:
        j = i**2
        while j<N+1:
            A[j]=False
            j = j+i

for i in range(N+1):
    if A[i] == True:
        B.append(i)

for i in range(T):
    diff = 10000
    for j in range(len(B)):
        k=0
        if B[j]>=C[i]:
            break
        while k<=j:
            if B[j]+B[k]==C[i] and abs(B[j]-B[k])<diff:
                a1 = B[k]
                a2 = B[j]
                diff = B[j]-B[k]
            k+=1
    print(a1,a2)