#2750

N = int(input())
A = []

for i in range(N):
    A.append(int(input()))

A.sort()

for i in range(N):
    print(A[i])