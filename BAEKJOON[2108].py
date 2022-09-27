#2108

import math
import sys

N = int(input())
A = []
B = [0]*8001
count = 0
Sum = 0
Max = -4000
Min = 4000

for i in range(N):
    a = int(sys.stdin.readline())
    if a>Max:
        Max = a
    if a<Min:
        Min = a
    Sum += a
    A.append(a)
    B[a+4000] += 1
    if B[a+4000] > count:
        C = []
        C.append(a)
        count += 1
    elif B[a+4000] == count:
        C.append(a)

A.sort()
C.sort()

print(round(Sum/N))
print(A[N//2])
try:
    print(C[1])
except:
    print(C[0])
print(Max-Min)