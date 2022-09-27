#9020

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
    for j in range(len(B)):
        if B[j]>=(C[i]//2):
            k = j
            break
    while True:
        if B[j]+B[k]>C[i]:
            k -= 1
        elif B[j]+B[k]<C[i]:
            j += 1
        else:
            print(B[k],B[j])
            break