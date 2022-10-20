#1269

N,M = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
C = []

for i in A-B:
    C.append(i)
for i in B-A:
    C.append(i)

print(len(C))