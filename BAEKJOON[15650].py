#15650

N,M = map(int,input().split())

A = []

for i in range(1,N+1):
    A.append([i])

while len(A[0]) != M:
    B = []
    for i in A:
        for j in range(1,N+1):
            if j > max(i):
                B.append(i+[j])
    A = []+B

for i in A:
    print(*i)