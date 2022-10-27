#2981

def newA(A,a):
    B = []
    for i in A:
        B.append(i-a)
    return B

def GCD(a,b):
    while a!=0:
        b = b%a
        a,b = b,a
    return b

N = int(input())
A = []
M = set()

for i in range(N):
    A.append(int(input()))
A.sort()
a = A[0]

for i in range(a):
    B = []+A
    for j in range(N-1):
        b = GCD(B[j],B[j+1])
        if b == 1 or b in M:
            break
        B[j+1] = b
        if j == N-2:
            M.add(b)
    A = newA(A,1)

print(*M)