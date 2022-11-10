#2579

N = int(input())
A = [0]*2*N

for i in range(N):
    A[N-1-i]=int(input())

total = [A[0]]
for i in range(N-2):
    if A[1+i]