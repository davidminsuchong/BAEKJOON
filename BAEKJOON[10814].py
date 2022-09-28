#10814

import sys

N = int(input())
A = []

for i in range(N):
    age,name = sys.stdin.readline().split()
    A.append([int(age),i,name])

A.sort()

for i in range(N):
    print(A[i][0],A[i][2])