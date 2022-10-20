#14425

import sys

N,M = map(int,input().split())
S = set()
s = []
count = 0

for i in range(N):
    S.add(sys.stdin.readline())
for i in range(M):
    s.append(sys.stdin.readline())

for i in s:
    if i in S:
        count += 1

print(count)