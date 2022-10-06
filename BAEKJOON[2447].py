#2447

N = int(input())

def starline(N):
    if N//3 == 0:
        return [["*"]]
    else:
        A = starline(N//3)
        M = len(A)
        B = []
        for i in range(M):
            B.append([A[i][0]*3])
        for i in range(M):
            B.append([A[i][0]+" "*M+A[i][0]])
        for i in range(M):
            B.append([A[i][0]*3])
        N = N//3
        return B

A = starline(N)
for i in range(len(A)):
        print(A[i][0])