#10989

import sys

N = int(input())
A = []
B = [0]*10000

for i in range(N):
    a = int(sys.stdin.readline())
    A.append(a)
    B[a-1] += 1