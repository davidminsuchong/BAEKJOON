#7568

N = int(input())
A = []
B = [1]*N

A.append(list(map(int,input().split())))

for i in range(N-1):
    A.append(list(map(int,input().split())))
    for j in range(0,1+i):
        if A[j][0] > A[-1][0] and A[j][1] > A[-1][1]:
            B[i+1]+=1
        elif A[j][0] < A[-1][0] and A[j][1] < A[-1][1]:
            B[j]+=1

print(*B)