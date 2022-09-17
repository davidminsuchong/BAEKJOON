#18870

N = int(input())
A = list(map(int,input().split()))
B = [0]*N

for i in range(N):
    C = [0]*N
    for j in range(N):
        if A[i]==A[j] and i!=j:
            C = [0]*N
            break
        elif A[j]>A[i]:
            C[j] += 1
    for k in range(N):
        B[k]+=C[k]
print(B)