#1015

N = int(input())
A = list(map(int,input().split()))
B = []+A
B.sort()
C = [0]*N

for i in range(N):
    a = A.index(B[i])
    C[a]=i
    A[a]=1001

print(*C)