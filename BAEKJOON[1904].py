#1904

A = [1,2]
N = int(input())

for i in range(N-2):
    A.append((A[i]+A[i+1])%15746)

print(A[N-1])
