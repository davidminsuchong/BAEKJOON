#11651

import sys

N = int(input())
A = []

for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    A.append([y,x])
A.sort()

for i in range(N):
    print(A[i][1],A[i][0])