#2775

T = int(input())
K = []
A = []
B = []

for i in range(T):
    K.append(int(input()))
    A.append(list(range(1,int(input())+1)))
    B.append([0]*len(A[i]))

for i in range(T):
    for j in range(K[i]):
        for k in range(len(A[i])):
            B[i][k] = sum(A[i][0:k+1])
        A[i] = list(B[i])
    print(B[i][-1])