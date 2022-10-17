#10989

import sys

N = int(input())
B = [0]*10000

for i in range(N):
    B[int(sys.stdin.readline())-1] += 1

for i in range(10000):
    if B[i] != 0:
        for j in range(B[i]):
            print(i+1)