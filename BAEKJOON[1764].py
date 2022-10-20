#1764

import sys

N,M = map(int,input().split())
A = set()
B = set()
C = []

for i in range(N):
    A.add(sys.stdin.readline().rstrip())
for i in range(M):
    B.add(sys.stdin.readline().rstrip())

for i in A&B:
    C.append(i)

C.sort()

print(len(C))

for i in C:
    print(i)