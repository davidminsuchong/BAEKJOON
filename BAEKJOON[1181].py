#1181

import sys

N = int(input())
A = []

for i in range(N):
    A.append(sys.stdin.readline().strip())

A = set(A)
A = list(A)

B = []
for i in range(len(A)):
    B.append([len(A[i]),A[i]])

B.sort()

for i in range(len(B)):
    print(B[i][1])