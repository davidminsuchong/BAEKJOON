#2738

N,M = map(int,input().split())
A = []
B = []
count = 0

for i in range(N):
    C = list(map(int,input().split()))
    A = A+C
for i in range(N):
    C = list(map(int,input().split()))
    B = B+C

for i in range(N):
    C = []
    for j in range(M):
        C.append(A[i*M+j]+B[i*M+j])
    print(*C)