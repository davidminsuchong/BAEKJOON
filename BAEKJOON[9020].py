#9020

import math
import sys

C = []
T = int(input())
for i in range(T):
    C.append(int(sys.stdin.readline()))
N = max(C)

A = list(range(2,N+1))
B = A.copy()

for i in range(len(A)):
    if bool(A[i]) == True:
        j = A[i]**2
        while j<N+1:
            try:
                B.remove(j)
                A[j-2] = False
                j = j+A[i]
            except:
                j = j+A[i]

for i in range(T):
    diff = 10000
    for j in range(len(B)):
        k=0
        if B[j]>=C[i]:
            break
        while B[k]<=C[i]-B[j] and k<=j:
            if B[j]+B[k]==C[i] and abs(B[j]-B[k])<diff:
                a1 = B[k]
                a2 = B[j]
                diff = B[j]-B[k]
            k+=1
    print(a1,a2)