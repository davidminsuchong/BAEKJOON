#14889

N = int(input())
A = []
B = []
a = int(N/2)

for i in range(N):
    b = list(map(int,input().split()))
    A.append(b)

for i in range(N):
    B.append([i])

while len(B[0])<a:
    C = []
    for i in B:
        for j in range(N):
            if j > max(i):
                C.append(i+[j])
    B = []+C

C = []
n = len(B)
oldc = 4000000

for i in range(n//2):
    c = 0
    for j in range(a):
        for k in range(j+1,a):
            l = n-1-i
            c += A[B[i][j]][B[i][k]]+A[B[i][k]][B[i][j]]-A[B[l][j]][B[l][k]]-A[B[l][k]][B[l][j]]
    if abs(c)<oldc:
        oldc = abs(c)

print(oldc)