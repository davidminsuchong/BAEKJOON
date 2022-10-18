#2798

N,M = map(int,input().split())
A = list(map(int,input().split()))
answer = 0

for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            B = A[i]+A[j]+A[k]
            if B>answer and B<=M:
                answer=B

print(answer)