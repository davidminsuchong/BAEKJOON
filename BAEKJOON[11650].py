#11650

import sys

N = int(input())
A = []

for i in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))

A.sort()

for i in range(N):
    print(A[i][0],A[i][1])