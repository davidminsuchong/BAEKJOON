#10816

N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
C = dict()
D = []

for i in A:
    C[i] = 0
for i in A:
    C[i] = C[i]+1
for i in B:
    try:
        D.append(C[i])
    except:
        D.append(0)

print(*D)