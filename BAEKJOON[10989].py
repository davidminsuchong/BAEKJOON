#10989

import sys

N = int(input())
A = []
B = [0]*10000

for i in range(N):
    a = int(sys.stdin.readline())
    if B[a]==0:
        A.append(a)
    B[a] += 1
    
A.sort()

for i in A:
    print((str(i)+"\n")*(B[i]-1)+str(i))