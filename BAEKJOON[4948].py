#4948

import math
import sys
A = []

while True:
    a = int(sys.stdin.readline())
    if a==0:
        break
    else:
        A.append(a)

N = max(A)
B = [0,0]+[1]*(2*N-1)
for j in range(2,math.ceil(math.sqrt(2*N))+1):
    if B[j] == 1:
        k = j**2
        while k<2*N+1:
            B[k]=0
            k = k+j

for i in range(len(A)):
    print(sum(B[A[i]+1:2*A[i]+1]))