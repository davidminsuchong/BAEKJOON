#10989

N = int(input())
A = []
B = [0]*10000
C = ["0"]*N

for i in range(N):
    a = input()
    A.append(a)
    B[int(a)-1] += 1

for i in range(9999):
    B[i+1] += B[i]

del B[9999]
B = [0]+B

for i in range(N):
    C[B[int(A[i])-1]] = A[i]
    B[int(A[i])-1]+=1

for i in range(N):
    print(C[i])