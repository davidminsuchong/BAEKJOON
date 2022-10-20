#10815

N = int(input())
A = set(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
C = []

for i in B:
    if i in A:
        C.append(1)
    else:
        C.append(0)

print(*C)