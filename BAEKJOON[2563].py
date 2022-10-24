#2563

A = []
for i in range(100):
    A.append([0]*100)
summ = 0

N = int(input())

for i in range(N):
    a,b = map(int,input().split())
    for j in range(a,a+10):
        for k in range(b,b+10):
            A[j][k] = 1

for i in range(100):
    summ += sum(A[i])

print(summ)